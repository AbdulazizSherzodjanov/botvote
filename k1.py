from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
BTN_STAT = 'Statistika📊'
ID_DICT = [] 
mks={}
mk1 = '1-maktab'
mk3 = '3-maktab'
mk4 = '4-maktab'
mk5 = '5-maktab'
mk6 = '6-maktab'
mk7 = '7-maktab'
mk8 = '8-maktab'
mk9 = '9-maktab'
mk10 = '10-maktab'
mk11 = '11-maktab'
mk12 = '12-maktab'
mk13 = '13-maktab'
mk14 = '14-maktab'
mk15 = '15-maktab'
mk16 = '16-maktab'
mk17 = '17-maktab'
mk18 = '18-maktab'
mk19 = '19-maktab'
mk20 = '20-maktab'
mk21 = '21-maktab'
mk22 = '22-maktab'
mk23 = '23-maktab'
mk24 = '24-maktab'
mk25 = '25-maktab'
mk26 = '26-maktab'
mk27 = '27-maktab'
mk28 = '28-maktab'
mk29 = '29-maktab'
mk30 = '30-maktab'
mk31 = '31-maktab'
mk32 = '32-maktab'
mk34 = '34-maktab'
mk36 = '36-maktab'
mk37 = '37-maktab'
mk38 = '38-maktab'
mk40 = '40-maktab'
mk41 = '41-maktab'
mk43 = '43-maktab'
mk44 = '44-maktab'
mk45 = '45-maktab'
mk46 = '46-maktab'
mk47 = '47-maktab'
mk50 = '50-maktab'
mk51 = '51-maktab'
mk66 = '66-maktab'
mk67 = '67-maktab'
mk74 = '74-maktab'
mk75 = '75-maktab'
mk76 = '76-maktab'
mk85 = '85-maktab'
mk88 = '88-maktab'
mkdim = '1-DIMI'
mkint = '40-INT'
mks[mk1] = []
mks[mk3] = []
mks[mk4] = []
mks[mk5] = []
mks[mk6] = []
mks[mk7] = []
mks[mk8] = []
mks[mk9] = []
mks[mk10] = []
mks[mk11] = []
mks[mk12] = []
mks[mk13] = []
mks[mk14] = []
mks[mk15] = []
mks[mk16] = []
mks[mk17] = []
mks[mk18] = []
mks[mk19] = []
mks[mk20] = []
mks[mk21] = []
mks[mk22] = []
mks[mk23] = []
mks[mk24] = []
mks[mk25] = []
mks[mk26] = []
mks[mk27] = []
mks[mk28] = []
mks[mk29] = []
mks[mk30] = []
mks[mk31] = []
mks[mk32] = []
mks[mk34] = []
mks[mk36] = []
mks[mk37] = []
mks[mk38] = []
mks[mk40] = []
mks[mk41] = []
mks[mk43] = []
mks[mk44] = []
mks[mk45] = []
mks[mk46] = []
mks[mk47] = []
mks[mk50] = []
mks[mk51] = []
mks[mk66] = []
mks[mk67] = []
mks[mk74] = []
mks[mk75] = []
mks[mk76] = []
mks[mk85] = []
mks[mk88] = []
mks[mkdim] = []
mks[mkint] = []
button = [
    [
        InlineKeyboardButton(text=mk1, callback_data=mk1),
        InlineKeyboardButton(text=mk3, callback_data=mk3),
    ],
        [
        InlineKeyboardButton(text=mk4, callback_data=mk4),
        InlineKeyboardButton(text=mk5, callback_data=mk5),
    ],
        [
        InlineKeyboardButton(text=mk6, callback_data=mk6),
        InlineKeyboardButton(text=mk7, callback_data=mk7),
    ],
            [
        InlineKeyboardButton(text=mk8, callback_data=mk8),
        InlineKeyboardButton(text=mk9, callback_data=mk9),
    ],        [
        InlineKeyboardButton(text=mk10, callback_data=mk10),
        InlineKeyboardButton(text=mk11, callback_data=mk11),
    ],        [
        InlineKeyboardButton(text=mk12, callback_data=mk12),
        InlineKeyboardButton(text=mk13, callback_data=mk13),
    ],        [
        InlineKeyboardButton(text=mk14, callback_data=mk14),
        InlineKeyboardButton(text=mk15, callback_data=mk15),
    ],        [
        InlineKeyboardButton(text=mk16, callback_data=mk16),
        InlineKeyboardButton(text=mk17, callback_data=mk17),
    ],        [
        InlineKeyboardButton(text=mk18, callback_data=mk18),
        InlineKeyboardButton(text=mk19, callback_data=mk19),
    ],        [
        InlineKeyboardButton(text=mk20, callback_data=mk20),
        InlineKeyboardButton(text=mk21, callback_data=mk21),
    ],        [
        InlineKeyboardButton(text=mk22, callback_data=mk22),
        InlineKeyboardButton(text=mk23, callback_data=mk23),
    ],        [
        InlineKeyboardButton(text=mk24, callback_data=mk24),
        InlineKeyboardButton(text=mk25, callback_data=mk25),
    ],        [
        InlineKeyboardButton(text=mk26, callback_data=mk26),
        InlineKeyboardButton(text=mk27, callback_data=mk27),
    ],        [
        InlineKeyboardButton(text=mk28, callback_data=mk28),
        InlineKeyboardButton(text=mk29, callback_data=mk29),
    ],        [
        InlineKeyboardButton(text=mk30, callback_data=mk30),
        InlineKeyboardButton(text=mk31, callback_data=mk31),
    ],        [
        InlineKeyboardButton(text=mk32, callback_data=mk32),
        InlineKeyboardButton(text=mk34, callback_data=mk34),
    ],        [
        InlineKeyboardButton(text=mk36, callback_data=mk36),
        InlineKeyboardButton(text=mk37, callback_data=mk37),
    ],        [
        InlineKeyboardButton(text=mk38, callback_data=mk38),
        InlineKeyboardButton(text=mk40, callback_data=mk40),
    ],        [
        InlineKeyboardButton(text=mk41, callback_data=mk41),
        InlineKeyboardButton(text=mk43, callback_data=mk43),
    ],        [
        InlineKeyboardButton(text=mk44, callback_data=mk44),
        InlineKeyboardButton(text=mk45, callback_data=mk45),
    ],        [
        InlineKeyboardButton(text=mk46, callback_data=mk46),
        InlineKeyboardButton(text=mk47, callback_data=mk47),
    ],        [
        InlineKeyboardButton(text=mk50, callback_data=mk50),
        InlineKeyboardButton(text=mk51, callback_data=mk51),
    ],        [
        InlineKeyboardButton(text=mk66, callback_data=mk66),
        InlineKeyboardButton(text=mk67, callback_data=mk67),
    ],        [
        InlineKeyboardButton(text=mk74, callback_data=mk74),
        InlineKeyboardButton(text=mk75, callback_data=mk75),
    ],        [
        InlineKeyboardButton(text=mk76, callback_data=mk76),
        InlineKeyboardButton(text=mk85, callback_data=mk85),
    ],        [
        InlineKeyboardButton(text=mk88, callback_data=mk88),
        InlineKeyboardButton(text=mkdim, callback_data=mkdim),
    ],        [
        InlineKeyboardButton(text=mkint, callback_data=mkint),
    ],
    
]
statistica = ReplyKeyboardMarkup([
    [BTN_STAT]
], resize_keyboard=True)
STAT=0
channel=[
    [
        InlineKeyboardButton(text='Kanal', url='https://t.me/basmala_bilim'),
        InlineKeyboardButton(text='Obuna bo\'ldim', callback_data='subscribe')
    ]
]
ids = '@basmala_bilim'
async def start(update,context):
    await update.message.reply_html(f'<b>Maktablarga ovoz beruvchi botga xush kelibsiz😊 \n\n❕Iltimos kanalga azo bo\'ling</b>',reply_markup=InlineKeyboardMarkup(channel))
    return STAT

