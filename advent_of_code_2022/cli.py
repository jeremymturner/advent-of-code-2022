"""Console script for advent_of_code_2022."""
import sys
import click


@click.command()
@click.argument('day')
def main(day):
    if day == "dayone":
        from advent_of_code_2022.dayone import calorie_counting



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
