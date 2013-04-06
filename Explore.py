# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pandas import DataFrame, Series
import pandas as pd

# <codecell>

pd.read_table("data/Town-Hall-Rich-List-2012/Town-Hall-Rich-List-2012.txt")

# <codecell>

data = _

# <codecell>

data.columns = ["council", "name", "title", "09-10", "10-11", "change", "details"]

# <codecell>

data

# <codecell>

c_data = data.convert_objects()

# <codecell>

c_data

# <codecell>

data['10-11'] = data['10-11'].apply(clean)

# <codecell>

def clean(sn):
    if sn == "-":
        return 0
    else:
        return long(str.replace(sn, ",", ""))

# <codecell>

def clean_pct(sp):
    if sp == "-":
        return np.float64(0.0)
    else:
        return np.float64(str.replace(sp, "%", ""))

# <codecell>

data.change = data.change.apply(clean_pct)

# <codecell>

data

# <codecell>

plt.scatter(data['09-10'][(data['09-10'] > 0) & (data['10-11'] > 0)], data['10-11'][(data['09-10'] > 0) & (data['10-11'] > 0)])

# <codecell>

tax_data = pd.read_table("data/Council-tax-Band-D.txt")

# <codecell>

tax_data

# <codecell>

def clean_tax(st):
    st = str(st)
    if st == "-":
        return np.float64(0)
    else:
        return np.float64(str.replace(st,",",""))

# <codecell>

tax_data.columns

# <codecell>

year_cols = ['2000-01', '2001-02', '2002-03', '2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11']

# <codecell>

tax_data[year_cols] = tax_data[year_cols].applymap(clean_tax)

# <codecell>

tax_data

# <codecell>

tax_data['2000-01']

# <codecell>

tax_data[year_cols].T

# <codecell>

tax_data.to_csv("data/cleaned/tax_data.csv")

# <codecell>

data.to_csv("data/cleaned/pay_data.csv")

# <codecell>

data

# <codecell>

tax_data

# <codecell>

column_names = list(tax_data.columns)

# <codecell>

column_names[0] = 'council'

# <codecell>

tax_data.columns = column_names

# <codecell>

all_data = pd.merge(tax_data, data)

# <codecell>

all_data.to_csv("data/cleaned/combined_data.csv")

# <codecell>

all_data['2010-11'].corr(all_data['10-11'])

# <codecell>

all_data

# <codecell>

hack_data = all_data[['council','2010-11','10-11','details','name','title']].copy()

# <codecell>

hack_data

# <codecell>

hack_data.columns = ['Council','TaxRate','Pay','Details','Name','Title']

# <codecell>

hack_data

# <codecell>


