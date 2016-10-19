
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

@media (max-width: 100px)
	body
		height: 100px;
		div
			height: 100px;

@media (min-width: 100px)
	body
		height: 100px;
		div
			width: 111px;
		