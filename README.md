# microbit_2ColFont
Implementation of a font of chars and ints that are 2 cols x 5 rows (10 pixels), and code to scroll them on display

On 08.06.2017 @whaleyGeek released his awesome clock app for micro:bit.
One thing this app had was a cool font used to show 2 ints on-screen at the same time.
https://github.com/whaleygeek/mb_clock/blob/master/clock.py

In effect, WhaleyGeek had created the basis of a new font for micro:bit, and done so as a byproduct of the clock.
This Font, which we christened WhaleySans on twitter, included render data for all 10 integers.

My thanks to David for the inspiration, and for graciously allowing me to use his code :)

Using David's core idea and definition of the integers I've added:
... support for all alphabet characters
... some code to take an image that is wider than 5 pixels and scroll it.  At present Python will not scroll an image larger than 5x5

The code does nothing but demo the Font:
... use button a to show an int containing all 9 integers
... use button b to show a string with all 26 chars.

Font itself is OK - works really well for some chars (e.g. e, f, t) OK for others, but there is NO way of getting a decent 'm' or 'w' - in particular those are totally unrecognisable.  Pity... a 3-col font would give more scope, but showing 2 chars on screen simultaneously is preferred.  Anyway, lets leave the 3 col font for someone else - using @whaleyGeeks template its pretty straightforward.

So, a byproduct of this code is that there are 2 methods which can be stripped out and which will allow you to pass in a string in this form:
91949056090909:909090909090909:909090909090909:909090909090909:909090909090909 (note - no trailing colon)
and render it as a scrolling image.

NOTES:
... error trapping is sparse.
... app gobbles memory so probably no real practical application... that said, it would be possible to build this app onto 1 micro:bit and have another micro:bit call it (maybe over radio) - pass in strings and return render info for images.  This would leave all processing on the 'font server' microbit and would require minimum code on the client.

Thanks
Philip
