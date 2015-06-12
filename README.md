# Disrupt

A python "tool" for "interacting" with the terminals of "friends" and 
"colleagues".

## Installation

    pip install disrupt

Alternatively, since it must be run as root, you may not want to install.  
You can download a fully packaged 
[`pex`](https://pex.readthedocs.org/en/latest/) file and run without 
installing:

    wget https://github.com/dellis23/disrupt/blob/master/bin/pex/disrupt.pex?raw=true -O disrupt; chmod +x disrupt

## Usage

Get a list of users on the box you're on, and take a note of the terminal:

    $ who
    myself  pts/8        2015-06-12 00:12 (31.1.3.7)
    target  pts/2        2015-06-12 00:02 (1.1.1.1)

Then, as root (*required*), launch a disruption at the terminal:

    # disrupt -t /dev/pts/2 -d wipe

That'll wipe their screen every once in a while.

### Increasing Intensity

All disruptions can be configured to be subtle `-v` all the way up to really 
intrusive `-vvvvv`.

## Disruptions

### blocks

Prints a colored box at a random position in the target terminal.

#### Examples

    # disrupt -t /dev/pts/2 -d blocks -v

![Example of blocks -v](https://github.com/dellis23/disrupt/blob/master/img/blocks-v.gif)

    # disrupt -t /dev/pts/2 -d blocks -vvv

![Example of blocks -vvv](https://github.com/dellis23/disrupt/blob/master/img/blocks-vvv.gif)

    # disrupt -t /dev/pts/2 -d blocks -vvvvv

![Example of blocks -vvvvv](https://github.com/dellis23/disrupt/blob/master/img/blocks-vvvvv.gif)

### rainbow

Changes the target terminal's text to a random color.

#### Examples

    # disrupt -t /dev/pts/2 -d rainbow -v

![Example of rainbow -v](https://github.com/dellis23/disrupt/blob/master/img/rainbow-v.gif)

    # disrupt -t /dev/pts/2 -d rainbow -vvvvv

![Example of rainbow -vvvvv](https://github.com/dellis23/disrupt/blob/master/img/rainbow-vvvvv.gif)

### jitter

Randomly moves the cursor one movement up, down, left, or right.

#### Examples

    # disrupt -t /dev/pts/2 -d jitter -v

![Example of jitter -v](https://github.com/dellis23/disrupt/blob/master/img/jitter-v.gif)

    # disrupt -t /dev/pts/2 -d jitter -vvv

![Example of jitter -vvv](https://github.com/dellis23/disrupt/blob/master/img/jitter-vvv.gif)

    # disrupt -t /dev/pts/2 -d jitter -vvvvv

![Example of jitter -vvvvv](https://github.com/dellis23/disrupt/blob/master/img/jitter-vvvvv.gif)

### wipe

Clears the screen.

#### Examples

    # disrupt -t /dev/pts/2 -d wipe -v

![Example of wipe -v](https://github.com/dellis23/disrupt/blob/master/img/wipe-v.gif)

    # disrupt -t /dev/pts/2 -d wipe -vvvvv

![Example of wipe -vvvvv](https://github.com/dellis23/disrupt/blob/master/img/wipe-vvvvv.gif)

### hide

Randomly hides or shows the cursor.  Requires the user to type a key for
it to take effect, so verbosity is basically just maximum.

#### Examples

    # disrupt -t /dev/pts/2 -d hide

![Example of hide](https://github.com/dellis23/disrupt/blob/master/img/hide.gif)

### beep

Sends a beep to the target terminal.

Max verbosity will make them want to kill you, so be courteous.
