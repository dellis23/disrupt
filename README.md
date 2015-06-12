# Disrupt

A python "tool" for "interacting" with the terminals of "friends" and 
"colleagues".

## Installation

    pip install disrupt

`pex` packages are planned to enable downloading and running without 
installation.

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

### rainbow

Changes the target terminal's text to a random color.

#### Examples

    # disrupt -t /dev/pts/2 -d rainbow -v

### jitter

Randomly moves the cursor one movement up, down, left, or right.

#### Examples

    # disrupt -t /dev/pts/2 -d jitter -v

### wipe

Clears the screen.

#### Examples

    # disrupt -t /dev/pts/2 -d wipe -v

### hide

Randomly hides or shows the cursor.  Requires the user to type a key for
it to take effect, so verbosity is basically just maximum.

#### Examples

    # disrupt -t /dev/pts/2 -d hide

### beep

Sends a beep to the target terminal.

Max verbosity will make them want to kill you, so be courteous.
