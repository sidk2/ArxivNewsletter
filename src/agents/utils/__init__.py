from strands.models import BedrockModel
from boto3 import Session
from ...constants import OPENAI_OSS_20B_ID

def load_paper_summary_prompt(file_path: str, **kwargs) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(**kwargs)


def get_boto3_session() -> Session:
    return Session()


def get_bedrock_model() -> BedrockModel:
    session = get_boto3_session()

    bedrock_model = BedrockModel(
        model_id=OPENAI_OSS_20B_ID,
        boto_session=session,
        temperature=0.3,
        # streaming=False,
    )

    return bedrock_model
