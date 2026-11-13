def prepare_history(messages):
  history = []
  for message in messages:
    if message.role == "assistant":
      role = "model"
    else:
      role = message.role
    history.append({
      "role": role,
      "parts": [
        {"text": message.content}
      ]
    })
  return history