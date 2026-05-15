import subprocess
import json
import os


def run_bandit_scan(filepath):

    output_file = "reports/bandit_output.json"

    command = [
        "python",
        "-m",
        "bandit",
        "-r",
        filepath,
        "-f",
        "json",
        "-o",
        output_file
    ]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        print("Bandit Output:")
        print(result.stdout)

        print("Bandit Errors:")
        print(result.stderr)

        if os.path.exists(output_file):

            with open(output_file, "r") as file:
                data = json.load(file)

            return data

        return {
            "results": []
        }

    except Exception as e:

        return {
            "results": [],
            "error": str(e)
        }