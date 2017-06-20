# Gentore: Secure password generation and Local storage
Tired of giving all your data and even passwords to random organizations and
corporates across the web? Well, time to switch then.  
Gentore is a simple piece of software made for personal use that may be useful
for you. It has the ability to generate particularly strong, randomized
passwords.  
This is an approach based on the same principle (entropy) but safer methods than seen
in [XKCD](https://www.xkcd.com/936/). Furthermore, it provides a simple way of
saving these passwords into an encrypted text file.  
For now, the application is in Alpha stage but very much usable.

## GUI

Most available password generators are CLI tools that can seem a little annoying when all you want is to generate a random password or a url-safe token. But Gentore is different. Gentore provides a neat, un-cluttered UI with an easy 'Generate' button that makes it all-too-obvious what to do next.

## Password Storage

Gentore uses `Fernet` from the module `cryptography` to provide a safe storage for your password. In addition to just the password, you also get control over what salt is used.  
Though I do not personally recommend this, the most secure course of action would be to do the following:

 1. Generate 2 passwords and write them down somewhere physically.
 2. Use one of the two you wrote down as the password and the other as the salt to save other passwords.

Personally, I don't find myself paranoid enough to do that. Since it is on local storage, a password and a salt that I'm sure to remember seems enough.

## Not Sure about Cross-platforming

Gentore doesn't require anything specific to Linux as far as I can see. Except maybe GtkHeaderBar in Gtk+. It should work.

## Typical password security checks

You're better off not doing these checks on actual passwords.

[Online Domain Tools Password Checker](http://password-checker.online-domain-tools.com/)  
WARNING: This site is particularly unsafe, it even lacks SSL

Category | Score
------------ | -------------
Strength | 100 %
Evaluation | Excellent
Standard Desktop PC | About 9 tredecillion years
Fast Desktop PC | About 2 tredecillion years
GPU | About 877 duodecillion years
Fast GPU | About 438 duodecillion years
Parallel GPUs | About 44 duodecillion years
Medium size botnet | About 9 undecillion years

[Kaspesky Secure Password Checker](https://password.kaspersky.com/)

Category | Score
------------ | -------------
General | 10000+ Centuries
ZX Spectrun | 10000+ Centuries
Mac Book Pro 2012 | 10000+ Centuries
Conficker botnet | 10000+ Centuries
Tianhe-2 Supercomputer | 10000+ Centuries

[How Secure Is My Password?](https://howsecureismypassword.net/)

It would take a computer about  
**2 DUODECILLION YEARS**  
to crack your password.

## What do I ask in return?

Really, nothing. I made this for my personal use and decided to let the world use it if they want it. Donations won't reach my corners anyway.  
But if you really, really wanna help, a more powerful Linux laptop would be nice. I'm from India and availability of good Linux laptops are horribly bad. Furthermore, I'm 16 and not independent from my parents, who are, at the moment, pretty much broke. I wish to keep my passion of programming and wish to support the projects I love but I'm very limited in what I can do. I'm on a loud Acer Aspire 3810TG with no capacity whatsoever for even proper browsing. A few of the projects I love are games and how do I contribute if I can't even play them to begin with. If you are interested in helping me out, please send a mail to <lastweakness@tuta.io>. I'm counting on you, generous strangers. :)
