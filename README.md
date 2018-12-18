# Backdoorgery
Totally legal and non-ToS breaking API into backloggery.com

### Functionality
Currently two public functions available:
- getConsoleMetrics: Shows the Unfinished/Beaten/Complete metrics for a user's console.
- getFortuneCookie: Pulls a random game from a user's backlogggery. Seemingly uses no filters.

#### Notes
Even though you have to log in to access the Fortune Cookie tab normally, you can actually just go to the URL directly and it will work. Not sure if this is a security flaw or just something they don't care about. It's technically no more invasive than seeing someone's profile, which you can do anyway.

A decent chunk of the response parsing is hard-coded because this is an ugly interpretation of an HTML cURL response. Not sure how else to do this through Python since there's no official API.

# Requires
- requests 2.18.4
- pyquery 1.4.0
