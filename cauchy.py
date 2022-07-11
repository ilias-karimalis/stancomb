from stancomb import mixture_model

print(mixture_model(
	"real gap;\n",	 # Data
	"real alpha;\n", # Shared Parameters
	[""],	# Non Shared Parameters
	["alpha ~ cauchy(-gap, 0.2)\nalpha ~ cauchy(gap, 0.2);", # Model 1
	 "alpha ~ normal(0, 5);"]	# Model 2
))
