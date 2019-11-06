import sublime
import sublime_plugin

class FeaturedScrollCommand(sublime_plugin.TextCommand):
    def run(self, edit, amount=1):
        self.view.run_command("scroll_lines", {"amount": amount})
        fwd = False
        if amount < 0:
        	amount = -amount
        	fwd = True

        for _ in range(amount):
            self.view.run_command("move", {"by": "lines", "forward": fwd})
