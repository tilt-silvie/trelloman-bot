# Trelloman-bot

## About
Trelloman-bot is slackbot.
Trelloman-bot post message to slack when a card is moved from ToDo list to Doing list or from Doing list to Done list.

## Installation

### install dependencies

``` sh
sudo apt-get install python3 python3-pip
sudo pip3 install flask py-trello slacker

```

### generate config file
Make `settings.cfg` file.

** settings.cfg **
```
[Flask]
my_url  =　# Your server url

[Trello]
api_key     = # Trello API Key
token       = # Trello API Token

board_name          = # Board name which to watch
todo_list_name      = # Todo list name
doing_list_name     = # Doin list name
done_list_name      = # Done list name

[Slack]
token   = # Slack API Token

```

### register Trello webhook
run `register_trello_webhook.py`.

``` sh
python3 trelloman_bot.py &
python3 register_trello_webhook.py
```

if you succeed to register webhook, a message [Registration succeeded!] appear in your terminal.

## Usage

run `trelloman_bot.py`.

``` sh
python3 trelloman_bot.py

```