import asyncio

from task.clients.client import DialClient
from task.constants import DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role


async def start(stream: bool) -> None:
    #TODO:
    # 1.1. Create DialClient
    # (you can get available deployment_name via https://ai-proxy.lab.epam.com/openai/models
    #  you can import Postman collection to make a request, file in the project root `dial-basics.postman_collection.json`
    #  don't forget to add your API_KEY)

    dial_client = DialClient(deployment_name="gpt-4")

    # 1.2. Create CustomDialClient

    custom_dial_client = DialClient(deployment_name="gpt-4")

    # set client
    client = dial_client

    # 2. Create Conversation object

    conversation = Conversation()

    # 3. Get System prompt from console or use default -> constants.DEFAULT_SYSTEM_PROMPT and add to conversation
    #    messages.

    system_prompt = input("Enter system prompt (press Enter for default): ").strip()
    if not system_prompt:
        system_prompt = DEFAULT_SYSTEM_PROMPT
        print("Using default system prompt.")
    else:
        print("Using custom system prompt.")

    conversation.add_message(Message(role=Role.SYSTEM, content=system_prompt))

    # 4. Use infinite cycle (while True) and get user message from console
   
   
    
    
    # 9. Test it with DialClient and CustomDialClient
    # 10. In CustomDialClient add print of whole request and response to see what you send and what you get in response

    while True:
        user_input = input("You: ").strip()

         # 5. If user message is `exit` then stop the loop
        if user_input.lower() == "exit":
            print("Exiting the chat.")
            break

        # 6. Add user message to conversation history (role 'user')
        conversation.add_message(Message(role=Role.USER, content=user_input))

        # 7. If `stream` param is true -> call DialClient#stream_completion()
        if stream:
            response = await client.stream_completion(conversation.get_messages())
        else:
            response = client.get_completion(conversation.get_messages())
            # print response content
            print(f"Assistant: {response.content}")

        # 8. Add generated message to history
        conversation.add_message(Message(role=Role.AI, content=response.content))

asyncio.run(
    start(True)
)
