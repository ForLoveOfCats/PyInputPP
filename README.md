# Pygame's input system sucks. Lets fix that!

**PyInput++ is a wrapper around pygame's event system allowing developers to more easily handle input in their games.**


## Who This Is For:

* Anyone wishing for an easier way to handle input in their games in a maintainable way.
* Anyone who wants a dead simple way to handle keys being held down in their games.
* Anyone who wants to be able to handle input from anywhere in their program.


## Who This Is Not For:

* Anyone who is used to and enjoys working with pygame's event system.
* Anyone who already has a project specific input system implemented.
* Anyone who wants to write their input system from scratch.
* Anyone looking for a pygame event callback system.


# Why does this exist?

I originally developed this library as an internal module for a game I was working on. The project required that different classes be able to handle their own input. I was also tired of working with the pygame event system. The event system is not bad it is just not always the best way to get input from the user. **This project does not exist to replace the event system.** In fact the entire list of events each frame is available via the ```controller.events.raw()``` function.


# Bug Reports and Pull Requests are Welcome!
