from stancomb import mixture_model

print(mixture_model(
	"real gap;\n",
	"real alpha;\n",
	[""],
	["alpha ~ cauchy(-gap, 0.2)\nalpha ~ cauchy(gap, 0.2);",
	 "alpha ~ normal(0, 5);"]
))
