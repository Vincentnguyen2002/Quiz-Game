DROP DATABASE IF EXISTS quiz;
CREATE DATABASE quiz;
USE quiz;

DROP TABLE IF EXISTS country;
CREATE TABLE country (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(20)
);

DROP TABLE IF EXISTS city;
CREATE TABLE city (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(20),
    country_id int(11),
	FOREIGN KEY (country_id) REFERENCES country (id) ON DELETE NO ACTION ON UPDATE CASCADE
);

DROP TABLE IF EXISTS player;
CREATE TABLE player (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(20) unique  -- turn name to unique
    );
    

DROP TABLE IF EXISTS quiz_question;
CREATE TABLE quiz_question (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    text varchar(255),
    location_id int(11),
	FOREIGN KEY (location_id) REFERENCES city (id) ON DELETE NO ACTION ON UPDATE CASCADE
    );   

DROP TABLE IF EXISTS quiz_question_option;
CREATE TABLE quiz_question_option (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    quiz_question_id int(11),
    text varchar(255),
    is_correct tinyint(1),
    FOREIGN KEY (quiz_question_id) REFERENCES quiz_question (id) ON DELETE NO ACTION ON UPDATE CASCADE
    ); 
    
DROP TABLE IF EXISTS quiz_session;
CREATE TABLE quiz_session (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_id int(11), 
    questions_answered int(11) DEFAULT 0,
    correct_counts int(11) DEFAULT 0,
	chances tinyint(4) default 3,
    is_open tinyint(1) default 1,
	FOREIGN KEY (player_id) REFERENCES player (id) ON DELETE NO ACTION ON UPDATE CASCADE
    ); 
    
DROP TABLE IF EXISTS current_quiz_session;
CREATE TABLE current_quiz_session (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	session_id int(11),
    player_id int(11),
    question_id int(11),
    question_option_id int(11),
    is_correct int(11),
	FOREIGN KEY (session_id) REFERENCES quiz_session (id) ON DELETE NO ACTION ON UPDATE CASCADE,
	FOREIGN KEY (player_id) REFERENCES player (id) ON DELETE NO ACTION ON UPDATE CASCADE,
	FOREIGN KEY (question_id) REFERENCES quiz_question (id) ON DELETE NO ACTION ON UPDATE CASCADE,
	FOREIGN KEY (question_option_id) REFERENCES quiz_question_option (id) ON DELETE NO ACTION ON UPDATE CASCADE
    ); 


 -- insert data into table
insert into country(name)
values  ("Saudi Arabia"), ("Pakistan"), ("Bangladesh"), ("India"), ("Iraq"), ("Finland");
select * from country;


insert into city(name,country_id)
value ("Dammam", 1), ("Lahore", 2), ("Dhaka", 3), ("Delhi", 4), ("Baghdad", 5),
	("Ghaziabad", 4), ("Patna", 4), ("Hapur", 4), ("Muzaffarnagar", 4), ("Peshawar", 2),("Helsinki",6);
select * from city;



insert into player(name)
value ("trung"), ("huy");
select * from player;



insert into quiz_question(text,location_id)
values 
("What is the primary source of water for Dammam?", 1),
("Which initiative has Dammam implemented to reduce air pollution?", 1),
("What organization in Dammam is responsible for waste management?", 1),
("Which park in Dammam is known for its eco-friendly features and sustainable design?", 1),
("How does Dammam promote recycling among its residents?", 1),

("Which river runs through Lahore, impacting its environmental conditions?", 2),
("What step has Lahore taken to address air pollution in recent years?", 2),
("Which environmental event is celebrated annually in Lahore to raise awareness?", 2),
("What is the status of Lahore in terms of plastic waste management?", 2),
("Which park in Lahore is known for its sustainable landscaping practices?", 2),

("How does Dhaka manage its water resources to promote cleanliness?", 3),
("Which initiative in Dhaka focuses on reducing noise pollution?", 3),
("What is the main challenge Dhaka faces in waste management?", 3),
("Which park in Dhaka is recognized for its efforts in biodiversity conservation?", 3),
("What steps has Dhaka taken to improve air quality?", 3),

