import os
import subprocess
import shutil

home_dir = os.path.expanduser("~") 

def installNeededPackages(packagename:list) -> None:
    print("⬇️ Installing needed packages")


    try:
        for package in packagename:
            subprocess.run(["yay", "-S",package,"--needed"])
        print("✅ Packages installed successfully")

    except:
        print("😥 Something went wrong skipping installing")


def backupFileFolders(home_dir:str,pathList:list) -> None:
    # full backupfiles path /home/user/backup_dotfiles
    bkp_dir = "backup_dotfiles"
    dest_parent = os.path.join(home_dir,bkp_dir)

    # check if file doesn't exist, if it doesn't create one
    if not os.path.exists(dest_parent):
        os.mkdir(dest_parent)


    # loop through every files included for dotfiles
    for path in pathList: 
        #full path i.e. if .zshrc we make it /home/user/.zshrc
        src_path = os.path.join(home_dir,path)
        dest_path = os.path.join(dest_parent,path)
        

        # if the file or folder already exists then backup it in dest_path
        if os.path.exists(src_path):
            # if file exist in dest path then remove it

            if os.path.islink(dest_path) or os.path.isfile(dest_path):
                print(f"removing {dest_path} ")
                os.remove(dest_path)  # remove file or symlink

            elif os.path.isdir(dest_path):
                shutil.rmtree(dest_path)  # remove folder recursively           

            print(f"backing up {src_path} to {dest_parent}")
            shutil.move(src_path,dest_parent)

def createSymlink(home_dir:str,pathList:list) -> None:
    # remove path if already exists
    gitdir = "dotfiles2"
    for fileF in pathList:
        src_path =os.path.join(home_dir,fileF)

        if os.path.exists(src_path):
            print(f"Removing {src_path}")

        if os.path.islink(src_path):
            os.unlink(src_path)
            print(f"Removed symlink {src_path}")
        elif os.path.exists(src_path):
            print(f"Removing {src_path}")
            subprocess.run(["rm","-rf",src_path])

        # make sure parent dir exists
        parent_dir = os.path.dirname(src_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

        # create symlinking
        dotpath = os.path.join(home_dir,gitdir,fileF)

        print(f"symlinking {dotpath} -> {src_path}")
        subprocess.run(["ln","-s",dotpath,src_path])

def setUpNormalStuff(home_dir:str) -> None:

    ohmyzsh_dir = os.path.join(home_dir, ".oh-my-zsh")
    zsh_custom = os.environ.get("ZSH_CUSTOM", f"{ohmyzsh_dir}/custom")
    p10k_dir = os.path.join(zsh_custom, "themes", "powerlevel10k")

    # 1. Remove existing .oh-my-zsh if it exists
    if not os.path.exists(ohmyzsh_dir):

        # 2. Install Oh My Zsh (non-interactive)
        print("Installing Oh My Zsh...")
        subprocess.run(
                [
                    "sh",
                    "-c",
                    "RUNZSH=no CHSH=no "
                    "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sh"
                    ],
                check=True
                )
    #2. Install zsh-autosuggestion
    autosuggestionDir = os.path.join(ohmyzsh_dir,"plugins","zsh-autosuggestion")

    if not os.path.exists(autosuggestionDir):
        print("Installing zsh-autosuggestions")

        subprocess.run(
                [
                    "git",
                    "clone",
                    "https://github.com/zsh-users/zsh-autosuggestions.git",
                    autosuggestionDir,
                    ],
                check=True
                )

    # 3. Install Powerlevel10k
    if not os.path.exists(p10k_dir):
        print("Installing Powerlevel10k...")
        subprocess.run(
                [
                    "git",
                    "clone",
                    "--depth=1",
                    "https://github.com/romkatv/powerlevel10k.git",
                    p10k_dir,
                    ],
                check=True
                )

    # If you havent done this please uncomment this, this will make sure you gtk theme will be applied all over the apps

    '''
    subprocess.run(["systemctl","--user","restart","xdg-desktop-portal-hyprland"])
    subprocess.run(["systemctl","--user","restart","xdg-desktop-portal"])
    subprocess.run(["gsettings","set","org.gnome.desktop.interface","color-scheme","prefer-dark"])

    '''

    print("Zsh setup complete.")



def main():
    neededPackages = ["wl-copy","pavucontrol","cava","swww","rofi","zsh","swaync","waybar","nwg-theme","xdg-desktop-portal-gtk","xdg-portal-hyprland","adw-gtk-dark","qt5ct","qt6ct","grim","slurp","kitty","thunar","wpctl","brightnessctl","network-manager-applet","zoxide","exa","gammastep","tealdeer","noto-fonts-emoji","ttf-jetbrains-mono-nerd","libcanberra","camera-shutter"]

    dotfilesIncludedFiles = [".zshrc",".config/gtk-3.0",".config/gtk-4.0",".config/hypr",".config/kitty",".config/nwg-look",".config/qt5ct",".config/qt6ct",".config/rofi",".config/swaync",".config/waybar",".config/xdg-desktop-portal"]
    # installNeededPackages(neededPackages)
    # backupFileFolders(home_dir,dotfilesIncludedFiles)
    # createSymlink(home_dir,dotfilesIncludedFiles)
    setUpNormalStuff(home_dir)


if __name__=="__main__":
    main()
