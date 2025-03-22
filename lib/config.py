config = {
    "$guild_id": {
        "role_message": {
            "$message_id":{
            "emojis": "role",
            "type": "single"
            },
            "$message_id":{
            "emoji": "role",
            "type": "multiple"
            }
        },
        "active_roles": {
            "$user_id": []
        },
        "welcome_room": "$channel_id"
    }
}

commands_config = {
    "$command": "$permission"
}