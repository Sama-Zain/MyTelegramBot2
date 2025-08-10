import os
import json
import gspread
from google.oauth2.service_account import Credentials 
from telebot import TeleBot, types

# ✅  التوكن بتاع البوت هنا
bot = TeleBot("8142209161:AAHP5OYE83laIzLsmB6i_XvlSkmv2zTx9QU", parse_mode="HTML")
ADMIN_ID=1437951187;

#اعدادات Google Sheets
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'])
creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
client = gspread.authorize(creds)

spreadsheet = client.open("BotCodes")
codes_sheet =spreadsheet.worksheet('codes')
user_codes_sheet = spreadsheet.worksheet("user_codes")

# ids فيديوهات الشرح
IPWEB_VIDEO_ID ="BAACAgQAAxkBAAIBcGiV_FL0GRELYcxRHU6C9GyCI06GAAK_GAACtASxUEdytYx3fYrvNgQ"
UNU_VIDEO_ID="BAACAgQAAxkBAAICAAFolgff_rNGfcJXd0ChZjf6ZCQJIQACzxgAArQEsVAzUVLyGujlMTYE"
VKSURF_VIDEO1_ID ="BAACAgQAAxkBAAICImiWDqT_AX6q7suVMGTmaTnnbT1pAALaGAACtASxUCbdR-1wTsa8NgQ"
VKSURF_VIDEO2_ID ="BAACAgQAAxkBAAICJmiWExCvmaj6n1tmXv5KouCmlM-5AALkGAACtASxUCKwgsEkVWRANgQ"
VKTARGET_VIDEO_ID="BAACAgQAAxkBAAIDQGiWJYziEa26A3UWuMIUIM1P7j11AAL3GAACtASxUPigHKj4jsxtNgQ"
AVISO_VIDEO1_ID="BAACAgQAAxkBAAIDZWiWM3omtWH6PorUyopZ50-OW5AuAALPHgACAVyxUM9nQkSbJYnpNgQ"
AVISO_VIDEO2_ID="BAACAgQAAxkBAAIDZ2iWNnDL-sxlAwsSg9C1m2_0CKVbAALTHgACAVyxUAo8sTdQH2I1NgQ"

# ids فيديوهات السحب
IPWEB_ID="BAACAgQAAxkBAAIFM2iW_eFXXvU21Ty02c-DCRYp3r8pAAK6HAACAVy5UPBKObloM5H7NgQ"
UNU_ID="BAACAgQAAxkBAAIFNWiW_5OqMl51URRWsNarus_fscBzAAK7HAACAVy5UDay9oKKsOrjNgQ"
VKSURF_ID1="BAACAgQAAxkBAAIFO2iXAXJyf0nnnueg1GS6nkwKQ5MPAALBHAACAVy5UBrqPBE6kJjGNgQ"
VKSURF_ID2="AgACAgQAAxkBAAIFW2iXLfnU6MnBIiZ6mr5EI5VRe9miAAKwzDEbAVy5UKfH3jNJ-Q-XAQADAgADeAADNgQ"
VKTARGET_ID="BAACAgQAAxkBAAIFOWiXAAHyPxby1YNK6y2nEQLojL375QACvRwAAgFcuVABVg1-_14qOTYE"
AVISO_ID1="BAACAgQAAxkBAAIFN2iXAAFJ7GsoaiKKWgbXxVvoV7FWiAACvBwAAgFcuVBjVJlZcVPe3DYE"


# ✅ القائمة الرئيسية
def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row("Start")
    menu.row("أكواد", "مواقع")
    menu.row("السحب", "القبض")
    return menu

# أمر إضافة أكواد (للأدمن فقط)
@bot.message_handler(commands=['addcodes'])
def add_codes(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(message.chat.id, "أرسل الأكواد (كل كود في سطر جديد):")
        bot.register_next_step_handler(message, save_codes)
    else:
        bot.send_message(message.chat.id, "❌ أنت لست الأدمن!")

def save_codes(message):
    codes = message.text.strip().split('\n')
    for code in codes:
        codes_sheet.append_row([code.strip()])
    bot.send_message(message.chat.id, f"✅ تم إضافة {len(codes)} الأكواد بنجاح.")

# ✅ قائمة المواقع الفرعية
def sites_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row("🔹 IP Web", "🔹 Aviso")
    menu.row("🔹 VK Target", "🔹 UNU")
    # menu.row("🔹 VK Surfing")
    menu.row("🔹 VK Surfing")
    menu.row("↩️ رجوع")
    return menu

# ✅ قائمة المواقع الفرعية (نسخة 2)
def sites_menu2():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row("🌐 IP Web", "🌐 Aviso")
    menu.row("🌐 VK Target", "🌐 UNU")
    menu.row("🌐 VK Surfing")
    menu.row("↩️ رجوع")
    return menu

# ✅ لما حد يعمل /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
       "👋 أهلاً بيك في بوت E‘ Make Money\n\nاختر من القائمة اللي تحت علشان تبدأ 💰👇",
        reply_markup=main_menu()
    )
