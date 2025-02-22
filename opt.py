import os
import re
import string
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
pakistani_firstnam  = [
    "Aaira", "Aaliya", "Aleena", "Amna", "Anaya", "Areeba", "Asma", "Ayesha",
    "Bushra", "Dania", "Emaan", "Faiza", "Faryal", "Fatima", "Hafsa", "Hina",
    "Iqra", "Khadija", "Mahnoor", "Maliha", "Mehak", "Nimra", "Noreen",
    "Rabia", "Rida", "Sadia", "Sana", "Sarah", "Sehar", "Shazia", "Sobia",
    "Sumaira", "Tahira", "Uzma", "Warda", "Yusra", "Zahra", "Zainab", "Zoya",
    "Afifa", "Anjum", "Arfa", "Asiya", "Aziza", "Benazir", "Bilqis", "Dilruba",
    "Dur-e-Shehwar", "Erum", "Farah", "Fiza", "Ghazala", "Gul", "Huma", "Huriya",
    "Inaya", "Javeria", "Kaneez", "Kiran", "Lubna", "Mahjabeen", "Mariam", "Mona",
    "Nadia", "Nasreen", "Nazia", "Neha", "Nida", "Parveen", "Quratulain", "Raheela",
    "Ramsha", "Rimsha", "Rukhsar", "Saadia", "Saima", "Saira", "Sania", "Shabana",
    "Shehnaz", "Shiza", "Sidra", "Simra", "Sundas", "Tabassum", "Tamanna", "Tehmina",
    "Tuba", "Uzairah", "Wania", "Yumna", "Zakia", "Zareen", "Zarmeen", "Zohra",
    "Adeela", "Afreen", "Ahlam", "Aila", "Aiman", "Ainul", "Ambar", "Amreen",
    "Anam", "Arisha", "Asifa", "Azra", "Bisma", "Dua", "Eram", "Erum", "Fahmida",
    "Farzana", "Ferdaus", "Firdaus", "Gulalai", "Gulshan", "Hajra", "Haniya",
    "Humaima", "Ifrah", "Iman", "Iram", "Irsa", "Jahanara", "Jameela", "Jannat",
    "Javaria", "Kainat", "Kashaf", "Komal", "Laila", "Maha", "Mahwish", "Malika",
    "Mansoora", "Mashal", "Masooma", "Mawra", "Mehrunisa", "Mehrun", "Minahil",
    "Momina", "Mubeena", "Mumtaz", "Munazza", "Munni", "Nargis", "Nazish", "Nigar",
    "Nimrah", "Noshaba", "Nosheen", "Palwasha", "Pakeeza", "Qudsia", "Rafia",
    "Rameeza", "Razia", "Rehana", "Roma", "Roshni", "Rukhsana", "Sabeen", "Sabiha",
    "Sabeeka", "Sadia", "Samina", "Saniah", "Sanober", "Shagufta", "Shaista",
    "Shaheen", "Shanzay", "Shehreen", "Shifa", "Shirin", "Sobia", "Sundus",
    "Suraiya", "Tania", "Tayeba", "Tooba", "Ujala", "Umme", "Wajeeha", "Wardah",
    "Yasmin", "Zahida", "Zarina", "Zarnab", "Zenia", "Zunaira",
    "Abeer", "Areej", "Armina", "Ayesha", "Bano", "Bushra", "Dur-e-Fishan",
    "Feroza", "Habiba", "Hajira", "Javeriya", "Kanza", "Kulsoom", "Maimoona",
    "Mehreen", "Najma", "Nayab", "Qaiser", "Rabab", "Ramla", "Reem", "Ruba",
    "Sadaf", "Sabahat", "Safoora", "Sania", "Shama", "Shanaya", "Shanzay",
    "Shazia", "Shumaila", "Simra", "Somia", "Sumaiya", "Tamana", "Tehreem",
    "Umama", "Uzaira", "Uzma", "Wajiha", "Zain", "Zeenat", "Zehra", "Zulaikha",
    "Abida", "Aafia", "Anum", "Asra", "Beenish", "Farida", "Firyal", "Ghazal",
    "Huda", "Jamila", "Kanwal", "Kashish", "Lareeb", "Malika", "Misha", "Nashra",
    "Nazmeen", "Noor", "Pari", "Rameen", "Rania", "Reema", "Ruba", "Saadia",
    "Sahar", "Samra", "Sara", "Sobia", "Sohni", "Sonia", "Sufia", "Tahmina",
    "Tayyaba", "Uzra", "Yusra", "Zara", "Zenia", "Zobia",
    "Aaima", "Afshan", "Aleema", "Aqsa", "Arishma", "Aymen", "Areesha", "Armina",
    "Aseefa", "Bismah", "Dur-e-Adan", "Dur-e-Makhnoon", "Elma", "Eshaal", "Faariha",
    "Fakhra", "Falak", "Faryha", "Fizza", "Ghaznina", "Gulbano", "Hafiza", "Haleema",
    "Haniya", "Hayat", "Heena", "Hoorain", "Iffat", "Iramnaz", "Irsa", "Jasmine",
    "Juwairiya", "Kainaat", "Khadeeja", "Komal", "Laika", "Lareen", "Lubaina",
    "Mahjabeen", "Mahveen", "Maiza", "Mehnaz", "Maimuna", "Minahil", "Misha",
    "Mishal", "Mubeena", "Muniba", "Mushk", "Nabeela", "Nabiha", "Najia", "Najiba",
    "Nashmia", "Naureen", "Nazima", "Nimrah", "Noshin", "Pakiza", "Parveen",
    "Qamar", "Qudsia", "Rabiya", "Raima", "Raniah", "Rehana", "Rihana", "Rishal",
    "Rohi", "Romaisa", "Rubaida", "Rumana", "Saadia", "Sabeena", "Sadiqa", "Saeeda",
    "Sahil", "Sahrish", "Sairah", "Sakina", "Salsabeel", "Samiyah", "Saniah",
    "Saniya", "Sarahya", "Seher", "Sheeba", "Sheherbano", "Shireen", "Siddra",
    "Simrah", "Sobiaa", "Sumaia", "Sumaira", "Sumbul", "Tabinda", "Tahmeena",
    "Tamseela", "Taniah", "Tehniyat", "Urooj", "Uzmaiya", "Wajeeha", "Yasmeen",
    "Zahabiya", "Zaira", "Zainaa", "Zakiaa", "Zaleeha", "Zarmina", "Zarmeena",
    "Zarqa", "Zawiyah", "Zoyaisha", "Zubaida", "Zulekha", "Zunain", "Zunisha",
    "Abiya", "Adiba", "Ameera", "Arjuman", "Aleeza", "Aliya", "Anabia", "Arishba",
    "Ashwaq", "Asiyaan", "Asna", "Ayza", "Aysha", "Bareera", "Baariha", "Bushrah",
    "Dawna", "Daneen", "Daniah", "Ezzah", "Eshqa", "Fahmida", "Fareeha", "Fariha",
    "Farrah", "Firdous", "Fizzaa", "Fizzaiah", "Ghazia", "Ghena", "Guleen",
    "Gullak", "Gulsim", "Habeeba", "Habeerah", "Haleemah", "Halima", "Hiba", "Hinaaz",
    "Hubaina", "Humaari", "Humna", "Iftikhar", "Ijlaal", "Inabia", "Irraa",
    "Ishfaq", "Ishqa", "Iqraah", "Ishaari", "Jasmya", "Jasminah", "Juwairah",
    "Khalida", "Khaliza", "Khulaa", "Kokab", "Laibnaz", "Leman",
    "Maherra", "Mahmeena", "Mahnooraz", "Mahnur", "Mahzabeen", "Mahwishaa",
    "Mahrun", "Manaahil", "Manha", "Maryam", "Mayeesha", "Maysarah", "Mishaal",
    "Mishbah", "Munirah", "Naaima", "Naaznin", "Naazir", "Nabiya", "Nazeeha",
    "Nidrah", "Noorana", "Nuha", "Nuzhat", "Parineh", "Peezahn", "Qadeeja",
    "Qurratain", "Rabeel", "Rabeeyah", "Rabiyaah", "Rabina", "Rahiba", "Reemana",
    "Reeman", "Reham", "Rehbeya", "Rehmah", "Rihaba", "Rozaah", "Rubab", "Ruhiya",
    "Safinah", "Safiya", "Sadafiya", "Saeedah", "Saeha", "Sameerah", "Saumya",
    "Saajra", "Sadiaah", "Salina", "Samaira", "Sanayaah", "Saniyaaz", "Shahwaz",
    "Sheryaar", "Shiraza", "Shafqat", "Subaina", "Suraiya", "Tabinaz", "Tahani",
    "Tahiyyah", "Tamanaah", "Tehzin", "Tanweez", "Tanjeela", "Tamkeen", "Uroojay",
    "Uzayn", "Umehna", "Umairah", "Umayma", "Waqina", "Waqariyah", "Wasinah",
    "Wisma", "Zahriyah", "Zaibunn", "Zainira", "Zakaraa", "Ziyaan", "Zuhaim",
    "Abiyaan", "Adreema", "Alizey", "Aameena", "Amenaaz", "Zerminaa",
    "Aabroo", "Aafiya", "Aaila", "Aamna", "Aanika", "Aarifa", "Aarwa", "Aasiya",
    "Abshira", "Adira", "Afra", "Ahana", "Ahlaam", "Ahlam", "Aiman", "Ainee",
    "Aizah", "Akifah", "Aleena", "Alma", "Alveena", "Amani", "Ambreen", "Amel",
    "Amira", "Amna", "Anaaya", "Anam", "Anaya", "Anjum", "Anwar", "Areeba",
    "Arfa", "Arisha", "Ariza", "Asfa", "Ashiya", "Asma", "Asrin", "Atiya",
    "Aurat", "Azka", "Azra", "Badia", "Badreya", "Bakhtawar", "Balqis", "Bano",
    "Barira", "Batool", "Bibi", "Bushra", "Chera", "Daneen", "Darakhshan",
    "Deeba", "Dilruba", "Dilshaad", "Dua", "Dur-e-Fishan", "Dur-e-Malika",
    "Eimaan", "Eira", "Eliza", "Emaan", "Ersa", "Esra", "Fadwa", "Fahima",
    "Faiqa", "Faiza", "Falah", "Fara", "Farah", "Fariya", "Farzana", "Fasiha",
    "Fathima", "Fayra", "Fazeela", "Fehmina", "Fehmida", "Fouzia", "Ghazala",
    "Ghazwa", "Gulehena", "Gulzar", "Hafsa", "Haleema", "Haniya", "Hanzala",
    "Hareem", "Hasina", "Hawwa", "Hayaa", "Heba", "Hidaya", "Hira", "Hooriya",
    "Humera", "Hurain", "Husna", "Huzai", "Ibtisam", "Ifra", "Imaan", "Inara",
    "Iram", "Irfana", "Irtiza", "Ishaal", "Ismat", "Ittehad", "Jaana", "Jahaan",
    "Jaleela", "Jamila", "Janat", "Javeria", "Jemima", "Kaashifah", "Kaif",
    "Kaneez", "Kanwal", "Kariman", "Kashaf", "Kausar", "Khadra", "Khurshid",
    "Kiran", "Kulsoom", "Laaiqa", "Lajwanti", "Lamia", "Laraib",
    "Layla", "Liyana", "Lubna", "Maha", "Mahera", "Mahira", "Mahrukh", "Maiza",
    "Malika", "Maneesha", "Manha", "Maqboola", "Marjaan", "Marwa", "Masooma",
    "Mehak", "Mehrunisa", "Mehwish", "Midhat", "Misbah", "Mohtarma", "Mumtaz",
    "Munaza", "Nadia", "Naima", "Najma", "Narmeen", "Nashit", "Nayab", "Naziha",
    "Nida", "Nighat", "Noor", "Noorain", "Nuha", "Numra", "Nureen", "Nuzhat",
    "Omaira", "Palwasha", "Parveen", "Qamarunnisa", "Qanitah", "Qareena",
    "Qudsia", "Rabail", "Rafia", "Rahat", "Raima", "Raisa", "Ramisha", "Rani",
    "Rania", "Rasheeda", "Reema", "Reshma", "Rida", "Rihana", "Rizwana", "Rohma",
    "Roohi", "Rozina", "Rukhsana", "Rumaisa", "Saba", "Sabeeka", "Sabiha",
    "Sadaf", "Safiya", "Sahar", "Sakeena", "Salma", "Saman", "Samavia", "Samiya",
    "Sania", "Sanober", "Sara", "Sarfraz", "Sarwat", "Sehar", "Shaima", "Shaista",
    "Shamaila", "Shamsa", "Sharmin", "Shazia", "Shereen", "Shiza", "Shumaila",
    "Sobia", "Sughra", "Sumaiya", "Sumbal", "Tabassum", "Tahira", "Taqdees",
    "Tanzeela", "Tara", "Tarannum", "Tazeen", "Tehmeena", "Ulfat", "Umaima",
    "Urooj", "Uzairah", "Uzma", "Vaqar", "Wahida", "Warda", "Wasila", "Yumna",
    "Zaara", "Zaina", "Zainab", "Zakia", "Zarafshan", "Zarghoona", "Zarina",
    "Zarnab", "Zarqa", "Zeenat", "Zhalay", "Ziyana", "Zoha", "Zubaida",
    "Zulfa", "Zulekha"
]

