from cmdstanpy import CmdStanModel

import numpy as np
from numpy.random import random, binomial

from stancomb import mixture_model

generated_model = mixture_model(
 	"int N;\nreal x[N];\nint y[N];",
    "",
 	"real beta;",
    "",
 	[""],
    [""],
    ["for (i in 1:N)\n\ty[i]~bernoulli(Phi(beta * x[i]));",
     "for (i in 1:N)\n\ty[i]~bernoulli_logit(beta * x[i]);"])

N = 30
x = random([N])
y = binomial(1, np.exp(3*x)/np.max(np.exp(3*x) + 1), size=N)

with open("./temp.stan", "w") as f:
    print(generated_model, file=f)

stan_file = "./temp.stan"
stan_model = CmdStanModel(stan_file=stan_file)
stan_model.compile()

data = {
    "N": N,
    "x": np.array(x),
    "y": np.array(y),
}

stan_fit = stan_model.sample(data=data)