# ✅ التعامل مع الرسائل النصية
@bot.message_handler(func=lambda m: m.content_type == 'text')
def handle_message(message):
    text = message.text

    if text == "Start":
        bot.send_message(
            message.chat.id,
            "👋 أهلاً بيك في بوت E‘ Make Money\n\nاختر من القائمة اللي تحت علشان تبدأ 💰👇",
            reply_markup=main_menu()
        )

    elif text == "القبض":
        bot.send_message(
            message.chat.id,
            """📸 لضمان قبول الشغل، يُرجى اتباع الخطوات التالية بدقة:

1️⃣ بعد الانتهاء من فديوهات السحب، لازم تبعت سكرين شوت يوضح إن النقاط اتحسبت (مكتوب فيها إن العملية مقبولة "مدفوعه")

2️⃣ ابعت السكرين مع رسالة فيها:
🔹 اسم الموقع اللي اشتغلت عليه  
🔹 الكود الخاص بيك  
🔹 الكاش اللي هتستلم عليه الفلوس  

3️⃣ ابعت كل ده على واتساب على الرقم ده 👇  
📱 <a href='https://wa.me/201040311607'>راسل Eslam على WhatsApp</a>

📌 أقل عدد نقاط مسموح بتسليمه حسب الموقع:

🌐 موقع VK Surfing: أقل عدد تسليم 106 نقطة  
🌐 مواقع IP Web - Aviso - VK Target - UNU: أقل عدد تسليم 50 نقطة  

⛔ أي تسليم أقل من الأرقام دي مش هيتحسب، فـ تأكد قبل ما تبعت.

🕒 التسليم متاح من يوم الجمعة لحد السبت، وبيوصلك سكرين إن الفلوس وصلت خلال 24 ساعة كحد أقصى.
""",
            reply_markup=main_menu(),
            disable_web_page_preview=True
        )
    
    elif message.text.strip() == "أكواد":
      user_id = str(message.from_user.id)

    # نبحث عن اليوزر في شيت user_codes
      user_codes_data = user_codes_sheet.get_all_values()
      existing_user = None
      for row in user_codes_data:
        if row[0] == user_id:
            existing_user = row[1]
            break

      if existing_user:
        bot.send_message(message.chat.id, f"📌 لقد حصلت على الكود من قبل: {existing_user}")

      elif len(codes_sheet.get_all_values()) == 0:
        bot.send_message(message.chat.id, "❌ لا توجد أكواد متاحة الآن.")

      else:
        codes_data = codes_sheet.get_all_values()
        code = codes_data[0][0]

        bot.send_message(message.chat.id, f"🎁 كودك هو: {code}")
        user_codes_sheet.append_row([user_id, code])
        codes_sheet.delete_rows(1)

    elif text == "السحب":
       bot.send_message(
        message.chat.id,
        "🌐 فيديوهات السحب :",
        reply_markup=sites_menu2()
    )
    elif text == "مواقع":
        bot.send_message(
            message.chat.id,
            "🌐 اختار الموقع اللي اشتغلت عليه:",
            reply_markup=sites_menu()
        )


    elif text == "↩️ رجوع":
        bot.send_message(
            message.chat.id,
            "✅ رجعتك للقائمة الرئيسية 💡",
            reply_markup=main_menu()
        )
    elif text == "🔹 IP Web":
     if IPWEB_VIDEO_ID:
        bot.send_video(
            message.chat.id,
            IPWEB_VIDEO_ID,
            caption=(
                "شغل موقع ipweb 👇🏼\n\n"
                "https://www.ipweb.pro/?Vvvvvv6556\n\n"
                "الشغل عباره عن انك بتعمل متابعه لناس / بتدخل جروب / لايك وبتبعت سكرين.\n"
                "ابعتوا لاسلام عشان تستلموا الكود و تفعلوا الاكونت وابدأو شغل لغاية ما الكود يتبعت.\n"
                "اهم حاجة وأنت بتسجل تخش من اللينك الي موجود فوق ده عشان القبض 👆\n\n"
                "ده بوت الخاص بالموقع، تقدر تشتغل عليه برضو، اهم حاجة تسجل بنفس اليوزر والباسورد بتوع الموقع 👇\n"
                "https://t.me/IPwebBot?start=bT1zbCZyPVZ2dnZ2djY1NTY\n\n"
                "🎥 الفيديو موضح كل حاجة بالتفاصيل 👆🏼"
            )
        )
        bot.send_message(
           message.chat.id,
           "السعر:\n"
           "ال110 نقطه ب 38 جنيه\n"
           "الليدر ب 39"
        )
     else:
        bot.send_message(message.chat.id, "⚠️ لسه مفيش فيديو مضاف، ارفعيه كملف الأول.")
    elif text == "🔹 UNU":
     if UNU_VIDEO_ID:
        bot.send_video(
            message.chat.id,
            UNU_VIDEO_ID,
            caption=(
                "الشغل علي موقع UNU 👇\n\n"
                "https://unu.im/re/3402211\n\n"
                "📌 اهم حاجة تخشوا من اللينك ده عشان القبض 👆\n"
                "في بداية الشغل الموقع لازم يقبلك 10 مهمات، وبعد كده بيفتحلك مهمات كتير.\n"
                "اهم حاجة تشوف المطلوب في المهمة وتنفذه بالظبط عشان المهمة تتقبل.\n"
                "📉 أقل تسليم: 50 نقطة.\n"
                "💬 لازم تبعتلي اليوزر بتاعك في الموقع عشان يتسجل عندي في السيستم."
            )
        )
        bot.send_message(
           message.chat.id,
           "السعر:\n"
           "ال100 نقطه ب 28 جنيه\n"
           "الليدر ب 29"
        )
     else:
        bot.send_message(message.chat.id, "⚠️ لسه مفيش فيديو مضاف، ارفعيه كملف الأول.")
    elif text == "🔹 VK Surfing":
      if VKSURF_VIDEO1_ID and VKSURF_VIDEO2_ID:
        # الفيديو الأول + الكابشن الأساسي
        bot.send_video(
            message.chat.id,
            VKSURF_VIDEO1_ID,
            caption=(
                "موقع Vk surfing 👇🏼\n\n"
                "https://vkserfing.ru/?ref=550605054\n\n"
                "لازم تسجل من خلال الينك ده عشان القبض 👆\n"
                "الشغل عبارة عن إنك بتعمل متابعه / لايك / كومنت / تشوف فيديو.\n"
                "الموقع اهم حاجة قبل ما تبدأ اي شغل تربط حسابات السوشيال ميديا بتاعتك عشان المهمه تتقبل في نفس الوقت.\n"
                "المهمات تقريبا بتجدد كل نص ساعة، ملهاش وقت معين برضو.\n\n"
                "🎥 الفيديو موضح كل حاجة 👆🏼"
            )
        )

        # الفيديو الثاني + الكابشن عن ربط الحسابات
        bot.send_video(
            message.chat.id,
            VKSURF_VIDEO2_ID,
            caption=(
                "💡 دي طريقة ربط الاكونتات بتاعتك في شغل Vk surfing\n"
                "❤️ اهم حاجة تحط صورة حقيقية في كل الاكونتات اللي هتربطها بالموقع."
            )
        )
        bot.send_message(
           message.chat.id,
           "السعر:\n"
           "ال130 نقطه ب 40 جنيه\n"
           "الليدر ب 41"
        )
      else:
        bot.send_message(message.chat.id, "⚠️ لسه واحد أو أكتر من الفيديوهات مش مضاف، ارفعهم كملفات الأول.")
    elif text == "🔹 VK Target":
      if VKTARGET_VIDEO_ID:
        bot.send_video(
            message.chat.id,
            VKTARGET_VIDEO_ID,
            caption=(
                "الشغل علي موقع Vk target 👇\n\n"
                "https://vktarget.ru/?ref=11040768\n\n"
                "📌 الموقع عبارة عن مهمات فولو ولايك.\n"
                "1️⃣ اهم حاجة وانت بتسجل تكون عارف الإيميل بتاعك وتقدر تفتحه في أي وقت، لأن ده ليه علاقة بالقبض.\n"
                "2️⃣ بعد ما تسجل، اربط الأكونتات بتاعتك في الموقع عشان ينزلك المهمات على طول.\n"
                "3️⃣ المهمات بتتجدد كل ساعة أو ساعتين ❤️"
            )
        )
        bot.send_message(
           message.chat.id,
           "السعر:\n"
           "ال110 نقطه ب 42 جنيه\n"
           "الليدر ب 43"
        )
      else:
        bot.send_message(message.chat.id, "⚠️ لسه مفيش فيديو VK Target مضاف، ارفعيه كملف الأول.")

    elif text == "🔹 Aviso":
      if AVISO_VIDEO1_ID and AVISO_VIDEO2_ID:
        # الفيديو الأول
        bot.send_video(
            message.chat.id,
            AVISO_VIDEO1_ID,
            caption=(
                "شغل علي موقع Aviso ❤️\n\n"
                "لينك التسجيل في الموقع:\n"
                "https://aviso.bz/?r=eslam51515\n\n"
                "‼️ قبل الشغل على الموقع ‼️\n"
                "الموقع عباره عن إنك بتعمل فولو ولايك وتشوف فيديوهات.\n"
                "علشان تبدأ تشتغل على الموقع، هتعمل 4 خطوات:\n"
                "1️⃣ تأكيد الإيميل زي ما أنا شارح في الفيديو.\n"
                "2️⃣ هتاخد مني كود (ولو معاك كود لأي موقع تاني أنا مدهولك استخدمه).\n"
                "3️⃣ هتبعتلي اسم الأكونت بتاعك ❤️"
            )
        )

        # الفيديو الثاني
        bot.send_video(
            message.chat.id,
            AVISO_VIDEO2_ID,
            caption="🎥 فيديو طريقة الشغل على موقع Aviso وإزاي تعمل نقاط وتتفاعل مع المهمات ❤️"
        )
        bot.send_message(
           message.chat.id,
           "السعر:\n"
           "ال110 نقطه ب 41 جنيه\n"
           "الليدر ب 42"
        )
      else:
        bot.send_message(message.chat.id, "⚠️ لسه مفيش فيديوهات Aviso مضافة، ارفعهم الأول.")

    elif text == "🌐 IP Web":
     if IPWEB_ID:
        bot.send_video(
            message.chat.id,
            IPWEB_ID,
            caption=(
                " فديو السحب بتاع شغل IP Web معاكم طول اليوم، تسلموا براحتكم ❤️\n\n"
                " التسليم بأي كمية، بس مش أقل من 30 نقطة."
                " هتبعتلي سكرين إن العملية اتقبلت ومعاها الكاش بتاعك."
                "📌 ثبتوه في الشات عشان أحولك القبض على طول ❤️"
            )
        )
     else:
        bot.send_message(
            message.chat.id,
            "⚠️ لسه مفيش فيديو مضاف، ارفعيه كملف الأول."
        )
    elif text == "🌐 UNU":
     if UNU_ID:
        bot.send_video(
            message.chat.id,
            UNU_ID,
            caption=(
                " تسليم شغل UNU ❤️\n\n"
                " التسليم هيكون من خلال الكود فقط."
                " لو معكش كود هتستلم مني واحد."
                " لو انت معاك كود وشغال أصلاً على IP Web، استخدم نفس الكود برضو في التسليم."
                " هتبعتلي سكرين إن العملية تمت معالجتها ❤️"
                " اهم حاجة تكون مأكد الجميل بتاعك من الإعدادات عشان عملية السحب تتم ‼️"
                "✅ ولما العملية تتقبل، هتبعتلي سكرين ومعاها رقم الكاش بتاعك ❤️"
            )
        )
     else:
        bot.send_message(
            message.chat.id,
            "⚠️ لسه مفيش فيديو مضاف، ارفعيه كملف الأول."
        )
    elif text == "🌐 VK Target":
     if VKTARGET_ID:
        bot.send_video(
            message.chat.id,
            VKTARGET_ID,
            caption=(
                " فديو السحب بتاع شغل VK Target ❤️\n\n"
                " لو معاك كود IP Web هتعمل نفس اللي انا عملته بالكود."
                " ولو معكش كود، ابعتلي وهبعتلك واحد تسلم بيه."
                " لما العملية تتقبل، ابعتلي سكرين ومعاها رقم الكاش ❤️"
                "‼️ اهم حاجة تكون مأكد الجميل بتاعك من الإعدادات، عشان هيجيلك عليها كود تأكيد العملية ❤️"
            )
        )
     else:
        bot.send_message(
            message.chat.id,
            "⚠️ لسه مفيش فيديو مضاف، ارفعيه كملف الأول."
        )
    elif text == "🌐 Aviso":
     if AVISO_ID1:
        bot.send_video(
            message.chat.id,
            AVISO_ID1,
            caption=(
                " فديو السحب بتاع موقع Aviso ❤️\n\n"
                " أقل تسليم 50 نقطة.\n"
                " هتبعتلي سكرين بالعملية بتاعت السحب ومعاها رقم الكاش بتاعك ❤️"
            )
        )
     else:
        bot.send_message(
            message.chat.id,
            "⚠️ لسه مفيش فيديو مضاف، ارفعيه كملف الأول."
        )

    elif text == "🌐 VK Surfing":
     if VKSURF_ID1:
        # إرسال الفيديو الأول مع الكابشن
        bot.send_video(
            message.chat.id,
            VKSURF_ID1,
            caption=(
                " ده فديو السحب وطريقة التسليم بتاعت شغل VK Surfing ❤️\n\n"
                " السحب طول اليوم وآخركم الساعة 11."
                " لو عملت عملية السحب بعدها هتتقبل الأسبوع اللي بعده مش بكره."
                " أقل تسليم 130 نقطة.\n\n"
                "‼️ أهم حاجة نتأكد إنه مفيش أي غرامات علينا في الأكونت، ولو مش عارف إزاي يبعتلي.\n"
                "‼️ وحطوا صور ناس حقيقية في الأكونتات اللي شغالين عليها."
                " الكود: P1122015134 — سلّموا بيه زي الفيديو.\n"
                "لو حصلت مشكلة، استلم مني كود مخصص ليك بعيد عن الكود الأساسي ❤️"
            )
        )
        # إرسال الصورة الثانية مع الكابشن
        if VKSURF_ID2:
            bot.send_photo(
                message.chat.id,
                VKSURF_ID2,
                caption=(
                    " عمليات شغل VK Surfing دايمًا بتتقبل يوم السبت.\n"
                    "ده بيكون شكل الأسكرين اللي بتسلمهولي عشان القبض.\n"
                    "⚠️ لو فتحت ولاقيت حظر في عمليات السحب، ابعتلي برايفت أبعثلك فيديو إزاي تفكه.\n"
                    "⚠️ لو جالك إن عليك غرامة عشان عملت أكتر من 30 مهمة غلط، ده معناه إنك كنت بتعمل مهمات وتخرج منها — وده ممنوع.\n"
                    "الموقع رجعلك النقط، هتخش على حاجة اسمها الغرامات وتشيلها كلها وتكمل شغل لحد الأسبوع اللي بعده.\n"
                    "وقبل التسليم، ابعتلي أخليك تسلم بكود مختلف ❤️"
                )
            )
        else:
            bot.send_message(
                message.chat.id,
                "⚠️ لسه مفيش صورة مضافة، ارفعها كملف الأول."
            )

    else:
        bot.send_message(
            message.chat.id,
            "⚠️ لسه مفيش فيديو مضاف، ارفعه كملف الأول."
        )

    # else:
    #     bot.send_message(
    #         message.chat.id,
    #         "❗مش فاهم الطلب، اختار من القايمة تحت 🙏",
    #         reply_markup=main_menu()
    #     )
    