pakistani_lastnam = [
    "Abbas", "Abbasi", "Abidi", "Afridi", "Ahmad", "Akhtar", "Ali", "Alvi",
    "Ansari", "Arain", "Ashraf", "Asif", "Aziz", "Baig", "Baloch", "Bhatti",
    "Bokhari", "Butt", "Chaudhry", "Chishti", "Dar", "Dastgir", "Durrani",
    "Farooqi", "Fazal", "Feroz", "Ghafoor", "Ghani", "Ghaus", "Gilani", "Haider",
    "Hameed", "Hamid", "Hashmi", "Hassan", "Hussain", "Iftikhar", "Iqbal", 
    "Ishtiaq", "Jafri", "Jahangir", "Jalil", "Jamil", "Jatoi", "Javed", "Jehangir",
    "Junaid", "Kamal", "Kamran", "Karim", "Kazmi", "Khalid", "Khan", "Khattak",
    "Khokhar", "Latif", "Lodhi", "Majeed", "Malik", "Mamoon", "Mansoor", 
    "Masood", "Mazhar", "Memon", "Mir", "Mirza", "Mustafa", "Naqvi", "Nasir",
    "Nawaz", "Nazir", "Niaz", "Noor", "Noreen", "Paracha", "Pirzada", "Qadir",
    "Qamar", "Qazi", "Rafiq", "Rahman", "Raja", "Rajput", "Rasheed", "Raza",
    "Razzaq", "Rehman", "Sabir", "Sadiq", "Saeed", "Safi", "Sajid", "Saleem",
    "Sami", "Saqib", "Sardar", "Shah", "Shahbaz", "Shaikh", "Sharif", "Sheikh",
    "Siddiqi", "Siddiqui", "Soofi", "Sultan", "Syed", "Tahir", "Talat", "Tariq",
    "Usmani", "Waheed", "Wali", "Wazir", "Younas", "Yusuf", "Zafar", "Zaheer",
    "Zahid", "Zaki", "Zaman", "Zia", "Zubair", "Abdul", "Abidi", "Adil", 
    "Ahmed", "Ajmal", "Akhund", "Alam", "Ali", "Altaf", "Amjad", "Anjum", 
    "Ansar", "Asghar", "Aslam", "Asrar", "Atif", "Azam", "Ayub", "Babar", 
    "Bashir", "Basit", "Bukhari", "Chohan", "Chughtai", "Danish", "Dawar",
    "Ehsan", "Faheem", "Faisal", "Fakhri", "Farrukh", "Fateh", "Fazal", 
    "Ghazanfar", "Gul", "Habib", "Hadi", "Hafeez", "Haidar", "Haleem", 
    "Hamza", "Hanif", "Haroon", "Hashim", "Hidayat", "Huma", "Humayun", 
    "Imran", "Inayat", "Irfan", "Ishaq", "Israr", "Jabbar", "Jalal", 
    "Jamshaid", "Junaid", "Kabir", "Kamal", "Kamran", "Khanani", "Khurram", 
    "Latif", "Mansha", "Mashood", "Mohiuddin", "Mufti", "Mujahid", "Mumtaz", 
    "Munir", "Murad", "Naeem", "Nawazish", "Nazeer", "Obaid", "Osman", 
    "Pasha", "Qasim", "Qudrat", "Rafique", "Rahim", "Rasheed", "Rehan", 
    "Saad", "Saadiq", "Saif", "Sajjad", "Sani", "Shabir", "Shad", "Shahid", 
    "Shaista", "Shamshad", "Shoaib", "Shuja", "Sohail", "Subhan", "Sufyan", 
    "Taimur", "Tanveer", "Tariq", "Tayyab", "Umair", "Umar", "Usman", 
    "Waqar", "Wasim", "Waseem", "Yasin", "Yousuf", "Zafarullah", "Zahid", 
    "Zakiuddin", "Zulfiqar", "Zunair", "Abbasi", "Abid", "Adeel", "Akram", 
    "Aliyan", "Amir", "Asad", "Basharat", "Bilal", "Chaudhry", "Durrani", 
    "Ehtesham", "Faisal", "Farhan", "Fazil", "Ghous", "Haq", "Haseeb", 
    "Hassan", "Idrees", "Jahanzaib", "Jawad", "Kabir", "Kazi", "Kazim", 
    "Lashari", "Mahmood", "Malik", "Mansoor", "Masood", "Nisar", "Nizami", 
    "Rafi", "Rashid", "Saboor", "Shafi", "Shujaat", "Suleman", "Tufail", 
    "Wahid", "Wazir", "Yameen", "Zaidi", "Zain", "Zaman", "Zeeshan",
    "Abro", "Achakzai", "Afzal", "Agha", "Ahmedzai", "Akbari", "Akhundzada", 
    "Alamgir", "Alizai", "Amil", "Anjum", "Arif", "Arzoo", "Asghar", "Aslam", 
    "Atif", "Aurangzeb", "Awan", "Azmat", "Babar", "Badshah", "Bahadur", 
    "Bajwa", "Baloch", "Bangash", "Barlas", "Basharat", "Batool", "Bhatti", 
    "Bhutto", "Bizenjo", "Chachar", "Chandio", "Channa", "Chatha", "Chishti", 
    "Daher", "Daudpota", "Dawar", "Dehlavi", "Dehwar", "Dewan", "Dina", 
    "Dogar", "Durrani", "Elyas", "Faqeer", "Fida", "Firdous", "Gabol", "Gardezi", 
    "Ghazi", "Ghulam", "Gohar", "Gondal", "Goraya", "Gulzar", "Hafeez", 
    "Haji", "Hamdani", "Hanif", "Hussaini", "Ibrahim", "Ikram", 
    "Imtiaz", "Inam", "Inayatullah", "Iqtidar", "Ismail", "Jadoon", "Jahangiri", 
    "Jalaluddin", "Jan", "Jatoi", "Jhandir", "Jilani", "Jogi", "Kalhoro", 
    "Kalwar", "Kanjo", "Kashif", "Kashmiri", "Katpar", "Kayani", "Khanum", 
    "Khanzada", "Khoso", "Khurram", "Khushal", "Khushdil", "Khuzdar", "Koreshi", 
    "Kundi", "Kurashi", "Laghari", "Langah", "Lashari", "Lohar", "Lukman", 
    "Machh", "Mahesar", "Mahmood", "Magsi", "Mahar", "Maher", "Malghani", 
    "Mamnoon", "Manzoor", "Marri", "Mashwani", "Matloob", "Mazari", "Meer", 
    "Mirani", "Mirjat", "Mitha", "Mokha", "Mukhtar", "Mumtaz", "Munawar", "Nadir", "Nafees", "Naheed", "Naqash", "Naqi", "Naseer", "Nasim", 
    "Nasreen", "Nawazish", "Nimra", "Nizamani", "Noorani", "Noorzai", 
    "Nusrat", "Osman", "Panhwar", "Pir", "Pirzada", "Qadeer", "Qadir", 
    "Qasmi", "Qureshi", "Rahim", "Raisani", "Rakhshani", "Ranjha", "Rasheed", 
    "Razzaq", "Sabri", "Safdar", "Safiullah", "Sahar", "Sajid", "Salamat", 
    "Salman", "Sanaullah", "Sarfaraz", "Satti", "Sawati", "Shaikhani", 
    "Shaista", "Sharifzada", "Sheedi", "Siddiq", "Somro", "Subhani", "Sulemani", 
    "Sumbal", "Surani", "Syedzada", "Tabassum", "Tahir", "Talpur", "Tanoli", 
    "Tariq", "Tasnim", "Tirmizi", "Turk", "Ubaid", "Umarzai", "Usman", 
    "Waqar", "Waseem", "Wasti", "Yamin", "Yaqoob", "Yousufzai", "Zahir", 
    "Zardari", "Zeb", "Ziauddin", "Zuberi", "Zulfiqar", "Zulqarnain", 
    "Abbass", "Abidi", "Admani", "Afandi", "Afsar", "Ahwazi", "Akhundzada", 
    "Almani", "Amirzai", "Anwar", "Ashrafi", "Aslamzai", "Atiqullah", 
    "Baban", "Baghban", "Bagra", "Baladi", "Barakzai", "Barlas", "Basra", 
    "Bazai", "Bhutta", "Bijarani", "Bukhari", "Chaghtai", "Charan", "Chitral", 
    "Chundrigar", "Dawar", "Dholkiya", "Durani", "Farooqi", "Fatehzada", 
    "Faheem", "Ghafoor", "Ghazanavi", "Ghaznavi", "Ghazali", "Hafeezullah", 
    "Hakimzada", "Haroonzai", "Hasanzai", "Hidayatullah", "Hijazi", 
    "Hussainzai", "Ihsan", "Ikhlaq", "Imdadullah", "Irfanullah", "Jaffari", 
    "Jamaati", "Janbaz", "Kakar", "Kamil", "Karim", "Karimullah", "Kazmi", 
    "Khakhwani", "Khakwani", "Khakwanzai", "Khanani", "Khatri", "Khoja", 
    "Kiyani", "Kohistani", "Lajwari", "Lakhani", "Lohani", "Mahesar", 
    "Makhdumi", "Malikzada", "Malwana", "Mashadi", "Mazari", "Meharban", 
    "Mehr", "Mehraban", "Memonzada", "Mirwani", "Mithani", "Moula", 
    "Mubarak", "Mubasher", "Mudassir", "Mufti", "Murad", "Murtaza", 
    "Mushtaq", "Naik", "Naikzada", "Nasiruddin", "Nasirzai", "Nawabzada", 
    "Nazim", "Niaz", "Noorzai", "Panjwani", "Paracha", "Patel", "Qalandar", 
    "Qamruddin", "Qasimzada", "Qavi", "Rahmanzai", "Rasheedullah", 
    "Rehmani", "Rehmat", "Sadiqzada", "Sahibzada", "Sajjadi", "Samar", 
    "Samdani", "Sanghar", "Sanjrani", "Sarmad", "Sarsar", "Sayani", "Sayyed", 
    "Shahab", "Shamsi", "Sherani", "Shujauddin", "Siddique", "Sindhi", 
    "Subhani", "Tabibzada", "Tahirzai", "Tirmizi", "Turkzai", "Usmanzai", 
    "Wakilzada", "Warraich", "Yaqoobzai", "Zaidan", "Zamanzai", "Zebzai", 
    "Zubaydi", "Zulfiqarzai"

]



