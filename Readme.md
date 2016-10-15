#A _very_ simple python css preprocessor. (Python 3)

This was made to be able to have a way to use preprocessed css on a machine where you're not able to install anything.
Of course assuming python is already installed.


###This:
```
body a
    height: 100px;
    width: 100px;


    div
        height: 30px;
        a
            width: 10px;
            h1
                color: black;
        span
            height: 1px;

div
    color: blue;
```
###Produces:
```
div {
	color: blue;
}

body a {
	height: 100px;
	width: 100px;
}

body a div a h1 {
	color: black;
}

body a div span {
	height: 1px;
}

body a div a {
	width: 10px;
}

body a div {
	height: 30px;
}


```

##Usage

Semicolons are mandatory, tabbing is used to denote hierarchy, and selectors are just lines without semicolons in them.

`python pypros.py file1 file2 fileN`

Note: the filename for ex.pyp would just be ex, the script will add the file endings

Flags:
    -w, sets the program to run until interrupted and watches the files passed to it