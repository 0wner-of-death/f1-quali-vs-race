import os
import fastf1
import pandas as pd


CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)
fastf1.Cache.enable_cache(CACHE_DIR)


def main():
    try:
        season = int(input("Enter season (e.g. 2023): "))
        race_name = input("Enter race name (e.g. Bahrain): ").strip()
    except ValueError:
        print("Invalid input. Season must be a number.")
        return

    print("\nLoading F1 data, please wait...\n")

    # Load qualifying session
    quali_session = fastf1.get_session(season, race_name, "Q")
    quali_session.load()

    # Load race session
    race_session = fastf1.get_session(season, race_name, "R")
    race_session.load()

    # Extract results
    quali_df = quali_session.results[
        ["Position", "FullName", "TeamName"]
    ].copy()

    race_df = race_session.results[
        ["Position", "FullName", "TeamName"]
    ].copy()

    # Rename columns
    quali_df.rename(columns={"Position": "Qualifying"}, inplace=True)
    race_df.rename(columns={"Position": "Race"}, inplace=True)

    # Merge qualifying & race results
    df = pd.merge(
        quali_df,
        race_df,
        on=["FullName", "TeamName"],
        how="inner"
    )

    # Calculate position change
    df["Change"] = df["Qualifying"] - df["Race"]

    # Sort by race position
    df.sort_values("Race", inplace=True)

    print("F1 Qualifying vs Race Comparison\n")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