("What measure has Delhi implemented to combat vehicular pollution?", 4),
("Which river flows through Delhi, affecting its environmental conditions?", 4),
("What is the primary cause of air pollution in Delhi during winter?", 4),
("Which green space in Delhi is actively involved in environmental conservation projects?", 4),
("How does Delhi promote waste segregation at the source?", 4),

("What steps has Muzaffarnagar taken to address water pollution?", 5),
("Which local initiative in Muzaffarnagar focuses on reducing single-use plastics?", 5),
("How does Muzaffarnagar promote green energy adoption?", 5),
("Which park in Muzaffarnagar is known for its eco-friendly facilities and recreational areas?", 5),
("What measures has Muzaffarnagar taken to improve public transportation for environmental sustainability?", 5),

("Which river flows through Baghdad, affecting its environmental conditions?", 6),
("How does Baghdad address water scarcity issues?", 6),
("Which initiative has Baghdad implemented to reduce air pollution?", 6),
("What is the primary challenge Baghdad faces in waste management?", 6),
("How does Baghdad promote environmental education and awareness?", 6),

("What steps has Ghaziabad taken to address air pollution?", 7),
("Which river flows near Ghaziabad, impacting its environmental conditions?", 7),
("What initiative has Ghaziabad launched to promote waste reduction?", 7),
("How does Ghaziabad involve the community in environmental conservation efforts?", 7),
("What measures has Ghaziabad taken to improve water quality?", 7),

("Which river flows through Patna, affecting its environmental conditions?", 8),
("What initiatives has Patna implemented to address water pollution?", 8),
("How does Patna promote green building practices?", 8),
("What challenges does Patna face in waste management?", 8),
("Which park in Patna is known for its sustainable landscaping practices?", 8),

("What initiatives has Hapur implemented to address air pollution?", 9),
("How does Hapur manage its water resources to promote cleanliness?", 9),
("What challenges does Hapur face in waste management?", 9),
("Which green space in Hapur is actively involved in environmental conservation projects?", 9),
("How does Hapur promote environmental education and awareness?", 9),

("What is the primary cause of air pollution in Peshawar?", 10),
("Which river runs through Peshawar, impacting its environmental conditions?", 10),
("What initiatives has Peshawar implemented to address water pollution?", 10),
("How does Peshawar promote green energy adoption?", 10),
("What is Peshawar doing to reduce plastic pollution?", 10),

("What are Finnish households encouraged to recycle?",11),
("Which of the following is a common eco-friendly cleaning practice in Finland?",11),
("How is hazardous waste typically disposed of in Finland?",11),
("Jokamiehenoikeus or Everyman Right  allows people who live in Finland to:",11),
("Finland has a national program called 'Siisti Biitsi', which focuses on keeping the beaches clean. What does 'Siisti Biitsi' mean in English?",11);

select * from quiz_question;




insert into quiz_question_option(text,quiz_question_id,is_correct)
values
("Desalination", 1, 1),
("River", 1, 0),
("Underground springs", 1, 0),
("Rainwater harvesting", 1, 0),

("Electric vehicle infrastructure", 2, 0),
("Ban on industrial activities", 2, 0),
("Tree plantation drives", 2, 1),
("Public transportation improvements", 2, 0),

("Dammam Environmental Agency", 3, 1),
("Green Initiative Council", 3, 0),
("Waste Management Authority", 3, 0),
("Clean City Corporation", 3, 0),

("Green Oasis Park", 4, 0),
("Eco Harmony Gardens", 4, 0),
("Sustainable City Park", 4, 0),
("Eco Oasis Gardens", 4, 1),

("Mandatory recycling bins in households", 5, 0),
("Cash incentives for recycling", 5, 0),
("Educational programs on recycling", 5, 0),
("All of the above", 5, 1),

("Ganges", 6, 0),
("Nile", 6, 0),
("Ravi", 6, 1),
("Danube", 6, 0),

("Planting more trees", 7, 0),
("Banning fireworks", 7, 0),
("Introducing electric public buses", 7, 1),
("Implementing carpooling initiatives", 7, 0),

