from cmdstanpy import CmdStanModel
import pandas as pd
import numpy as np

vweather_df = pd.read_csv("./weatherstats_vancouver_daily.csv")
vprecip = np.array(vweather_df["precipitation"].iloc[::-1])
N, = vprecip.shape

from stancomb import mixture_model
generated_model = mixture_model(
    "int<lower=0> N;\nvector[N] y;",                                                       # Data
    "",
    "",
    "",
    ["real alpha_1;\nreal<lower=-1, upper=1> beta_1;\nreal<lower=0> sigma_1;",                                     # AR(1) params
     "real mu_2;\nreal<lower=0> alpha_2;\nreal<lower=0, upper=1> beta_2;"],                     # ARCH(1) params
    [],
    ["for (n in 2:N) {\ny[n] ~ normal(alpha_1 + beta_1 * y[n-1], sigma_1);\n}\n",                 # AR(1) Model
     "for (n in 2:N) {\ny[n] ~ normal(mu_2, sqrt(alpha_2 + beta_2 * pow(y[n-1] - mu_2, 2)));\n}\n"] # ARCH(1) Model
)

with open("./precip.stan", "w") as f:
    print(generated_model, file=f)

data = {
    "N": 250,
    "y": vprecip[0:250]
}

from cmdstanpy import CmdStanModel
stan_file = "./precip.stan"
stan_model = CmdStanModel(stan_file=stan_file)
stan_model.compile()

stan_fit = stan_model.sample(data=data)
