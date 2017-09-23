from trello import TrelloClient
import configparser

SETTINGS_FILE = "settings.cfg"


def main():
    # read settings
    settings = configparser.ConfigParser()
    settings.read(SETTINGS_FILE, encoding="utf-8")

    webhook_url = settings.get("Flask", "my_url") + "/webhook"
    api_key = settings.get("Trello", "api_key")
    token = settings.get("Trello", "token")
    board_name = settings.get("Trello", "board_name")

    # fetch a board
    client = TrelloClient(
        api_key=api_key,
        token=token
    )

    all_boards = client.list_boards()
    webhook_board = None

    for board in all_boards:
        if board.name == board_name:
            webhook_board = board
            break

    if webhook_board is None:
        print("Board [" + board_name + "] is not found.")
        return

    # register a board to webhook
    webhook = client.create_hook(callback_url=webhook_url, id_model=webhook_board.id)

    if webhook is False:
        print("Failed webhook registration")
        return

    print("Registration succeeded!")


if __name__ == "__main__":
    main()
