"""Console script for advent_of_code_2022."""
import sys
import click


@click.command()
@click.argument('day')
def main(day):
    if day == "dayone":
        from advent_of_code_2022.dayone import calorie_counting
    
    if day == "daytwo":
        from advent_of_code_2022.daytwo import rock_paper_scissors

    if day == "daythree":
        from advent_of_code_2022.daythree import rutsack

    if day == "dayfour":
        from advent_of_code_2022.dayfour import cleanup
    
    if day == "dayfive":
        from advent_of_code_2022.dayfive import supply

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
