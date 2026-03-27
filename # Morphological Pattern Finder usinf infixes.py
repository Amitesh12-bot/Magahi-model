# Morphological Pattern Finder

# Sample text corpus
text = """bihaar sariiph meṃ baabuu saamlaal bḍaa mokhtaar halaa baakii i bḍaa bhut
niicataa ke baad hol aa hal. phile i bḍii gariib hal aa. baabuu jii gaaḍii vaanii k-r
halathin, aur inkar phuphaa, guruai k-r halthin aur uhe inkaa miḍil paas
krailthin. piich i bihaar meṃ ek mokhtaar ke yahaaṃ rasoiigirii karake
mukhtaarkaarii ke imatih aan delkaa aur i tiin loghḍaniyaaṃ ke baad paas kar
gel aa. aad mii hosiy aar hal aa aur dhurphandii. kuch uunch-niic triikaa se
mokhtaarkaarii chal aa lelk aa. mahal par ek gariib kaayth ke kuch rupyaa
karj aa delk aa hal, suud muur lagaake okraa se makaan likhaa lelk aur thoḍe
din meṃ dumhal aa makaan aaliisaan banaailk aa. ohe kaayth sugnlaal pher
rasoiy aa ke kaam kare l aglain. aise to kariib-kariib sabhe sark aarii kaam kare
vaal aa thoḍe bhut khosaamdii hove k-r hath. i to musalmaani i vaads aahat aur
hindust aan ke gulaam ke phal he. baakii inkaa meṃ e kar maatraa kuch jaade hal
aur haakim vagairah ke khuub khos ekare se r-kh hal aa. baakii ais an kaam meṃ
bagaair cugalkhoorii ke baṛh tii nai hove he ekare se sahar ke reis inkaa se kuch
kaun chal r-h hal aa. san 1326 ph. ke cait meṃ molavii mojahphar navaab
es-ḍii-o maanabhuum se badal ke aila a aur haladhar sin gh sab-ḍipṭii ek bars
kavle se hal aa. e ne kuch din se saam laal ke junuun raay bah adur hove ke chaṛh

gel hal. e kar kaabil to u j a-n hal aa ke ham nai hii baakii apan dhurataaii
par unkaa bharos aa hal. aave ke jahinaa khabar hal saamlaal kiul sṭ esan
ek roj pher tekraa se pahunch gel aa aur kel nar ke hiaan chaay paanii ke
bandobast kar delk aa aur saat baje saanjh ke jab naab saaheb gaaḍii se
utarlaa ke bakhtiaarpur ke gaaḍii meṃ savaar hovath pahunch ke aadaab bandagii
kailk aa aur apan nisaan pataa batailk aa aur bollaa ke pacchim ke gaaḍii
aave meṃ abhi i der he, jabtak calke naas taa paanii kar lel jaae. navaab saaheb
bollaa ke abhi i khaahis nai he. tab ii bḍii aarju min tii kailk aa ke kalah
se ham hajur eh aan ailuṃ h aur intajaam kailuṃ h. navaab saaheb bhitre bhit ar
to kuch ajab ais an samjath magar reis ghar ainaa ke rahal aa ke vajah se ruukh se
baat nai kar sakath. bollaa (urduu meṃ) -
akhane maaf k-r.
saam
nai hajur.
navaab - bait hale tabiiyat paraes aan ho gel he, khailuuṃ he se pach al nai ais an
bujhaa he.
saam - (e ne o ne dekhke au tab jarise pair chuukhe) hamraa par khaabindii
kail jaae.

navaab saaheb ke ḍher khosaamdii se bhaṭ hol hal baakii ais an khaahmakhaah
to koii nai maaluum bhel. aakhir meṃ samjhalak ke i nai maan at, ete duur se aal
he. e kraa naaraaj karnaa bhii aadami yat se baahar samjh kar bollaa (urduu meṃ)
ch-l.
aakhir kel nar ke kamraa meṃ dunu gel aa aur khidmatgaar gairah ke
chiijabast dekhate rahe kah delk aa. khaansaamaa tiin-caar ṭukḍaa bis kuṭ aur
chaay au aṇḍaa gairah hisaab se laa-laa ke navaab saaheb ke bhiirii rakhe l agal
aur mokhtaar saaheb ṭebul ke duusar taraf bait hal aa.
jaae.
navaab saaheb bollaa (dardaū meṃ)- apne ke bhii laake d.
khaansaamaa - je hukum.
mokhtaar saaheb caṭ se haath joṛ ke bollaa - (urduu meṃ) - maaf kail
khaansaamaa thatham gel.

navaab - nai, ii to tab kirakiraa ho jaat.
saam - nai, ham biisno hii.
navaab - oh, biisno asal dil se hove chaahii.
saam
nai hujur, bḍaa moskil hai.
navaab - acchaa, kuch phal-val laake de bhaaii. au hinduu chaay vaale ko
bul aa laao.
saam - jii haan.
khaansaamaa tab jaake kuch kel aa vo kevlaa le aal aur hinduu chaay vaal aa
ke bol aa ke duu pyaal aa chaay alag duusar ṭebul par rakhalk aur kevāḍii lag aite
cal gel.
kh aite-kh aite navaab saaheb puchlaka
k-ah bihaar kaisan jagah he?
saam - bhut puraan jagah au bhut acchaa jagah hai.
navaab
mokhtaar sab?
saam
acchaa hath.
navaab vak iilo r-h hath?
saam - jii haan.
navaab - vak iil sab aur"""

# Convert text to lowercase
text = text.lower()

# Tokenization (split text into words)
words = text.split()

# Ask user to enter a infixes
infixes = input("Enter a infixes (-l-, -n-, -wa-, -d-, -r-, -m-): ")

# List to store matched words
matched_words = []

# Loop through words
for word in words:
    # Remove punctuation
    word = word.strip(".,!?():\"-")
    
    # Check if word appers with the infixes
    if (word.startswith(infixes) == False and word.endswith(infixes) == False and infixes in word):
        matched_words.append(word)

# Print extracted words
print("\nWords containing internal with", infixes, ":")
print(matched_words)

# Frequency calculation
frequency = {}

for word in matched_words:
    if word in frequency:
        frequency[word] +=+ 1
    else:
        frequency[word] = 1

# Display frequencies
print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)
