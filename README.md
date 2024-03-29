# Text Adventure (Tentative)

## Author
Varun Peesapati

## What works at the moment
* The player can enter (and confirm) their name at the beginning of the adventure.
* The typewriter effect works as intended for the text that's part of the narrative.
* Sentences that exceed the maximum width of the screen are now wrapped.
* The text speed of the typewriter effect can now be changed depending on the context of the line (to give more weight to the narrative context).
* The narrative seamlessly transitions from one page to another without any hiccups (including ones with options in them as well).
* The line would forgo the typewriter effect when any key (except `ESCAPE`) is pressed to speed up the process.
* Choosing different options would now alter the narrative.
* The text now waits for the player to proceed with the rest of the narrative.

## Ideas yet to be implemented
* ~~Wrapping of long sentences that exceed the width of the screen.~~
* An original script with (sorta) branching narratives.
* A save feature that allows users to save at certain points and re-join at the same place at any other time.
* Update README with details of the completed project.

## References
* Typewriter effect: https://stackoverflow.com/a/31382966
* Wrapping text in pygame: https://stackoverflow.com/questions/49432109/how-to-wrap-text-in-pygame-using-pygame-font-font