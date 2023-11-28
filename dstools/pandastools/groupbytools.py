def get_groupby_size(df, atts):
    return df.groupby(atts, as_index=False).size()
