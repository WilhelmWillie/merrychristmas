# Merry Christmas

Christmas Coding Challenge: A self-made challenge where I code for 9 hours straight

Goal: To create a card-generation application that users can customize using user-provided photos and messages.

## Time Constraints:

* **12:00 PM - 1:30 PM** 
  Research + Planning Stage
* **1:30 PM - 9:30 PM** 
  Code Marathon
* **9:30 PM - 11:00 PM** 
  Release + Cleanup

## Log:
* **1:22 PM** About to begin a 9 hour journey of coding. I'm going to be using Django and MySQL in the backend. The biggest challenge for me will be the fact that I don't know Django very well. My end product will probably be messy and unsafe but this will be a good learning experience.
* **1:42 PM** MySQL database & table set up. Table is composed of 6 columns (id, slug, to, from, message, img). The 'id' column is used for indexing purposes. 'slug' is the unique identifier used to access the card through a URL (e.g. merrychristmas.wilhelmwillie.com/card/43838). The 'to', 'from', 'message', and 'img' columns are used for customizing the card. 'img' stores the image file name without the extension. My goal is for images to be stored in an /uploads/ directory all a .jpg extension.
* **1:57 PM** Figures.. I ran into an error loading the MySQLdb module for Django..
* **2:41 PM** Pretty significant delay.. MySQL is being iffy..
* **3:10 PM** I'm an idiot. We're back in business!
* **3:26 PM** Card model created yay! For clarification on the time restraints, I cannot push anymore new code after 9:30. However, from 9:30 - 11:00 PM, I'll allow myself to clean up existing code for release at merrychristmas.wilhelmwillie.comcard
* **3:41 PM** Updated Card model to include the slug.. For some reason I forgot to. In addition, I'm also working on getting the views and URL routing set up.
* **4:26 PM** Took a slight break. Back to the grind. Implementing a few templates.
* **4:53 PM** Starting to get a hang of Django. Still confused by it but I'll have it down soon.
* **5:24 PM** Dinner break. Made progress on the front-end.
* **6:42 PM** Progress made. Working on form validation and etc.
* **7:49 PM** Back-end almost done! I was planning to add facial recognition to the photo upload portion to be fancy. However, due to time restraints, I won't be adding it. Maybe later?
* **9:28 PM** Finished with the front end! I do have one more feature to add that I'll touch in the cleanup/release phase.. But yay I'm done!
* **12:42 PM (December 23rd)** Finished with the project overall. I broke the time constraints rules (whoops) but the final product is ready for release. I'll be spending the next few hours trying to get an actual working product working on merrychristmas.wilhelmwillie.com