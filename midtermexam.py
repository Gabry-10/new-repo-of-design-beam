import pandas as pd

# Read the Excel or CSV file
df = pd.read_csv("231000476.csv")   # change to .xlsx if needed

# Convert units to be consistent
# w: kN/m → N/m
df["w_N_per_m"] = df["UDL_kN_per_m"] * 1000

# E: MPa → N/m²
df["E_N_per_m2"] = df["E_MPa"] * 1e6

# I: mm^4 → m^4
df["I_m4"] = df["I_mm4"] * 1e-12

# L already in meters
df["L"] = df["Span_m"]

# ===== Calculations =====

# Maximum Bending Moment (kN·m)
df["M_max_kNm"] = (df["UDL_kN_per_m"] * df["L"]**2) / 8

# Maximum Deflection (m)
df["deflection_m"] = (5 * df["w_N_per_m"] * df["L"]**4) / (384 * df["E_N_per_m2"] * df["I_m4"])

# Convert deflection to mm (better for engineering)
df["deflection_mm"] = df["deflection_m"] * 1000

# ===== Results =====

print("\n===== Results for Each Beam =====")
print(df[["Beam_ID", "M_max_kNm", "deflection_mm"]])

# Find maximum values overall
max_moment = df["M_max_kNm"].max()
max_moment_beam = df.loc[df["M_max_kNm"].idxmax(), "Beam_ID"]

max_deflection = df["deflection_mm"].max()
max_deflection_beam = df.loc[df["deflection_mm"].idxmax(), "Beam_ID"]

print("\n===== MAX VALUES =====")
print(f"Maximum Bending Moment = {max_moment:.2f} kN·m (Beam {max_moment_beam})")
print(f"Maximum Deflection = {max_deflection:.2f} mm (Beam {max_deflection_beam})")

df.to_csv("result.csv",index=False)