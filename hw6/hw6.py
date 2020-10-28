# Step 1
import pandas as pd
import matplotlib

# Step 2
dataset = pd.read_csv("chipotle.tsv", sep='\t')
# OR
dataset = pd.read_table("chipotle.tsv")

# Step 3
chipo = dataset

# Step 4
print(chipo.head(10)) 

# Step 5
chipo_subset = chipo[["item_name", "quantity"]]                        # extract
chipo_subset = chipo_subset.groupby("item_name", as_index=False).sum() # groupby
chipo_subset = chipo_subset.sort_values("quantity", ascending=False)   # sort

chipo_top5 = chipo_subset.head(5) # only take top 5

chipo_plot = chipo_top5.plot.bar("item_name", "quantity")
chipo_plot.set_xlabel("Item name")
chipo_plot.set_ylabel("Total sold")
chipo_plot.set_title("Top 5 Items Bought at Chipotle")
matplotlib.pyplot.show()

# Step 6
chipo_subset = chipo[["order_id", "quantity", "item_price"]]          # extract
chipo_subset = chipo_subset.groupby("order_id", as_index=False).sum() # groupby

chipo_plot = chipo_subset.plot.scatter("item_price", "quantity")
chipo_plot.set_xlabel("Order Price ($)")
chipo_plot.set_ylabel("Items Purchased")
chipo_plot.set_title("Items Purchased vs Order Price")
matplotlib.pyplot.show()


# panda links:
# https://stackoverflow.com/questions/49188960/how-to-show-all-of-columns-name-on-pandas-dataframe/49189503#49189503v
# https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-output-from-series-to-dataframe#comment114163633
# _10374456
# https://stackoverflow.com/questions/38985053/pandas-groupby-and-sum-only-one-column
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