("Clean Air Day", 8, 0),
("Earth Hour", 8, 0),
("Green Day Festival", 8, 0),
("Eco Awareness Week", 8, 1),

("Plastic ban in effect", 9, 0),
("High recycling rates", 9, 0),
("Plastic-free zones established", 9, 1),
("All of the above", 9, 0),

("Shalimar Gardens", 10, 0),
("Iqbal Park", 10, 0),
("Jallo Park", 10, 1),
("Model Town Park", 10, 0),

("Rainwater harvesting", 11, 0),
("River dredging projects", 11, 1),
("Water desalination", 11, 0),
("All of the above", 11, 0),

("Silent City Campaign", 12, 0),
("Noise-Free Dhaka Project", 12, 1),
("Quiet Streets Initiative", 12, 0),
("Hush Hush Dhaka", 12, 0),

("Lack of recycling facilities", 13, 0),
("High population density", 13, 1),
("Insufficient waste collection infrastructure", 13, 0),
("All of the above", 13, 0),

("National Botanical Garden", 14, 0),
("Ramna Park", 14, 0),
("Baldha Garden", 14, 1),
("Suhrawardy Udyan", 14, 0),

("Introduction of electric rickshaws", 15, 1),
("Strict emission standards for industries", 15, 0),
("Plantation drives", 15, 0),
("All of the above", 15, 0),

("Odd-even traffic rule", 16, 1),
("Increased parking fees", 16, 0),
("Carpooling lanes", 16, 0),
("All of the above", 16, 0),

("Yamuna", 17, 1),
("Ganges", 17, 0),
("Brahmaputra", 17, 0),
("Godavari", 17, 0),

("Industrial emissions", 18, 0),
("Crop burning", 18, 1),
("Vehicular emissions", 18, 0),
("Construction activities", 18, 0),

("India Gate Lawns", 19, 0),
("Lodhi Gardens", 19, 1),
("Nehru Park", 19, 0),
("Sanjay Van", 19, 0),

("Mandatory recycling bins", 20, 1),
("Awareness campaigns", 20, 0),
("Fines for non-compliance", 20, 0),
("All of the above", 20, 0),

("River cleaning projects", 21, 1),
("Sewage treatment plants", 21, 0),
("Community water conservation programs", 21, 0),
("All of the above", 21, 0),

("Plastic-Free Muzaffarnagar Campaign", 22, 1),
("Green Bag Movement", 22, 0),
("Say No to Plastic Drive", 22, 0),
("Eco-Friendly Muzaffarnagar Project", 22, 0),

("Solar panel subsidies", 23, 1),
("Wind energy incentives", 23, 0),
("Biogas projects", 23, 0),
("All of the above", 23, 0),

("Gandhi Park", 24, 0),
("City Greenery Gardens", 24, 0),
("Eco Oasis Park", 24, 1),
("Green Harmony Park", 24, 0),

("Introduction of electric buses", 25, 1),
("Improved cycling infrastructure", 25, 0),
("Carpooling initiatives", 25, 0),
("All of the above", 25, 0),

("Tigris", 26, 0),
("Euphrates", 26, 1),
("Jordan", 26, 0),
("Nile", 26, 0),

("Desalination plants", 27, 1),
("Water conservation campaigns", 27, 0),
("River restoration projects", 27, 0),
("All of the above", 27, 0),

("Tree plantation drives", 28, 1),
("Strict emission standards for industries", 28, 0),
("Ban on open burning", 28, 0),
("All of the above", 28, 0),

("Lack of recycling infrastructure", 29, 0),
("High population density", 29, 0),
("Insufficient waste collection services", 29, 1),
("All of the above", 29, 0),

("Green Schools Program", 30, 1),
("Environmental Awareness Week", 30, 0),
("Eco-friendly Curriculum Initiative", 30, 0),
("All of the above", 30, 0),

("Ban on fireworks", 31, 1),
("Plantation drives", 31, 0),
("Introduction of electric buses", 31, 0),
("All of the above", 31, 0),

("Yamuna", 32, 1),
("Ganges", 32, 0),
("Hindon", 32, 0),
("Betwa", 32, 0),

