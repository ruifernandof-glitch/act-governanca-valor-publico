"""Análise de clusters dos ACTs 2025 (k-means sobre as somas D1–D5).

Substitua por seu script original, se preferir; este reproduz os parâmetros
descritos no artigo.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "dados" / "matriz_codificacao_act_2025.csv")
X = df[[f"soma_D{i}" for i in range(1, 6)]].to_numpy(dtype=float)
Xz = StandardScaler().fit_transform(X)

linhas = []
for k in range(2, 10):
    km = KMeans(n_clusters=k, random_state=42, n_init=100).fit(Xz)
    linhas.append({"k": k, "inercia": km.inertia_, "silhueta": silhouette_score(Xz, km.labels_)})
diag = pd.DataFrame(linhas)
print(diag.round(3).to_string(index=False))
diag.to_csv(BASE / "dados" / "diagnostico_k.csv", index=False)

km4 = KMeans(n_clusters=4, random_state=42, n_init=100).fit(Xz)
df["cluster_kmeans"] = km4.labels_
centroides = pd.DataFrame(km4.cluster_centers_, columns=[f"D{i}_z" for i in range(1, 6)])
centroides["n"] = pd.Series(km4.labels_).value_counts().sort_index().values
print(centroides.round(2))
df.to_csv(BASE / "dados" / "matriz_com_clusters.csv", index=False)
