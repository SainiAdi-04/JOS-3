import matplotlib.pyplot as plt
import pandas as pd
import jos3

# 1. Run Original JOS-3
model_orig = jos3.JOS3()
model_orig.setpt_cr[0] = 37.46
model_orig.options["sweat_model"] = "original"

model_orig.To = 29
model_orig.simulate(30)
model_orig.To = 43
model_orig.simulate(60)

df_orig = pd.DataFrame(model_orig.dict_results())

# 2. Run Modified Model (defaults to 36.9 °C and switched sweating)
model_mod = jos3.JOS3()

model_mod.To = 29
model_mod.simulate(30)
model_mod.To = 43
model_mod.simulate(60)

df_mod = pd.DataFrame(model_mod.dict_results())

# 3. Plot Comparison
plt.figure(figsize=(9, 6))

# Top graph: Mean Skin Temperature
plt.subplot(2, 1, 1)
plt.plot(df_orig["TskMean"], label="Original JOS-3", color="black", linestyle="--")
plt.plot(df_mod["TskMean"], label="Modified Model", color="red")
plt.ylabel("Skin Temp (°C)")
plt.title("Original JOS-3 vs Modified Model")
plt.legend()
plt.grid(True)

# Bottom graph: Sweating (Skin Wettedness)
plt.subplot(2, 1, 2)
plt.plot(df_orig["WetMean"], label="Original JOS-3", color="black", linestyle="--")
plt.plot(df_mod["WetMean"], label="Modified Model", color="blue")
plt.xlabel("Time (min)")
plt.ylabel("Skin Wettedness")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("comparison_curve.png")
print("Saved comparison_curve.png")
