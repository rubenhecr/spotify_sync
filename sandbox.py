from spotify_user_auth import SpotifyAPI

client_id = "a0814e8cfd6c467ebf47eec3eb5fbbab"
client_secret = "f4cbcf7a681e4cf480f902dbd47f310b"

def main():

    spotify_client = SpotifyAPI(client_id)
    result = spotify_client.perform_auth()
    print(result)

if __name__ == "__main__":
    main()