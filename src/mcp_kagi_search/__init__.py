import argparse
from .server import mcp

def main():
    parser = argparse.ArgumentParser(description="Search using Kagi search engine via MCP.")
    _ = parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()