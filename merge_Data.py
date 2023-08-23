import pandas as pd

def get_County_List():
    county_list = ["Baker", "Benton", "Clackamas", "Clatsop", "Columbia", "Coos", "Crook", "Curry", "Deschutes",
                    "Douglas", "Gilliam", "Grant", "Harney", "Hood River", "Jackson", "Jefferson", "Josephine",
                    "Klamath", "Lake", "Lane", "Lincoln", "Linn", "Malheur", "Marion", "Morrow", "Multnomah",
                    "Polk", "Sherman", "Tillamook", "Umatilla", "Union", "Wallowa", "Wasco", "Washington",
                    "Wheeler", "Yamhill"]
    return county_list


def delete_lines(fileName, head, targetFN):
    fin = open(fileName, 'r')
    lines = fin.readlines()
    fout = open(targetFN, 'w')
    adjusted_lines = ''.join(lines[head:])
    fout.write(adjusted_lines)


def clean_CSV():
    county_list = get_County_List()
    for county in county_list:
        prec_dir = "./Precipitation_By_County/"
        temp_dir = "./Temperature_By_County/"
        target_dir = "./Precipitation_Temperature/"
        temp_excep = "_Temp.csv"
        prec_excep = "_Prec.csv"
        precFN = prec_dir + county + prec_excep
        tempFN = temp_dir + county + temp_excep
        lines_to_del = 3
        delete_lines(precFN, lines_to_del, target_dir+county+prec_excep)
        delete_lines(tempFN, lines_to_del, target_dir+county+temp_excep)


def merge_Data():
    county_list = get_County_List()
    dir = "./Precipitation_Temperature/"
    temp_excep = "_Temp.csv"
    prec_excep = "_Prec.csv"
    climate_excep = "_Climate.csv"
    climate_path = "./Merged_Data/"

    for county in county_list:
        precFN = dir + county + prec_excep
        tempFN = dir + county + temp_excep
        climateFN = climate_path + county + climate_excep

        prec_df = pd.read_csv(precFN)
        temp_df = pd.read_csv(tempFN)

        prec_df.rename(columns={'Value':'Precipitation'}, inplace=True)
        temp_df.rename(columns={'Value':"Temperature"}, inplace=True)

        climate_df = temp_df
        climate_df['Precipitation'] = prec_df['Precipitation']/30
        climate_df.to_csv(climateFN)


merge_Data()