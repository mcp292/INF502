import pandas as pd
import matplotlib

dataset = pd.read_csv("chipotle.tsv", sep='\t')
# OR
# dataset = pd.read_table("chipotle.tsv")

chipo = dataset

print(chipo.head(10)) # TODO: fix print
# print(chipo.columns.tolist())

### Step 5. Create a bar plot of the top 5 items bought (total quantity per item)
# TODO: limit to 5 cleanly
chipo_top5 = chipo.sort_values("quantity", ascending=False)
chipo_top5 = chipo_top5.head(5) # only take top 5 

chipo_plot = chipo_top5.plot.bar("item_name", "quantity")
chipo_plot.set_ylabel("Quantity")
chipo_plot.set_title("Top 5 Items Bought at Chipotle")
#matplotlib.pyplot.show()

### Step 6. Create a scatterplot with the number of items orderered per order price
#### Hint: Price should be in the X-axis and Items ordered in the Y-axis
#(You will have to groupby and use the result
#print(chipo.groupby(["item_price", "quantity"]).sum())

#selected_cols = ["item_price", "quantity"]
#chipo_plot = chipo[selected_cols].groupby(selected_cols, as_index=False).sum()


chipo_subset = chipo[["item_price", "quantity"]]
chipo_subset = chipo_subset.groupby("item_price", as_index=False).sum()

#chipo_plot = chipo[selected_cols].groupby("item_price", as_index=False).sum()
#chipo_plot = chipo.groupby(["item_price"]).sum()
print("\n\n\nhere")
print(chipo_subset.columns.tolist())
print(chipo_subset.head(5))

chipo_plot = chipo_subset.plot.scatter("item_price", "quantity")
chipo_plot.set_xlabel("Item Price ($)")
chipo_plot.set_ylabel("Items Purchased")
chipo_plot.set_title("Items Purchased vs Item Price")
matplotlib.pyplot.show()
