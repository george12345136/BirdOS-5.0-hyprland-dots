# BirdOS-5.0-hyprland-dots
This is the the new version of BirdOS Hyprland setup!

WARNING: WE STILL DID NOT HAVE MADE AN INSTALLER SCRIPT, THIS IS A MANUAL INSTALL, DONT MESS UP!

NOTE: Installer script may release in a point release of BirdOS 5.x or 6.X or 7.x

Install Guide:

BirdOS 5.0 Install Guide

What we are gonna use for BirdOS:

DE: KDE Plasma(Offers Powerful tools than needed!) WM: Hyprland(Works also on niri with some extra configuration than is not recommended…) Icon: Papirus Theme:Breeze(Default to KDE Plasma).

1.0. Prepare installation of Arch Linux(If you don`t have Arch Linux):

NOTE: If you have done this step,go to Step 3.0.

Arch Linux installation is very hard, right?

No, because Arch Linux Developers have created an installer for Arch Linux called archinstall, imagine as an Ubuntu installer but in terminal and using only Enter and Keys(Ctrl or Control is required, and the entire keyboard also).

1.1. You need a Flash Drive(USB) at least 8 GB of space.

1.2. Now boot on your Flash Drive(USB)

1.3. Now type archinstall

1.4. Now after you are at archinstall do those things:

Disk configuration > Partitioning > Use the best-effort default partition layout > select your disk > ext4 > No > Back

Bootloader > Bootloader > Grub > Back

Authentication > User account > Add a user > (type your username) > (type your password) > (re-type your password)

    Yes(if you select no, the half(and the entire) system config is cooked) > Confirm and exit > Back

Profile > Type > Desktop > KDE Plasma > Back

Network configuration > Use NetworkManager(necessary to configure internet graphically in GNOME and KDE Plasma)

NOTE: If you don't Select NetworkManager your system is also cooked

Now press Install > Yes

After the install ends press Reboot system and remove after pressing it your Flash Drive

2.0. First Boot:

You will see GRUB at the first boot(and any other)simply wait 5s or press Enter to boot to Arch Linux, after that, you will go to SDDM to type your user password and press Ender, now wait until KDE Plasma is loaded.

3.0. Install Packages

3.1. Type:

sudo pacman -Syu 

3.2. Then type:

sudo pacman -S firefox kitty fastfetch pavucontrol swaync hyprlock waybar htop rofi git thunar swww hyprland papirus-icon theme hyprshot power-profiles-daemon

Install yay:

git clone https://aur.archlinux.org/yay.git 
cd yay

makepkg -si

Now install those(Just Press Enter and type your password when is asking for it!):

yay -S matugen

yay -S wlogout

yay -S nerd-fonts #install them all

yay -S apple_cursor

yay -S apple-fonts

3.3. After the installation of the packages is done, type on your terminal: 

cd ~/.config

And then:

git clone https://github.com/george12345136/BirdOS-5.0-hyprland-dots.git 

3.4. Now close the Terminal

3.5. Log out from the KDE Plasma session and go to the session and select Hyprland from the session and log in.

4.0. Troubleshooting(Easy level and is NOT* from the terminal)Open your Terminal(Now is Kitty), to open it simply press:(Super Key is the Windows Key)SUPER KEY + Q and type: chmod u+x ~/.config/hypr/wallpaper-switcher.sh

4.1. Now download or use the default BirdOS Wallpapers on the Pictures folder(IMPORTANT)

4.2. Now go to the terminal and type: swww img /home/(your username)/Pictures/(your_wallpaper_name.format)and press Enter while also typing matugen image /home/(your username)/Pictures/(your_wallpaper_name.format)

4.3. Now Press SUPER KEY + M to exit and re-log in back and BOOM is done 👍


