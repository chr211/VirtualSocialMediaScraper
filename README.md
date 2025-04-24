**Data Collection and Processing with Python to **

**Improve Open Source Intelligence**

Christopher O’Brien

College of Applied Science, University of Arizona

Cybv 498: Senior Capstone

Professor Jordan VanHoy

November 14, 2020

# Table of Contents

# List of Figures

# Abstract

This paper explores the application of Python for both the collection and processing of open-source intelligence. I focuses mainly on data that can be collected from social media web sites like Facebook and Twitter. Data processing includes natural language processing and multiprocessing applied to the scraped open-source data. A practical hands-on project using Python called Cyberapolis Scraper was created within the Cyberapolis environment. This is a proof of concept application to show the basic process of constructing an open-source intelligence collection and processing tool in a virtual environment. The basic functionality of the tool is shown in the accompanying video. Additionally, the basic theory of each concept involved in creating this type of tool is detailed. This includes defining open-source intelligence, the utility of Python, web scraping libraries in Python, and natural language processing.

# Data Collection and Processing with Python to Improve Open Source Intelligence

The International Data Corporation predicts that summation of all digitally created content will triple from 45 Zettabytes in 2019 to 175 Zettabytes in 2025 (Reinsel et. al.,2018). The volume and complexity of this information has the potential to become overwhelming. Open source intelligence relies on the collection and processing of a significantly large subset of this entire dataset. The large volume and diversity of data may hold patterns and evidence which are inaccessible using manual methods of collection and processing. The increase in size and complexity of data sets necessitates automated methods of collection and processing to create intelligence products derived from open source data. The Python programming language provides several easy and efficient ways to automate the collection and processing of open source data using natural language processing. Python also provides the ability to process data in parallel, which can greatly reduce data processing times. Natural language processing and multiprocessing implemented with Python have the potential to greatly increase the speed of data analysis and discover patterns and anomalous behavior in open source intelligence.

There is a need for customized collection and aggregation of open source data that is not readily available with conventional tools. This lack of control and customization may create functional and financial roadblocks to productivity and efficiency. It may become necessary to develop a new solution using one of several programming languages. Many languages can be difficult to master and subsequently have long development times. The Python programming language stands apart from the others in breadth of libraries and relatively easy implementation and portability. A tool called the Cyberapolis Scraper has been created for this report to illustrate how NLP can be applied to data scraped from open sources in a closed virtual environment. This will show how natural language processing with Python is an ideal choice for open-source intelligence analysis.

# Open Source Intelligence

One definition of intelligence is “information that has been refined and analyzed to make it actionable” (Brown et. al., 2017). The datasets that make up this information can be both public and private. The realm of public data collection, refinement, and analysis is referred to as open source intelligence. “Open source intelligence is an intelligence-gathering discipline that involves the collection, analysis, and interpretation of information from publicly available sources to produce “usable” intelligence” (Moore, 2010). The sources range from local and international news to social media and social networks; Facebook, Twitter, and blogs are great examples.

“There are four categories of open source information and intelligence” which include open source data (OSD), information (OSINF), intelligence (OSINT), and validated open-source intelligence. OSD is data that comes directly from the source of origin which may include original images and audio recordings and associated metadata (Hassan, 2018). OSINF is data that has been filtered or processed by a secondary entity so it is no longer in its original complete state. OSINT is data that has been processed in relation to specific requirements (Hassan, 2018). This could include searching for key names or places and the application of tools like NLP to extract patterns. Validated OSINT is intelligence that who authenticity has been verified with a high degree of certainty (Hassan, 2018). This is necessary as misinformation is commonplace in open source data platforms such as social media.

# Why Python is the Ideal Choice for Data Processing and Collection

Justification for the use of Python is needed in order to understand its usefulness for cybersecurity applications like web scraping of OSINT and data analysis  using NLP. Python scripts create a bridge between data and tools by utilizing high level code within libraries to create new ways of interaction with tools and frameworks. This high-level code makes programming easier by abstracting ideas rather than getting lost in tedious language specific syntax and details. This is ideal for the security practitioner who does not want to waste time in implementation details.