def generate_random_phone_number():
    random_number = str(random.randint(1000000, 9999999))
    third = random.randint(0, 4)
    forth = random.randint(1, 7)
    phone_formats = [
        f"03{third}{forth} {random_number}",
        f"03{third}{forth}{random_number}",
        f"+92 3{third}{forth} {random_number}",
        f"+923{third}{forth}{random_number}"
    ]
    return random.choice(phone_formats)
import random


def generate_user_details():
    fn = random.choice(pakistani_firstnam)
    ln = random.choice(pakistani_lastnam)
    year = random.randint(1960, 2006)
    date = random.randint(1, 28)
    month = random.randint(1, 12)
    formatted_date = f"{date:02d}-{month:02d}-{year:04d}"
    password = generate_random_password()
    phone_number = generate_random_phone_number()
    return fn, ln, date,year,month, phone_number, password

def generate_random_password():
    length = random.randint(10, 16)
    all_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
import random
from datetime import datetime

def generate_old_android_ua():
    # Seed random with current time for variation
    random.seed(datetime.now().timestamp())
    
    # Components
    android_versions = [
        ("4.0.3", "2011"),
        ("4.0.4", "2012"),
        ("4.1.1", "JRO03"),
        ("4.1.2", "JZO54"),
        ("4.2.1", "JOP40"),
        ("4.2.2", "JDQ39"),
        ("4.3", "JSS15"),
        ("4.4.2", "KOT49"),
        ("4.4.3", "KTU84"),
        ("4.4.4", "KTU84Q")
    ]
    
    devices = [
        ("Galaxy Nexus", "Samsung"),
        ("Nexus S", "Samsung"),
        ("Xperia Z", "Sony"),
        ("Xperia SP", "Sony"),
        ("One M7", "HTC"),
        ("One M8", "HTC"),
        ("Optimus G", "LG"),
        ("G2", "LG"),
        ("Moto X", "Motorola"),
        ("DROID RAZR", "Motorola")
    ]

 
    android_ver, android_code = random.choice(android_versions)
    device, manufacturer = random.choice(devices)
    
    # Build number generation
    build_number = f"{android_code}"
    if android_ver.startswith("4.0"):
        build_number += f".{random.choice(['IMM76', 'GRK39', 'IMM76D'])}"
    else:
        build_number += random.choice(["D", "E", "F"]) + str(random.randint(10,99))
    
    # Chrome version correlation
    chrome_major = random.randint(
        18 if android_ver.startswith("4.0") else 25,
        35 if android_ver.startswith("4.4") else 32
    )
    chrome_build = random.randint(1000, 1999)
    chrome_patch = random.randint(50, 199)
    
    # WebKit version logic
    webkit_base = "534.30" if chrome_major < 25 else "537.36"
    webkit_ver = f"{webkit_base}.{random.randint(1, 99)}" if random.random() > 0.7 else webkit_base
    
    return (
        f"Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build_number}) "
        f"AppleWebKit/{webkit_ver} (KHTML, like Gecko) "
        f"Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Mobile Safari/{webkit_ver.split('.')[0]}.0"
    )

