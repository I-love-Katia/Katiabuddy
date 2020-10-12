
"""
Created on Sun Dec  8 01:02:23 2019

@author: arkar// Katia you are my everything

"""

import textwrap

def katiaspirit(targetskill):
    skill=set([str(targetskill)])
    
    universityname=" Queensland University of Technology"
    levelofexperience=" entry level"
    degreeobtained="Bachelor degree of Engineering (Process Engineering) and a Master's degree of Engineering (Mechanical Engineering)"
    jobpositioninput=" Graduate Engineering Program"
    companyname=" Accenture"
    advertismentlocation="LinkedIn"
    jobinterested=""
    twothingsyoulikeaboutcompnay="powerful established global presence with community and technological leadership"
    firstcorevalueyoulike="the culture of respect"
    secondcorevalueyoulike="adherance to the best principle"
    twobestcorevaluesofcompanyyoulike=firstcorevalueyoulike+'and'+secondcorevalueyoulike
    
    datanalystjob=set(['data', 'data analytics','data engineer'])
    waterengineerjob=set(['water','water treatment','wastewater'])
    draftingjob=set(['cad','drafting','ansys', 'nastran','lockheedmartin'])
    drilleng=set([])
    qualityeng=set([])
    assetmangeng=set([])
    automationeng=set(['scada'])
    
    
    
    if skill.issubset(datanalystjob):
        summary_data_analyst= f"""
       I am writing this letter to apply for {jobpositioninput} with {companyname} which was advertised at {advertismentlocation}. I am currently graduated  from {universityname}  with a {Bachelor degree of Engineering (Process Engineering) and a Master's degree of Engineering (Mechanical Engineering)}. I have a strong interest in data science and data engineering field along with the expertise in mechanical and chemical engineering related areas.
I have strong motivation to work with {companyname} due to its {twothingsyoulikeaboutcompany}. Amongst the core values of the company, I highly value {the culture of respect and adherence to the best principles}. For instance, I have practiced best possible time and team management   has allowed me to have better achievement in my Master’s degree compare with my other educational levels.  In addition to this,  my roles during my previous internship made me develop engineering mindset, responsible workplace interactions, open-mindedness, teamwork and safety-oriented attitude which are essential for working in your company.  
Regarding with data engineering and data science experience, as a technical support assistant/research assistant in Queensland University of Technology, I have learnt how to put statistical analysis into professional practice. This includes formulating and predicting the equations of machine efficiency and output productivity using the high dimensional input data that I had collected from the industrial/commercial grade process machine while I was assisting in testing. 
Moreover, through data analytics and optimization subject of the Master’s of Engineering program, I developed my passion in using various machine learning algorithms with activity and image data to predict the correct classification output. In my free time, I love to write machine learning code with python libraries at home. For example, during this pandemic season, I have written a program with my own logic to design an automatic web download crawler, and parsing of pdf document data to perform sentiment analysis and clustering signature pattern collection of the writer. I am also the passionate reader of O’Reilly computing books and the enthusiast of deep learning models. I enjoy spending my holiday with online computer vision technology lectures delivered by Stanford University. I believe my personal hobbies will serve as great intangible assets of Accenture.
To support my application, I have attached a copy of my resume and academic transcripts. I believe that I have a high potential to be valuable candidate of the company and looking forward to the opportunity to discuss my application in more detail at an interview. Please do not hesitate to contact my email arkar.nyanhein@connect.qut.edu.au or my mobile number +(61) 0401839236 for further application processing.

                
"""        
        my_wrap = textwrap.TextWrapper(width = 100)
        wrap_list = my_wrap.wrap(text=summary_data_analyst)
        for line in wrap_list:
            print(line)
        
        print('\n' '\n Key Skills \n Unsupervised Machinelearning \n Python \n Matlab \n Clustering ' )
        print()
    
    elif skill.issubset(waterengineerjob):
        skill1="ANSYS modelling"
        object1="water flow"
        summary_water_engineer=f"""Summary: 
I am recently  graduated {levelofexperience} {degreeobtained} from {universityname} writing to express my interest and enthusiasm towards {jobpositioninput} in {companyname}.

\n As a entry level engineer, I am willing to work and adapt in the fast changing technologies in water industry with analytical and innovative mindset. 
I am also good at applying {skill1} on {object1} adhering to the current industrial practice along with knowledge in 
        
        
        """
        my_wrap = textwrap.TextWrapper(width = 100)
        wrap_list = my_wrap.wrap(text=summary_water_engineer)
        for water_line in wrap_list:
            print(water_line)
        print('Key Skills \n Pipe Sizing \n ANSYS \n Solid Work \n Wastewater Chemistry')
    
    elif skill.issubset(draftingjob):
        print('I believe I can draw')
        
    elif skill.issubset(draftingjob):
        pass 
    