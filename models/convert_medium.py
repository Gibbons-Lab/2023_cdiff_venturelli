#!/usr/bin/env python

import pandas as pd
from sys import argv

if __name__ == "__main__":
    path = argv[1]
    sheet = argv[2]
    out = argv[3]

    skel = pd.read_excel(path, sheet)
    dfs = []
    for _, row in skel.dropna().iterrows():
        d = pd.DataFrame({
            "component": row.Component,
            "flux": row["Concentration (mM)"],
            "compound": row.molecules.split(",")
        })
        dfs.append(d)
    med = pd.concat(dfs).groupby("compound").flux.sum().reset_index()
    med["medium"] = "DM38"
    med.to_csv(f"data/{out}.tsv", index=False, sep="\t")
