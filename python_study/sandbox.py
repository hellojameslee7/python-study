import re
import datetime
import typing


# in order of priority
DATE_PATTERNS = [
    re.compile(r'(\d{4})-(\d{2})-(\d{2})'),
    re.compile(r'(\d{4})(\d{2})(\d{2})')
]


def extract_date_from_filename(filename: str) -> typing.Union[datetime.date, None]:
    """
    Given a filename, will attempt to parse a date from it using various defined date patterns.
    Will return at the first successful date compilation.

    Args:
        filename: string of the filename to pull a date from

    Returns:
        date parsed from the file, if any
    """
    for date_pattern in DATE_PATTERNS:
        matched = date_pattern.search(filename)
        if matched:
            y, m, d = map(int, matched.groups())
            return datetime.date(y, m, d)


def build_filename_to_date_map(filenames: typing.List[str]) -> typing.Dict[str, datetime.date]:
    """
    Given a list of filenames, will return a dictionary of filename: date of the date parsed from the filename.

    Args:
        list of filenames

    Returns:
        dictionary of filename: date
    """
    return {
        k: v for k, v in {
            filename: extract_date_from_filename(filename)
            for filename in filenames
        }.items()
        if v
    }


def get_latest_files(filenames: typing.List[str]) -> typing.List[str]:
    """
    Given a list of filenames, will return the filenames with the latest dates parsed from the filename.

    Args:
        filenames: list of filenames to parse a date from

    Returns:
        list of filenames with the latest date parsed (
            will often be a list of 1 item, unless multiple files have the same date
                )
    """
    filename_to_date_map = build_filename_to_date_map(filenames)

    max_date = max(filename_to_date_map.values())

    return [
        filename for filename, date in filename_to_date_map.items()
        if date == max_date
    ]


def get_earliest_files(filenames: typing.List[str]) -> typing.List[str]:
    """
    Given a list of filenames, will return the filenames with the earliest dates parsed from the filename.

    Args:
        filenames: list of filenames to parse a date from

    Returns:
        list of filenames with the earliest date parsed (
            will often be a list of 1 item, unless multiple files have the same date
                )
    """
    filename_to_date_map = build_filename_to_date_map(filenames)

    min_date = min(filename_to_date_map.values())

    return [
        filename for filename, date in filename_to_date_map.items()
        if date == min_date
    ]
