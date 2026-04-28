def truncate_text(text: str, limit: int = 3000) -> str:
    if not text:
        return ""

    if len(text) <= limit:
        return text

    truncated = text[:limit]

    # avoid cutting in middle of word
    last_space = truncated.rfind(" ")
    if last_space > 0:
        truncated = truncated[:last_space]

    return truncated + "…"