async def callback(update, context):
    id1=1567764330
    id2=5672908862
    id3=6036909801
    user_id = update.effective_user.id
    query = update.callback_query
    if query.data == 'subscribe':
        chat_member =  await context.bot.get_chat_member(ids, user_id)
        if chat_member.status == "member" or chat_member.status == 'creator':
            await query.message.delete()
            if user_id == id1 or user_id == id2 or user_id == id3:
                await query.message.reply_text('Siz ovoz berishinggiz mumkin😊 \n\nQaysi makttabga ovoz berasiz❔', reply_markup=InlineKeyboardMarkup(button))
            elif user_id in ID_DICT:
                await query.message.reply_text("Siz avval ovoz bergansiz.", reply_markup=statistica)
            else:
                await query.message.reply_text('Siz ovoz berishinggiz mumkin😊 \n\nQaysi makttabga ovoz berasiz❔', reply_markup=InlineKeyboardMarkup(button))
                ID_DICT.append(user_id)
                

        else:
            await query.message.reply_text("Siz kanalga obuna bo'lmagansiz. Iltimos, avval kanalga obuna bo'ling!")
    if query.data == mk1:
        mks[mk1].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk3:
        mks[mk3].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk4:
        mks[mk4].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk5:
        mks[mk5].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk6:
        mks[mk6].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk7:
        mks[mk7].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk8:
        mks[mk8].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk9:
        mks[mk9].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk10:
        mks[mk10].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk11:
        mks[mk11].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk12:
        mks[mk12].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk13:
        mks[mk13].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk14:
        mks[mk14].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk15:
        mks[mk15].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk16:
        mks[mk16].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk17:
        mks[mk17].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk18:
        mks[mk18].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk19:
        mks[mk19].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk20:
        mks[mk20].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk21:
        mks[mk21].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk22:
        mks[mk22].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk23:
        mks[mk23].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk24:
        mks[mk24].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk25:
        mks[mk25].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk26:
        mks[mk26].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk27:
        mks[mk27].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk28:
        mks[mk28].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk29:
        mks[mk29].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk30:
        mks[mk30].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk31:
        mks[mk31].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk32:
        mks[mk32].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk34:
        mks[mk34].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk36:
        mks[mk36].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk37:
        mks[mk37].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk38:
        mks[mk38].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk40:
        mks[mk40].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk41:
        mks[mk41].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk43:
        mks[mk43].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk44:
        mks[mk44].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk45:
        mks[mk45].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk46:
        mks[mk46].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk47:
        mks[mk47].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk50:
        mks[mk50].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk51:
        mks[mk51].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk66:
        mks[mk66].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk67:
        mks[mk67].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk74:
        mks[mk74].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk75:
        mks[mk75].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk76:
        mks[mk76].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk85:
        mks[mk85].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mk88:
        mks[mk88].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mkdim:
        mks[mk1].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
    if query.data == mkint:
        mks[mk1].append(1)
        await query.message.delete()
        await query.message.reply_text(f'Ovoz muvaffaqiyatli qabul qilindi', reply_markup=statistica)
async def statistika(update, context):
    lens = []
    for k, q in mks.items():
        a = len(q)
        lens.append(f'{a}ball {k}da')
    lens.sort(reverse=True)
    statistic_text = "\n".join(lens)
    await update.message.reply_text(f'Maktablar statistikasi📊 \n{statistic_text}')
  
def main():
    updater = ApplicationBuilder().token('6686527588:AAHW6_ov08_ndmdw5tx7qNuDV8sD7LbeLIg').build()
    updater.add_handler(CallbackQueryHandler(callback))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STAT: [MessageHandler(filters=filters.Regex('^('+BTN_STAT+')$'), callback=statistika)]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    updater.add_handler(conv_handler)
    updater.run_polling()
main()