from selenium.common.exceptions import NoSuchElementException
def create_33mail(driver):

    ua = generate_old_android_ua()
    fn, ln, date, year, month, phone_number, password = generate_user_details()
    url = "https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk"

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "dpr": "1",
        "priority": "u=0, i",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": f"{ua}",
        "viewport-width": "720"
    }
    
    session = requests.Session()
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find("form")
    if form:
        action_url = requests.compat.urljoin(url, form["action"]) if form.has_attr("action") else url
        inputs = form.find_all("input")
        data = {
            "firstname": f"{fn}",
            "lastname": f"{ln}",
            "birthday_day": f"{date}",
            "birthday_month": f"{month}",
            "birthday_year": f"{year}",
            "reg_email__": f"{phone_number}",
            "sex": "2",
            "encpass": f"{password}",
            "submit": "Sign Up"
        }
        for inp in inputs:
            if inp.has_attr("name") and inp["name"] not in data:
                data[inp["name"]] = inp["value"] if inp.has_attr("value") else ""

        submit_response = session.post(action_url, headers=headers, data=data)
        if "c_user" in session.cookies:
            uid = session.cookies.get("c_user")
            
        else:
            print("UID not found")
            return
    else:
        print("No form found in the response.")
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    change_email_url = "https://m.facebook.com/changeemail/"
    email_response = session.get(change_email_url, headers=headers)
    soup = BeautifulSoup(email_response.text, "html.parser")
    form = soup.find("form")
    
    if form:
        action_url = requests.compat.urljoin(change_email_url, form["action"]) if form.has_attr("action") else change_email_url
        inputs = form.find_all("input")
        data = {}
        for inp in inputs:
            if inp.has_attr("name") and inp["name"] not in data:
                data[inp["name"]] = inp["value"] if inp.has_attr("value") else ""
        data["new"] = f"{username}@hadiaamir.33mail.com"
        data["submit"] = "Add"
        submit_response = session.post(action_url, headers=headers, data=data)
        driver.implicitly_wait(6)
        for i in range(15):
            if i==12:
                return
            try:
                driver.find_element(By.XPATH, '//a[@title="Inbox"]').click()
                code_text = driver.find_element(By.XPATH, '//span[contains(text(),"code")]')
                code_string = code_text.text
                clean_code = re.search(r'\d+', code_string).group()
                break 
            except:
                continue
        otp =clean_code
        driver.find_element(By.XPATH,'//input[@id="idSelectAll"]')
        driver.implicitly_wait(3)
        try:
            # Check if the message container exists
            MESSAGES = driver.find_element(By.XPATH, '//div[@class="item-container-wrapper relative"]')
            if MESSAGES:
                try:
                    # Check if the "Select All" checkbox exists and click it
                    select_all_checkbox = driver.find_element(By.XPATH, '//input[@id="idSelectAll"]')
                    select_all_checkbox.click()
                except NoSuchElementException:
                    print("Select All checkbox not found")
                time.sleep(3)
                try:
                    # Check if the button exists and click it
                    button = driver.find_element(By.XPATH, '//button[@data-testid="toolbar:movetotrash"]')
                    button.click()
                except NoSuchElementException:
                    print("Button not found")
        except NoSuchElementException:
            print("Message container not found")
        print(f"{uid}|{password}|{username}")
        email=f"{username}@hadiaamir.33mail.com"
        file_path = "/sdcard/otp.txt"
        if not os.path.exists(file_path):
            open(file_path, "w").close()

        
        credentials = f"{uid}|{password}|{otp}|{email}\n"

        # Append to the file
        with open(file_path, "a") as file:
            file.write(credentials)

    else:
        print("No email form found.")
    
    return



