def priority_terms():
    directory = input('Please enter the path of the tweets files: ').strip()
    try:
        os.chdir(directory)
    except:
        print('The path is not correct\n')
        return
    ifExists = os.path.exists('Expert_Term_Analysis')
    if not ifExists:
        os.makedirs('Expert_Term_Analysis')
    else:
        shutil.rmtree('Expert_Term_Analysis')
        os.makedirs('Expert_Term_Analysis')
    file_list = os.listdir()
    temp = []
    for ele in file_list:
        if ele[-3:] == 'csv':
            temp.append(ele)
    temp.sort()
    
    
    
    #COMMUNITY
    '''
    Personalities = ['Beck', 'birx', 'bolton', 'boris', 'cuomo', 'donald', 'fauci', 'gupta', 'Hannity', 'Hewitt', 'johnson', 'Limbaugh', 'Medve', 'merkel',
                     'obama', 'Pelosi', 'pence', 'president', 'putin', 'Savage', 'Trudeau', 'Trump', 'Xi']

    Politics = ['Black Lives Matter', 'BLM', 'borders', 'boris', 'china', 'chinavirus', 'chinese', 'Chinese Virus', 'conspiracy', 'Constitution',
                'confederate', 'cuomo', 'democrat', 'dems', 'donald', 'fake', 'fake news', 'floyd', 'god', 'GOP',
                'governors', 'hoax', 'johnson', 'lab', 'Marxist', 'obama', 'party', 'pelosi', 'political', 'protest',
                'president', 'Progressive', 'protest', 'racism', 'republican', 'reps', 'restriction', 'Socialist', 'thugs',
                'trump', 'white', 'wuhan', 'Wuhan Virus']

    Economy = ['airline', 'bankruptcy', 'bar', 'cancel/cancellation', 'check', 'close', 'cost', 'cruise', 'depression', 'economic',
               'economy', 'employer', 'forgiveness', 'furlough', 'gym', 'insurance', 'job', 'layoff', 'loan', 'lockdown',
               'market', 'meatpacking', 'money', 'mortgage', 'open', 'opening up', 'paid leave', 'payroll', 'recession', 'recover/recovery',
               'rent', 'reopen', 'restaurant', 'restrictions', 'school', 'shut', 'stimulus', 'stock market', 'travel', 'unemployment',
               'union', 'university', 'Wall Street', 'workers', 'workplace']

    Community = ['administration', 'americans', 'cdc', 'city', 'communities', 'community', 'confined', 'contact', 'country', 'europe',
                 'fda', 'global', 'government', 'governor/governors', 'govt', 'homes', 'italy', 'korea', 'Law', 'Lockdown',
                 'Mask', 'nation', 'national', 'niaid', 'nih', 'Niosh', 'osha', 'protest', 'public', 'social',
                 'state', 'tracing', 'Travel', 'u.s.', 'uk', 'WHO']

    #PERSONAL
    Personal = ['Beach', 'Church', 'coping', 'Cruise', 'Dating', 'Diet', 'Dinner', 'Eating out', 'Escape', 'Exercise',
                'feeling', 'God', 'Going out', 'groups', 'Holiday', 'Medication', 'Party', 'Restaurant', 'Self-care', 'Services',
                'shopping', 'Skill', 'Sports', 'Trip', 'vacation', 'Worship',]


    COVID_19_Expression = ['Ache', 'Chest', 'Chill', 'congestion', 'Cough', 'Diarrhea', 'Fever', 'headache', 'ill', 'Infection',
                           'myalgia', 'Nausea', 'respiratory', 'Smell', 'sore throat', 'stuffed nose', 'Throat', 'Vomit']
    

    #ACTIONS/PHASES
    Prevention = ['100000/100,000', 'air', 'Alcohol', 'barrier', 'cases', 'contact', 'control', 'death', 'disinfectant', 'Disinfectant',
                  'disinfectants', 'distancing', 'epidemiologist', 'face', 'Feet', 'Ft', 'Glove', 'Hand', 'hand washing', 'immune',
                  'infections', 'isolation', 'kn95', 'leach', 'lockdown', 'Lysol', 'Mask', 'n95', 'neutralizing', 'osha',
                  'outbreak', 'pandemic', 'pcr', 'plan', 'PPE', 'prevent', 'protect', 'quarantine', 
                  'rate', 'reinfection', 'respirator', 'safety', 'Sanitizer', 'scientists', 'Soap', 'social distancing',
                  'spread', 'test', 'thousands', 'transmission', 'ultraviolent', 'vaccine', 'Wash']

    Treatment = ['Acetaminophen', 'antibodies', 'ards', 'arthritis', 'asthma', 'bleach', 'blood', 'breathing', 'cardiac', 'chloroquine',
                 'contracted', 'copd', 'cough', 'cure', 'diabetes', 'dies', 'doctors', 'dying', 'exposed', 'fever',
                 'hcw', 'healthcare', 'Heat', 'hospitals', 'Humidity', 'hydroxychloroquin', 'Hydroxychloroquine', 'hydroxychloroquine', 'hydroxychloroquine', 'hypertension',
                 'hypertensive', 'icu', 'immunity', 'infection', 'intubation', 'isolation', 'light', 'Miracle', 'nasopharyngeal', 'nasopharynx',
                 'nurse', 'patient', 'pharmacy', 'rationing', 'recovery', 'Remdesivir', 'respiratory', 'sars', 'surgery', 'Testing',
                 'Treating', 'treatment', 'Tylenol', 'Vaccine', 'Ventilator']

    Risk = ['Compromise', 'Danger', 'Defenseless', 'Endanger', 'Exposure', 'Gamble', 'Hazard', 'Imperil', 'Jeopardize',
            'Peril', 'Risk', 'Susceptible', 'Threat', 'trouble', 'Vulnerable']

    #ad_hoc
    ad_hoc = ['ABC', 'Bloomberg', 'CBS', 'CNN', 'Fox', 'HuffPost', 'MSNBC', 'Newsweek', 'NPR', 'PBS',
              'Time', 'Wall Street Journal', 'Washington Post', 'WSJ']
    '''

    #Terms
    Special_terms = ['100000', '5G', 'ABC', 'Acetaminophen', 'Ache', 'administration', 'air', 'airline', 'Alcohol', 'americans',
                     'antibodies', 'ards', 'Arizona', 'arthritis', 'asthma', 'Atlanta', 'Austin', 'AZ', 'bankruptcy', 'bar',
                     'barrier', 'Beach', 'Beck', 'birx', 'Black Lives Matter', 'bleach', 'BLM', 'blood', 'Bloomberg', 'Bolton',
                     'borders', 'Boris', 'Boston', 'breathing', 'Brooklyn', 'CA', 'California', 'cancellation',
                     'cardiac', 'Carlson', 'cases', 'CBS', 'cdc', 'Chandler', 'check', 'Chest', 'Chicago', 'Chill',
                     'china', 'china virus', 'chinese', 'Chinese Virus', 'chloroquine', 'chloroquinequine', 'Church', 'city', 'close', 'closed', 'CNN',
                     'Columbus', 'community', 'Compromise', 'confederate', 'confined', 'congestion', 'conspiracy', 'Constitution', 'contact',
                     'contracted', 'control', 'copd', 'coping', 'cost', 'cough', 'country', 'cruise',
                     'cuomo', 'cure', 'Dallas', 'Danger', 'Dating', 'death', 'Defenseless', 'democrat', 'dems', 'depression',
                     'Detroit', 'diabetes', 'Diarrhea', 'Diet', 'dies', 'Dinner', 'disinfectant', 'distancing', 'doctor', 'donald', 'dying',
                     'dyspnea', 'Eating out', 'economic', 'economy', 'employer', 'Endanger', 'epidemiologist', 'Escape', 'europe', 'Exercise',
                     'exposed', 'Exposure', 'face', 'fake', 'fake news', 'fauci', 'fda', 'feeling', 'Feet', 'fever',
                     'FL', 'Flagstaff', 'Florida', 'floyd', 'forgiveness', 'Fox', 'Ft', 'furlough', 'GA', 'Gamble',
                     'Georgia', 'Gilbert', 'Glendale', 'global', 'Glove', 'god', 'Going out', 'GOP', 'government',
                     'governor', 'govt', 'group', 'gupta', 'gym', 'Hand', 'hand washing', 'Hannity', 'Hazard', 'hcw',
                     'headache', 'healthcare', 'Heat', 'Hewitt', 'hoax', 'Holiday', 'home', 'hospital', 'Houston', 'HuffPost',
                     'Humidity', 'hydroxychloroquin', 'hydroxychlorquine', 'hydroxychloroquine', 'hypertension', 'hypertensive', 'icu', 'IL', 'ill',
                     'Illinois', 'immune', 'immunity', 'Imperil', 'Infection', 'insurance', 'intubation', 'isolation', 'italy', 'Jeopardize',
                     'job', 'johnson', 'kn95', 'korea', 'lab', 'Law', 'layoff', 'light', 'Limbaugh', 'loan',
                     'Lockdown', 'Los Angeles', 'Lysol', 'MA', 'Manhattan', 'Maricopa', 'market', 'Marxist', 'Mask', 'Massachusetts',
                     'meatpacking', 'Medication', 'Medve', 'merkel', 'Mesa', 'MI', 'Miami', 'Michigan', 'Miracle', 'money',
                     'mortgage', 'MSNBC', 'myalgia', 'n95', 'nasopharyngeal', 'nasopharynx', 'nation', 'national', 'Nausea', 'neutralizing',
                     'New York', 'New York Times', 'Newsweek', 'niaid', 'nih', 'Niosh', 'NPR', 'nurse', 'NY', 'NYT',
                     'obama', 'OH', 'Ohio', 'open', 'opening up', 'Orlando', 'osha', 'outbreak', 'PA', 'paid leave',
                     'pandemic', 'party', 'patient', 'payroll', 'PBS', 'pcr', 'Pelosi', 'pence', 'Pennsylvania', 'Peoria',
                     'Peril', 'pharmacy', 'Philadelphia', 'Phoenix', 'Pima', 'Pittsburg', 'plan', 'political', 'PPE',
                     'president', 'prevent', 'Progressive', 'protect', 'protest', 'public', 'putin', 'quarantine', 'racism', 'racist',
                     'rate', 'rationing', 'recession', 'recover', 'recovery', 'reinfection', 'Remdesivir', 'rent', 'reopen',
                     'reps', 'republican', 'respirator', 'respiratory', 'Restaurant', 'restriction', 'Risk', 'safety', 'San Antonio', 'San Diego',
                     'San Francisco', 'Sanitizer', 'sars', 'Savage', 'school', 'scientists', 'Scottsdale', 'Self-care', 'Services', 'shopping',
                     'short of breath', 'shortness of breath', 'shut', 'Skill', 'Smell', 'Soap', 'social', 'social distancing', 'Socialist', 'sore throat',
                     'Sports', 'spread', 'state', 'stimulus', 'stock market', 'stuffed nose', 'surgery', 'Susceptible', 'Tampa', 'Tempe',
                     'test', 'testing', 'Texas', 'thousands', 'Threat', 'Throat', 'thugs', 'Time', 'tracing', 'transmission',
                     'travel', 'treating', 'treatment', 'Trip', 'trouble', 'Trudeau', 'Trump', 'Tucson', 'TX', 'Tylenol',
                     'u.s.', 'uk', 'u.k.', 'ultraviolet', 'unemployment', 'union', 'university', 'vacation', 'vaccine',
                     'Ventilator', 'vitamin c', 'vitamin d', 'Vomit', 'Vulnerable', 'Wall Street', 'Wall Street Journal', 'Wash', 'Washington Post', 'white',
                     'WHO', 'workers', 'workplace', 'World Health Organization', 'Worship', 'WSJ', 'wuhan', 'Wuhan Virus', 'Xi', 'Yuma']
                     

    #Location
    California = ['CA', 'California', 'Los Angeles', 'San Francisco', 'San Diego']

    Texas = ['Texas', 'TX', 'Dallas', 'Houston', 'San Antonio', 'Austin']

    New_York = ['New York', 'NY', 'Brooklyn', 'Manhattan']

    Florida = ['Florida', 'FL', 'Miami', 'Orlando', 'Tampa']

    Illinois = ['Illinois', 'IL', 'Chicago']

    Georgia = ['Georgia', 'GA', 'Atlanta']

    Other = ['Pennsylvania', 'PA', 'Philadelphia', 'Pittsburg', 'Michigan', 'MI', 'Detroit', 'Massachusetts', 'MA', 'Boston', 'Ohio', 'OH', 'Columbus']

    Arizona = ['Arizona', 'AZ', 'Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Scottsdale', 'Gilbert', 'Glendale', 'Tempe', 'Pima', 'Maricopa', 'Peoria', 'Yuma', 'Flagstaff']

    Locations_list = California + Texas + New_York + Florida + Illinois + Georgia + Other + Arizona
    Locations = {}
    for e in Locations_list:
        Locations[e] = True


    #emotions
    Emotions = ['positive', 'negative', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']

    #Source
    Source = ['Retweet', 'Organization (has URL)', 'Other (assumed to be original)']
    

    
    #Read the NRC file
    NRC_map = {'positive': [], 'negative': [], 'anger': [], 'anticipation': [], 'disgust': [], 'fear': [], 'joy': [], 'sadness': [], 'surprise': [], 'trust': []}
    with open('NRC-Emotion-Lexicon-Wordlevel-v0.92.txt', 'r+') as f:
        for line in f:
            line = line.strip()
            if line:
                temp_NRC = line.split('\t')
                if temp_NRC[2] == '1' and temp_NRC[1] in NRC_map:
                    NRC_map[temp_NRC[1]].append(temp_NRC[0])
    
    
    nlp = spacy.load('en', disable=['pareser', 'ner'])
    stop_words_list = nlp.Defaults.stop_words
    stop_words = {}
    for element in stop_words_list:
        stop_words[element] = True
    
    
    
    with open('Expert_Term_Analysis/COVID.csv', 'w+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        first_row = []
        first_row += ['ID'] + ['Text'] + Special_terms + Emotions + Source + ['Date']
        #first_row += ['ID'] + ['Screen Name'] + ['User Name'] + ['Retweet Count'] + ['Followers Count']
        writer.writerow(first_row)
        
        Special_terms_nlp = nlp_terms(Special_terms, nlp)
        
        
        for ele in temp:
            reader = None
            with open(ele, 'r', encoding='utf-8') as file:
                reader = list(csv.reader(file))
                reader = preprocess(reader)

            for i in range(1, len(reader)):
                
                lemmatization = nlp(reader[i][4].lower())
                row = [reader[i][0], reader[i][4]]
                for e in range(len(Special_terms)):
                    row.append(exist_Term(lemmatization, reader[i][4], Special_terms[e], Special_terms_nlp[e], Locations, reader[i][5]))

                #emotions
                row += get_emotions(lemmatization, stop_words, NRC_map)

                #source
                row += get_source(reader[i][4])

                row.append(reader[i][3].split()[0])
                
                #row = [reader[i][0], reader[i][1], reader[i][2], reader[i][7], reader[i][12]]
                
                writer.writerow(row)
                
            print('Done')
        

def get_source(original_text):
    source = [0, 0, 0]
    if original_text[0:2] == 'RT':
        source[0] = 1
    if 'https://' in original_text:
        source[1] = 1
    if source[0] == 0 and source[1] == 0:
        source[2] = 1
    return source

def get_emotions(lemmatization, stop_words, NRC_map):
    emotions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index_map = {0: 'positive', 1: 'negative', 2: 'anger', 3: 'anticipation', 4: 'disgust',5: 'fear', 6: 'joy', 7: 'sadness', 8: 'surprise', 9: 'trust'}
    for e in lemmatization:
        if e.lemma_ not in stop_words:
            for i in range(len(emotions)):
                if e.lemma_ in NRC_map[index_map[i]]:
                    emotions[i] += 1
    return emotions

def exist_Term(lemmatization, original_string, term, term_nlp, Locations, loc):
    if term not in Locations:
        size = len(term.strip().split())
        if term == 'WHO':
            if term in original_string:
                return 1
            else:
                return 0
        if size > 1 or term == 'u.s.' or term == 'u.k.':
            if term.lower() in original_string.lower():
                return 1
        else:
            if term == '5G':
                if term in original_string:
                    original_string_list = original_string.strip().split()
                    if term in original_string_list:
                        return 1
            elif term == '100000':
                for ele in lemmatization:
                    if ele.lemma_ == '100000' or ele.lemma_ == '100,000':
                        return 1
            else:
                for ele in lemmatization:
                    if ele.lemma_ == term_nlp:
                        return 1
        return 0
    else:
        location = loc.strip().lower().split(',')
        for ele in location:
            if term.lower() == ele.strip():
                return 1
        return 0

def nlp_terms(terms, nlp):
    terms_nlp = []
    for e in terms:
        s = nlp(e.lower())
        terms_nlp.append(s[0].lemma_)
    return terms_nlp


def preprocess(reader):
    total = 0
    unique = {}
    temp = []
    for ele in reader:
        if len(ele) > 10:
            total += 1
            key = ele[0]
            if key not in unique:
                unique[key] = True
                temp.append(ele)
    return temp
            
          
priority_terms()
