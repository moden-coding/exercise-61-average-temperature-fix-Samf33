#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    print(df.iloc[181:212,6])
    return df.iloc[181:212,6].mean()
def main():
    result = average_temperature()
    print(f"Average temperature in July: {result:.1f}")

if __name__ == "__main__":
    main()
