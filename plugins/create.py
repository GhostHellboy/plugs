# Made By @Kraken_The_BadASS
# Keep Credits else gay....

"""Create Private Groups
Available Commands:
.create (b|g) GroupName"""
from telethon.tl import functions
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="create (b|g|c) (.*)"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="create (b|g|c) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    event = await edit_or_reply(event, "Creating wait sar.....")
    if type_of_group == "b":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@sarah_robot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            await event.client(
                functions.messages.DeleteChatUserRequest(
                    chat_id=created_chat_id, user_id="@sarah_robot"
                )
            )
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Group `{}` created successfully. Join {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group in ["g", "c"]:
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about="Created By Hêllẞø†",
                    megagroup=type_of_group != "c",
                )
            )

            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Channel `{}` created successfully. Join {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    else:
        await event.edit("Read `.plinfo create` to know how to use me")


CmdHelp("create").add_command(
    "create b", "Name of your grp", "Creates a super and send you link"
).add_command(
    "create g", "Name of your grp", "Creates a private grp and send you link"
).add_command(
    "create c", "Name of your channel", "Creates a channel and sends you link"
).add()