
class ProvinceHandler:

    data = {
        'Ale-Taha Institute Of Higher Education' : 'Tehran',
        'Alzahra University' : 'Tehran',
        'Amirkabir University of Technology' : 'Tehran',
        'Ardabil Technical and Vocational University' : 'Ardabil',
        'Azad U of Tehran Center' : 'Tehran',
        'Azad U of Tehran South' : 'Tehran',
        'Azad University of Lahijan' : 'Gilan',
        'Azarbijan Shahid Madani U' : 'Azerbaijan, East',
        'Babol University of Technology' : 'Mazandaran',
        'Birjand University' : 'Khorasan, South',
        'Bonab Faculty of Engineering' : 'Azerbaijan, East',
        'Bu-Ali Sina University' : 'Hamadan',
        'Fasa University' : 'Fars',
        'Ferdowsi University of Mashhad' : 'Khorasan, Razavi',
        'Ghias-al-din Jamshid Kashani' : 'Qazvin',
        'Golestan University of Grogan' : 'Golestan',
        'Gonbad Kavoos University' : 'Golestan',
        'Guilan U' : 'Gilan',
        'Hakim Sabzevari University' : 'Khorasan, Razavi',
        'Hamedan University of Technology' : 'Hamadan',
        'Imam Reza University of Mashhad' : 'Khorasan, Razavi',
        'Imam-Khomeini International University' : 'Qazvin',
        'Institute for Advanced Studies in Basic Sciences' : 'Zanjan',
        'Iran University of Science & Technology' : 'Tehran',
        'Isfahan University of Technology' : 'Isfahan',
        'Islamic Azad University of Karaj' : 'Alborz',
        'Islamic Azad University of Mashhad' : 'Khorasan, Razavi',
        'Islamic Azad University of Najaf Abad' : 'Isfahan',
        'Islamic Azad University of Parand' : 'Tehran',
        'Islamic Azad University of Qazvin' : 'Qazvin',
        'Jahrom University' : 'Fars',
        'Karaj Sama University' : 'Alborz',
        'Kashmar Higher Education Institute' : 'Khorasan, Razavi',
        'Khaje Nasir Toosi University of Technology' : 'Tehran',
        'Kharazmi University' : 'Tehran',
        'Khatam Alanbia University of Technology' : 'Tehran',
        'Khayyam University' : 'Khorasan, Razavi',
        'Mahallat Institute Of Higher Education' : 'Markazi',
        'Mazandaran University of Science and Technology' : 'Mazandaran',
        'Mohaghegh Ardebili University' : 'Ardabil',
        'Pasargad University of Shiraz' : 'Fars',
        'Payam Noor University of Najaf Abad' : 'Isfahan',
        'Payame Noor Bandar Abbas' : 'Hormozgan',
        'Payame Noor University of Mashhad' : 'Khorasan, Razavi',
        'Payame Noor University of Hamedan' : 'Hamadan',
        'Payame Noor University of Hashtgerd' : 'Alborz',
        'Persian Gulf University' : 'Bushehr',
        'Qom Islamic Azad University' : 'Qom',
        'Qom Technical And Vocational University' : 'Qom',
        'Qom University' : 'Qom',
        'Razi University of Kermanshah' : 'Kermanshah',
        'Refah University' : 'Tehran',
        'Sadjad University of Technology' : 'Khorasan, Razavi',
        'Safahan University of Isfahan' : 'Isfahan',
        'Semnan University' : 'Semnan',
        'Shahab Danesh University' : 'Qom',
        'Shahed University' : 'Tehran',
        'Shahid Bahonar University of Kerman' : 'Kerman',
        'Shahid Beheshti University' : 'Tehran',
        'Shahid Chamran University of Ahvaz' : 'Khuzestan',
        'Shahid Rajaei U' : 'Tehran',
        'Shahrekord University' : 'Chahar Mahaal and Bakhtiari',
        'Shahrood University' : 'Semnan',
        'Sharif University of Technology' : 'Tehran',
        'Sheikhbahaee Universtity' : 'Isfahan',
        'Shiraz University' : 'Fars',
        'Shiraz University of Technology' : 'Fars',
        'Somayeh Najaf Abad Technical College' : 'Isfahan',
        'Tehran Technical College of Shariaty' : 'Tehran',
        'Tuyserkan Faculty of Engineering' : 'Hamadan',
        'University of Isfahan' : 'Isfahan',
        'University of Science & Culture' : 'Tehran',
        'University of Tabriz' : 'Azerbaijan, East',
        'University of Tehran' : 'Tehran',
        'U of Zabol' : 'Sistan and Baluchestan',
        'University of Kashan' : 'Isfahan',
        'University of Kurdistan' : 'Kurdistan',
        'University of Semnan' : 'Semnan',
        'University of Sistan and Baluchestan' : 'Sistan and Baluchestan',
        'University of Zanjan' : 'Zanjan',
        'Urmia University' : 'Azerbaijan, West',
        'Urmia University Of Technology' : 'Azerbaijan, West',
        'Vali-E-Asr University' : 'Kerman',
        'Yazd University' : 'Yazd'
    }

    @staticmethod
    def get_province(university):
        if university in ProvinceHandler.data.keys():
            return ProvinceHandler.data[university]
        else:
            return None
    
    @staticmethod
    def get_all_provinces():
        return [s.strip() for s in open("provinces.txt").readlines()]

print(ProvinceHandler.get_all_provinces())

