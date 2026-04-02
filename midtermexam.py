import pandas as pd

# Read file
df = pd.read_csv("231000476.csv")

# ===== USER INPUTS (EDIT THESE) =====
df["h_mm"] = 500              # section depth (mm) ← CHANGE if needed
sigma_allow = 250            # MPa (steel example)
# ===================================

# ===== Unit Conversions =====
df["w_N_per_m"] = df["UDL_kN_per_m"] * 1000
df["E_N_per_m2"] = df["E_MPa"] * 1e6
df["I_m4"] = df["I_mm4"] * 1e-12
df["L"] = df["Span_m"]

# ===== Structural Calculations =====

# Max Moment (kN·m)
df["M_max_kNm"] = (df["UDL_kN_per_m"] * df["L"]**2) / 8

# Convert to N·mm for stress
df["M_Nmm"] = df["M_max_kNm"] * 1e6

# Section properties
df["h_m"] = df["h_mm"] / 1000
df["c_m"] = df["h_m"] / 2

# Convert I to mm^4 for stress calc
df["I_mm4"] = df["I_mm4"]

# ===== Bending Stress =====
# σ = M*c / I
df["stress_MPa"] = (df["M_Nmm"] * (df["h_mm"]/2)) / df["I_mm4"]

# ===== Deflection =====
df["deflection_m"] = (5 * df["w_N_per_m"] * df["L"]**4) / (384 * df["E_N_per_m2"] * df["I_m4"])
df["deflection_mm"] = df["deflection_m"] * 1000

# ===== Allowable Deflection =====
df["allowable_deflection_mm"] = (df["L"] * 1000) / 250

# ===== CHECKS =====
df["Stress_OK"] = df["stress_MPa"] <= sigma_allow
df["Deflection_OK"] = df["deflection_mm"] <= df["allowable_deflection_mm"]

df["SAFE"] = df["Stress_OK"] & df["Deflection_OK"]

# ===== OUTPUT =====
print("\n===== DESIGN CHECK RESULTS =====")
print(df[[
    "Beam_ID",
    "M_max_kNm",
    "stress_MPa",
    "deflection_mm",
    "allowable_deflection_mm",
    "Stress_OK",
    "Deflection_OK",
    "SAFE"
]])

# Summary
unsafe_beams = df[df["SAFE"] == False]

if len(unsafe_beams) == 0:
    print("\n✅ All beams are SAFE")
else:
    print("\n❌ Unsafe beams:")
    print(unsafe_beams["Beam_ID"])