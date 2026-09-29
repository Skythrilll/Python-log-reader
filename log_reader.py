successful_logins = 0
failed_logins = 0

failed_ip = {}

with open('security.log', 'r')as file:

    for line in file:
        if "LOGIN SUCCESS" in line:
            successful_logins = successful_logins + 1

        elif "LOGIN FAILED" in line:
            failed_logins = failed_logins + 1
            parts = line.split()
            ip = parts[5].replace("ip", '')
            if ip in failed_ip:
                failed_ip[ip] = failed_ip[ip] + 1
            else:
                failed_ip[ip] = 1

print("\n ---------- Securiyty Log Report ----------")
print("Successful logins: ", successful_logins)
print("Failed logins: ", failed_logins)

print("\n Failed login attempt by ip address:")
for ip, count in failed_ip.items():
    print(ip, ':', count)

print('\n -------Security alerts ---------')
for ip, count in failed_ip.items():
    if count >= 3:
        print("Security alert: ", ip, " has failed to login", count , "times")
