class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """ 𝙷𝙴𝚑  {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """
𝙷𝚎𝚛𝚎 𝚊𝚛𝚎 𝚜𝚘𝚖𝚎 𝚍𝚎𝚝𝚊𝚒𝚕𝚜 𝚢𝚘𝚞 𝚗𝚎𝚎𝚍 𝚝𝚘 𝚔𝚗𝚘𝚠.

✯ 𝙱𝙾𝚃 𝚃𝚈𝙿𝙴 : 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚅𝟹	
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href="https://t.me/SinhalaCryptoNews">Sinhala Crypto News 𝚂</a>
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽3 
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: 𝚟𝟹.𝟷.𝟷 [ 𝙱𝙴𝚃𝙰 ]
✯ 𝚂𝙾𝚄𝚁𝙲𝙴 : 🔐"""  

      
    MANUELFILTER_TXT = """𝙷𝚎𝚕𝚙: <b>Filters</b>
- 𝙵𝚒𝚕𝚝𝚎𝚛 𝚒𝚜 𝚝𝚑𝚎 𝚏𝚎𝚊𝚝𝚞𝚛𝚎 𝚠𝚎𝚛𝚎 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚜𝚎𝚝 𝚊𝚞𝚝𝚘𝚖𝚊𝚝𝚎𝚍 𝚛𝚎𝚙𝚕𝚒𝚎𝚜 𝚏𝚘𝚛 𝚊 𝚙𝚊𝚛𝚝𝚒𝚌𝚞𝚕𝚊𝚛 𝚔𝚎𝚢𝚠𝚘𝚛𝚍 𝚊𝚗𝚍 𝚝𝚎𝚜𝚜𝚊 𝚠𝚒𝚕𝚕 𝚛𝚎𝚜𝚙𝚘𝚗𝚍 𝚠𝚑𝚎𝚗𝚎𝚟𝚎𝚛 𝚊 𝚔𝚎𝚢𝚠𝚘𝚛𝚍 𝚒𝚜 𝚏𝚘𝚞𝚗𝚍 𝚝𝚑𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 
<b>NOTE:</b>
𝟷. 𝚃𝚑𝚒𝚜 𝚋𝚘𝚝 𝚜𝚑𝚘𝚞𝚕𝚍 𝚑𝚊𝚟𝚎 𝚊𝚍𝚖𝚒𝚗 𝚙𝚛𝚒𝚟𝚒𝚕𝚕𝚊𝚐𝚎. 
𝟸. 𝚘𝚗𝚕𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚌𝚊𝚗 𝚊𝚍𝚍 𝚏𝚒𝚕𝚝𝚎𝚛𝚜 𝚒𝚗 𝚊 𝚌𝚑𝚊𝚝. 
𝟹. 𝚊𝚕𝚎𝚛𝚝 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚑𝚊𝚟𝚎 𝚊 𝚕𝚒𝚖𝚒𝚝 𝚘𝚏 𝟼𝟺 𝚌𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """𝙷𝚎𝚕𝚙: <b>Buttons</b>
- 𝙱𝚘𝚝 𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝚜 𝚋𝚘𝚝𝚑 𝚞𝚛𝚕 𝚊𝚗𝚍 𝚊𝚕𝚎𝚛𝚝 𝚒𝚗𝚕𝚒𝚗𝚎 𝚋𝚞𝚝𝚝𝚘𝚗𝚜.
<b>NOTE:</b>
𝟷. 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚠𝚒𝚕𝚕 𝚗𝚘𝚝 𝚊𝚕𝚕𝚘𝚠𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚎𝚗𝚍 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚠𝚒𝚝𝚑𝚘𝚞𝚝 𝚊𝚗𝚢 𝚌𝚘𝚗𝚝𝚎𝚗𝚝, 𝚜𝚘 𝚌𝚘𝚗𝚝𝚎𝚗𝚝 𝚒𝚜 𝚖𝚊𝚗𝚍𝚊𝚝𝚘𝚛𝚢. 
𝟸. 𝙱𝚘𝚝 𝚜𝚞𝚙𝚙𝚘𝚛𝚝𝚜 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚠𝚒𝚝𝚑 𝚊𝚗𝚢 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚖𝚎𝚍𝚒𝚊 𝚝𝚢𝚙𝚎. 
𝟹. 𝙱𝚞𝚝𝚝𝚘𝚗𝚜 𝚜𝚑𝚘𝚞𝚕𝚍 𝚋𝚎 𝚙𝚛𝚘𝚙𝚎𝚛𝚕𝚢 𝚙𝚊𝚛𝚜𝚎𝚍 𝚊𝚜 𝚖𝚊𝚛𝚔𝚍𝚘𝚠𝚗 𝚏𝚘𝚛𝚖𝚊𝚝
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/SECLK)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message, You should use @NETFLIXLKBOT to get Movies )</code>"""
    AUTOFILTER_TXT = """𝙷𝚎𝚕𝚙: <b>Auto Filter</b>
<b>NOTE:</b>
  𝟷. 𝙼𝚊𝚔𝚎 𝚖𝚎 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗 𝚘𝚏 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚒𝚏 𝚒𝚝'𝚜 𝚙𝚛𝚒𝚟𝚊𝚝𝚎. 
  𝟸. 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚝𝚑𝚊𝚝 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚍𝚘𝚎𝚜 𝚗𝚘𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚌𝚊𝚖𝚛𝚒𝚙𝚜, 𝚙𝚘𝚛𝚗 𝚊𝚗𝚍 𝚏𝚊𝚔𝚎 𝚏𝚒𝚕𝚎𝚜. 
  𝟹. 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚝𝚑𝚎 𝚕𝚊𝚜𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚖𝚎 𝚠𝚒𝚝𝚑 𝚚𝚞𝚘𝚝𝚎𝚜. 
  
  𝙸'𝚕𝚕 𝚊𝚍𝚍 𝚊𝚕𝚕 𝚝𝚑𝚎 𝚏𝚒𝚕𝚎𝚜 𝚒𝚗 𝚝𝚑𝚊𝚝 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚝𝚘 𝚖𝚢 𝚍𝚋."""
    CONNECTION_TXT = """𝙷𝚎𝚕𝚙 : <b>Connections</b>
 - 𝚄𝚜𝚎𝚍 𝚝𝚘 𝚌𝚘𝚗𝚗𝚎𝚌𝚝 𝚋𝚘𝚝 𝚝𝚘 𝙿𝙼 𝚏𝚘𝚛 𝚖𝚊𝚗𝚊𝚐𝚒𝚗𝚐 𝚏𝚒𝚕𝚝𝚎𝚛𝚜 
 - 𝚒𝚝 𝚑𝚎𝚕𝚙𝚜 𝚝𝚘 𝚊𝚟𝚘𝚒𝚍 𝚜𝚙𝚊𝚖𝚖𝚒𝚗𝚐 𝚒𝚗 𝚐𝚛𝚘𝚞𝚙𝚜. 
<b>NOTE:</b>
𝟷. 𝙾𝚗𝚕𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚌𝚊𝚗 𝚊𝚍𝚍 𝚊 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗.
2. 𝚂𝚎𝚗𝚍  <code>/connect</code> 𝚏𝚘𝚛 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚗𝚐 𝚖𝚎 𝚝𝚘 𝚞𝚛 𝙿𝙼 
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝙷𝚎𝚕𝚙: <b>Extra Modules</b>
<b>NOTE:</b>
𝚝𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚎𝚡𝚝𝚛𝚊 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜 𝚘𝚏 𝚝𝚎𝚜𝚜𝚊 
<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
𝚃𝚑𝚒𝚜 𝚖𝚘𝚍𝚞𝚕𝚎 𝚘𝚗𝚕𝚢 𝚠𝚘𝚛𝚔𝚜 𝚏𝚘𝚛 𝚖𝚢 𝚊𝚍𝚖𝚒𝚗𝚜
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
★ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    
    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, 
ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ᴏʀ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ᴍᴏᴠɪᴇ ғᴏʟʟᴏᴡ ᴛʜᴇ ғᴏʀᴍᴀᴛ ʙᴇʟᴏᴡ
Uncharted | Dune 2021 | Troll 2022 720p 

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀ sᴇʀɪᴇs ғᴏʟʟᴏᴡ ᴛʜᴇ ғᴏʀᴍᴀᴛ ʙᴇʟᴏᴡ
Loki S01E01 | You S03 | Wednesday S01 720p

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""
    
    
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : Sinhala Crypto News
• ᴀʙᴏᴜᴛ : <a href='https://t.me/SinhalaCryptoNews'>Sinhala Crypto News</a>
• ᴅᴍ ʟɪɴᴋ : <a href='https://t.me/SinhalaFilms_LK'>Sinhala Crypto News</a></b>"""
