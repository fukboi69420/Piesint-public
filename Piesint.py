import os
import scripts
print(" ________  ___  _______   ________  ___  ________   _________   
print("|\   __  \|\  \|\  ___ \ |\   ____\|\  \|\   ___  \|\___   ___\ ")
print("\ \  \|\  \ \  \ \   __/|\ \  \___|\ \  \ \  \\ \  \|___ \  \_| ")
print(" \ \   ____\ \  \ \  \_|/_\ \_____  \ \  \ \  \\ \  \   \ \  \  ")
print("  \ \  \___|\ \  \ \  \_|\ \|____|\  \ \  \ \  \\ \  \   \ \  \ ")
print("   \ \__\    \ \__\ \_______\____\_\  \ \__\ \__\\ \__\   \ \__\")
print("    \|__|     \|__|\|_______|\_________\|__|\|__| \|__|    \|__|")
print("                            \|_________|                        ")
attack = input("What are you researching? (user,email,site,ip,name) ")
if attack == "site":
    site = input("Enter the site: ")
    scripts.site(site)
elif attack == "user":
    user = input("Enter the user:")
    scripts.user(user)
elif attack == "email":
    email = input("Enter the email:")
    scripts.email(email)
elif attack == "ip":
    ip = input("Enter the ip:")
    scripts.ip(ip)
elif attack == "name":
    name = input("Enter the first name:")
    lname = input("Enter the last name:")
    scripts.name(name,lname)
