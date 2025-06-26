import pandas as pd

def load_mutation_data(file_path):
    """
    Load somatic mutation data from a CSV file and filter relevant mutations.
    """
    try:
        df = pd.read_csv(file_path)
        somatic = df[df['mutation_type'] == 'somatic']
        return somatic
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def get_unique_genes(df):
    """
    Return a list of unique gene names from the DataFrame.
    """
    if df is not None:
        return df['gene'].unique().tolist()
    return []
