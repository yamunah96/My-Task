error_occurrences=0
warning_occurrences=0
info_occurrences=0
with open("application.log","r") as file:
    with open("errors.txt","a") as errorfile:
        with open("warings.txt","a") as waringfile:
            datafile =file.readlines()
            print(f"The total log is {len(datafile)}")
            for line in datafile:
                # print(line)
                if "INFO" in line:
                    info_occurrences+=1
                if "ERROR" in line:
                    error_occurrences+=1
                    errorfile.write(line)
                if "WARNING" in line:
                    warning_occurrences+=1
                    waringfile.write(line)

print(f"Count of info  occurrences: {info_occurrences},Count of error  occurrences: {error_occurrences}, Count of warning  occurrences: {warning_occurrences}")
