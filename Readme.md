#A _very_ simple python css preprocessor. (Python 3)

This was made to be able to have a way to use preprocessed css on a machine where you're not able to install anything.
Of course assuming python is already installed.


###This:
```

div
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

        img
            display: auto;

        &:hover
            color: #49f;

div
    div
        color: white;
    height: 100px;
    width: 10px;

body
    background: #111;
    color: #e11;
```
###Produces:
```
div {
	height: 100px;
	width: 10px;
}

body a {
	height: 100px;
	width: 100px;
}

body a div {
	height: 30px;
}

body a div a {
	width: 10px;
}

body a div a h1 {
	color: black;
}

body a div span {
	height: 1px;
}

body a div img {
	display: auto;
}

body a div:hover {
	color: #49f;
}

div div {
	color: white;
}

body {
	background: #111;
	color: #e11;
}
```

##Usage

Semicolons are mandatory, tabbing is used to denote hierarchy, and selectors are just lines without semicolons in them.
Mixed tabbing is not supported.

`python pypros.py file1 file2 fileN`

Note: the filename for ex.pyp would just be ex, the script will add the file endings, or it can be ex.pyp and the output
file will be ex.css

Flags:
    -w, sets the program to run until interrupted and watches the files passed to it