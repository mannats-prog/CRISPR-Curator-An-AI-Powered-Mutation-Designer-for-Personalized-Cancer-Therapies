from src.analyze_mutations import load_mutation_data, get_unique_genes

def main():
    # Load mutation data
    mutation_df = load_mutation_data("data/sample_mutations.csv")
    
    # Extract gene list
    gene_list = get_unique_genes(mutation_df)

    # Display basic output
    print("Detected mutated genes:")
    for gene in gene_list:
        print(f"- {gene}")

if __name__ == "__main__":
    main()
