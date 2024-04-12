import requests

def deleter_action(token_deleter, vanity_url, guild_id):
    try:
        delete_response = requests.delete(f"https://discord.com/api/v10/invites/{vanity_url}", headers={"Authorization": token_deleter})
        print(f"Davet bağlantısı silme işlemi: {delete_response.status_code}")

        request_body = {"code": vanity_url}
        patch_response = requests.patch(f"https://discord.com/api/v7/guilds/{guild_id}/vanity-url", json=request_body, headers={"Authorization": token_deleter})
        print(f"Sunucu URL'sini değiştirme işlemi: {patch_response.status_code}")
    except Exception as e:
        print('Hata oluştu:', e)

def main():
    token_deleter = input('Token: ')
    vanity_url = input('Vanity-URL: ')
    guild_id = input('Sunucu id: ')
    deleter_action(token_deleter, vanity_url, guild_id)

if __name__ == "__main__":
    main()