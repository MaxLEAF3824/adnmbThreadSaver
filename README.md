# adnmbThreadSaver

[adnmbThreadSaver in a nutshell]:  
adnmb.com is an anonymous forum that is similar to 4chan and 2ch. Saving threads from this website could be very inconvenient.  
This is a simple python script, which saves threads from adnmb.com, it's based on selenium so you need to download selenium package and the corresponding webdriver for you web browser. This repo includes the source and a executable file.(But Runing the exe requires an extra webdriver fire, which is expected to download by yourself.)  
    
[Preparation]:  
The program supports three browsers: Chrome, Edge and Firefox. Before running the program, you need to download the corresponding webdriver file.  
webdriver for Chrome: https://sites.google.com/a/chromium.org/chromedriver/home  
webdriver for Microsoft Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  
webdriver for Firefox: https://github.com/mozilla/geckodriver  
The webdriver file can be put in either of the two following places:  
1. Put it in the same directory as the program  
2. Put it in any directory in Path  
  
[How to use it]:  
To save a thread from adnmb.com, the thread number is the only thing you need. An adnmb account is not necessary, But you are only able to save the first 90 pages(891 replies) of the webpage at most, if you are not logged in.  

[Features]:  
1. "PO only mode":Only save content from the publisher of the thread.  
2. Save the author and time info or not? It's up to you: You can choose whether to save the time and the publish info or not.  
3. Shortcut "user_pwd.txt": you need a "user_pwd.txt" which saves your adnmb email&password in two simple lines, put it in the same directory as the program, and you don't need to type your email and password everytime you log in with the program.  
