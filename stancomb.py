# We reserve the keyword theta and require that there is no need for parameter renaming.
def mixture_model(
        data_string, 
        shared_parameter_string,
        parameter_string_list,
        model_string_list):

	def model_lp_sum(i):
		if i == 0: return ''
		elif i == 1: return '- lp[1]'
		else: return f'- sum(lp[1:{i-1}])'

	n_models = len(model_string_list)
	model_string = ''.join([model+f'\nlp[{i+1}] = target() {model_lp_sum(i)} - log_jac;\n' for i, model in enumerate(model_string_list)])
	model_block_string = (f'real log_jac = target();\n'
							f'vector[{n_models}] lp;\n'
							f'{model_string}'
							f'target += -target();\n'
							f'target += log_sum_exp(log(theta) + lp) + log_jac;') 
    
	model = (f'data {{\n{data_string}\n}}\n'
    				 f'parameters {{\nsimplex[{len(model_string_list)}] theta;\n'
    				 f'{shared_parameter_string + "".join(parameter_string_list)}\n}}\n'
    				 f'model {{\n{model_block_string}\n}}')
	return model

