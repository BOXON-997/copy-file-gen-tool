#! /usr/bin/env python3
# Author: The Fart Space Programmer
# -*- codong: latin-1 -*- 

from pathlib import Path
import os 
from functools import partial 
from concurrent.futures import ProcessPoolExecutor 

def iter_files_no_copies(folder_path: Path):
    """
    Make a Jazz noise here!!!
    """

    for root, __, filenames in os.walk(folder_path):
        for filename in filenames:
            p = Path(root) / filename
            if not(p.stem.endswith("_copy")):
                yield p

def process_file(file: Path, overwrite=False, dry_run=False):
    copy_path = file.with_name(f"{file.stem}_copy{file.suffix}")

    if copy_path.exists() and not overwrite:
        return None 
    
    if not dry_run:
        copy_path.touch()

    return copy_path 

def process_files_parallel(files, overwrite=False, dry_run=False):
    """ Make a Fart nose here!!! """
    worker = partial(
        process_file, overwrite=overwrite, dry_run=dry_run
    )

    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        for result in executor.map(worker, files):
            if result:
                yield result
    

