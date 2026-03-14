import random
from fastapi import FastAPI
planet_names = [
"Averia","Zorath","Velion","Xentara","Krylon","Arctara","Nebulon","Taloria","Xyphos","Dravion","Voraxis","Nythera",
"Zypheron","Aetheris","Vortalis","Lunaris","Eryndor","Zyraxis","Krythos","Vexara","Kratos","Karaken","Cxzten","Xopen",
"Zoseta","Vexilon","Arionis","Zypheris","Nexara","Zorveth","Velkara","Xenthor","Kalthera","Orvaxis","Zytheron","Talion",
"Vorathis","Nyxaris","Dravionis","Velthor","Xarkalis","Zenthon","Orthera","Talvionis","Kalvex","Vorenthis","Nytheronix",
"Zoralisix","Veltrion","Xalvex","Dravexis","Taltheron","Orvexis","Zentharaix","Kaltheron","Voraxion","Nytheraix",
"Zorvethis","Velorix","Xenthoris","Talvexis","Kalorath","Vorenthara","Nyxeron","Dravexon","Veltharis","Xarkonix",
"Zenthoris","Orvethara","Talorix","Kaltheris","Vorathion","Nytheralis","Zorvexion","Velarion","Xenthara","Dravionex",
"Talveth","Kalorion","Voralisix","Nyxathor","Zorenthis","Velorath","Xenvaris","Draventh","Talorath","Kalvionis",
"Vorenthion","Nytheraxion","Zorvexis","Velkarion","Xentharis","Dravexara","Taltheris","Kalorixis","Voraxisar",
"Nyxarion","Zorathis","Veltheron","Xenvarion","Dravaris","Talvexion","Kaltheronix","Vorenthax","Nytherisara",
"Zorvexionis","Velkaris","Xenthax","Dravoris","Taltherax","Kalorenth","Voratharis","Nytheronara","Zorenthara",
"Veloraxis","Xenvarisix","Draventhara","Talvethion","Kaltheraris","Vorenthisara","Nytheraxara","Zorvethara",
"Velkaraxis","Xentharaix","Dravexaris","Taltheraris","Kaloraxis","Vorentharaix","Nyxaraxis","Averon","Zorvion",
"Velthar","Xenaris","Kalthor","Orveth","Zylar","Talvion","Vorenth","Nyxara","Dravor","Velaris","Xenthor","Kalvex",
"Oraxis","Zythera","Taloris","Vorath","Nytheron","Dravex","Velor","Xenvar","Kalther","Orvion","Zyrax","Talvex",
"Voralis","Nyxaris","Dravionex","Velthion","Xenor","Kaldris","Orther","Zyphor","Talor","Vorenthis","Nytherax",
"Dravaris","Velkar","Xenthis","Kalvar","Orvex","Zylaris","Talther","Vorax","Nytheris","Dravoris","Veltharion",
"Xeneth","Kalor","Orvath","Zyron","Talveth","Voraris","Nyxeth","Dravorion","Velaxis","Xenara","Kalthera","Orvaxis",
"Zytheron","Talion","Vorathis","Nyxaris","Dravionis","Velthor","Xarkalis","Zenthon","Orthera","Talvionis","Kalvexis",
"Vorenthara","Nytheronix","Zoralisix","Veltrion","Xalvex","Dravexis","Taltheron","Orvexis","Zentharaix","Kaltheron",
"Voraxion","Nytheraix","Zorveth","Velorix","Xenthoris","Talvexis","Kalorath","Vorenthara","Nyxeron","Dravexon",
"Veltharis","Xarkonix","Zenthoris","Orvethara","Talorix","Kaltheris","Vorathion","Nytheralis","Zorvexion","Velarion",
"Xenthara","Dravionexis","Talvethis","Kalorion","Voralisix","Nyxathor","Zorenthis","Velorath","Xenvaris","Draventh",
"Talorath","Kalvionis","Vorenthion","Nytheraxion","Zorvexis","Velkarion","Xentharis","Dravexara","Taltheris",
"Kalorixis","Voraxisar","Nyxarion","Zorathis","Veltheron","Xenvarion","Dravarisix","Talvexion","Kaltheronix",
"Vorenthax","Nytherisara","Zorvexionis","Velkaris","Xenthax","Dravorisix","Taltherax","Kalorenth","Voratharis",
"Nytheronara","Zorenthara","Veloraxis","Xenvarisix","Draventhara","Talvethion","Kaltheraris","Vorenthisara",
"Nytheraxara","Zorvethara","Velkaraxis","Xentharaix","Dravexaris","Taltheraris","Kaloraxis","Vorentharaix","Nyxaraxis"
"Averia","Zorath","Velion","Xentara","Krylon","Arctara","Nebulon","Taloria","Xyphos","Dravion","Voraxis","Nythera","Zypheron","Aetheris","Vortalis","Lunaris","Eryndor","Zyraxis","Krythos","Vexara","Kratos","Karaken","Cxzten","Xopen","Zoseta","Vexilon","Arionis","Zypheris","Nexara","Zorveth","Velkara","Xenthor","Kalthera","Orvaxis","Zytheron","Talion","Vorathis","Nyxaris","Dravionis","Velthor","Xarkalis","Zenthon","Orthera","Talvionis","Kalvex","Vorenthis","Nytheronix","Zoralisix","Veltrion","Xalvex","Dravexis","Taltheron","Orvexis","Zentharaix","Kaltheron","Voraxion","Nytheraix","Zorvethis","Velorix","Xenthoris","Talvexis","Kalorath","Vorenthara","Nyxeron","Dravexon","Veltharis","Xarkonix","Zenthoris","Orvethara","Talorix","Kaltheris","Vorathion","Nytheralis","Zorvexion","Velarion","Xenthara","Dravionex","Talveth","Kalorion","Voralisix","Nyxathor","Zorenthis","Velorath","Xenvaris","Draventh","Talorath","Kalvionis","Vorenthion","Nytheraxion","Zorvexis","Velkarion","Xentharis","Dravexara","Taltheris","Kalorixis","Voraxisar","Nyxarion","Zorathis","Veltheron","Xenvarion","Dravaris","Talvexion","Kaltheronix","Vorenthax","Nytherisara","Zorvexionis","Velkaris","Xenthax","Dravoris","Taltherax","Kalorenth","Voratharis","Nytheronara","Zorenthara","Veloraxis","Xenvarisix","Draventhara","Talvethion","Kaltheraris","Vorenthisara","Nytheraxara","Zorvethara","Velkaraxis","Xentharaix","Dravexaris","Taltheraris","Kaloraxis","Vorentharaix","Nyxaraxis","Averon","Zorvion","Velthar","Xenaris","Kalthor","Orveth","Zylar","Talvion","Vorenth","Nyxara","Dravor","Velaris","Xenthor","Kalvex","Oraxis","Zythera","Taloris","Vorath","Nytheron","Dravex","Velor","Xenvar","Kalther","Orvion","Zyrax","Talvex","Voralis","Nyxaris","Dravionex","Velthion","Xenor","Kaldris","Orther","Zyphor","Talor","Vorenthis","Nytherax","Dravaris","Velkar","Xenthis","Kalvar","Orvex","Zylaris","Talther","Vorax","Nytheris","Dravoris","Veltharion","Xeneth","Kalor","Orvath","Zyron","Talveth","Voraris","Nyxeth","Dravorion","Velaxis","Xenara","Kalthera","Orvaxis","Zytheron","Talion","Vorathis","Nyxaris","Dravionis","Velthor","Xarkalis","Zenthon","Orthera","Talvionis","Kalvexis","Vorenthara","Nytheronix","Zoralisix","Veltrion","Xalvex","Dravexis","Taltheron","Orvexis","Zentharaix","Kaltheron","Voraxion","Nytheraix","Zorveth","Velorix","Xenthoris","Talvexis","Kalorath","Vorenthara","Nyxeron","Dravexon","Veltharis","Xarkonix","Zenthoris","Orvethara","Talorix","Kaltheris","Vorathion","Nytheralis","Zorvexion","Velarion","Xenthara","Dravionexis","Talvethis","Kalorion","Voralisix","Nyxathor","Zorenthis","Velorath","Xenvaris","Draventh","Talorath","Kalvionis","Vorenthion","Nytheraxion","Zorvexis","Velkarion","Xentharis","Dravexara","Taltheris","Kalorixis","Voraxisar","Nyxarion","Zorathis","Veltheron","Xenvarion","Dravarisix","Talvexion","Kaltheronix","Vorenthax","Nytherisara","Zorvexionis","Velkaris","Xenthax","Dravorisix","Taltherax","Kalorenth","Voratharis","Nytheronara","Zorenthara","Veloraxis","Xenvarisix","Draventhara","Talvethion","Kaltheraris","Vorenthisara","Nytheraxara","Zorvethara","Velkaraxis","Xentharaix","Dravexaris","Taltheraris","Kaloraxis","Vorentharaix","Nyxaraxis"
]

planet_atmosphere=["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon",
"Sodium","Magnesium","Aluminium","Silicon","Phosphorus","Sulfur","Chlorine","Argon",
"Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc",
"Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton",
"Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium",
"Indium","Tin","Antimony","Tellurium","Iodine","Xenon",
"Caesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium",
"Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury",
"Thallium","Lead","Bismuth","Polonium","Astatine","Radon",
"Francium","Radium","Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium",
"Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium","Roentgenium","Copernicium",
"Nihonium","Flerovium","Moscovium","Livermorium","Tennessine","Oganesson"]

life=["likely","unlikely"]
app=FastAPI()
@app.get("/")
def home():
    return {"message": 'API working successfully.Visit /docs for more'}
@app.get("/gen-planet")
def gen_plante():
    planet_temprature=random.randint(1,1000)
    planet_gravity=random.randint(10,100)
    return {"Planet":random.choice(planet_names),"Temperature":str(planet_temprature)+"℃","Gravity":str(planet_gravity)+"g","Atmosphere":random.choice(planet_atmosphere),"Life":random.choice(life)}