Python is most productive when using an objected-oriented paradigm, but it may also be used to implement a procedural paradigm. When used with an object-oriented paradigm, programs may be neatly divided into classes with behaviors that are intuitive to even non-programmers. These strengths of Python will likely lead programmers to spend less time debugging memory and syntax errors compared with more powerful languages like C.

There are drawbacks to this convenience; the dynamic typing of variables slows down execution considerably compared with compiled languages(Giesbrecht, 2015). This might pose a problem if a more comprehensive program is required and speed begins to become an issue. However, this does not detract from the simplicity and effectiveness of Python; scripts can be developed in far less time than their equivalent implementations in languages like C. Dynamic typing removes the need for explicit declarations of variable types and initialization, which saves space and time. Furthermore, list and dictionary data structures are built into the languages and ready to be applied without the need for extra design time. It is the significantly shorter development and maintenance time that makes Python appealing for use in time sensitive security applications.

Another convenience of Python is that is an interpreted scripting language. As long as the target computer where the script will run has a Python interpreter, it should be able to utilize the python libraries to successfully interact with the system. This means the script is not directly interacting with the hardware, but instead, is sending messages through libraries to make system calls. This is a weakness compared with languages like C which can directly access memory and hardware with quickness and ease. The Python Ctypes library can help create a bridge for memory access, but it is not ideal when compared with C or assembly. Despite this weakness, the broad system interoperability makes it appealing since it does not need to be compiled or extensively configured for each unique system architecture. This enables the programmer to make changes without worrying about the underlying architecture (Miller, Bryce, 2016). This also makes it portable across several platforms, enabling easy implementation in a variety of environments (O’Conner, 2012).

There is a “widening gap between technology developers and investigators” (Hosmer, 2015). Investigators are not necessarily technologically proficient and that is where Python is useful. It abstracts complex ideas in order to enable the creation of intuitive solutions that can be implemented by a wider population. A cyber security practitioner with knowledge of Python can help reduce organizational expenditures on tools that cover wide varieties of hardware and situations (Hosmer, 2015). In this way, Python can be used to lessen the dependence on tools and contextualize data in a wider variety of ways to make it useful.

Python’s standard and third-party libraries provide the ability to perform most, if not all, tasks required of any field within cybersecurity. There is a wide variety of choices for each third-party library type which creates more opportunities for customization. The choice of library also depends on how granular the programmer wants to be when manipulating data. This is the case across all types of libraries from networking to data manipulation and depends on the context of the program.

The power of these libraries comes from their ability to create automated solutions using Python that can be easily adapted to any situation. For example, a penetration tester who knows Python can quickly customize and adapt their tools to a client’s environment, while one who does not might have to seek new tools or advice which wastes time and money. A forensic examiner may sometimes work with unique hardware or environments that do not work well with standard tools. In time sensitive cases, an examiner who know Python can create a solution that retrieves the necessary data. Unique cases might have to be outsourced or might never be solved if the examiner does not have these Python skills.

# Data collection with Python

There is no shortage of publicly available data on websites. Twitter alone had more than 500 million tweets per day in 2013 from its base of several hundred million users (Twitter, 2013).  Automated tools like theHarvester are able to collect targeted information Twitter, Linkedin, and more (KaliTools, n.d). Tools like these are not always ideal in all situations and Python can be used to create a custom solution to collect and analyze data.

There are various sources of public data available for intelligence ranging from social media to domain tools and metadata. There are many scripts which scrape, or selectively extract data, using relatively passive methods. Additionally, there are those are more active like Enumall which use brute force to create wordlists and check them against domains to discover previously unknown subdomains (Troia, 2020). Selection and creation of active vs passive tools depends on the level of desired anonymity and digital footprint created (Hassan, 2017). When creating and using Python scripts to collect data, care must be taken not to disrupt the target service. Many web applications provide API to interact with the data. Often, the API contains call and rate limits to prevent both accidental and intentional denial of service and other issues. In some cases, the creation or use of a tool may not use an API, therefore, special care must be taken so as not to disrupt service or break terms of service.

