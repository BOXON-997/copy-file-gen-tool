#! /usr/bin/env python3
# Author: The Fart Space Programmer
# -*- codong: latin-1 -*-

import typer 
import logging
from pathlib import Path 

from copyGenTool.core import (
    iter_files_no_copies,
    process_files_parallel
)

app = typer.Typer()

def configure_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO 
    logging.basicConfig(
        level=level,
        format=("%(asctime)s - %(levelname)s) - %(message)s"),
    
    )


@app.command()
def run(
    path: str = typer.Option(".", help="Base Directory"),
    overwrite: bool = typer.Option(False, help="Overwrite existing file"),
    dry_run: bool = typer.Option(False, help="Dry run mode"),
    verbose: bool = typer.Option(False, help="Verbose Loggging")
):
    configure_logging(verbose)
    base = Path(path).resolve()

    existing_files = iter_files_no_copies(base)

    if not existing_files:
        logging.warning("No existing files found!!!")
        raise typer.Exit(code=1)
    
    created_total = int()

    for created in process_files_parallel(existing_files, overwrite=overwrite, dry_run=dry_run):
        created_total += 1
        if dry_run:
            logging.info(f"Would create: {created}")
        else:
            logging.info(f"Created: {created}")

    logging.info(f"Total created: {created_total}")

if __name__ == "__main__":
    app()
