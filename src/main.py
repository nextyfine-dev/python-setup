from rich.console import Console
import time

# Initialize the console for rich output
console = Console()


def welcome_message() -> None:
    console.print("[bold green]Welcome to the Python Project![/bold green]")
    console.print("[cyan]Initializing the environment...[/cyan]")


def main() -> None:
    # Show the welcome message
    welcome_message()

    # Simulate some initialization process
    console.print("[yellow]Setting up necessary components... Please wait.[/yellow]")
    time.sleep(2)

    # Once setup is complete, print a success message
    console.print(
        "[bold green]All systems are go! Ready to start working.[/bold green]"
    )

    # Additional logic for your project can follow
    # For example, running the core functions of your app
    console.print("[blue]Starting the application now...[/blue]")


if __name__ == "__main__":
    main()