("Zero Waste City Project", 33, 1),
("Plastic-Free Ghaziabad Campaign", 33, 0),
("Waste-to-Energy Program", 33, 0),
("All of the above", 33, 0),

("Community clean-up events", 34, 1),
("Environmental workshops", 34, 0),
("Green citizen awards", 34, 0),
("All of the above", 34, 0),

("River cleaning projects", 35, 1),
("Sewage treatment plants", 35, 0),
("Rainwater harvesting programs", 35, 0),
("All of the above", 35, 0),

("Ganges", 36, 1),
("Yamuna", 36, 0),
("Brahmaputra", 36, 0),
("Godavari", 36, 0),

("River cleaning campaigns", 37, 1),
("Sewage treatment plants", 37, 0),
("Wetland restoration projects", 37, 0),
("All of the above", 37, 0),

("Solar panel subsidies", 38, 1),
("Wind energy incentives", 38, 0),
("Hydropower projects", 38, 0),
("All of the above", 38, 0),

("Plastic bag ban", 39, 1),
("Plastic recycling programs", 39, 0),
("Plastic-free zones", 39, 0),
("All of the above", 39, 0),

("Eco Park", 40, 1),
("Buddha Smriti Park", 40, 0),
("Sanjay Gandhi Biological Park", 40, 0),
("Rajdhani Vatika", 40, 0),

("Ban on open burning", 41, 1),
("Introduction of electric rickshaws", 41, 0),
("Plantation drives", 41, 0),
("All of the above", 41, 0),
 
("Rainwater harvesting", 42, 0), 
("River restoration projects", 42, 0), 
("Water desalination", 42, 0), 
("All of the above", 42, 0), 

("Lack of recycling facilities", 43, 0),
("High population density", 43, 0),
("Insufficient waste collection infrastructure", 43, 0),
("All of the above", 43, 0), 
 
("City Park", 44, 0), 
("Green Harmony Gardens", 44, 0), 
("Eco Oasis Park", 44, 0), 
("Hapur Botanical Garden", 44, 0), 

("School programs on environmental conservation", 45, 0), 
("Community workshops", 45, 0), 
("Eco-friendly events", 45, 0), 
("All of the above", 45, 0), 
 
("Industrial emissions", 46, 0), 
("Vehicular emissions", 46, 0), 
("Agricultural practices", 46, 0), 
("All of the above", 46, 0), 

("Ganges", 47, 0), 
("Kabul", 47, 0), 
("Jhelum", 47, 0), 
("Chenab", 47, 0), 
 
("River cleaning campaigns", 48, 0), 
("Sewage treatment plants", 48, 0), 
("Wetland restoration projects", 48, 0), 
("All of the above", 48, 0), 

("Solar panel subsidies", 49, 0), 
("Wind energy incentives", 49, 0), 
("Hydropower projects", 49, 0), 
("All of the above", 49, 0), 

("Plastic bag ban", 50, 0), 
("Plastic recycling programs", 50, 0), 
("Plastic-free zones", 50, 0), 
("All of the above", 50, 0), 
 
("Electronics and appliances",51,0), 
("Hazardous chemicals",51,0),
("Garden waste",51,0),
("Glass, paper, and certain plastics",51,1),

("Using harsh chemical cleaners",52,0), 
("Using single-use plastic cleaning tools ",52,0),
("Using environmentally friendly cleaning products",52,1),
("Disposing of cleaning waste in water bodies",52,0),

("It is thrown in regular household trash.",53,0),
("It is recycled along with regular waste.",53,0),
("It is taken to specialized collection points.",53,1),
("It is buried in backyard pits.",53,0),

("Drive off-road vehicles anywhere in the wilderness",54,0),
("Camp and pick berries and mushrooms on public and private lands",54,1),
("Dump household waste in nature reserves",54,0),
("Cut down trees in national parks for firewood",54,0),

("Beautiful Beaches",55,0),
("Clean Coast",55,1),
("Sunny Shores",55,0),
("Pristine Seashores",55,0);




insert into quiz_session(player_id)
value (1), (2);




insert into current_quiz_session ( session_id, player_id, question_id, question_option_id, is_correct)
value (1,1,1,1,0), (1,1,1,4,1);











    
    