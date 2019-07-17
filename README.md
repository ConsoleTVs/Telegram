# Telegram

Probably the most minimalist and realistically usable telegram API wrapper.

# Usage

- `-XXXXXXXXXXXXXX`: Chat ID
- `YYYYYYYYYYYYYY`: Bot token

## Determine the chat id to use.
```py
chat_id = -XXXXXXXXXXXXXX
```
## Initiate the telegram instance given the token.
```py
bot = Telegram('YYYYYYYYYYYYYY')
```
## Send a message to a chat.
```py
print(bot.sendMessage({
  'chat_id': chat_id,
  'text': 'Que pasa cracks, soc el erik'
}))
```
## Send a photo to a chat.
```py
print(bot.sendPhoto({
  'chat_id': chat_id,
  'photo': 'https://i.barkpost.com/wp-content/uploads/2016/04/consome-panchi2-1.png'
}))
```
## Send a gif to a chat.
```py
print(bot.sendAnimation({
  'chat_id': chat_id,
  'animation': 'https://media1.tenor.com/images/197ce34997b0f239cf1f7e36dd3b8087/tenor.gif'
}))
```
