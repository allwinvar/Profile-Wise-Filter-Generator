# YouTube Filter List Generator

This tool automates the creation of filter lists for YouTube, designed to be used with ad blockers like uBlock Origin. It combines data from YAML configuration files containing account-specific CSS selectors and blocklists to generate filter rules.

## Features

*   **Automated Filter List Generation:**  Automatically generates filter lists based on provided configuration.
*   **Account-Specific Filters:** Supports creating filters tailored to individual YouTube accounts.
*   **Multiple Filter Types:** Handles cosmetic filters, no-login filters, and whole-site filters.
*   **CSS Selector Comparison:**  Compares CSS selectors to identify common and divergent parts, optimizing filter rules.
*   **YAML Configuration:** Uses YAML files for easy configuration of accounts, CSS selectors, and blocklists.

## Prerequisites

*   **Python 3.x:**  The script is written in Python 3.
*   **PyYAML:**  A Python library for parsing YAML files. Install with: `pip install pyyaml`
*   **cssselect:** A Python library for CSS selector parsing. Install with: `pip install cssselect`

## Configuration Files

The tool relies on two main types of configuration files:

1.  **`youtube-accounts.yaml`:**  This file defines your YouTube accounts and their associated CSS selectors.  Example:

    ```yaml
    accounts:
      account1:
        css-path: "body > div.style-scope.ytd-watch-page > div.style-scope.ytd-watch-page-renderer"
        img: "image.jpg"
      account2:
        css-path: "body > div.style-scope.ytd-watch-page > div.style-scope.ytd-watch-page-renderer"
        img: "anotherimage.png"
    no-login:
      account1:
        css-path: "body > div.style-scope.ytd-watch-page > div.style-scope.ytd-watch-page-renderer"
    whole:
      account1:
        css-path: "body > div.style-scope.ytd-watch-page > div.style-scope.ytd-watch-page-renderer"
    ```

2.  **`blocklists.yaml`:** This file contains your blocklists, organized into categories like `cosmetic-filters`, `no-login`, and `whole`. Example:

    ```yaml
    - cosmetic-filters:
        account1:
          selector: "div.some-class"
          comment: "Comment for account1's cosmetic filter"
    - no-login:
        account1:
          selector: "span.another-class"
          comment: "Comment for account1's no-login filter"
    - whole:
        account1:
          selector: "a.yet-another-class"
          comment: "Comment for account1's whole-site filter"
    ```

## Usage

1.  **Place the script (`your_script_name.py`) and the configuration files (`youtube-accounts.yaml`, `blocklists.yaml`) in the same directory.**

2.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

3.  **The generated filter list will be saved in a file named `blocklists.txt`.**

## Script Explanation

The script reads the YAML configuration files, iterates through the accounts and blocklists, compares CSS selectors, and generates filter rules in the format required by ad blockers.  The `compare_selectors` function is crucial for identifying common and divergent parts of the selectors, ensuring efficient filter creation.

## Dependencies

*   [PyYAML](https://pyyaml.org/wiki/PyYAML)
*   [cssselect](https://pypi.org/project/cssselect/)

## License

[Choose an appropriate license, e.g., MIT License](https://opensource.org/licenses/MIT)