Aside from APIs, many Python libraries exist to accommodate the creation of custom scripts to gather open source data for intelligence. Many Python libraries exist to accommodate the collection of data from web pages. The Urllib3 and Requests provide the ability of basic http protocol exchange. This includes web resource retrieval and posting of data, like login information for example. With the ability to send and retrieve data, a method of parsing and organizing the data is needed as a supplement. Third party Python libraries like Beautifulsoup and Scrapy can be used for locating and scraping web data.  Beautifulsoup is used with the Lxml parser to provide the ability to harvest the html content from a web page and create a searchable object. Finally, there is sometimes a need for ability to interact with a web page using clicks and mouse movements. There are several libraries that provide this functionality. Selenium is a popular choice since it provides both the ability to send mouse events in addition to providing scraping ability similar to Beautifulsoup.

# Web Scraping for OSINT

A large amount of OSINT resides on public web pages. Legal considerations for each website must be reviewed before considering collecting data. These terms of access are commonly found in a web site’s terms of service and privacy policy. Some websites might disallow scraping unless permission is formally granted, in which case access might be limited. Many sites provide application programming interfaces (API) in order to control how developments interaction with data. It is possible to avoid using the API when creating a program which collects data, but it is necessary to research whether or not this violates the terms of service. Additionally, in some cases non-public data is not properly protected may be collected (Hassan, 2018). Ultimately, there are two important considerations related to scraping data: ownership of content and possible denial of service (Heydt, 2018).

Denial of service is a potential issue when the requests become so frequent that they deny the ability for other users by taking up too many resources (and run up costs) or crashing the site completely (Heydt, 2018). Ownership of and use of data may be less intuitive. Reckless damage from scraping may potentially violate the Computer Fraud and Abuse Act (CFAA). Trespass to Chattels may apply if a scraper has caused loss of value to target party (Baesens, 2018). The Digital Millennium Copyright Act (DMCA) might be an issue if the intended use of the scraped data does not fall under the fair use provisions (Heydt, 2018). Finally, there may be laws that apply within a country or region like the General Data Protection Regulation (GDPR). The GDPR protects the personally identifiable information of the citizens of European Union member countries (Nadeau, 2020).

The collection of data from web sites is referred to as web scraping. While websites share common design features, they can be highly dynamic and unique in some cases and it is necessary to create a customized tool for each particular case. Python scripting provides the ability to help in both specialized and commonly seen cases to create an automated solution which solves lower level data processing issues. This reduces time spent manipulating the data in order for the user to perform higher level duties more pertinent to the overall task. Once the data is scraped and parsed, it needs to be processed. The intended use may require customization. Python provides several ways for the security practitioner to implement these custom solutions.

Time sensitive digital forensics applications commonly require a thorough examination of artifacts within evidence. For example, files can be scraped from a web site and hashed and exchangeable image file format (EXIF) data can be analyzed. Python provides an investigator several ways to create custom automated tools relevant to each case rather than having to purchase or learn a new tool. Penetration testers often need to perform several scans in parallel and in succession. This might involve scraping an organization’s public and private websites to gather intelligence. Without the ability to customize this automation for each client, the auditor is entirely dependent on the limited functionality of each tool. Further, the ability to understand and create custom scripts shields the investigator from potential unwanted and malicious behavior of third-party scripts.

Since web scraping has the potential to gather real-time data, it provides an opportunity for analysis of current events. This data can be used to develop open source intelligence products for various purposes. Predictive analytical methods like machine learning can be applied to the data to help make decisions for the future based on current data. Machine learning uses artificial intelligence techniques to recognize patterns in data (Swamynathan, 2017). Machine learning techniques can be applied to the web scraped data to classify and categorize it so it can be easily organized for later use.

