from flask import Flask, render_template, request
import random

app = Flask(__name__)
from flask import Response

@app.route('/sitemap.xml')
def sitemap():
    with open('sitemap.xml', 'r') as f:
        xml_content = f.read()
    return Response(xml_content, mimetype='application/xml')


# Simple keyword-to-vibe mappings
vibes = {
    "sherehe": ("Sherehe Minister 🎉", 95),
    "chapaa": ("Money Moves Only 💸", 90),
    "msupa": ("Certified Msupa wa Power 💅", 92),
    "msee": ("Real G Vibes 🧢", 85),
    "ndai": ("Cruising in Style 🚗", 87),
    "ushago": ("Ocha Mode Activated 🌾", 70),
    "nyama": ("Choma Chief 🍖", 89),
    "niaje": ("Niaje Budah Energy 🤝", 78),
    "sasa": ("Sasa Fiti Vibes 👋", 75),
    "hustle": ("Hustle Nation Certified 💼", 91),
    "mpesa": ("Till Number Vibes 📲", 84),
    "sponsor": ("Soft Life Activated 💅", 93),
    "gava": ("Gava Approved Moves 🏛️", 79),
    "siku hizi": ("Gen Z Nairobi Mood 🧃", 77),
    "form": ("Form Ni Gani? Energy 🔥", 88),
    "cheza kama wewe": ("Main Character on the Dancefloor 💃", 94),
    "mapema": ("Mapema Ndio Best ⏰", 86),
    "riggy g": ("Deputy Vibes Only 🧢", 80),
    "wueh": ("Wueh! Shocked but Vibing 😳", 73),
    "sina maoni": ("Silent But Deadly Vibes 🤫", 76),
    "tulia": ("Chillax Boss 😌", 72),
    "mambo": ("Mambo Iko Sawa 🌞", 78),
    "vibing": ("Vibes on Vibes 🔥", 89),
    "drip": ("Dripped Out Dripmaster 💧", 91),
    "chill": ("Cooler Than a Freezer ❄️", 74),
    "pressure": ("Pressure Ziko 🔥", 68),
    "ghosted": ("Casper Vibes 👻", 50),
    "nyash": ("Certified Nyash Analyst 🍑", 88),
    "sambaza": ("Sambaza the Vibes 📡", 83),
    "mambo ni mengi": ("Too Much Sauce 🥵", 69),
    "soko": ("Market Mood Activated 🛒", 77),
    "squad": ("Squad Goals Achieved 👯", 86),
    "vibaya": ("Vibes Gone South 😬", 52),
    "siku": ("Siku Fiti Energy 🌤️", 75),
    "mrembo": ("Slay Queen Certified 👑", 90),
    "budah": ("Budah Mode: ON 🧢", 82),
    "kanairo": ("Kanairo Chronicles 🏙️", 88),
    "matatu": ("Stage Commander Energy 🚐", 80),
    "mjengo": ("Hard Hat Hustler 🧱", 72),
    "kibanda": ("Kibanda Connoisseur 🍛", 76),
    "viboko": ("Discipline Energy 🪭", 60),
    "sambaza": ("Vibe Distributor 📡", 83),
    "mchongo": ("Mchongo Mastermind 💼", 85),
    "soko": ("Soko Hustler 🛍️", 79),
    "supu": ("Supu Slayer 🍲", 74),
    "kizunguzungu": ("Dizzy With Vibes 🌀", 66),
    "mambo vipi": ("Mambo Vipi Mood 🌈", 77),
    "sina stress": ("Unbothered & Thriving 😎", 88),
    "sina time": ("Booked & Busy 🕒", 84),
    "sina pesa": ("Broke But Vibing 💀", 62),
    "sina story": ("Lowkey Legend 🤫", 76),
    "sina energy": ("Battery Low Mode 🔋", 58),
    "sina brakes": ("No Brakes, Just Vibes 🏎️", 90),
    "sina filter": ("Raw & Real Energy 🎤", 81),
    "sina shame": ("Shameless Vibes Only 😈", 79),
    "sina chills": ("Zero Chill Detected 🥶", 73),
    "sina morals": ("Morals Left the Chat 😅", 70),
    "sina plan": ("Freestyling Life 🎲", 68),
    "sina clue": ("Lost But Vibing 🧭", 65),
    "sina brakes": ("Full Send Energy 🚀", 91),

}
fallbacks = [
    ("Vibe iko low, jaribu tena 😶", random.randint(40, 65)),
    ("Uko na mysterious aura 🤔", random.randint(55, 70)),
    ("Hakuna vibe hapa bana 😬", random.randint(45, 68)),
    ("Vibe haijakam, pole sana 😅", random.randint(50, 69)),
    ("Pressure ni ya gava, si wewe 😤", random.randint(50, 66)),
    ("Umeachwa na vibe kama ex 😭", random.randint(42, 64)),
    ("Vibe yako imeenda ushago 🌾", random.randint(48, 67)),
    ("Si poa, jaribu tena kesho 😐", random.randint(45, 65)),
    ("Vibe yako iko kwa matatu wrong route 🚐", random.randint(43, 66)),
    ("Umeangusha vibe kama KCSE ya 2012 📉", random.randint(40, 63)),
    ("Vibe yako ni kama chai bila mkate ☕", random.randint(44, 68)),
    ("Uko na silent disco ya one person 🎧", random.randint(46, 69)),
    ("Vibe imepotea kama network ya Safaricom 📵", random.randint(41, 65)),
    ("Hii caption ni kama ugali bila sukuma 😬", random.randint(43, 67)),
    ("Vibe yako ni kama jaba ya expired 😵", random.randint(40, 62)),
    ("Caption yako iko na blackout ⚡", random.randint(42, 66)),
    ("Vibe yako ni kama matatu ya Rongai—haijafika bado 🚌", random.randint(45, 68)),
    ("Umejaribu, lakini bado haijakam 😓", random.randint(47, 69)),
    ("Vibe yako ni kama nyoka kwa bible study 🐍📖", random.randint(44, 66)),
    ("Caption yako iko na stress ya landlord 🏠", random.randint(46, 68)),
    ("Vibe yako ni kama WiFi ya neighbor—imefungwa 🔒", random.randint(43, 65)),
    ("Uko na energy ya Monday morning 😩", random.randint(42, 64)),
    ("Caption yako ni kama chai ya hostel—too weak ☕", random.randint(45, 67)),
    ("Vibe yako ni kama mtu wa mjengo kwa sherehe 🧱", random.randint(41, 63)),
    ("Umevaa drip ya emotions but hakuna vibe 💧", random.randint(44, 66)),
    ("Vibe yako ni kama password ya ex—imekuwa changed 🔐", random.randint(43, 65)),
    ("Caption yako ni kama nywele ya kinyozi wa 50 bob ✂️", random.randint(40, 62)),
    ("Vibe yako ni kama TikTok ya 2 views 📱", random.randint(45, 68)),
    ("Umeachwa na vibe kama mtu wa last born 😭", random.randint(42, 64)),
    ("Caption yako ni kama ugali ya microwave 🍽️", random.randint(44, 67)),
    ("Vibe yako ni kama mtu wa group project—missing 😅", random.randint(41, 63)),
    ("Uko na energy ya mtu alikosa chai ya staffroom ☕", random.randint(43, 66)),
    ("Vibe yako ni kama password ya WiFi ya gava—classified 🔒", random.randint(45, 68)),
    ("Caption yako ni kama jua ya January—too harsh ☀️", random.randint(46, 69)),
    ("Vibe yako ni kama mtu wa sherehe bila fare 🎉🚫", random.randint(42, 65)),
    ("Umechoka kama simu ya kabambe 🔋", random.randint(40, 62)),
    ("Vibe yako ni kama mtu wa TikTok na 0 likes 😬", random.randint(43, 66)),
    ("Caption yako ni kama ugali ya hostel—dry 😩", random.randint(44, 67)),
    ("Vibe yako ni kama mtu wa group chat—ghosted 👻", random.randint(41, 64)),
    ("Uko na energy ya mtu alikosa chai ya kanisa ☕", random.randint(45, 68)),
    ("Vibe yako ni kama password ya ex—umeachwa 😭", random.randint(42, 65)),
    ("Caption yako ni kama jaba ya expired 😵", random.randint(40, 63)),
    ("Vibe yako ni kama mtu wa mjengo kwa sherehe 🧱", random.randint(44, 66)),
    ("Umevaa drip ya emotions but hakuna vibe 💧", random.randint(43, 65)),
    ("Vibe yako ni kama password ya WiFi ya gava—classified 🔒", random.randint(45, 68)),
    ("Caption yako ni kama nywele ya kinyozi wa 50 bob ✂️", random.randint(40, 62)),
    ("Vibe yako ni kama TikTok ya 2 views 📱", random.randint(45, 68)),
    ("Umeachwa na vibe kama mtu wa last born 😭", random.randint(42, 64)),
    ("Caption yako ni kama ugali ya microwave 🍽️", random.randint(44, 67)),
    ("Vibe yako ni kama mtu wa group project—missing 😅", random.randint(41, 63)),
    ("Uko na energy ya mtu alikosa chai ya staffroom ☕", random.randint(43, 66)),
    ("Vibe yako ni kama password ya WiFi ya gava—classified 🔒", random.randint(45, 68)),
    ("Caption yako ni kama jua ya January—too harsh ☀️", random.randint(46, 69)),
    ("Vibe yako ni kama mtu wa sherehe bila fare 🎉🚫", random.randint(42, 65)),
    ("Umechoka kama simu ya kabambe 🔋", random.randint(40, 62)),
    ("Vibe yako ni kama mtu wa TikTok na 0 likes 😬", random.randint(43, 66)),
    ("Caption yako ni kama ugali ya hostel—dry 😩", random.randint(44, 67)),
    ("Vibe yako ni kama mtu wa group chat—ghosted 👻", random.randint(41, 64)),
    ("Uko na energy ya mtu alikosa chai ya kanisa ☕", random.randint(45, 68)),
    ("Vibe yako ni kama password ya ex—umeachwa 😭", random.randint(42, 65)),
    ("Caption yako ni kama jaba ya expired 😵", random.randint(40, 63)),
    ("Vibe yako ni kama mtu wa mjengo kwa sherehe 🧱", random.randint(44, 66)),
    ("Umevaa drip ya emotions but hakuna vibe 💧", random.randint(43, 65)),
    ("Vibe yako ni kama password ya WiFi ya gava—classified 🔒", random.randint(45, 68)),
    ("Caption yako ni kama nywele ya kinyozi wa 50 bob ✂️", random.randint(40, 62)),
    ("Vibe yako ni kama TikTok ya 2 views 📱", random.randint(45, 68)),
    ("Umeachwa na vibe kama mtu wa last born 😭", random.randint(42, 64)),
    ("Caption yako ni kama ugali ya microwave 🍽️", random.randint(44, 67)),
    ("Vibe yako ni kama mtu wa group project—missing 😅", random.randint(41, 63)),
    ("Uko na energy ya mtu alikosa chai ya staffroom ☕", random.randint(43, 66)),
    ("Vibe yako ni kama password ya WiFi ya gava—classified 🔒", random.randint(45, 68)),
    ("Caption yako ni kama jua ya January—too harsh ☀️", random.randint(46, 69)),
    ("Vibe yako ni kama mtu wa sherehe bila fare 🎉🚫", random.randint(42, 65)),
    ("Umechoka kama simu ya kabambe 🔋", random.randint(40, 62)),
    ("Vibe yako ni kama mtu wa TikTok na 0 likes 😬", random.randint(43, 66)),
    ("Caption yako ni kama ugali ya hostel—dry 😩", random.randint(44, 67)),
    ("Vibe yako ni kama mtu wa group chat—ghosted 👻", random.randint(41, 64)),
    ("Uko na energy ya mtu alikosa chai ya kanisa ☕", random.randint(45, 68)),
    ("Vibe yako ni kama password ya ex—umeachwa 😭", random.randint(42, 65)),
    ("Caption yako ni kama jaba ya expired 😵", random.randint(40, 63)),
    ("Vibe yako ni kama mtu wa mjengo kwa sherehe 🧱", random.randint(44, 66)),]
    
def analyze_vibe(caption):
    for word, (vibe, score) in vibes.items():
        if word in caption:
            return {"vibe": vibe, "score": score}
    vibe, score = random.choice(fallbacks)
    return {"vibe": vibe, "score": score}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        caption = request.form["caption"].lower()
        result = analyze_vibe(caption)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(directory='.', path='sitemap.xml')

