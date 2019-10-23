with open("requirements.txt", "r") as input, open("clean_requirements.txt", "w") as output:
    for line in input.readlines():
        line = line.strip()

        if line.startswith("#"):
            continue

        line = line.split("=")[0]

        print(line)
        output.write(line + "\n")
