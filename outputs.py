output_dict = {
    "Bed-bug": "Symptoms: Red, itchy welts often in a line or cluster; may cause localized swelling.\nTreatment: Clean the area with soap and water; apply antihistamine creams or take oral antihistamines to reduce itching.",
    "bedbug": "Symptoms: Red, itchy welts often in a line or cluster; may cause localized swelling.\nTreatment: Clean the area with soap and water; apply antihistamine creams or take oral antihistamines to reduce itching.",
    "Bee-bite": "Symptoms: Immediate sharp pain, swelling, and redness at the sting site.\nTreatment: Remove the stinger promptly; clean the area; apply ice; consider antihistamines for itching and seek medical attention if allergic reactions occur.",
    "Beetle":"Symptoms: Contact with blister beetles can cause redness, swelling, and the formation of large, painful blisters filled with clear fluid. Some individuals may also experience headache, nausea, and lethargy.\nTreatment: Gently wash the affected area with soap and water. Apply a cold compress to alleviate swelling and pain. Over-the-counter treatments such as calamine lotion, baking soda paste, or hydrocortisone cream (0.5% or 1%) can help reduce itching and discomfort. Seek medical attention if severe reactions occur or if the blisters do not improve.",
    "Chigger-bites": "Symptoms: Intense itching and red, pimple-like bumps, often around the waist, ankles, or warm skin folds.\nTreatment: Wash affected areas with soap and water; apply an antiseptic; use antihistamines or corticosteroid creams to alleviate itching.",
    "Conenose Bite": "Symptoms: Often painless bites that may trigger allergic reactions; in some regions, potential for Chagas disease transmission.\nTreatment: Clean the area; monitor for allergic reactions; seek medical advice if symptoms worsen.",
    "Fire-Ant": "Symptoms: Burning pain, followed by red, swollen spots that may develop into pus-filled blisters.\nTreatment: Clean the area; apply cold compresses; use antihistamines or corticosteroid creams; seek medical attention if reactions become severe.",
    "Fleas": "Symptoms: Clusters of small, red, itchy bumps, typically on the legs and ankles.\nTreatment: Wash the area with soap and water; apply anti-itch creams; avoid scratching to prevent infection.",
    "Gnat-bites": "Symptoms: Small, red, itchy bumps with possible swelling.\nTreatment: Clean the area; apply cold compresses; use antihistamines or anti-itch creams.",
    "Horse-Fly": "Symptoms: Immediate sharp pain with red, swollen bumps; may lead to infection.\nTreatment: Clean thoroughly; apply an antiseptic; use cold compresses; consult a doctor if signs of infection appear.",
    "Lice": "Symptoms: Intense itching and red bumps on the scalp, neck, and shoulders.\nTreatment: Use over-the-counter or prescription treatments; wash clothing and bedding in hot water.",
    "Midges": "Symptoms: Small, red, itchy bumps; possible swelling.\nTreatment: Clean the area; apply anti-itch creams; use antihistamines if necessary.",
    "Mites": "Symptoms: Intense itching with red, pimple-like bumps; may present with scabies-like burrows in some cases.\nTreatment: Consult a healthcare provider for appropriate treatment; maintain good hygiene.",
    "Mosquito": "Symptoms: Itchy, red bumps; potential risk of transmitting diseases such as West Nile virus.\nTreatment: Clean the area; apply anti-itch creams; use antihistamines if needed.",
    "Scabies": "Symptoms: Intense itching, particularly at night, with thin, irregular burrow tracks that may appear as tiny blisters or bumps.\nTreatment: Use prescription creams or lotions; treat all household members and close contacts simultaneously.",
    "Scorpion": "Symptoms: Sharp pain, swelling, numbness, or tingling; severe cases may cause more serious systemic symptoms.\nTreatment: Clean the area; apply ice; seek medical attention immediately for severe reactions.",
    "Spider": "Symptoms: Varies by species; may include redness, pain, and swelling. Certain species like the brown recluse or black widow can cause serious reactions.\nTreatment: Clean the area; apply ice; seek medical attention if serious symptoms develop.",
    "Tick": "Symptoms: Small red bump; potential for disease transmission (e.g., Lyme disease).\nTreatment: Remove the tick promptly and carefully; clean the area; monitor for signs of tick-borne illnesses.",
    "Wasp": "Symptoms: Immediate pain, redness, and swelling; possible severe allergic reactions.\nTreatment: Clean the area; apply ice; take antihistamines for itching; seek emergency care if signs of a severe allergic reaction occur."
    "Yellow-Jacket": "Symptoms: Immediate pain, redness, and swelling; possible severe allergic reactions.\nTreatment: Clean the area; apply ice; take antihistamines for itching; seek emergency care if signs of a severe allergic reaction occur."

}

def getInfo(key):
    return output_dict[key]
