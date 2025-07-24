# UTDR Mod Loader

**A simple yet effective mod loader for UNDERTALE and DELTARUNE mods and fangames!**  
Built for flexibility, style, and ease of use.

---

## 🚀 Features

* Launch UNDERTALE/DELTARUNE mods and fangames from a single hub
* Display custom icons, descriptions, and images for each mod
* Supports different game types (All UT/DR versions & fangames)
* Hand-made custom UI by a cool guy (not to be confused with [Papyrus](https://undertale.fandom.com/wiki/Papyrus))
* Clean, DELTARUNE-style UI using the familiar font of Determination Mono (credit to the creator of [https://saveeditor.spamton.com](https://saveeditor.spamton.com/))

---

## 🛠️ Requirements

* Latest version of [Python](https://www.python.org/downloads/) (See below for more info)
* Python module: `psutil` (Install it by running `python -m pip install psutil`)

## 💡 During Python installation, make sure to:
* Check "Add Python to PATH"
* Check "Run with administrative privilages"
* Check "Disable path length limit" (found after install)
* Check "Install pip"

*If you've already installed Python for other projects, press Windows+R and type `sysdm.cpl`. From there, go to Advanced > Environment Variables > System Variables and verify that `C:\Users\_YOUR_USERNAME_HERE_\AppData\Local\Programs\Python\Python###\` (may vary based off of what version you got; ie: Python313) has the variable `PATH` attached to it.*

---

## 💻 How to Use

I have included some examples of base mods in there, but chances are, they will not work if you try to load them up. This is because the actual data that gets stored is only the location of the folder containing the `.exe` file, so **no actual game data gets saved through this launcher**.

It is recommended to move the UTDR Launcher folder somewhere you won't forget it and/or to add the UTDR Launcher folder to your Quick Access when setting up mods.
To add a mod
* Start by locating the file called *`mods.json`* and take note of the way that the data is structured. If you have 3 or less mods, you can go ahead and replace the current, already existing example mods and delete the data for the ones you aren't using.
* Take note of the data and its format. It is important that you do not leave out any parts of the data, as all of it is required and you may recieve unknown or undocumented errors.
* If you must add in a mod, perform the following:
      a. Make sure to
      * sure

___TIP:___ *If it crashes or says, "Failed to load mods" after you modify mods.json, check the Troubleshooting section below.*
