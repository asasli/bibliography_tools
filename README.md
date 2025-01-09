# Bibliography Tools

Tools for LaTeX bibliography.

Before you start, activate your desired conda environment and ```pip install bibtexparser```
## 1. Combining Bibliographies

Combining multiple bibliographies into a single document is crucial for various reasons:

- **Streamlined References**: Having all references in one place makes it easier to search, manage, and cite them.
- **Consistency**: Ensures uniform formatting and style throughout the document.
- **Efficiency**: Saves time and reduces errors by avoiding duplicate entries and consolidating efforts in bibliography management.
- **Collaboration**: Simplifies the process for collaborative projects where multiple contributors need to merge their references.

These tools help in effectively merging and managing your LaTeX bibliographies with ease.

### Example

```bash
python combine_bib.py --file1 bib1.bib --file2 bib2.bib --output bib12.bib
```

## 2. Spotting Common Entries in Bibliography

Spot common entries in a given bibliography file. You can effectively remove duplicate entries in the ```.bib``` file and move them to a separate file for easier management and debugging.

### Example
```bash
python spot_common_bib.py --file bibliography.bib --output test
```
