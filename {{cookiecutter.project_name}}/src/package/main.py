import numpy as np
from rich.console import Console
from rich.table import Table

def sum(arr1: np.ndarray, arr2: np.ndarray) -> int:
    result = np.sum(arr1 + arr2)
    return result

def main():
    console = Console()
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    result = sum(arr1, arr2)
    
    table = Table(title="Array Operations")
    table.add_column("Array 1", style="cyan")
    table.add_column("Array 2", style="magenta") 
    table.add_column("Sum", style="green")
    
    table.add_row(str(arr1.tolist()), str(arr2.tolist()), str(result))
    
    console.print(table)
    console.print(f"[bold green]Total sum: {result}[/bold green]")
    
if __name__ == "__main__":
    main()