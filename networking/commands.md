# Networking Commands Cheat Sheet

This repository contains commonly used networking commands for Linux and Windows systems.
It is intended for students and beginners learning networking and cybersecurity.

---

## Contents

* IP and Interface Commands
* Connectivity Testing
* DNS Commands
* Routing Commands
* Network Scanning
* File Transfer

---

## IP and Interface

### Linux

```
ip a
ifconfig
hostname -I
```

### Windows

```
ipconfig
ipconfig /all
getmac
```

---

## Connectivity

```
ping google.com
traceroute google.com   (Linux)
tracert google.com      (Windows)
```

---

## DNS

```
nslookup google.com
dig google.com
host google.com
```

---

## Routing

```
netstat -tuln
ss -tuln
route
ip route
```

Windows:

```
netstat -ano
route print
```

---

## Network Scanning

```
nmap 192.168.1.1
nmap -sV target.com
```

---

## File Transfer

```
scp file.txt user@host:/path
rsync -av file.txt user@host:/path
ftp
```

---

## Notes

* Commands may require administrator/root privileges.
* Use scanning tools only on authorized systems.

---

## License

MIT License
