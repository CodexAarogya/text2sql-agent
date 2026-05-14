from typing import TypedDict, Optional, Annotated

class ModelOutput(TypedDict):
    """Structured response schema"""

    query: Annotated[
        str,
        "Equivalent query generated for the natural-language input"
    ]

    message: Annotated[
        Optional[str],
        "Summary message or count info"
    ]

    values: Annotated[
        Optional[list[str]],
        "Returned values like names, items, rows"
    ]

    success: Annotated[bool, "Execution Status"]