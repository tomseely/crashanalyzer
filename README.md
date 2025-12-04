# Minecraft Crash Log Analyzer

- Project overview and purpose
    - This project is a website that acts as a Minecraft crash log analyzer using Google's AI, Gemini. It takes a file and gives the user output on what their issue is and how to solve it. Its purpose is to help Minecraft players quickly solve their game issues without having to dive in and understand the log files that may be complicated for inexperiences and young players. This can make resolving these types of issues more streamlined, especially as more context may be given to Gemini such that its solutions are more specific and accurate.

- Video link of your project
    - https://youtu.be/V3EKhOz56EY
- Installation and setup instructions
    - If the repository is public then the website can be accessed at https://tomseely.github.io/crashanalyzer/
    - However if it is private then the website can still be locally hosted on the machine with a Gemini API Key and cloning the repository
        - This can be done by changing the environment variable by doing the following command in the terminal: `export GENAI_API_KEY=your_key_here` or by adding it to `/crashanalyzer/.apikey.txt`
- How to run the program and reproduce results
    - If the website works then that can be accessed a file can be submitted to analyze.
    - Run `python3 crashanalyzer/tests/app.py` and open the local port in the browser to view the website.
        - Note that this .py is different from the one called normally when the site works since the index.html reads from the local port rather than the Render site
    - On the site provide a log or crash log and submit, and it will call the Gemini API with the given key and show the output of the error in your log and how to fix it.
- Technologies or libraries used
    - GitHub Pages
    - Render
    - Flask
    - Google Gemini
    - VSCode Copilot
- Author(s) and contribution summary
    - Thomas Seely - Author
