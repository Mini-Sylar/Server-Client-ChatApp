# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased] - 2021-08-07
### Added
- No new major features just fixes
### Changed
- fixed logic causing disconnect message to be treated as a key
- Fixed colors being re-assigned whenever someone left
- When someone leaves and rejoins the color will be updated again 
  (This might be changed to retain the old color)
### Issues
- No issues found
<hr>


## [Unreleased] - 2021-08-06
### Added
- Major Fixes to all color assignment issues. There will be no crashes now
- Added code to show usernames currently connected to the server
- Updated Screenshots
### Changed
- Reworked the assignment of colors and now they work perfectly 
  it will mostly assign light colors (fingers crossed) to each user
- Username has been moved slightly (Color will remain black)
- Server messages are now formatted properly
### Issues
- All major issues have been fixed
<hr>


## [Unreleased] - 2021-08-03
### Added
- Added usernames to each message to help tell each user apart
- Added parameter to assign different colors to different users
- Added function to randomly assign colors to users
### Changed
- the default green is no longer assigned as default since having multiple users with that same color will be 
an eyesore
### Issues
- Issue with dictionary not updating member keys and hence cannot assign colors (Causes crashes)
<hr>


## [Unreleased] - 2021-07-01
### Added
- Added screenshots of the new labels
### Changed
- Removed the "'b" that shows with server messages
### Issues
- No major issues found
<hr>


## [Unreleased] - 2021-07-01
### Added
- Added screenshots of the new labels
### Changed
- Admin messages are now centered and include timestamps
- Fixed an issue which was causing text not to align properly when resizing window
- Some more code cleanup
- Updated Readme
- Username can not be more than 20 characters
### Issues
- No major issues found
<hr>

## [Unreleased] - 2021-06-30
### Added
- Added timestamps to messages
- Added Bubble for Admin/Server messages (White)
### Changed
- Fixed issue causing high cpu usage
- Found a work-around for names not aligning
### Issues
- Messages from Admin/Server are not centered 
- Name in the sliding bar does not align with the user icon
<hr>

## [Unreleased] - 2021-06-29
### Added
- Added Chat Bubbles in message window
### Changed
- Chat bubbles replace console like screen. both options will be accessible in future builds 
- UI Code seperated from functions to allow easier debugging 
- Label class has been removed from function's file into its own module
### Issues
- Chat bubbles duplicate messages received
- Name in the sliding bar does not align with the user icon