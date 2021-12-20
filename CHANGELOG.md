# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## <span style="color:orange">[Unreleased] - 2021-12-18</span>
### <span style="color:teal"> <span style="color:teal">Added
- Added Emoji Support
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Reworked UI to include emoji button. For testing purposes, 6 are available, more will be included
### <span style="color:red">Issues
- Quality of emoji is a bit grainy(Might just be the font)
<hr>


## <span style="color:orange">[Unreleased] - 2021-12-18</span>
### <span style="color:teal"> <span style="color:teal">Added
- Some UI Changes
- Rounded Text input area
- Re-designed send button
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Fixed issue with name not aligning in slide menu (Hopefully once and for all)
- Reworked the animations for hiding and showing the username and icon
- Font in side-panel now match
- Colors have been further darkened
- Window title changed (idk why this wasn't done earlier)
- Fixed issue where text indent would reset after sending a message
### <span style="color:red">Issues
- Send button can still send empty messages
- ~~After sending a message, text box indent resets~~
<hr>


##<span style="color:orange"> [Unreleased] - 2021-12-16
### <span style="color:teal"> <span style="color:teal">Added
- No new major features just fixes
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- !! Should color be unassigned for some reason, a default color will automatically be assigned
- !! Fix issue where users with similar names won't have their messages sent. 
  - Suggestions made by: [Martin](https://www.mfitzp.com/forum/u/martin) to use UUID
### <span style="color:red">Issues
- No issues found
<hr>


## <span style="color:orange">[Unreleased] - 2021-08-24
### <span style="color:teal"> <span style="color:teal">Added
- No new major features just fixes
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- changed the logic for assigning colors. This fixes colors being re-assigned when someone joins or leaves
- Name aligns properly with message now
### <span style="color:red">Issues
- No issues found
<hr>


##<span style="color:orange"> [Unreleased] - 2021-08-07
### <span style="color:teal">Added
- No new major features just fixes
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- fixed logic causing disconnect message to be treated as a key
- Fixed colors being re-assigned whenever someone left
- When someone leaves and rejoins the color will be updated again 
  (This might be changed to retain the old color)
### <span style="color:red">Issues
- No issues found
<hr>


## <span style="color:orange">[Unreleased] - 2021-08-06
### <span style="color:teal">Added
- Major Fixes to all color assignment issues. There will be no crashes now
- Added code to show usernames currently connected to the server
- Updated Screenshots
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Reworked the assignment of colors and now they work perfectly 
  it will mostly assign light colors (fingers crossed) to each user
- Username has been moved slightly (Color will remain black)
- Server messages are now formatted properly
### <span style="color:red">Issues
- All major issues have been fixed
<hr>


## <span style="color:orange">[Unreleased] - 2021-08-03
### <span style="color:teal">Added
- Added usernames to each message to help tell each user apart
- Added parameter to assign different colors to different users
- Added function to randomly assign colors to users
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- the default green is no longer assigned as default since having multiple users with that same color will be 
an eyesore
### <span style="color:red">Issues
- Issue with dictionary not updating member keys and hence cannot assign colors (Causes crashes)
<hr>


##<span style="color:orange"> [Unreleased] - 2021-07-01
### <span style="color:teal">Added
- Added screenshots of the new labels
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Removed the "'b" that shows with server messages
### <span style="color:red">Issues
- No major issues found
<hr>


## <span style="color:orange">[Unreleased] - 2021-07-01
### <span style="color:teal">Added
- Added screenshots of the new labels
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Admin messages are now centered and include timestamps
- Fixed an issue which was causing text not to align properly when resizing window
- Some more code cleanup
- Updated Readme
- Username can not be more than 20 characters
### <span style="color:red">Issues
- No major issues found
<hr>

## <span style="color:orange">[Unreleased] - 2021-06-30
### <span style="color:teal">Added
- Added timestamps to messages
- Added Bubble for Admin/Server messages (White)
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Fixed issue causing high cpu usage
- Found a work-around for names not aligning
### <span style="color:red">Issues
- Messages from Admin/Server are not centered 
- Name in the sliding bar does not align with the user icon
<hr>

## <span style="color:orange">[Unreleased] - 2021-06-29
### <span style="color:teal">Added
- Added Chat Bubbles in message window
### <span style="color:green"><span style="color:blue"><span style="color:pink">Changed
- Chat bubbles replace console like screen. both options will be accessible in future builds 
- UI Code seperated from functions to allow easier debugging 
- Label class has been removed from function's file into its own module
### <span style="color:red">Issues
- Chat bubbles duplicate messages received
- Name in the sliding bar does not align with the user icon