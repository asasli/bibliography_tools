import bibtexparser
import argparse

# Load a BibTeX file
def load_bibtex(file):
    with open(file, 'r', encoding='utf-8') as bibfile:
        return bibtexparser.load(bibfile)

# Write a BibTeX file
def write_bibtex(entries, output_file):
    with open(output_file, 'w', encoding='utf-8') as bibfile:
        bibfile.write(bibtexparser.dumps(entries))

# Get unique entries
def get_unique_entries(file1, file2, output_file):
    bib1 = load_bibtex(file1)
    bib2 = load_bibtex(file2)

    keys1 = set(entry['ID'] for entry in bib1.entries)
    keys2 = set(entry['ID'] for entry in bib2.entries)

    # Keep entries unique to each file
    unique_entries = [entry for entry in bib1.entries if entry['ID'] not in keys2]
    unique_entries += [entry for entry in bib2.entries if entry['ID'] not in keys1]

    # Write to output file
    unique_bib = bibtexparser.bibdatabase.BibDatabase()
    unique_bib.entries = unique_entries
    write_bibtex(unique_bib, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process two BibTeX files and output unique entries.")
    parser.add_argument('--file1', type=str, help='Path to the first BibTeX file')
    parser.add_argument('--file2', type=str, help='Path to the second BibTeX file')
    parser.add_argument('--output_file', type=str, help='Path to the output BibTeX file')

    args = parser.parse_args()

    # Get unique entries
    get_unique_entries(args.file1, args.file2, args.output_file)
    print(f"Unique entries saved to {args.output_file}")