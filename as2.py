file_name = "mbox.txt"  
email_hosts = {}
with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("From:"):
                email = line.split()[1]
                host = email.split('@')[1]
                email_hosts[host] = email_hosts.get(host, 0) + 1
for host in email_hosts:
        print(host)
print(f"Total {len(email_hosts)} hosts printed")
