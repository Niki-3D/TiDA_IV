import random
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich.panel import Panel


class EdgePickingGame:
    def __init__(self, nums=None):
        if nums is None:
            nums = [random.randint(1, 100) for _ in range(10)]
        self.nums = nums
        self.player_score = 0
        self.ai_score = 0
        self.console = Console()

        self.dp = {}
        self.compute_optimal_strategy()

    def compute_optimal_strategy(self):
        n = len(self.nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = self.nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    self.nums[i] - dp[i + 1][j],
                    self.nums[j] - dp[i][j - 1]
                )

        self.dp = dp

    def ai_move(self):
        n = len(self.nums)
        if n == 0:
            return None

        if n == 1:
            return "top"

        top_score_diff = self.nums[0] - self.dp[1][n - 1]
        bottom_score_diff = self.nums[n - 1] - self.dp[0][n - 2]

        if top_score_diff > bottom_score_diff:
            return "top"
        else:
            return "bottom"

    def make_move(self, side, is_player):
        if not self.nums:
            return False

        if side.lower() == "top":
            value = self.nums.pop(0)
        elif side.lower() == "bottom":
            value = self.nums.pop(-1)
        else:
            return False

        if is_player:
            self.player_score += value
            self.console.print(f"[bold green]You picked {value} from the {side}. Your score: {self.player_score}[/]")
        else:
            self.ai_score += value
            self.console.print(f"[bold red]AI picked {value} from the {side}. AI score: {self.ai_score}[/]")

        return True

    def display_game_state(self):
        if not self.nums:
            return

        table = Table(title="Edge Picking Game", show_header=True)
        table.add_column("Index", style="cyan")
        table.add_column("Value", style="yellow")

        for i, num in enumerate(self.nums):
            table.add_row(str(i), str(num))

        self.console.print(table)

        scores_table = Table(title="Current Scores", show_header=True)
        scores_table.add_column("Player", style="bold")
        scores_table.add_column("Score", style="bold")
        scores_table.add_row("You", f"[green]{self.player_score}[/]")
        scores_table.add_row("AI", f"[red]{self.ai_score}[/]")

        self.console.print(scores_table)

    def announce_winner(self):
        self.console.print("\n[bold]===== GAME OVER =====\n")

        final_table = Table(title="Final Scores", show_header=True)
        final_table.add_column("Player", style="bold")
        final_table.add_column("Score", style="bold")
        final_table.add_row("You", f"[green]{self.player_score}[/]")
        final_table.add_row("AI", f"[red]{self.ai_score}[/]")

        self.console.print(final_table)

        if self.player_score > self.ai_score:
            self.console.print(Panel("[bold green]Congratulations! You win![/]"))
        elif self.player_score < self.ai_score:
            self.console.print(Panel("[bold red]AI wins! Better luck next time![/]"))
        else:
            self.console.print(Panel("[bold yellow]It's a tie![/]"))

    def play_game(self):
        self.console.print(Panel("[bold cyan]Welcome to the Edge Picking Game![/]"))
        self.console.print("In this game, you and the AI take turns picking numbers from either end of the list.")
        self.console.print("The player with the highest total score at the end wins.")

        player_first = None
        while player_first is None:
            choice = input("\nDo you want to go first? (yes/no): ").lower()
            if choice in ["yes", "y"]:
                player_first = True
            elif choice in ["no", "n"]:
                player_first = False
            else:
                self.console.print("[yellow]Please enter 'yes' or 'no'.[/]")

        player_turn = player_first

        while self.nums:
            self.display_game_state()

            if player_turn:
                self.console.print("\n[bold green]Your turn![/]")
                valid_move = False
                while not valid_move:
                    move = input("Pick from 'top' or 'bottom': ").lower()
                    if move in ["top", "t"]:
                        valid_move = self.make_move("top", True)
                    elif move in ["bottom", "b"]:
                        valid_move = self.make_move("bottom", True)
                    else:
                        self.console.print("[yellow]Invalid input. Please enter 'top' or 'bottom'.[/]")
            else:
                self.console.print("\n[bold red]AI's turn...[/]")
                move = self.ai_move()
                self.make_move(move, False)

            player_turn = not player_turn

        self.announce_winner()


def main():
    print("Edge Picking Game Options:")
    print("1. Enter custom numbers")
    print("2. Use random numbers with default size (10)")
    print("3. Generate random numbers with custom size")

    option = input("Select an option (1-3): ")

    if option == "1":
        custom_list = input("Enter a list of numbers separated by spaces: ")
        try:
            nums = [int(x) for x in custom_list.split()]
            game = EdgePickingGame(nums)
        except ValueError:
            print("Invalid input. Using random numbers instead.")
            game = EdgePickingGame()
    elif option == "3":
        try:
            size = int(input("Enter the size of the random list (1-100): "))
            size = max(1, min(100, size))  # Limit size between 1 and 100
            max_value = int(input("Enter the maximum value for random numbers (1-10000): "))
            max_value = max(1, min(10000, max_value))  # Limit max value between 1 and 10000
            nums = [random.randint(1, max_value) for _ in range(size)]
            game = EdgePickingGame(nums)
        except ValueError:
            print("Invalid input. Using default random numbers.")
            game = EdgePickingGame()
    else:
        game = EdgePickingGame()

    game.play_game()


if __name__ == "__main__":
    main()