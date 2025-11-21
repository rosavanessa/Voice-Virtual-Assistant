import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig


load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

user_name = "Alex"
schedule = "Sales Meeting with Taipy at 10.00; Gym with Sophie at 17:00"
prompt = f"You are a helpful assistnt. Your interlocutor has the following schedule. {schedule} "
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
  "agent": {
    "prompt": {
      "prompt": prompt,
    },
    "first_message": first_message,
  },
}

config = ConversationConfig(
  conversation_config_override=conversation_override,
  extra_body={},
  dynamic_variables={},
)

client = ElevenLabs(api_key=API_KEY)

conversation = Conversation(
  client,
  AGENT_ID,
  config=config,
  requires_auth=True,
  audio_interface=DefaultAudioInterface(),
)