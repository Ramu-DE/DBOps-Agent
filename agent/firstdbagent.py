from strands import Agent, tool
import boto3
import os

# 1. Define the AI model
model = 'us.anthropic.claude-sonnet-4-20250514-v1:0'
# TODO1: Define the model here

# 2. Create a tool to list Aurora clusters
@tool
def list_aurora_clusters() -> str:
    """List all Aurora clusters in the current region."""
    rds = boto3.client('rds',region_name=os.getenv('AWS_REGION'))
    response = rds.describe_db_clusters()
    clusters = response['DBClusters']           
    return clusters
# TODO2: Add database tool here

# 3. Create the system prompt
prompt = """You are a database assistant. You can list Aurora clusters. Keep responses simple and helpful."""
# TODO3: Add the system prompt here

# 4. Create the agent
agent = Agent(
    system_prompt=prompt,
    model=model,
    tools=[list_aurora_clusters]
)

while True:
    question = input("\n💬 Your question: ")
    if question.lower() in ['exit', 'quit']:
        break
    response = agent(question)
    #print(f"📊 {response}")
