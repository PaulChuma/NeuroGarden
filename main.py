# Entry point for NeuroGarden CLI demo
from core.agent import Agent

def main():
    agent = Agent("Echo")
    while True:
        msg = input("You: ")
        if msg.lower() in ('exit', 'quit'):
            break
        print(agent.respond(msg))

if __name__ == "__main__":
    main()
