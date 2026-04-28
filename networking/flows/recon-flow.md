#   Reconnaissance flow (recon flow)

## Goal
Gather as much information as possible about a target before scanning or attacking.

---

##-step-1 : Identify Target
 -Domain: example.com
 -IP address:use:
  nslookup X.com

---

##-ste-2 : WHOIS Lookup
find domain registration details:
whois X.com

---

##-step-3 : DNS Enumeration
Get DNS records:
dig X.com

Check subdomains:
-- nslookup
-- online tools (like crt.sh)

---

## step-4 : Find Subdomains
-subfinder -d X.com
-assetfinder X.com
-amass enum -d X.com

---

## step-5 : check live hosts
-ping X.com
-http -l subdomain.com

---

## step-6 : Port Scanning(Basic)
- nmap X.com
- nmap -sV X.com

---

## step-7 : Direction Enumeration
Find hidden paths:
 - gobuster dir -u http:X.com -w
  wordlist.txt
 - dirsearch -u http: X.com

 ---

 ##step-8 : Technology Detection 
 - whatweb example.com
 - wappalyzer (browser extension)


 ---

##step-9 : collect emails / Info
-theHarvester -d X.com -b google

---
##step-10 : save results
always save output:
-nmap -oN scan.txt X.com
