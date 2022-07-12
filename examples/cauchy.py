from stancomb import mixture_model
import pystan

generated_model = mixture_model(
	"real gap;",	 					 						# Data
	"", 							 							# Transformed Data
	"real alpha;", 					 							# Shared Parameters
	"", 							 							# Transformed Shared Parameters
	[""],							 							# Non Shared Parameters
	[""], 							 							# Non Shared Transformed Parameters
	["alpha ~ cauchy(-gap, 0.2)\nalpha ~ cauchy(gap, 0.2);", 	# Model 1
	 "alpha ~ normal(0, 5);"]								 	# Model 2
)
