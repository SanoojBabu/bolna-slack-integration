import json

def transform_bolna_to_slack(data: dict) -> dict:
    call_id = data.get("id")
    agent_id = data.get("agent_id")
    duration = data.get("conversation_duration")
    transcription = (data.get("transcript"))
    summary = (data.get("summary"))
    tele = data.get("telephony_data")
    link = tele.get("recording_url")

    response = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "📞 Call Log Summary",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Execution ID*:\n{call_id}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Agent ID*:\n{agent_id}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Duration*:\n{duration}"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Transcription*\n\n```\n{transcription}```"
                }

            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"📝 *Summary*\n{summary}"
                }
            },
            {
                "type": "markdown",
                "text": f"**For Full Recording:** [Click Here]({link})"
            }
        ]
    }

    print(json.dumps(response, indent=2))
    return response
