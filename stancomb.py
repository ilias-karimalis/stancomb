# We reserve the keyword theta and require that there is no need for parameter renaming.
# NOTE: no support for transformed data, parameters
def mixture_model(
        data,
		transformed_data,
        shared_params,
		transformed_shared_params,
        param_list,
		transformed_param_list,
        model_list):

	def model_lp_sum(i):
		if i == 0: return ''
		elif i == 1: return '- lp[1]'
		else: return f'- sum(lp[1:{i-1}])'

	n_models = len(model_list)
	
	model_string = ''.join([model+f'\nlp[{i+1}] = target() {model_lp_sum(i)} - log_jac;\n' for i, model in enumerate(model_list)])
	model_block = (
		f'model {{\n'
		f'real log_jac = target();\n'
		f'vector[{n_models}] lp;\n'
		f'{model_string}'
		f'target += -target();\n'
		f'target += log_sum_exp(log(theta) + lp) + log_jac;\n}}'
	)

	transformed_data = f'transformed data {{\n{transformed_data}\n}}\n' if len(transformed_data)>0 else ''
	data_blocks = f'data {{\n{data}\n}}\n' + transformed_data

	transformed_params = transformed_shared_params + "".join(transformed_param_list) 
	transformed_params = f'transformed parameters {{{transformed_params}\n}}\n' if len(transformed_params) > 0 else ''
	parameter_blocks = (
		f'parameters {{\nsimplex[{len(model_list)}] theta;\n'
		f'{shared_params + "".join(param_list)}\n}}\n' + transformed_params
	)
	
	model = data_blocks + parameter_blocks + model_block
	return model

# Our next step is making it work with arbitrary Stan models with the single prerequisite that theta
# is a reserved parameters and that models don't have any shared parameters.
MIXTURE_MODEL = 1


def stancomb(stan_file1, stan_file2, model_type=MIXTURE_MODEL):
	pass