options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://account.proton.me/login")
driver.implicitly_wait(80)
username_field=driver.find_element(By.XPATH,'//input[@id="username"]')
username_field.click()
username_field.send_keys("shahzebpya@proton.me")
pasword_field=driver.find_element(By.XPATH,'//input[@id="password"]')
pasword_field.click()
pasword_field.send_keys("Malik@1234")
time.sleep(4)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(6)
driver.get("https://mail.proton.me/u/6/inbox")
driver.find_element(By.XPATH,'//input[@id="idSelectAll"]')
driver.implicitly_wait(7)
try:
    # Check if the message container exists
    MESSAGES = driver.find_element(By.XPATH, '//div[@class="item-container-wrapper relative"]')
    if MESSAGES:
        try:
            # Check if the "Select All" checkbox exists and click it
            select_all_checkbox = driver.find_element(By.XPATH, '//input[@id="idSelectAll"]')
            select_all_checkbox.click()
        except NoSuchElementException:
            print("Select All checkbox not found")
            time.sleep(3)
        try:
            # Check if the button exists and click it
            button = driver.find_element(By.XPATH, '//button[@data-testid="toolbar:movetotrash"]')
            button.click()
        except NoSuchElementException:
            print("Button not found")
except NoSuchElementException:
    print("Message container not found")

for i in range(1000):
    create_33mail(driver)
