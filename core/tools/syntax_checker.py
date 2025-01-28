import ast

class SyntaxChecker:
    """
    Tool for checking syntax issues in Python scripts.
    """

    def check(self, file_path):
        """
        Check the syntax of a Python script.

        :param file_path: Path to the Python script.
        :return: List of syntax issues (if any).
        """
        issues = []

        try:
            with open(file_path, "r") as file:
                source_code = file.read()

            # Attempt to parse the source code into an Abstract Syntax Tree (AST)
            ast.parse(source_code, filename=file_path)

        except SyntaxError as e:
            issues.append({
                "type": "SyntaxError",
                "message": e.msg,
                "line": e.lineno,
                "offset": e.offset,
            })
        except FileNotFoundError:
            raise FileNotFoundError(f"Python script not found: {file_path}")
        except Exception as e:
            issues.append({
                "type": "Exception",
                "message": str(e),
            })

        return issues

if __name__ == "__main__":
    # Example usage
    checker = SyntaxChecker()
    try:
        results = checker.check("example_script.py")
        if results:
            print("Syntax Issues Found:", results)
        else:
            print("No syntax issues detected.")
    except Exception as e:
        print(f"Error: {e}")
