import pandas as pd
import datacompy

orders = pd.read_table("http://bit.ly/chiporders")


# Drop rows having nulls in column 'choice_description'
orders_notnull = orders[orders["choice_description"].notnull()].copy()

# replace Veggie Bowl to Veg Bowl in column 'item_name'
orders_notnull.loc[:, "item_name"] = orders_notnull["item_name"].str.replace(
    "Veggie Bowl", "Veg Bowl", case=False
)



# replace Veggie Bowl to Veg Bowl in column 'choice_description'
orders_notnull.loc[:, "choice_description"] = orders_notnull["choice_description"].str.replace(
    "cheese", "cheeeessseeeeee", case=False
)



#  drop columns 'quantity'
orders_notnull.drop(["quantity"], axis=1, inplace=True)



df_compare = datacompy.Compare(
    orders,
    orders_notnull,
    join_columns=["order_id", "item_name"],
    abs_tol=0.0001,
    rel_tol=0,
    df1_name="original",
    df2_name="new",
)

# print compare report just like SAS proc compare
print(df_compare.report())


# Other options to print other statictis of comparision individually
#print(df_compare.df1_unq_rows)
#print(df_compare.intersect_rows)
#print(df_compare.df2_unq_rows)
#print(df_compare.df1_unq_columns())


