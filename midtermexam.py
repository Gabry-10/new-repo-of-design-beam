import pandas as pd
df = pd.read_excel("231000476.csv")

Beamid = df["Beam_ID"][0]
Span = df["Span_m"][0]
Udl = df["UDL_kN_per_m"][0]
e = df["E_MPa"][0]
i =df["I_mm4"][0]
z= df["Z_mm3"][0]
fy= df["fy_MPa"][0]



df.to_csv("result.csv",index=False)
print("done") 
