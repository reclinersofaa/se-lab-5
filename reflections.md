1. **Which issues were the easiest to fix, and which were the hardest? Why?**

    The easiest fixes were style issues like removing the unused import logging, fixing C0303 trailing whitespace, and using f-strings, as these only required minor deletions or syntax changes. The hardest fixes involved correcting the mutable default argument (logs=None) and implementing input validation in add_item, as these required a deeper understanding of Python's function binding and conditional logic to prevent runtime bugs.

2. **Did the static analysis tools report any false positives? If so, describe one example.**

    Yes, one example was the Pylint warning for W0603 (Using the global statement) in load_data and save_data. While using a class would be better, the code's simple design relies on the global stock_data. In this minimal context, the global keyword is a necessary design choice to manage the inventory dictionary across functions without a full class refactoring, making the warning technically correct but acceptable for the current scope.

3. **How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.**

    I would integrate static analysis tools in two phases: locally using a pre-commit hook (like pre-commit framework) to run Flake8 for style checks before code is staged, and within the Continuous Integration (CI) pipeline (e.g., GitHub Actions) to run Bandit for security and Pylint for code quality checks. This ensures that only compliant, secure, and high-quality code is merged into the main branch.

4. **What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

    The code is significantly more robust after fixing the overly broad except: and adding input validation, preventing unexpected crashes from bad data. Readability improved through the use of with open(...) for file handling and converting function names to snake_case. Finally, security was vastly improved by eliminating the dangerous eval() call, resulting in higher overall code quality.