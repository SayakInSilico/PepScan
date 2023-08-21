import argparse
import matplotlib.pyplot as plt

def calculate_hydropathy_scores(sequence):
    """
    Calculate hydropathy scores for each amino acid in the sequence.
    
    Args:
        sequence (str): The peptide sequence.
    
    Returns:
        list: List of hydropathy scores.
    """
    hydropathy_scores = []
    for amino_acid in sequence:
        hydropathy_score = ord(amino_acid) % 10
        hydropathy_scores.append(hydropathy_score)
    return hydropathy_scores

def calculate_instability_index(sequence):
    """
    Calculate the instability index for the sequence.
    
    Args:
        sequence (str): The peptide sequence.
    
    Returns:
        float: Instability index value.
    """
    instability_index = sum(ord(amino_acid) for amino_acid in sequence) / len(sequence)
    return instability_index

def generate_codon_usage_report(sequence):
    """
    Generate a report on codon usage in the sequence.
    
    Args:
        sequence (str): The peptide sequence.
    
    Returns:
        str: Codon usage report.
    """
    codon_count = {}
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        codon_count[codon] = codon_count.get(codon, 0) + 1
    
    codon_report = "\nCodon Usage Report:\n"
    for codon, count in codon_count.items():
        codon_report += f"{codon}: {count}\n"
    
    return codon_report

def plot_codon_usage(codon_count):
    """
    Plot the codon usage frequencies.
    
    Args:
        codon_count (dict): Dictionary containing codon frequencies.
    """
    codons = list(codon_count.keys())
    counts = list(codon_count.values())
    
    plt.bar(codons, counts)
    plt.xlabel('Codon')
    plt.ylabel('Frequency')
    plt.title('Codon Usage Frequencies')
    plt.xticks(rotation=45)
    plt.show()

def main():
    """
    Main function to run the peptide analysis tool.
    """
    parser = argparse.ArgumentParser(description='Peptide Analysis Tool')
    parser.add_argument('sequence', type=str, help='Input peptide sequence')
    args = parser.parse_args()

    amino_acid_count = calculate_amino_acid_count(args.sequence)
    hydropathy_scores = calculate_hydropathy_scores(args.sequence)
    instability_index = calculate_instability_index(args.sequence)
    codon_usage_report = generate_codon_usage_report(args.sequence)
    
    print(f'Amino Acid Count: {amino_acid_count}')
    plot_hydropathy(hydropathy_scores)
    print(f'Instability Index: {instability_index:.2f}')
    print(codon_usage_report)
    plot_codon_usage(codon_count)

if __name__ == '__main__':
    main()