## An Example of Web Scraping with Cyberapolis Scraper.

These libraries can be used to collect open source information on social media sites like Facebook and Twitter. They can also be used during penetration testing to collect information from an organization’s internal web sites. Below are two examples used to log into the Socialpark Facebook clone site within the Cyberapolis virtual environment. One uses the Selenium library, the other uses requests. It is important to note that this example is for academic purposes to show how the Selenium library can be used to automate login and scraping of a website which has granted permission to do so.

**Figure ****1** Social Park HTML login tags

![Figure 1](img_docx/image_8.png)

First, the html tags for the login boxes need to be found so that they can be used as targets for automated login. This is done by inspecting each element in a browser’s developer tab. (See figure 1.) When submitting the form it is necessary to analyze the network window in the developers tab to see how the data is submitted. In the case of Socialpark, there is an additional piece of data called __requestVerificationToken that needs to be scraped and submitted on login. (See figure 2.)

**Figure ****2**** **Socialpark login token.

![Figure 2](img_docx/image_6.png)

The code in figure 3 below opens a session to Socialpark and uses the BeautifulSoup library to parse out the session cookie and then login. Next, it searches for a post with a direct website address rather than using the search box. Above the value “cyberapolis%20power” is the search term, but this may be replaced with a variable. Finally, Beautifulsoup is used to extract a list of authors from the results by searching for div tags with class names of “author-name”. This method works will only work for one page of results as Socialpark requires the user to click a button to load more. A library like Selenium is required to create actions in order to automate button click to retrieve the complete result list. Selenium’s html parsing interface is similar to Beautifulsoup, but it requires a browser driver to automate actions.

**Figure ****3**** **Beautiful Soup login example.

![Figure 3](img_docx/image_5.png)

Seen below is an alternate login method for Socialpark which uses Selenium’s ‘send_keys’ and click methods to interact with the website in addition to supporting the execution of Javascript (See figure 4.) There is no need for the requests library and no need to keep track of login tokens as the driver manages this for the user.

**Figure ****4**** **Using Selenium to send login data.

![Figure 4](img_docx/image_3.png)

# OSINT Data Processing and Analysis with Python

## Natural Language Processing

The Natural Language Toolkit (NLTK) is one example of a machine learning library that can be applied to data gather from open sources. Natural language processing is a discipline which applies ideas from computer science and artificial intelligence to process natural human languages (Lane et. al., 2019). It uses statistical analysis via machine learning for a wide variety of applications from event and behavior prediction to broad sentiment analysis of various social media groups (Lane et. al., 2019).

Machine learning is a field within artificial intelligence which is comprised of self-improving algorithms that make decisions, predictions, and classifications (Polyakov, 2018). The algorithms accomplish this without human interaction by creating models based on training sets of data. The quality and amount of data is important because the behavior of these algorithms is entirely dependent on it. The significant increase in digital data creation expected in the near future enables machine learning tools like NLP to be applied in many circumstances to aid in organizational decision-making and for the swift creation of intelligence products.

An OSINT scraper tool can incorporate the NLTK on data gathered from data gathered from web sites to categorize and find patterns.  Social media profiles like Twitter, Facebook, and blogs are common targets to collect data for use with the NLTK. The Cyberapolis Scraper program will be designed to collect this information from Socialpark and Chirpyhub and apply the NLTK library to process data. This processed data may then be used for various purposes including correlating accounts, guessing passwords, or predictive behavior based on likes, friend lists, and post history. This may be especially useful in cyber security analysis scenarios when performing reconnaissance on a target and specifically within forensics to establish patterns of behavior and social networks. This may also be applied by social media companies for the “Automated detection of false information and fake social media accounts” (Marcellino et. al, 2020).

