import pandas as pd


def describe_clusters(df, cluster):
    for cluster_number in range(0, len(cluster.cluster_centers_)):
        print("================================")
        print("CLUSTER", cluster_number)
        print("total elements:", (cluster.labels_ == cluster_number).sum())
        for unique in df.ix[cluster.labels_ == cluster_number, "building_kind"].unique():
            print(
                "n ",
                unique,
                "=",
                len(
                    df.ix[cluster.labels_ == cluster_number].loc[
                        df["building_kind"] == unique
                    ]
                ),
                "out of",
                len(df.loc[df["building_kind"] == unique]),
            )