universities = [
    ['Ale-Taha Institute Of Higher Education'],
    ['Alzahra University', 'Alzahra U'],
    ['Amirkabir University of Technology', 'Amirkabir UT'],
    ['Ardabil Technical and Vocational University'],
    ['Azad U of Tehran Center'],
    ['Azad U of Tehran South'],
    ['Azad University of Lahijan'],
    ['Azarbijan Shahid Madani U'],
    ['Babol University of Technology'],
    ['Birjand University'],
    ['Bonab Faculty of Engineering'],
    ['Bu-Ali Sina University'],
    ['Fasa University', 'Fasa U'],
    ['Ferdowsi University of Mashhad', 'Ferdowsi U of Mashhad'],
    ['Ghias-al-din Jamshid Kashani', 'Ghis-al-din Jamshid Kashani , Abyek'],
    ['Golestan University of Grogan'],
    ['Gonbad Kavoos University'],
    ['Guilan U', 'Guilan University'],
    ['Hakim Sabzevari University'],
    ['Hamedan University of Technology'],
    ['Imam Reza University of Mashhad'],
    ['Imam-Khomeini International University', 'Imam-Khomeini U'],
    ['Institute for Advanced Studies in Basic Sciences'],
    ['Iran University of Science & Technology'],
    ['Isfahan University of Technology', 'Isfahan UT'],
    ['Islamic Azad University of Karaj'],
    ['Islamic Azad University of Mashhad', 'Azad U of Mashhad'],
    ['Islamic Azad University of Najaf Abad'],
    ['Islamic Azad University of Parand', 'Azad U of Parand'],
    ['Islamic Azad University of Qazvin'],
    ['Jahrom University', 'Jahrom U'],
    ['Karaj Sama University'],
    ['Kashmar Higher Education Institute'],
    ['Khaje Nasir Toosi University of Technology', 'Khaje Nasir Toosi UT'],
    ['Kharazmi University', 'Kharazmi U'],
    ['Khatam Alanbia University of Technology', 'Khatam Alanbia UT'],
    ['Khayyam University', 'Khayyam U'],
    ['Mahallat Institute Of Higher Education'],
    ['Mazandaran University of Science and Technology', 'Mazandaran UST'],
    ['Mohaghegh Ardebili University'],
    ['Pasargad University of Shiraz', 'Pasargad U of Shiraz'],
    ['Payam Noor University of Najaf Abad', 'PayamNoor University Of Najaf Abad'],
    ['Payame Noor Bandar Abbas'],
    ['Payame Noor University of Mashhad', 'Payame Noor Mashhad'],
    ['Payame Noor University of Hamedan'],
    ['Payame Noor University of Hashtgerd'],
    ['Persian Gulf University', 'Persian Gulf U'],
    ['Qom Islamic Azad University'],
    ['Qom Technical And Vocational University'],
    ['Qom University'],
    ['Razi University of Kermanshah'],
    ['Refah University'],
    ['Sadjad University of Technology', 'Sadjad UT'],
    ['Safahan University of Isfahan'],
    ['Semnan University'],
    ['Shahab Danesh University'],
    ['Shahed University', 'Shahed U'],
    ['Shahid Bahonar University of Kerman', 'Shahid Bahonar U of Kerman'],
    ['Shahid Beheshti University', 'Shahid Beheshti U'],
    ['Shahid Chamran University of Ahvaz', 'Shahid Chamran U of Ahvaz'],
    ['Shahid Rajaei U'],
    ['Shahrekord University', 'Shahrekord U'],
    ['Shahrood University', 'Shahrood U'],
    ['Sharif University of Technology', 'Sharif UT'],
    ['Sheikhbahaee Universtity'],
    ['Shiraz University', 'Shiraz U'],
    ['Shiraz University of Technology'],
    ['Somayeh Najaf Abad Technical College'],
    ['Tehran Technical College of Shariaty'],
    ['Tuyserkan Faculty of Engineering'],
    ['University of Isfahan', 'U of Isfahan'],
    ['University of Science & Culture', 'U of Science & Culture'],
    ['University of Tabriz', 'U of Tabriz'],
    ['University of Tehran', 'U of Tehran', 'U of Tehran Eng'],
    ['U of Zabol'],
    ['University of Kashan'],
    ['University of Kurdistan'],
    ['University of Semnan'],
    ['University of Sistan and Baluchestan'],
    ['University of Zanjan'],
    ['Urmia University', 'Urmia U'],
    ['Urmia University Of Technology', 'Urmia UT'],
    ['Vali-E-Asr University', 'Vali-E-Asr U'],
    ['Yazd University', 'Yazd U', 'Yazd University of Iran']
]

def get_university_name(name):
    for row in universities:
        if name in row:
            return row[0]
    
    return None