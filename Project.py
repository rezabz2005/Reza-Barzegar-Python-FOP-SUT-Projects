import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# In 2
df = pd.DataFrame(pd.read_csv("housePrice.csv"))
# In 3
rows_cols = (len(df.axes[0]), len(df.axes[1]))
print(rows_cols)
# In 4
print(df)
# In 5
print(df.head(10))
# In 6
print(df.tail(10))
# In 7
sample_df = pd.DataFrame(df.sample(10))
print(sample_df)
# In 8
print(df.info())
# In 9
print(df.describe())
# In 10
df = df.replace("", np.nan)
empty_cells_count = df.isna().sum()
print(empty_cells_count)
# In 11
df = df.dropna()
# In 12
print(df.dtypes)
# In 13
df["Area"] = pd.to_numeric(df["Area"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Price(USD)"] = pd.to_numeric(df["Price(USD)"], errors="coerce")
# In 14
df = df*1
# In 15
df_T = df.describe().transpose()
print(df_T)
# In 16
column_names = df.columns.tolist()
print(column_names)
# In 17
def pascal_case(name):
    return "".join(word.capitalize() for word in name.split("_"))
column_names = df.columns.tolist()
new_column_names = {name: pascal_case(name) for name in column_names}
# In 18
for name in column_names:
    if( len(name) < 8 ):
        print(name)
# In 19
string = ""
for name in column_names:
    string += name + " "
string = string.rstrip().replace(" ","-")
print(string)
# In 20
df = df.rename( columns = new_column_names )
# In 21
df_without_price = df.drop(["Price", "Price(usd)"], axis=1)
# In 22
print(df_without_price)
# In 23
print(df[["Area", "Room", "Price"]])
# In 24
print(df[df.index % 2 == 0])
# In 25
dict = df.nunique().to_dict()
print(dict)
# In 26
print(list(df["Address"].unique()))
# In 27
example_dict = {columns: list(df[columns].unique()) for columns in df}
print(example_dict)
# In 28
address_counts = df["Address"].value_counts().to_dict()
print(address_counts)
# In 29
numeric_df = df.select_dtypes(include=[np.number])
max_values = numeric_df.max()
min_values = numeric_df.min()
range_values = max_values - min_values
print("Max Values:\n", max_values)
print("\nMin Values:\n", min_values)
print("\nRange of Values:\n", range_values)
# In 30
new_df = df[df["Area"] < df["Area"].quantile(0.25)]
print(new_df)
# In 31
print(new_df[["Area","Room","Price"]])
# In 32
df_sorted_by_price = df.sort_values("Price")
print(df_sorted_by_price)
# In 33
print(df_sorted_by_price.iloc[::-1])
# In 34
print(df_sorted_by_price[df_sorted_by_price["Elevator"] == 1])
# In 35
print(df.groupby("Address")["Area"].sum())
# In 36
df_example = df.groupby("Address")["Area"].aggregate(["mean"])
print(df_example)
# In 37
print(pd.crosstab(df["Room"], df["Parking"]))
# In 38
print(pd.crosstab(df["Room"], df["Warehouse"]))
# In 39
print(pd.crosstab(df["Room"], df["Elevator"]))
# In 40
print(df[df["Room"].isin(range(6))].groupby("Room")["Price"].mean())
# In 41
print(df.groupby(["Room", "Parking"]).agg({"Price": "mean"}).reset_index())
# In 42
df["Score"] = df["Parking"] + df["Warehouse"] + df["Elevator"]
# In 43
print((df[df["Area"] < 100]["Parking"].sum() / len(df[df["Area"] < 100])) * 100)
# In 44
print((len(df[(df["Score"] >= 1)]) / len(df)) * 100)
# In 45
print(df[(df["Room"] > 2) & (df["Score"] >= 1)])
# In 46
print(df[((df["Room"] >= 2) & (df["Room"] <= 4)) & (df["Parking"] >= 1)])
# In 47
df["New"] = df["Price"] / df["Area"]
df = df.sort_values("New")
print(list(df["Address"].iloc[:50:].unique()))
# In 48
plt.scatter(df["Area"], df["Price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Scatter plot of Price vs Area")
plt.show()
# In 49
plt.scatter(df["Area"], df["Price"], color = "black")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Scatter plot of Price vs Area")
plt.show()
# In 50
plt.scatter(df["Area"], df["Price"],marker = "*", color = "black")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Scatter plot of Price vs Area")
plt.show()
# In 51
plt.scatter(df["Room"], df["Price"],marker = "*", color = "black")
plt.xlabel("Room")
plt.ylabel("Price")
plt.title("Scatter plot of Room vs Area")
plt.show()
# In 52
plt.scatter(df["Score"], df["Price"], color = "red")
plt.xlabel("Score")
plt.ylabel("Price")
plt.title("Scatter plot of Price vs Score")
plt.show()
# In 53
plt.hist(df["Price"], bins=30)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Histogram of Price")
plt.show()
# In 54
sns.kdeplot(df["Price"])
plt.xlabel("Price")
plt.title("KDE of Price")
plt.show()
# In 55
sns.pairplot(df, diag_kind="kde")
plt.show()
# In 56
sns.heatmap(df[["Area","Price","Price(usd)","Elevator","Warehouse","New","Score","Room","Parking"]].corr(), annot=True)
plt.show()
# In 57
sns.heatmap(df[["Area","Price","Price(usd)","Elevator","Warehouse","New","Score","Room","Parking"]].corr(), annot=True, cmap="RdYlGn")
plt.show()
# In 58
counts = df["Parking"].value_counts()
colors = ["#e8f5e9","#81C784"]
explode = (0.1,) * len(counts)
plt.pie(counts, labels=counts.index, colors=colors[:len(counts)], explode=explode, autopct='%1.1f%%')
plt.title("Pie Chart of Parking")
plt.show()
# In 59
colors1 = ["#AAFF00", "#E4D00A", "#2AAA8A"]
colors2 = ["#5F9EA0", "#50C878", "#90EE90"]
variables = ["Warehouse", "Parking", "Elevator"]
distributions = [df[var].value_counts() for var in variables]
explodes = [[0.1 if value == dist.min() else 0 for value in dist] for dist in distributions]
for i, (dist, explode) in enumerate(zip(distributions, explodes)):
    plt.subplot(1, 3, i+1)
    plt.pie(dist,colors=[colors1[i],colors2[i] ], labels=dist.index, explode=explode, autopct='%1.1f%%')
    plt.title(variables[i])
plt.show()
# In 60
plt.boxplot(df['Price'], patch_artist=True,
            boxprops={"facecolor":"red", "color":"red"},
            medianprops={"color":"white"},
            flierprops={"markerfacecolor":"red", "markeredgecolor":"red"})
plt.title("Boxplot of Price")
plt.xlabel("Price")
plt.show()
# In 61
bp = plt.boxplot(df['Price'], patch_artist=True,
            boxprops={"facecolor":"red", "color":"red", "linewidth":5},
            medianprops={"color":"white", "linewidth":5},
            flierprops={"markerfacecolor":"red", "markeredgecolor":"red"})
plt.title("Boxplot of Price", fontsize=12)
plt.xlabel("Price", fontsize=12)
plt.show()
# In 62
plt.hist(df["Room"], color="green")
plt.title("Histogram of Room")
plt.xlabel("Room")
plt.ylabel("Frequency")
plt.show()
# In 63
variables = ["Elevator", "Parking", "Warehouse"]
colors = ["gold", "yellowgreen", "lightcoral"]
for i, var in enumerate(variables):
    plt.subplot(1, 3, i+1)
    plt.hist(df[var], color=colors[i])
    plt.title("Histogram of " + var)
    plt.xlabel(var)
    plt.ylabel("Frequency")
plt.show()
# In 64
price_range = df["Price"].max() - df["Price"].min()
bins = pd.cut(df["Price"], bins=4, labels=["cheap", "AveUnderMean", "AveUpperMean", "Expensive"])
df["PriceRange"] = bins
sns.countplot(x="PriceRange", data=df)
plt.title("Countplot of Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.show()
# In 65
random_sample = df["Price"].sample(frac=0.02)
random_sample.sort_index(inplace=True)
plt.plot(random_sample.index, random_sample, color="red")
plt.title("Line Plot of Random Sample from Price")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()
# In 66
random_sample = df["Price"].sample(frac=0.02)
random_sample.sort_values(inplace=True)
plt.plot(range(len(random_sample)), random_sample, color="red")
plt.title("Line Plot of Sorted Random Sample from Price")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()
# In 67
random_sample = df["Price"].sample(frac=0.02)
random_sample.sort_values(inplace=True)
plt.plot(range(len(random_sample)), random_sample, color="red")
plt.scatter(range(len(random_sample)), random_sample, color="blue")
plt.title("Line Plot of Sorted Random Sample from Price")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()
# In 68
df_sorted = df.sort_values(by="Area")
plt.plot(df_sorted["Area"], df_sorted["Price(usd)"])
plt.title("Line Plot of Price(usd) vs Area")
plt.xlabel("Area")
plt.ylabel("Price(usd)")
plt.show()
# In 69
df_sorted = df_sorted.dropna(subset=["Area", "Price"])
x = df_sorted["Area"]
y = df_sorted["Price"]
coefficients = np.polyfit(x, y, 1)
line = np.poly1d(coefficients)
plt.plot(x, y)
plt.plot(x, line(x))
plt.title("Price(usd) vs Area with Trendline")
plt.xlabel("Area")
plt.ylabel("Price(usd)")
plt.show()
# In 70
df_sorted = df_sorted.dropna(subset=["Area", "Price"])
x = df_sorted["Area"]
y = df_sorted["Price"]
coefficients = np.polyfit(x, y, 1)
line = np.poly1d(coefficients)
plt.plot(x, y)
plt.plot(x, line(x), "r--")
plt.title("Price(usd) vs Area with Trendline")
plt.xlabel("Area")
plt.ylabel("Price(usd)")
plt.show()
# In 71
sns.barplot(x="Room", y="Price", data=df)
plt.title("Barplot of Price vs Room")
plt.xlabel("Room")
plt.ylabel("Price")
plt.show()
# In 72