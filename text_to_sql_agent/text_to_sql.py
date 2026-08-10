import os

from dotenv import load_dotenv

from sqlalchemy import text, inspect

from sql_statements import engine

from smolagents import CodeAgent, OpenAIServerModel, tool


load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")


with engine.connect() as connection:
    result = connection.execute(
        text("SELECT * FROM receipts")
    )

inspector = inspect(engine)

columns_info = [
    (col["name"], col["type"])
    for col in inspector.get_columns("receipts")
]

table_description = (
    "Table 'receipts':\n"
    + "\n".join(
        f"- {name}: {col_type}"
        for name, col_type in columns_info
    )
)

@tool
def sql_engine(query: str) -> str:
    """
    Execute a SQL query against the receipts table.

    The available table is:

    receipts:
    - receipt_id
    - customer_name
    - price
    - tip

    Args:
        query: The SQL query to execute.
    """

    with engine.connect() as connection:

        result = connection.execute(
            text(query)
        )

        # Convert database rows into text
        # so the agent can understand the result.
        output = ""

        for row in result:
            output += "\n" + str(row)

        return output


model = OpenAIServerModel(
    model_id="deepseek-v4-flash",
    api_base="https://api.deepseek.com",
    api_key=deepseek_api_key,
)


agent = CodeAgent(
    tools=[sql_engine],
    model=model,
)


agent.run("What is the difference between the highest and lowest receipt?")