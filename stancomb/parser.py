# Tokenizer
sample_source = """
data {
real gap;
}
parameters {
simplex[2] theta;
real alpha;
}
model {
real log_jac = target();
vector[2] lp;
alpha ~ cauchy(-gap, 0.2)
alpha ~ cauchy(gap, 0.2);
lp[1] = target()  - log_jac;
alpha ~ normal(0, 5);
lp[2] = target() - lp[1] - log_jac;
target += -target();
target += log_sum_exp(log(theta) + lp) + log_jac;
}
"""

print(list(sample_source))

def tokenize(sample_source):
    lsource = list(sample_source)
    i = 0
    stripped_array = []
    while i < len(lsource):

        
        
        i += 1


        