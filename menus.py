"""
Menus.py is a separate file that will contain all menus a user could face within the
program. This keeps code clean as well as makes it easier for us to expand/reduce/adjust
the menu as need be. All menus as of right now are saved in dictionary format.
"""
logInMenu = {"1": "Log In", "2": "Register"}

registerMenu = {1:"Enter an email: ", 2: "Enter a password: "}

rankIssueMenu = {"Banned": "You have been banished from the guild, if you believe this is an error please reach out to your GM.", "Inactive": "You are currently inactive status. What would you like to do?"} 
#We do not need a kicked message because kicked status can just be their character being deleted, only time it is an issue is if they are banned from joining the guild.

bannedStatusMenu = {"1": "Drop association", "2": "Exit"}

inactiveStatusMenu = {"1": "Request for reactivation", "2": "Drop guild"}

mainMenu = {1: "Update Gear", 2: "Add Attendance", 3: "Request Leave", 4: "View Leave Requests", 5: "View Member Growth", 6: "Manage Officers", 7: "Ban Members", 8: "Remove Bans"}
