"""CLI command at root, inferring the file formats from the file type and performing the needed operation."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from loguru import logger
import typer

from gatpack.core.infer_and_run_command import infer_and_run_command


def infer(
    # Note: This should probably be a list of strings like the other was for globbing.
    file: Annotated[
        Path,
        typer.Argument(
            help="Incoming file to be processed.",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Argument(help="Where to save the resulting files"),
    ],
) -> None:
    """CLI command at root, inferring the file formats from the file type and performing the needed operation."""
    try:
        logger.info(f"Inferring needed operation and processing file at {file}")
        logger.info(f"And saving to {output}")
        infer_and_run_command(file, output)
    except Exception as e:
        logger.error(f"Failed to infer and run command: {e}")
        raise typer.Exit(1)
