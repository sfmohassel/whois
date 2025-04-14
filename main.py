from locale import atoi
import os
from time import sleep
import click
from dotenv import load_dotenv
from prettytable import PrettyTable

from whois import check_domain_availability

load_dotenv()


@click.group()
def cli():
    pass


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


@cli.command()
@click.option(
    "--domains",
    prompt="Domain names without extension (comma separated)",
    help="Domain names without extension.",
)
@click.option(
    "--extensions", help="Domain extensions (comma separated).", default="com,ai,net"
)
@click.option(
    "--only-available", is_flag=True, default=True, help="Show only available domains."
)
def whois(domains, extensions, only_available):
    """Check if a domain is available."""
    if not domains:
        click.echo("Please provide a domain names.")
        return

    if not extensions:
        click.echo("Please provide domain extensions.")
        return

    click.echo(f"Checking availability for '{domains}' with extensions: '{extensions}'")

    extensions = [ext.strip() for ext in extensions.split(",")]
    domains = [domain.strip() for domain in domains.split(",")]
    available_domains = []

    for domain in domains:
        for ext in extensions:
            full_domain = f"{domain.strip()}.{ext.strip()}"
            available_domains.append(full_domain)

    table = PrettyTable()
    table.field_names = ["Domain", "Available", "Error"]
    for domain in available_domains:
        # Simulate domain availability check
        sleep(atoi(os.getenv("SLEEP", "1")))
        res = check_domain_availability(domain)
        if only_available and not res["available"]:
            continue
        table.add_row([domain, res["available"], res["error"]])
    print(table)


if __name__ == "__main__":
    cli()
