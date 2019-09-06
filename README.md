# Alacritty Color Switcher

## Example
```
> acs --list
one_dark
tomorrow_night
solarized_light
solarized_dark
nord

> acs --apply nord
nord # -> ~/.config/alacritty/alacritty.yml is updated

> acs --switch
one_dark #
```

Warning: please make a backup of your `alacritty.yml` since `acs` over-writes
the content with the changed color file! Also some formatting will be lost!


## Install
```
pip install git+https://github.com/tbehner/alacritty-color-switcher.git
```
