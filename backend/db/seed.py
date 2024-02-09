from db.main import Database

candidates = [
    {
        "user_id": "1234567890",
        "username": "john_doe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "address": "123 Main Street, Cityville, State, Country",
        "nationalID": "123-45-6789",
        "party_name": "Progressive Alliance",
        "manifesto_summary": "Prioritizing education and healthcare, fostering innovation, and promoting equality.",
        "manifesto": """
    As a candidate representing the Progressive Alliance, I am dedicated to creating a brighter future for our community.
    
    Education is the cornerstone of progress. I will work tirelessly to ensure that every child has access to quality education, regardless of their background. By investing in our schools and teachers, we can empower the next generation to thrive in an ever-changing world.
    
    Healthcare is a fundamental human right. No one should have to choose between putting food on the table and receiving medical care. I will advocate for affordable and accessible healthcare for all, working towards a system that prioritizes the well-being of every individual.
    
    Innovation drives economic growth and prosperity. I will support policies that encourage entrepreneurship and technological advancement, creating new opportunities for businesses and workers alike. By fostering a culture of innovation, we can secure a brighter future for generations to come.
    
    Equality is not negotiable. I will fight against discrimination in all its forms, whether based on race, gender, sexual orientation, or socioeconomic status. By championing diversity and inclusion, we can build a more just and equitable society for everyone.
    
    Together, we can build a future that works for all of us. Vote for progress. Vote for the Progressive Alliance.
    """,
    },
    {
        "user_id": "0987654321",
        "username": "jane_smith",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "address": "456 Oak Avenue, Townsville, State, Country",
        "nationalID": "987-65-4321",
        "party_name": "Unity Party",
        "manifesto_summary": "Building stronger communities through investment in infrastructure and social programs.",
        "manifesto": """
    As a proud member of the Unity Party, I am committed to building a brighter future for our community.
    
    Strong communities are built on solid foundations. I will prioritize investment in infrastructure, including roads, bridges, and public transportation, to ensure that our towns and cities are connected and accessible to all.
    
    Social programs play a vital role in supporting those in need and fostering a sense of belonging. I will work to expand access to affordable housing, healthcare, and childcare, providing a safety net for families facing hardship.
    
    Economic prosperity depends on a skilled and educated workforce. I will advocate for increased funding for education and job training programs, equipping individuals with the tools they need to succeed in today's competitive job market.
    
    Environmental sustainability is essential for the health and well-being of future generations. I will promote renewable energy initiatives and conservation efforts, safeguarding our natural resources for years to come.
    
    Together, we can build a community that works for everyone. Vote for unity. Vote for the Unity Party.
    """,
    },
    {
        "user_id": "2468101214",
        "username": "sam_jackson",
        "first_name": "Sam",
        "last_name": "Jackson",
        "email": "sam.jackson@example.com",
        "address": "789 Pine Street, Villagetown, State, Country",
        "nationalID": "246-81-01214",
        "party_name": "Liberty Coalition",
        "manifesto_summary": "Protecting civil liberties, promoting economic freedom, and ensuring government accountability.",
        "manifesto": """
    As a candidate for the Liberty Coalition, I am dedicated to defending the principles of freedom and justice that are the foundation of our democracy.
    
    Civil liberties are the cornerstone of a free society. I will oppose any attempts to infringe upon our constitutional rights, including freedom of speech, religion, and assembly. I will fight against government surveillance and censorship, ensuring that every individual can express themselves without fear of reprisal.
    
    Economic freedom is essential for prosperity and opportunity. I will advocate for lower taxes, reduced regulation, and free-market policies that empower entrepreneurs and small businesses. By fostering a climate of innovation and competition, we can unleash the full potential of our economy.
    
    Government accountability is non-negotiable. I will work to root out corruption and waste, holding elected officials to the highest standards of transparency and integrity. I will champion reforms that increase government efficiency and ensure that taxpayer dollars are spent wisely.
    
    Our liberties are under attack, but together, we can defend them. Vote for liberty. Vote for the Liberty Coalition.
    """,
    },
    {
        "user_id": "1357924680",
        "username": "sarah_miller",
        "first_name": "Sarah",
        "last_name": "Miller",
        "email": "sarah.miller@example.com",
        "address": "321 Elm Street, Hamletville, State, Country",
        "nationalID": "135-79-24680",
        "party_name": "Green Alliance",
        "manifesto_summary": "Advocating for environmental protection, sustainable development, and social justice.",
        "manifesto": """
    As a candidate representing the Green Alliance, I am committed to building a more sustainable and equitable future for all.
    
    Environmental protection is paramount. I will push for policies that combat climate change, preserve natural habitats, and promote renewable energy sources. By investing in clean technologies and conservation efforts, we can mitigate the impacts of climate change and safeguard our planet for future generations.
    
    Sustainable development is key to long-term prosperity. I will support initiatives that balance economic growth with environmental stewardship, ensuring that our communities thrive without sacrificing the health of our ecosystems. By prioritizing green infrastructure and smart urban planning, we can create cities that are both livable and sustainable.
    
    Social justice is at the heart of our movement. I will advocate for policies that address systemic inequalities, including access to healthcare, education, and affordable housing. By lifting up marginalized communities and amplifying their voices, we can build a more just and inclusive society for all.
    
    Together, we can create a world that works for people and the planet. Vote green. Vote for the Green Alliance.
    """,
    },
    {
        "user_id": "9876543210",
        "username": "alex_wong",
        "first_name": "Alex",
        "last_name": "Wong",
        "email": "alex.wong@example.com",
        "address": "567 Maple Avenue, Suburbia, State, Country",
        "nationalID": "987-65-43210",
        "party_name": "Progressive Front",
        "manifesto_summary": "Championing social justice, economic equality, and healthcare reform.",
        "manifesto": """
    As a candidate for the Progressive Front, I am committed to creating a fairer and more equitable society for all.
    
    Social justice is our guiding principle. I will fight against discrimination and inequality in all its forms, working to dismantle systemic barriers that hold marginalized communities back. By centering the voices of those most affected by injustice, we can build a more inclusive and compassionate society.
    
    Economic equality is essential for a thriving society. I will advocate for policies that redistribute wealth and opportunity, including higher taxes on the wealthy, a living wage for all workers, and robust social safety nets. By closing the wealth gap and ensuring that everyone has access to the resources they need to succeed, we can create a more prosperous future for everyone.
    
    Healthcare is a fundamental human right. I will push for comprehensive healthcare reform that guarantees universal coverage and lowers prescription drug costs. By prioritizing preventive care and investing in community health centers, we can improve health outcomes for all Americans and reduce disparities in access to care.
    
    Together, we can build a future that works for everyone, not just the privileged few. Vote for progress. Vote for the Progressive Front.
    """,
    },
    {
        "user_id": "2468013579",
        "username": "mike_thompson",
        "first_name": "Mike",
        "last_name": "Thompson",
        "email": "mike.thompson@example.com",
        "address": "789 Oak Street, Smalltown, State, Country",
        "nationalID": "246-80-13579",
        "party_name": "Conservative Coalition",
        "manifesto_summary": "Upholding traditional values, promoting fiscal responsibility, and strengthening national security.",
        "manifesto": """
    As a candidate for the Conservative Coalition, I am dedicated to preserving the values that have made our country great.
    
    Traditional values are the bedrock of our society. I will defend the sanctity of life, traditional marriage, and religious freedom against the encroachment of secularism and moral relativism. By promoting family values and personal responsibility, we can strengthen the fabric of our communities and instill a sense of purpose and belonging in our citizens.
    
    Fiscal responsibility is essential for long-term prosperity. I will advocate for smaller government, lower taxes, and reduced spending to reign in government waste and ensure that taxpayers' dollars are spent wisely. By balancing the budget and reducing the national debt, we can create a more stable and prosperous economy for future generations.
    
    National security is our top priority. I will support a strong military and robust border security measures to protect our nation from external threats. I will also stand up to globalism and defend American sovereignty against international organizations and agreements that seek to undermine our independence and sovereignty.
    
    Together, we can uphold the principles that have made America the greatest nation on earth. Vote conservative. Vote for the Conservative Coalition.
    """,
    },
]


if __name__ == "__main__":
    db = Database()
    for candidate in candidates:
        db.collection('candidates').add(candidate)
    print("Candidates added successfully!")