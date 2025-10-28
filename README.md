# HyprFoolscreen

Fool apps into thinking they are fullscreen, while actually they are not *(evil laughter)*

This is actually a built in [feature](https://wiki.hypr.land/Configuring/Dispatchers/#fullscreenstate) of Hyprland, you just call:

```sh
hyprctl dispatch fullscreenstate <real state> <what app thinks>
```

So this is just a simple GUI wrapper for that feature. Like, really simple, but gets the job done

## Usage

So, to install it, you can download the [`hypr-foolscreen.py`](./hypr-foolscreen.py) file, or clone the repo somewhere

Then, you can map it in Hyprland config to something like

```conf
bind = SUPER, F, exec, /where/you/saved/hypr-foolscreen.py
```

And it's done! Enjoy fooling apps

Seriously though, you can use this to make a floating YouTube player or something, it's useful
