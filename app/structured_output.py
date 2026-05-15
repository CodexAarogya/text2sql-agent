from typing import TypedDict, Annotated, Optional

class ModelResponse(TypedDict):
    """
    Structured response format for Text-to-SQL agent outputs.

    This schema defines the standardized output returned after converting
    natural language queries into PostgreSQL queries and interpreting results.

    Attributes:
        query (str):
            PostgreSQL query generated from the user's natural language input.

        messages (Optional[str]):
            Optional summary or explanation of database-related results,
            such as counts, aggregations, or computed insights.

        values (Optional[list[str]]):
            Optional list of extracted result values from the database,
            such as names, IDs, or other returned fields in string format.

        status (bool):
            Indicates whether the query generation/execution was successful.
            True = success, False = failure.
    """
    query: Annotated[str, "PostgreSQL query equivalent to natural-language input."]
    messages: Annotated[Optional[str], "If output contains any information related to db (example: total counts)"]
    values: Annotated[Optional[list[str]], "If output contains collection of values like arrays, dictionary, lists, etc (example: name of customers from USA)"]
    status: Annotated[bool, "Query response status (success - True, failure - False)"]