from groq import Groq
import streamlit as st

def count_tokens(messages: list) -> int:
    """Rough token estimate: ~1.3 tokens per word."""
    total_words = sum(len(m["content"].split()) for m in messages)
    return int(total_words * 1.3)

def trim_history(messages: list, max_tokens: int = 6000) -> list:
    """Keep most recent messages within token budget."""
    trimmed = []
    token_count = 0
    for msg in reversed(messages):
        tokens = int(len(msg["content"].split()) * 1.3)
        if token_count + tokens > max_tokens:
            break
        trimmed.insert(0, msg)
        token_count += tokens
    return trimmed

def format_messages_for_api(
    history: list,
    system_prompt: str,
    max_tokens: int = 6000
) -> list:
    """Build the messages array for the Groq API call."""
    trimmed = trim_history(history, max_tokens)
    return [{"role": "system", "content": system_prompt}, *trimmed]

def stream_response(client: Groq, messages: list, model: str, **kwargs):
    """Stream response and return full text."""
    stream = client.chat.completions.create(
        model=model, messages=messages, stream=True, **kwargs
    )
    return st.write_stream(
        chunk.choices[0].delta.content or ""
        for chunk in stream
    )