As previously mentioned, natural language processing (NLP) analyzes human languages by converting them into a format that can be processed statistically. All of the steps and stages included in this process are together referred to as a pipeline (Howard et. al. 2019).  The pipeline must be customized for the grammar and vocabularies of one of the thousands of human languages and dialects spoken today. The context and semantics of words and sentences is important to extract meaning. Once a language flows through an NLP pipeline, meanings can be extracted and categorized by sentiment. It has been shown that machines using NLP can even detect sarcasm more accurately than humans in certain cases (Howard et. al. 2019). This process can be automated in order to “quickly discover associations, transactions” between various “entity types” like people, places and dates within large amounts of data (Moore, 2010).

The extraction of information using NLP from a body of text, whether it be a tweet or a news article, is a multistep process. Before, “entity types” can be found and categorized the text needs to be tokenized into smaller structures that may take the form of single words, collocated words, or phrases (Noubours et. al., 2013). This action is easily performed using the NLTK string command ‘split’. This splits the corpus, or the entire collection of words and word sequences for a document, into a set of word tokens that can easily further reduced and filtered (Lane, 2019). For example, this can be useful for interpreting contractions as the same token as two separate words and ignoring capitalization.

The list of tokens can be reduced to a set without duplicates that forms a what is called a vocabulary (Lane, 2019). Normalization is the reduction of the vocabulary by grouping similar words and phrases (Lane, 2019). For example, both variant spellings and misspellings can be identified and grouped to optimize a vocabulary. Root word stems can also be analyzed in a vocabulary to group similar forms of the same word. This is called stemming, which is a part of the more general process called normalization. Many of these types of normalization can be performed with Python’s regular expression library to identify and extract or ignore custom pattern in text.

The tokens may be further tagged to identify parts of speech in order to process them according to class. The vocabulary may also be reduced to what are called n-grams, or sequences of ‘n’ number of words. This is useful for modifying words such as when “not” is used to negate a subsequent word (Lane, 2019). Similarly, “the semantic root of a word”, or lemma,  may be identified using Python’s Lemmatizer library (Lane, 2019). Unique groupings of words can also be identified in this way to identify ideas and locations like “United States.” Further, the syntactic analysis can be used to a more abstract analysis of the entire text sample in order to summarize and categorize it for further more general analysis like sentiment analysis or “trend diagnosis” (Noubours et. al, 2013). Sentiment analysis is used to identify the opinions of the author of the target text in relation to all of the identified entity types (Noubours et. al., 2013). One interesting NLTK library is the Valance Aware Dictionary for Sentiment Reasoning (VADER). VADER is a dictionary of words with associated scores for positive, negative, and neutral sentiment (Lane, 2019). The VADER library is applied to a corpus to parse the words in the vocabulary and calculate either an overall sentiment or phrase score. This could be applied to OSINT collected from sources like twitter to determine the sentiment statistics on a certain subject.

In addition to the text mining, sentiment categorization, and behavior prediction, NLP is used to generate coherent sentences both isolated and in response to input. These applications are commonly referred to as chatbots and robot journalists (Howard et.al., 2019). One further possible cyber security application of this beyond author attribution might be the generation of new conversations based on a past samples for deceptive purposes. During the 2016 United States presidential election there were accusations of Russian interference within social media. Fake accounts were created to emulate personas with both liberal and conservative ideologies for the purpose of creating “discord and division” and “spreading misinformation” (Marcellino et. al. , 2020). NLP techniques were used with data from posts of verified “Russian malign accounts” to identify and classify other Russian troll accounts (Marcellino et. al., 2020). NLP techniques can, therefore, be used for both the generation and detection of different categories of languages.

It is clear that this is a unique and potentially effective tool for use in cyber security within social media. Additional applications of NLP exist outside the realm of social media and also outside of natural languages. The identification of software vulnerabilities can be accomplished by training it with specific programming language code (Kanal, 2019). Malicious code hidden within thousands of lines of benign code can be detected using semantic networks that identify and categorize relationships between individual words (Wang et. al., 2017). Finally, malware commonly obfuscates domain names used for communications with command and control servers; the code commonly generates these domains algorithmically and eventually connects successfully. NLP tools and techniques can be applied to DNS queries to identify those domains which are likely to have been generated algorithmically (Koh, 2018). All of these methods are automated and improve efficiency and provide security through detection and prevention. NLP tools like the NLTK contain much more complex statistical capabilities which can be applied to OSINT and beyond.

