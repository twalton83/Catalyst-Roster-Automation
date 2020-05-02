# Catalyst-Roster-Automation
Selenium based Python app that automates the download process for Catalyst reports. 

## The Issue
My current role requires that I download .csvs from multiple webpages in order to update rosters. The website itself is at least one decade outdated, and takes multiple clicks to download a single .csv for one program out of many. My goal is to automate this process using Selenium, so with only a few keystrokes I can automatically download all of the rosters for the day, two times a day.

## Feature Wishlist
 * [X] Automatic Login to Catalyst
 * [X] Downloading .csvs (partially done)
 * Automatically runs 2x per day
 * [X] Creation of a Folder, labeled, for the downloads for the day 
 * Replace and delete old downloads
 * Eventually update the existing rosters in OneDrive 
 * GUI interface 
 * Downloading of only relevant programs/excluding unneeded programs
 * "Bypass" 2FA if already logged in on different browser instance 
