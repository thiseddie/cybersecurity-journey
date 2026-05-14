# DeepNmapScanner.py

```python
import nmap
import json
import csv
import socket
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track

console = Console()


class DeepNmapScanner:

    def __init__(self, target):
        self.target = target
        self.scanner = nmap.PortScanner()
        self.results = {}

    def banner(self):
        console.print(
            Panel.fit(
                "[bold cyan]Deep Nmap Scanner[/bold cyan]\n"
                "Advanced Network Enumeration Toolkit",
                border_style="green"
            )
        )

    def run_scan(self):

        arguments = "-sS -sV -O -Pn -T4 --top-ports 1000"

        console.print(f"\n[cyan]Scanning:[/cyan] {self.target}")
        console.print(f"[yellow]Arguments:[/yellow] {arguments}\n")

        self.scanner.scan(
            hosts=self.target,
            arguments=arguments
        )

        self.parse_results()

    def parse_results(self):

        for host in self.scanner.all_hosts():

            host_data = {
                "hostname": self.scanner[host].hostname(),
                "state": self.scanner[host].state(),
                "protocols": {},
                "os": []
            }

            if 'osmatch' in self.scanner[host]:
                for osmatch in self.scanner[host]['osmatch']:
                    host_data['os'].append({
                        'name': osmatch['name'],
                        'accuracy': osmatch['accuracy']
                    })

            for proto in self.scanner[host].all_protocols():

                ports = self.scanner[host][proto].keys()

                host_data['protocols'][proto] = []

                for port in ports:

                    service = self.scanner[host][proto][port]

                    service_data = {
                        'port': port,
                        'state': service.get('state', ''),
                        'service': service.get('name', ''),
                        'product': service.get('product', ''),
                        'version': service.get('version', ''),
                        'extrainfo': service.get('extrainfo', '')
                    }

                    host_data['protocols'][proto].append(service_data)

            self.results[host] = host_data

    def display_results(self):

        for host, data in self.results.items():

            console.print(
                f"\n[bold green]Host:[/bold green] {host}"
            )

            console.print(
                f"[bold blue]Hostname:[/bold blue] {data['hostname']}"
            )

            console.print(
                f"[bold yellow]State:[/bold yellow] {data['state']}"
            )

            if data['os']:
                console.print("\n[bold magenta]Possible Operating Systems:[/bold magenta]")

                for os_data in data['os']:
                    console.print(
                        f"- {os_data['name']} "
                        f"({os_data['accuracy']}%)"
                    )

            for proto in data['protocols']:

                table = Table(title=f"{proto.upper()} Ports")

                table.add_column("Port")
                table.add_column("State")
                table.add_column("Service")
                table.add_column("Product")
                table.add_column("Version")

                for service in data['protocols'][proto]:

                    table.add_row(
                        str(service['port']),
                        service['state'],
                        service['service'],
                        service['product'],
                        service['version']
                    )

                console.print(table)

    def export_json(self):

        filename = (
            f"scan_{self.target.replace('/', '_')}.json"
        )

        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)

        console.print(
            f"\n[green]JSON report saved:[/green] {filename}"
        )

    def export_csv(self):

        filename = (
            f"scan_{self.target.replace('/', '_')}.csv"
        )

        with open(filename, 'w', newline='') as csvfile:

            fieldnames = [
                'host',
                'protocol',
                'port',
                'state',
                'service',
                'product',
                'version'
            ]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for host, data in self.results.items():

                for proto in data['protocols']:

                    for service in data['protocols'][proto]:

                        writer.writerow({
                            'host': host,
                            'protocol': proto,
                            'port': service['port'],
                            'state': service['state'],
                            'service': service['service'],
                            'product': service['product'],
                            'version': service['version']
                        })

        console.print(
            f"[green]CSV report saved:[/green] {filename}"
        )


if __name__ == '__main__':

    console.print(
        "[bold cyan]Deep Nmap Scanner[/bold cyan]"
    )

    target = input("Target IP / CIDR: ")

    scanner = DeepNmapScanner(target)

    scanner.banner()

    scanner.run_scan()

    scanner.display_results()

    scanner.export_json()

    scanner.export_csv()