## Multiprocessing of Data with Python

Many tasks within cybersecurity involve performing repetitive actions on a large amount of data. This can take the form of searching for a string within thousands of posts associated with millions of users. It can also manifest itself in web scraping with the processing of thousands of twitter accounts for certain data. Many programs execute linearly rather than parallel so that each step must be completed before the next can be executed. When the work required per file is high, the total processing time will increase proportional to the number of files. With this knowledge, a designer can identify cases where processing in parallel would lead to a significant decrease in processing time. In these cases, Python provides libraries that makes parallel processing easy to implement. In the case of web scraping, both the collection and analysis may be designed to process in parallel. However, extra care must be taken when processing network connections to avoid denial of service. Each library provides a unique approach utilizing methods from multithreading and multicore processing to distributed machines and cloud solutions

The choice between multithreading and multiprocessing depends on many factors including whether the data is dependent on shared resources. Many network applications of parallel programming are done with threads that use a concept called a semaphore to lock execution until it is safe to access a resource (O’Connor,2012). Multithreading is best used in cases where a thread of execution might have to wait for data and executing another thread in parallel is advantageous during this wait time. Multiprocessing differs from multithreading in that a new process with its own memory space is created for each processor and is truly executing in parallel rather than concurrently in a shared memory space as in multithreading. This is an important consideration in cases when data might need to be shared and accessed between tasks.

The multiprocessing library is easy to implement on a single machine for non-dependent repetitive tasks like file hashing or searching. The multiprocessing library also enables the user to create a finite number of processes before compile time and block the calling process until they are ready using the process and join methods. Below is an example of how the processing time of the author’s single threaded hash program was improved by using the Python multiprocessing for subsequent integration into the Cyberapolis Scraper program. Any files associated with a user have a unique hash that is calculated and can be compared to a database. The original implementation, seen in figure 5, walked a directory tree and stored every file in fileList. Each file in fileList was processed sequentially and the test case yielded a value of 211 seconds processing time for 4590 files.

**Figure ****5**** **Single Processing implementation.

![Figure 5](img_docx/image_2.png)

The original single-process program hashed 23Gb or 4590 files in 211 seconds (See Figure 6.)

**Figure ****6**** **Time taken for single process implementation.

![Figure 6](img_docx/image_1.png)

Next, multiprocessing capabilities were added to the function. First, a Pool object was created and initialized the number of parallel processes to 12; this is the number of logical cores in this particular processor which can be found using the function cpu_count (Hosmer, 2015). Func is set to a partial function whose arguments never change (root and dirList are passed in case relative directory search is used versus absolute in the future). Partial is necessary because map technically only takes one argument for a function and this works around that limitation. This function is passed to the map function with an iterable object that is passed to a new separate multiHash function for each file entry. The multiprocessor map function creates a new process for each core from an entry in the iterable fileList. All of the separate spawned process’ return values are returned in one list stored in hashEntryList (See Figure 7.)

**Figure ****7**** **Multiprocessing of a hash function.

![Figure 7](img_docx/image_7.png)

These changes above enable the hashes to be processes in parallel, reducing the time taken from 211 seconds to 66 seconds to process 23Gb (See Figure 8.)

**Figure ****8**** **Time taken to hash using multiprocessing.

![Figure 8](img_docx/image_4.png)

Note that there is an issue in the multiprocessing library when running in Windows that requires any function passed to map to be imported rather than within the calling module (Python, 2015).

