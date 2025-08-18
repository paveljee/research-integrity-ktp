import os
import pandas as pd
import warnings

CATEGORY_LABEL = 'Category'
CATEGORY_IS_HEALTH = {  # as assigned by Pavel on 2025-08-18, meaning 'category label suggestive of relevance to human health/biomedicine'
    'Agricultural Sciences': False,
    'Biology and Biochemistry': True,
    'Chemistry': False,
    'Clinical Medicine': True,
    'Computer Science': False,
    'Cross-Field': True,  # note that this includes many
    'Economics and Business': False,
    'Engineering': False,
    'Environment and Ecology': False,
    'Geosciences': False,
    'Immunology': True,
    'Materials Science': False,
    'Mathematics': False,
    'Microbiology': True,
    'Molecular Biology and Genetics': True,
    'Neuroscience and Behavior': True,
    'Pharmacology and Toxicology': True,
    'Physics': False,
    'Plant and Animal Science': False,
    'Psychiatry and Psychology': True,
    'Social Sciences': True,
    'Space Science': False
}

def count_rows_in_xlsx(folder_path, csv_report_path):
    total = 0
    total_health = 0
    total_health_no_cross = 0
    category_label = CATEGORY_LABEL.lower()
    def cat_unify(cat: str) -> str:
        return cat.replace(' and ','/').replace(' & ','/').replace(', general','')
    category_is_health = {cat_unify(cat.lower()): is_health for cat, is_health in CATEGORY_IS_HEALTH.items()}
    categories = list(category_is_health.keys())
    all_counts_df = pd.DataFrame(columns=["hcr_category"] + categories)
    all_counts_df.loc[-1] = ["is_health"] + [str(category_is_health[cat]) for cat in categories]  # insert health row
    all_counts_df.index = all_counts_df.index + 1  # shift existing rows down
    all_counts_df = all_counts_df.sort_index()  # reorder so header is first, health row second
    print("Assumptions:\n-----------")
    print(f"Column name containing category: '{category_label}'")
    health_cats = [cat for cat, is_health in category_is_health.items() if is_health]
    print(f"{len(categories)} categories are known ad hoc, as follows:")
    print(f"Category labels suggestive of relevance to human health/biomedicine:")
    for cat in health_cats:
        print(f"- {cat}")
    print(f"Not suggestive categories:")
    for cat in categories:
        if cat not in health_cats:
            print(f"- {cat}")
    print("\nAnalysis:\n-------\nRow count per file (i.e., per year):\n")
    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".xlsx") and not file.startswith("~$"):
            path = os.path.join(folder_path, file)
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", UserWarning)
                    df = pd.read_excel(path)
                count = len(df)  # excludes header by default
                total += count
                edited_df = df.copy()
                edited_df.columns = [str(col).lower() for col in edited_df.columns]
                #print(f"'{category_label}' in lowercased headers: {True if category_label in [str(col).lower() for col in edited_df.columns] else False}")  # True for all from 2014 to 2024
                #print("headers available:")
                #for col in edited_df.columns:
                #    print(f"- {col}")
                #year_cats = [cat_unify(str(cat).lower()) for cat in edited_df[category_label].unique()]
                #print("categories available:")
                #for cat in unique_cats:
                #    print(f"- {cat}")
                #print(f"total unique categories: {len(year_cats)}")  # 21 in 2014-2017, 22 in 2018-2022, 21 in 2023-2024
                #additional_cats = set(year_cats) - set(categories)
                #cats_not_found = set(categories) - set(year_cats)
                #print(f"additional categories found in year: {additional_cats if len(additional_cats)>0 else None}")  # None across 2014-2024
                #print(f"known categories not found in year: {cats_not_found if len(cats_not_found)>0 else None}")  # 'cross-field' in 2014-2017 and 'mathematics' in 2023-2024 
                count_health = sum(edited_df[category_label].str.lower().apply(cat_unify).map(category_is_health))
                total_health += count_health
                count_cross = len(edited_df[edited_df[category_label].str.lower()=='cross-field'])
                def dump_csv_report(csv_report_path):
                    category_counts = edited_df[category_label].str.lower().apply(cat_unify).value_counts()
                    row_counts = [category_counts.get(cat, 0) for cat in categories]
                    all_counts_df.loc[len(all_counts_df)] = [file] + row_counts  # append counts as a new row
                    #csv_path = os.path.join(folder_path, csv_report_path)
                    all_counts_df.to_csv(csv_report_path, index=False)
                    print(f"\nCSV of all categories written to: {csv_report_path}")
                dump_csv_report(csv_report_path)
                count_health_no_cross = count_health - count_cross
                total_health_no_cross += count_health_no_cross
                print(f"- {file}: {count} (health/biomedicine: {count_health_no_cross}, {round(count_health_no_cross/count*100,1)}%; plus cross-field: {count_cross}, {round(count_cross/count*100,1)}%)")
                #print("\n")
            except Exception as e:
                print(f"{file}: Error - {e}")
    print(f"\nTotal rows (excluding headers): {total}")
    total_cross = total_health - total_health_no_cross
    print(f"\nOf these, in health: {total_health_no_cross}, {round(total_health_no_cross/total*100,1)}%; in cross-field: {total_cross}, {round(total_cross/total*100,1)}%")
