import bibtexparser
import os
import argparse

# Load a BibTeX file
def load_bibtex(file):
    with open(file, 'r', encoding='utf-8') as bibfile:
        return bibtexparser.load(bibfile)

# Write a BibTeX file
def write_bibtex(entries, output_file):
    with open(output_file, 'w', encoding='utf-8') as bibfile:
        bibfile.write(bibtexparser.dumps(entries))

# Move out common entries (duplicate entries based on citation keys)
def move_common_entries(bib_file, output_dir):
    bib = load_bibtex(bib_file)
    
    # Dictionary to track citation keys and their corresponding entries
    citation_dict = {}
    common_entries = []
    unique_entries = []

    # Check each entry in the BibTeX file
    for entry in bib.entries:
        entry_key = entry['ID']
        if entry_key in citation_dict:
            # If this entry already exists, it's a common entry
            common_entries.append(entry)
        else:
            citation_dict[entry_key] = entry
            unique_entries.append(entry)
    
    # Write the remaining (unique) entries back to the original BibTeX file
    remaining_bib = bibtexparser.bibdatabase.BibDatabase()
    remaining_bib.entries = unique_entries
    write_bibtex(remaining_bib, bib_file)
    print(f"Saved {len(unique_entries)} remaining (unique) entries to {bib_file}")

    # Write common entries to a separate file
    if not common_entries:
        print("No common entries found.")
        return
    
    common_bib = bibtexparser.bibdatabase.BibDatabase()
    common_bib.entries = common_entries
    common_file = os.path.join(output_dir, 'common_entries.bib')
    write_bibtex(common_bib, common_file)
    print(f"Saved {len(common_entries)} common entries to {common_file}")

def main():
    parser = argparse.ArgumentParser(description='Categorize BibTeX entries into unique and common entries.')
    parser.add_argument('--file', type=str, help='Path to the BibTeX file')
    parser.add_argument('--output', type=str, help='Directory to save the output files')
    
    args = parser.parse_args()
    
    # Ensure the output directory exists
    os.makedirs(args.output, exist_ok=True)
    
    # Move common entries and save the remaining entries
    move_common_entries(args.file, args.output)

if __name__ == '__main__':
    main()