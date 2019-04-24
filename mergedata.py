import pandas as pd

geo_filename = "data/" + "Data Geographies - v1 - by Gapminder.xlsx"

files = {
    "population": "population_total.csv",
    "pop_dens": "population_density_per_square_km.csv",
    "income": "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
    "life": "life_expectancy_years.csv",
    "co2": "co2_emissions_tonnes_per_person.csv",
    "children": "children_per_woman_total_fertility.csv",
    "childmort": "child_mortality_0_5_year_olds_dying_per_1000_born.csv",
}

dfs = {}

for table in files:
    df = pd.read_csv("data/" + files[table])
    dfs[table] = pd.melt(
        df, id_vars="country", var_name="year", value_name=""
    ).set_index(["country", "year"])
data = pd.concat(dfs, axis=1)
data.columns = data.columns.get_level_values(0)


geo = pd.read_excel(geo_filename, sheet_name="list-of-countries-etc")
geo.rename(columns={"name": "country"}, inplace=True)

pd.merge(data.reset_index(), geo, on="country").to_csv("gapminder.csv", index=False)
