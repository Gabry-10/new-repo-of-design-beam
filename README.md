# Beam Analysis Python

## 📌 Overview

This project performs structural analysis for simply supported beams **Uniformly Distributed Load (UDL)**.

The script:

* Reads beam data from a CSV file
* Calculates:

  * Maximum Bending Moment
  * Maximum Deflection
* Identifies the beam with:

  * Maximum moment
  * Maximum deflection
* Exports results to a new CSV file

---

## 📂 Input File Format

The input file (`231000476.csv`)

| Column Name  | Description                 |
| ------------ | --------------------------- |
| Beam_ID      | Beam identifier             |
| Span_m       | Beam length (meters)        |
| UDL_kN_per_m | Uniform load (kN/m)         |
| E_MPa        | Modulus of Elasticity (MPa) |
| I_mm4        | Moment of Inertia (mm⁴)     |

---

## ⚙️ Calculations

### 🔹 Maximum Bending Moment

[
M_{max} = \frac{wL^2}{8}
]

### 🔹 Maximum Deflection

[
\delta_{max} = \frac{5wL^4}{384EI}
]

---

## 🔄 Unit Conversions

| Parameter  | From → To  |
| ---------- | ---------- |
| Load       | kN/m → N/m |
| E          | MPa → N/m² |
| I          | mm⁴ → m⁴   |
| Deflection | m → mm     |

---

## ▶️ How to Run

1. Install required library:

```bash
pip install pandas
```

2. Run the script:

```bash
python your_script_name.py
```
## 🔀 Workflow

* Implemented the design check in a separate branch
* Created a Pull Request to merge into `main`
* Changes were reviewed before merging
<img width="1902" height="546" alt="Screenshot 2026-04-02 182454" src="https://github.com/user-attachments/assets/fba02b0a-1f34-45e8-8a72-42d476eb3f02" />


## 📤 Output

### Console Output:

* Table of results for each beam
* Maximum bending moment and its beam
* Maximum deflection and its beam

### File Output:

* `result.csv` → 
---

## 🧠 Example Output

```
Maximum Bending Moment = 120.50 kN·m (Beam B3)
Maximum Deflection = 8.25 mm (Beam B2)
```

## output of the code
<img width="1092" height="608" alt="image" src="https://github.com/user-attachments/assets/0dd17012-5685-4b61-b88b-99f3993696e7" />


## ⚠️ Assumptions

* Simply supported beam
* Uniformly distributed load only
* Linear elastic behavior

---

## 🚀 Future Improvements

* Add point loads
* Support cantilever beams
* Plot shear & moment diagrams
* Full structural solver

---

## 👨‍💻 Author

Mohammed Walid