There was a time reduction of nearly 70 percent when using the multiprocessing libraries. This time reduction becomes more noticeable as data loads increase. This multiprocessing improvement can be applied in many other areas of open source data gathering and processing. This is significant and can be critical in situations where malware signatures are being sought in memory or disk across several machines in order to contain an outbreak. This processing was compared with the off-the-shelf forensic toolset Autopsy which took an estimated 240 seconds to calculate hashes on the same data. Despite taking additional time to redesign, only a few new function calls need to be imported from the multiprocessing library to improve any tool’s efficiency. Multiprocessing using Python clearly provides an easy way to improve both gathering and processing and processing of data.

# Networking Libraries for Data Collection in Python.

Data collection across networks for cybersecurity applications involves choosing how to securely interact with several standard protocols. Network security deals with the transmission of this data between hosts and networking hardware. More generally, it involves policies and controls that support confidentiality, integrity, and accessibility. The way in which the data can be used can be divided into offensive and defense purposes and the corresponding “threats and countermeasures” (Pfleeger, 2015). The National Cyber Security Center describes penetration testing as "a method for gaining assurance in the security of an IT system by attempting to breach some or all of that system's security, using the same tools and techniques as an adversary might” (National Cyber Security Center, N.D.). Although there are physical and social aspects involved with both, a large portion relies on network data. Network security monitoring commonly consists of dealing with attacks by protecting, detecting, responding, and restoring (Sanders, Smith, 2013).

Basic networking connections and functionality is a prerequisite to any type of network application including web data scraping. There are several Python libraries for basic network functionality and the choice depends on the level of detail the programmer desires. For example, the Urllib libraries provide the ability to send simple http commands like GET and POST similar to the Linux tool curl. The requests library also provides this functionality but with less muddled interfaces and more efficient error handling. More general networking functions involving opening a transmission control protocol (TCP) socket to a specific port can be accomplished with the socket library. Additionally, if the designer is creating a penetration testing program to capture and manipulate IP packets between two hosts, a more powerful library like Scapy or Dpkt will be required to work alongside the socket library.

A common concept among all the libraries is that of a socket. “A socket is the interface between the application layer and the transport layer within a host” (Kurose, 2016). It allows the process to communicate with the network. The socket library contains basic high level methods necessary to create a transport layer protocol socket. A socket object will need to be created and initialized to the desired socket family type. The AF_INET family for IPv4 will be the most likely family for most security applications. There are other possibilities which include AF_INET6 (IPv6), AF_BLUETOOTH (Bluetooth), AF_VSOCK (virtual machine), and more. Next, SOCK_STREAM for TCP and SOCK_DGRAM for the UDP protocol are selected depending on application. These are the basic properties required for a socket object.

A socket object may either actively connect to destination address and port or passively listen on a local port. To connect to a foreign address, the connect method of the socket object is called and passed a tuple with the destination IP address and port. Now that there is a socket connection established, data encoded in bytes can be sent using the socket object’s send command. The data sent will depend on the what the target address expects – or does not expect in the case of exploitation. Data transmission is bidirectional across a socket. To retrieve data waiting in the socket object’s buffer, the socket object’s recv method is called with an argument that sets the number of bytes requested. It is necessary to use additional libraries like Crypto if encryption is required.

These are the basic tools required for transmitting data over a network using sockets. The requests and urllib3 libraries work in much the same way, but are more suited for application-layer http data. These tools can be used to test network applications by creating fuzzers and protocol analyzers by sending and analysis custom data (O’Connor, 2015).  For more complete protocol functionally, like SSH for example, Python libraries like Paramiko exist to provide basic functionality (Paramiko, n.d.). An example of multiprocessing seen in the next section can also be integrated into most network applications which would benefit from the parallel processing of separate sockets to increase speed.

# Conclusion

**	**It has been shown that Python’s standard networking libraries in combination with various third-party data processing libraries like Selenium can be used to create a program to easily scrape data from the web for open source intelligence. Web scraping with Python libraries is also implemented and customized with relative ease as shown in the Cyberapolis scraping program. Additionally, libraries like the natural language toolkit can be applied to the gathered data to process and filter the data to eliminate unusable information. Advanced natural language processing techniques implemented with Python were shown to be effective and easy to implement. This enables timely creation of intelligence packages that can be customized with ease using Python. Multiprocessing techniques were applied to both collection and processing stages was shown to significantly reduce processing time. Therefore, natural language processing and multiprocessing implemented with Python has the potential to greatly increase the speed of data analysis and discover patterns and anomalous behavior for open source intelligence.

