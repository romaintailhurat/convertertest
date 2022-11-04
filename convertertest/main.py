from sdmx2jsonld.transform.parser import Parser
from prefect import flow, task
from pathlib import Path

@task
def convert():

    home = str(Path(__file__).cwd())

    with open(home + "\\turtles\\structures-tourism.ttl") as ttl:
        parser = Parser()
        # Base mode of the parser, will print the result =)
        parser.parsing(content=ttl)
    

@flow
def run():
    convert()

run()


