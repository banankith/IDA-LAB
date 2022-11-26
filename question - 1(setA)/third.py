p.crosstab(df["pep"], df.sex)
p.crosstab(df["pep"], df["age"])
p.crosstab(df["pep"], df.sex).plot.bar()
p.crosstab(df["pep"], df["age"]).plot.bar()
