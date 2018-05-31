word = input('Введите пожалуйста информацию в строку:')
len_word = int(len(word))
var_obs = len_word // 2
print ('x' * 20)
print ('x' + ' ' * ((10 - 2 - int(var_obs) // 2)) + word  + ' ' * (10 - 2 - int(var_obs) // 2)  + "х")
print ('x' * 20)
