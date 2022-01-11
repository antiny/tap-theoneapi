"""Stream type classes for tap-theoneapi."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_theoneapi.client import TheOneApiStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class BooksStream(TheOneApiStream):
    """Define custom stream."""
    name = "books"
    path = "/book"
    records_jsonpath = "$.docs[*]"
    primary_keys = ["_id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "_id",
            th.StringType,
            description="The book's system ID"
        ),
        th.Property(
            "age",
            th.IntegerType,
            description="The user's age in years"
        ),
    ).to_dict()


class CharactersStream(TheOneApiStream):
    """Define custom stream."""
    name = "characters"
    path = "/character"
    primary_keys = ["_id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("_id", th.StringType),
        th.Property("birth", th.StringType),
        th.Property("death", th.StringType),
        th.Property("gender", th.StringType),
        th.Property("race", th.StringType),
        th.Property("spouse", th.StringType),
        th.Property("wikiUrl", th.StringType),

    ).to_dict()