# # ✅ لما المستخدم يرفع فيديو كملف (Document)
# @bot.message_handler(content_types=['document'])
# def handle_document_video(message):
#     if message.document.mime_type.startswith("video/"):
#         file_id = message.document.file_id
#         bot.send_message(
#             message.chat.id,
#             f"🎥 تم استلام الفيديو كملف.\n📎 File ID:\n<code>{file_id}</code>",
#             parse_mode="HTML"
#         )
#     else:
#         bot.send_message(
#             message.chat.id,
#             "❗الملف المرفوع مش فيديو، من فضلك ارسل فيديو بصيغة mp4 كملف أو فيديو عادي.",
#             reply_markup=main_menu()
#         )

# # ✅ لما المستخدم يرسل فيديو عادي (Video)
# @bot.message_handler(content_types=['video'])
# def handle_video(message):
#     file_id = message.video.file_id
#     bot.send_message(
#         message.chat.id,
#         f"🎥 تم استلام الفيديو.\n📎 File ID:\n<code>{file_id}</code>",
#         parse_mode="HTML"
#     )

@bot.message_handler(content_types=['photo', 'document'])
def get_file_id(message):
    if message.photo:
        file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, f"Photo ID: {file_id}")
    elif message.document:
        file_id = message.document.file_id
        bot.send_message(message.chat.id, f"Document ID: {file_id}")

# ✅ تشغيل البوت
print("✅ Bot is running...")
bot.infinity_polling()
