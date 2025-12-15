# F1 Qualifying vs Race Comparison (FastF1)

A professional, lightweight Python CLI application that compares **Formula 1 qualifying positions** with **final race results** for a given Grand Prix. The project uses the **FastF1** library to access official F1 timing data and presents clear insights into position gains and losses during the race.

---

## ✨ Key Features

* Uses **official Formula 1 timing data** via FastF1
* Compares **Qualifying vs Race** positions per driver
* Calculates **positions gained or lost** during the race
* Simple, fast **CLI-based workflow**
* Automatic local **data caching** for faster re-runs
* Clean, readable output suitable for analysis and reporting

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **FastF1** – F1 timing & telemetry access
* **Pandas** – data processing and comparison

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/f1-quali-vs-race-fastf1.git
cd f1-quali-vs-race-fastf1
pip install -r requirements.txt
```

> ℹ️ The first run requires an active internet connection to download session data. Subsequent runs use cached data and are significantly faster.

---

## ▶️ Usage

Run the application from the project root:

```bash
python src/main.py
```

You will be prompted to enter:

* **Season** (e.g. `2023`)
* **Race name** (e.g. `Bahrain`, `Monza`, `Silverstone`)

---

## 📊 Example Output

```text
F1 Qualifying vs Race Comparison

Qualifying  FullName            TeamName        Race  Change
1           Max Verstappen      Red Bull        1     0
2           Sergio Perez        Red Bull        2     0
7           Lewis Hamilton      Mercedes        3     +4
2           Charles Leclerc     Ferrari         6     -4
```

* **Positive Change** → Positions gained during the race
* **Negative Change** → Positions lost during the race

---

## 📁 Project Structure

```text
f1-quali-vs-race-fastf1/
├── src/
│   └── main.py
├── cache/              # Auto-generated FastF1 cache
├── requirements.txt
└── README.md
```

---

## 🚀 Future Enhancements

* CSV export of results
* Race-wide position change visualizations
* Season-level analysis
* Driver-specific performance tracking

---

## 📄 License

This project is open-source and intended for educational and portfolio use.

---

## 🙌 Acknowledgements

* **FastF1** community for maintaining an excellent F1 data library
* Formula 1 for the sport that inspires data-driven storytelling

---

If you are interested in motorsport analytics, data visualization, or Python-based CLI tools, feel free to explore, fork, or extend this project.