# References

Baessens, Bart. Broucke, Seppe vanden. (2018). Practical Web Scraping for Data Science. Apress.

Brown, Rebekah. Roberts, Scott. (2017). Intelligence-driven Incident Response. O’Reilly Media.

Comparing Python to Other Languages. (n.d.).

Giesbrecht, Shelly. (2015). Coding for Incident Response: Solving the Language Dilemma. Sans Institute.

Goldstein, Julia. Ghoul, Mike. (2017). Identifying Fake News with NLP. NYC Data Science Academy.

Heydt, Michael. (2018). Python Web Scraping Cookbook. Packt Publishing

Kanal, Eliezer. (2019). Artificial Intelligence in Practice: Securing Your Code Using Natural Language Processing. Carnegie Mellon University Software Engineering Institute.

Koh, Joewie. Rhodes, Barton. (2018). Inline Detection of Domain Generation Algorithms with Context-Sensitive Word Embeddings.

Lane, Hobson. Howard, Cole. Hapke, Hannes. (2019). Natural Language Processing in Action. Understanding, Analyzing, and Generating Text With Python. Manning Publications.

Leaniz, Jean. (2015). Timline Analysis with Apache Spark and Python. Sans.

Marcellino, William. Cox, Kate. Galai, Katerina. Slapakova, Linda. JacyCocks, Amber. Harris, Ruth. (2020). Human-machine detection of online-based malign information.

Miller, Preston, and Chapin Bryce. (2016). Learning Python for forensics: learning the art of designing, developing, and deploying innovative forensic solutions through Python. Birmingham, UK: Packt Publishing Limited.

Moore, David. (2010). Critical Thinking and Intelligence Analysis. Books Express Publishing.

Nadeau, Michael. (2020). General Data Protection Regulation (GDPR): What you need to know to stay compliant.

National Cyber Security Centre (N.D.). Penetration Testing. Advice on how to get the most from penetration testing.

Noubours, Sandra. Pritzkau, Albert. Schade, Ulrich. (2013). NLP is an essential ingredient of effective OSINT frameworks.

O’Brien, Christopher (2020). Cyberapolis Scraper.

O’Connor, T.J. (2010). Grow Your Own Forensic Tools: A Taxonomy of Python Libraries Helpful for Forensic Analysis. Sans

O’Connor, T.J. (2012). Violent Python: A Cookbook for Hackers, Forensic Analysts, Penetration Testers, and Security Engineers. Syngress.

Paramiko (n.d.) Welcome to Paramiko’s Documentation

Pfleeger Charles. Pfleeger, Shari. (2015). Security in Computing. Prentice Hall Press.

Python Bug Tracker Issue25053. (2015).

Sanders, Chris. Smith, Jason. (2013). Applied Network Security Monitoring: Collection, Detection, and Analysis. Syngress Publishing.

Scarfone, Karen. Souppaya, Murugiah. Cody, Amanda. Orebaugh, Angela. (2008). SP 800-115: Technical Guide to Information Security Testing and Assessment.

Swamynathan, Manohar. (2017). Mastering Machine Learning With Python in Six Easy Steps: A Practical Implementation Guide to Predictive Data Analytics Using Python. Apress

The Harvester Package Description (n.d.).

Troia, Vinny. (2020). Hunting Cyber Criminals. Wiley.

Twitter. (2013). New Tweets per second record, and how!

Wang, Shanshan. Yan, Qiben. Chen, Zhenxiang. Yang, Bo. Zhao, Chuan. Conti, Mauro. (2017). Detecting Android Malware Leveraging Text Semantics of Network Flows.