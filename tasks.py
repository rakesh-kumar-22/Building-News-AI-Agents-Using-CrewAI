from crewai import Task
from tools import tool
from agent import news_researcher,news_writer
# Research task

research_task=Task(
    description=(
        "Identify the next big thing abot the {topic}"
        "Focus on identifying the pros ,cons and overall narrative"
        "Your final report should clearly articulate the key points"
        "its amrket oppertunities and potential risks."
    ),
    expected_output="A comphrensive 3 paragraph long report",
    tools=[tool],
    agent=news_researcher
)

#writing task with language model configuration
write_task=Task(
    description=(
        "Compose an insightful article on {topic}"
        "Focus on the latest trends and how it impacts the industry"
        "This article should be easy to understand,positive and engaging"
    ),
    expected_output="A 4 paragraph article on {topic} formatted as markdown",
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file="new-blog-post.md"
) 