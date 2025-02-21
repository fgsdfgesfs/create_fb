import os
import random
import re
import string
import time
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



def generate_user_agent():
    user_agent="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.81 Mobile Safari/537.36"
    return user_agent





def save_random_screenshot(driver, folder="/sdcard/atlogs/"):
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)

    # Generate a random filename (8-12 lowercase letters)
    random_filename = ''.join(random.choices(string.ascii_lowercase, k=random.randint(8, 12))) + ".png"

    # Full file path
    filepath = os.path.join(folder, random_filename)

    # Save the screenshot
    driver.save_screenshot(filepath)

    print(f"Screenshot saved as: {filepath}")
    return filepath  # Return filename for reference




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
    return fn, ln, formatted_date, phone_number, password

def generate_random_password():
    length = random.randint(10, 16)
    all_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
from selenium.webdriver.common.keys import Keys

def create_accounts():
    try:
        print("Setting up Chrome options...")
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        print("Added --no-sandbox argument")
        options.add_argument("--disable-dev-shm-usage")
        print("Added --disable-dev-shm-usage argument")
        options.add_argument("--headless=new")
        print("Added --headless=new argument")
        options.add_argument("--window-size=375,812")
        print("Set window size to mobile")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        print("Added experimental options")
        options.add_experimental_option("useAutomationExtension", False)
        
        print("Initializing WebDriver...")
        driver = webdriver.Chrome(options=options)
        print("WebDriver initialized successfully")
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.81 Mobile Safari/537.36"})
        print("User agent set to mobile")
        
        print("Generating user details...")
        firstname, lastname, dob, phone, password = generate_user_details()
        print(f"Generated: {firstname} {lastname}, DOB: {dob}, Phone: {phone}")
        
        print("Navigating to Facebook registration...")
        driver.get("https://m.facebook.com/reg/")
        
        print("Loaded Facebook registration page")
    except Exception as e:
        print(f"Initialization error: {str(e)}")
        if driver:
            print("Quitting driver due to initialization error")
            driver.quit()
        return
    
    try:
        print("Starting registration process...")
        driver.implicitly_wait(7)
        print("Clicking Get Started/Next...")
        driver.find_element(By.XPATH, '//*[@aria-label="Get Started" or @aria-label="Next"]').click()
        print("Clicked initial button")
        
        driver.implicitly_wait(30)
        print("Entering first name...")
        driver.find_element(By.XPATH, '//input[@aria-label="First name"]').send_keys(firstname)
        print("Entered first name")
        
        print("Entering last name...")
        driver.find_element(By.XPATH, '//input[@aria-label="Surname" or @aria-label="Last name"]').send_keys(lastname)
        print("Entered last name")
        
        time.sleep(random.uniform(1.5, 2.5))
        print("Clicking Next after name...")
        driver.find_element(By.XPATH, '//div[@aria-label="Next" and @role="button"]').click()
        print("Clicked Next after name")
        
        print("Handling date of birth...")
        input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="date"]')
        input_field.clear()
        input_field.send_keys(dob)
        print(f"Entered DOB: {dob}")
        
        time.sleep(random.uniform(1.5, 2.5))
        print("Clicking Next after DOB...")
        driver.find_element(By.XPATH, '//div[@aria-label="Next" and @role="button"]').click()
        print("Clicked Next after DOB")
        
        print("Selecting gender...")
        driver.find_element(By.XPATH, '//div[@aria-label="Female"]').click()
        print("Selected Female gender")
        
        time.sleep(random.uniform(1.5, 2.5))
        print("Clicking Next after gender...")
        driver.find_element(By.XPATH, '//div[@aria-label="Next" and @role="button"]').click()
        print("Clicked Next after gender")
        
        print("Entering phone number...")
        number = driver.find_element(By.XPATH, '//input[@aria-label="Mobile number"]')
        number.click()
        time.sleep(random.uniform(0.5, 2.5))
        number.send_keys(phone)
        print(f"Entered phone: {phone}")
        
        print("Clicking Next after phone...")
        driver.find_element(By.XPATH, '//div[@aria-label="Next" and @role="button"]').click()
        print("Clicked Next after phone")
        
        time.sleep(random.uniform(0.5, 3.5))
        driver.implicitly_wait(6)
        try:
            print("Checking for continue button...")
            sad = driver.find_element(By.XPATH, '//span[contains(text(),"Continue creating account")]')
            time.sleep(random.uniform(0.5, 3.5))
            sad.click()
            print("Clicked continue button")
        except Exception as e:
            print(f"No continue button found: {str(e)}")
        
        print("Entering password...")
        driver.find_element(By.XPATH, '//input[@aria-label="Password"]').send_keys(password)
        print("Entered password")
        
        time.sleep(random.uniform(2, 5))
        print("Clicking final Next...")
        driver.find_element(By.XPATH, '//div[@aria-label="Next" and @role="button"]').click()
        print("Clicked final Next")
        
        try:
            print("Looking for Save button...")
            driver.find_element(By.XPATH, '//div[@aria-label="Save"]').click()
            print("Clicked Save button")
        except Exception as e:
            print(f"No Save button: {str(e)}")
        
        try:
            print("Looking for I Agree button...")
            driver.find_element(By.XPATH, '//div[@aria-label="I agree"]').click()
            print("Clicked I Agree")
        except Exception as e:
            print(f"No I Agree button: {str(e)}")
        
        print("Waiting for account creation...")
        time.sleep(20)
        driver.refresh()
        print("Refreshed page")
        
        if "checkpoint" in driver.current_url:
            print("Checkpoint detected! Aborting...")
            driver.quit()
            return
        
        print("Checking cookies for UID...")
        uid = None
        cookies = driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'c_user':
                uid = cookie['value']
                break
        if uid is None:
            print("No UID found! Saving screenshot...")
            save_random_screenshot(driver=driver)
            driver.quit()
            return
        print(f"Found UID: {uid}")
        
        print("Navigating to email change page...")
        driver.get("https://m.facebook.com/changeemail/")  
        print(f"Current URL: {driver.current_url}")
        
        if "checkpoint" in driver.current_url:
            print("Checkpoint during email change! Aborting...")
            save_random_screenshot(driver=driver)
            driver.quit()
            return
        file_path = "/sdcard/novery_accounts.txt"
        if not os.path.exists(file_path):
            open(file_path, "w").close()
            print(" Created new accounts file")  # Added

        credentials = f"{uid}|{password}\n"
        with open(file_path, "a") as file:
            file.write(credentials)
        print(f" Saved credentials: {uid[:4]}***")  # Added partial UID
        
        print(f" Success! Account created: {uid}|{proton_main}")  # Added
        driver.quit()
        return
        
    except :
        print(" Critical error occurred")  # Added
        if driver:
            print(" Saving screenshot and cleaning up")  # Added
            save_random_screenshot(driver=driver)
for i in range(1000):
    create_accounts()
