import os
import platform
import shutil
import sys
import time

from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ╔════════════════════════════════════════════════════════════════════╗
# ║                                                                    ║
# ║                    ENVIRONMENT FINDER v0.1                         ║
# ║                       by SwiftGlitxh                               ║
# ║                                                                    ║
# ╠════════════════════════════════════════════════════════════════════╣
# ║                                                                    ║
# ║  SCRIPT NAME : environment_finder.py                               ║
# ║  AUTHOR      : SwiftGlitxh                                         ║
# ║  VERSION     : 0.1                                                 ║
# ║  LANGUAGE    : Python 3                                            ║
# ║  LICENSE     : MIT License                                         ║
# ║  COPYRIGHT   : (c) 2026 SwiftGlitxh                                ║
# ║                                                                    ║
# ╠════════════════════════════════════════════════════════════════════╣
# ║  DESCRIPTION                                                       ║
# ║                                                                    ║
# ║  A Python-based system inspection utility that displays            ║
# ║  operating system details, Python configurations, installed        ║
# ║  development tools, and environment variables.                     ║
# ║                                                                    ║
# ╠════════════════════════════════════════════════════════════════════╣
# ║  FEATURES                                                          ║
# ║                                                                    ║
# ║  [+] Operating system and architecture detection                   ║
# ║  [+] Python version and executable discovery                       ║
# ║  [+] Virtual environment detection                                 ║
# ║  [+] Git, pip, Node.js, and Docker PATH checks                     ║
# ║  [+] Environment variable inspection                               ║
# ║  [+] Structured terminal output                                    ║
# ║                                                                    ║
# ╠════════════════════════════════════════════════════════════════════╣
# ║  SECURITY NOTICE                                                   ║
# ║                                                                    ║
# ║  Environment variables may contain sensitive information.          ║
# ║  Do not share raw output without redacting secrets, tokens,        ║
# ║  credentials, and identifying system information.                  ║
# ║                                                                    ║
# ╠════════════════════════════════════════════════════════════════════╣
# ║  GITHUB  : https://github.com/swiftglitxh                          ║
# ║  LICENSE : https://opensource.org/licenses/MIT                     ║
# ║                                                                    ║
# ╚════════════════════════════════════════════════════════════════════╝

console = Console()


def main():
    console.print(
    Align.center(
        Panel(
            Align.center(
                "[bold cyan]ENVIRONMENT FINDER[/bold cyan] [dim]v0.1[/dim]\n"
                "[dim]by @SwiftGlitxh[/dim]"
            ),
            border_style="cyan",
            padding=(1, 4),
            width=38,
        )
    )
)

    table = Table(
        title="[bold cyan]OPERATING SYSTEM INFORMATION[/bold cyan]",
        border_style="cyan",
        show_lines=True,
    )
    table.add_column("Check", style="cyan", no_wrap=True)
    table.add_column("Result", overflow="fold")

    in_venv = (
        sys.prefix != sys.base_prefix
        or hasattr(sys, "real_prefix")
    )

    checks = [
        ("Operating system", platform.system()),
        ("OS release", platform.release()),
        ("Architecture", platform.machine()),
        ("Python version", platform.python_version()),
        ("Python executable", sys.executable),
        ("Working directory", os.getcwd()),
        ("Virtual environment", "Active" if in_venv else "Inactive"),
    ]

    with Live(table, console=console, refresh_per_second=10):
        for label, result in checks:
            table.add_row(label, Text(str(result)))
            time.sleep(0.2)

        table.add_section()

        for tool in ("git", "python", "python3", "pip", "node", "docker"):
            path = shutil.which(tool)
            table.add_row(tool, Text(path or "Not found on PATH"))
            time.sleep(0.2)

    second_table = Table(
        title="ENVIRONMENT VARIABLES",
        border_style="cyan",
        caption="by @SwiftGlitxh",
        show_lines=True,
    )
    second_table.add_column("Variable", style="cyan")
    second_table.add_column("Value", overflow="fold")

    with Live(
        second_table,
        console=console,
        refresh_per_second=10,
        vertical_overflow="ellipsis",
    ):
        for name, value in sorted(os.environ.items()):
            second_table.add_row(Text(name), Text(value))
            time.sleep(0.05)

    console.print("\n[bold green]Checks complete.[/bold green]")


if __name__ == "__main__":
    main()
