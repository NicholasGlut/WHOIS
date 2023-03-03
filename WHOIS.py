import whois
import socket

print("""\nThis tool will check basic information on a desired website.
Please enter a web address or type 'exit' to exit""")

while True:
    #define domain
    domain = input('Input web address: ')
    if domain == 'exit':
        break

    # Attempts to connect to domain
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        print(f'Unable to connect to {domain}. Please try again.')
        continue

    # Gathers and iterates through all data and prints them
    try:
        data = whois.whois(domain)
        data_dict={}
        for attr in dir(data):
            value = getattr(data,attr)
            if (value is not None and 
                not callable(value) and 
                "whois" not in str(attr).lower() and  
                "terms" not in str(attr).lower() and 
                not attr.startswith('_')):
                data_dict[attr] = value
                print(f"{attr} : {value}")
            
    except Exception as e:
        print(f"WHOIS lookup failed for {domain}: {e}")
