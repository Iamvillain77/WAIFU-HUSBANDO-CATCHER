class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5909658683"
    sudo_users = "5909658683", "5909658683"
    GROUP_ID = -1002062270433
    TOKEN = "7655351916:AAFtcg28puGFFa2_bl3liWrCShsf43RDtgc"
    mongo_url = "mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = [""https://files.catbox.moe/sjzwp3.jpg""]
    SUPPORT_CHAT = "oldskoolgc"
    UPDATE_CHAT = "oldskoolgc"
    BOT_USERNAME = "Waifu_World_Robot"
    CHARA_CHANNEL_ID = "-1002270830955"
    api_id = 26062263
    api_hash = "f22fee8f0b782fbdf3a91a342763f56d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
