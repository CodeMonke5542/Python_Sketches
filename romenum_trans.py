#The goal of this program is, eventually, to output a properly formatted roman numeral from a decimal input or the other way around as well
"""Ideas:Let us say if 9 or 4 are in the final position of the number then let us replace that number with IV or IX     """
#Alt code letter is normal letter * 1000
"""def num_to_rome_v1(n):
    box_of_rome = ' '
    if n == 0:
        print('Nulla')
    if n == 1 or n == 2 or n == 3:
        box_of_rome += 'I'* n
    if n == 4:
        box_of_rome += 'IV'
    if n == 5 or n == 6 or n == 7 or n == 8:
        box_of_rome += 'V' + ('I'*(n-5))
    if n == 9:
        box_of_rome += 'IX'
    if n == 10 or n == 11 or n == 12 or n == 13:
        box_of_rome += 'X' + ('I'*(n-10))
    if n == 14:
        box_of_rome += 'XIV'
    if n == 15 or n == 16 or n == 17 or n == 18:
        box_of_rome += 'XV' + ('I'*(n-15))
    if n == 19:
        box_of_rome += 'XIX'
    if n == 20 or n == 21 or n == 22 or n == 23:
        box_of_rome += 'XX' + ('I'*(n-20))
    if n == 24:
        box_of_rome += 'XXIV'


    


    print(box_of_rome)


for i in range(25):
    num_to_rome_v1(i)"""


def num_to_rome_v2(n):
    n_string = str(n)
    n_list = []
    n_zeros = '0' * (len(n_string)+5)
    n_list.extend(n_zeros)
    n_list.extend(n_string)


    i_mult_one = int(n_list[-1])
    i_mult_x = int(n_list[-2])
    i_mult_c = int(n_list[-3])
    i_mult_m = int(n_list[-4])
    i_mult_xalt = int(n_list[-5])
    i_mult_calt = int(n_list[-6])
    i_mult_malt = int(n_list[-7])

    list_1 = ['1','2','3'] #commonly used list of numbers
    list_2 = ['5','6','7','8'] # ^

    
    if any(n_list[-1] == x for x in (list_1)):
        n_list[-1] = 'I' * i_mult_one
    if n_list[-1] == '4':
        n_list[-1] = 'IV'
    if any(n_list[-1] == x for x in (list_2)):
        n_list[-1] = 'V' + ('I'*(i_mult_one - 5))
    if n_list[-1] == '9':
        n_list[-1] = 'IX'
    

    if any(n_list[-2] == x for x in (list_1)):
        n_list[-2] = 'X' * i_mult_x
    if n_list[-2] == '4':
        n_list[-2] = 'XL'
    if any(n_list[-2] == x for x in (list_2)):
        n_list[-2] = 'L' + ('X'*(i_mult_x - 5))
    if n_list[-2] == '9':
        n_list[-2] = 'XC'


    if any(n_list[-3] == x for x in (list_1)):
        n_list[-3] = 'C' * i_mult_c
    if n_list[-3] == '4':
        n_list[-3] = 'CD'
    if any(n_list[-3] == x for x in (list_2)):
        n_list[-3] = 'D' + ('C'*(i_mult_c-5))
    if n_list[-3] == '9':
        n_list[-3] = 'CM'


    if any(n_list[-4] == x for x in (list_1)):
        n_list[-4] = 'M' * i_mult_m
    if n_list[-4] == '4':
        n_list[-4] = 'MṼ'
    if any(n_list[-4] == x for x in (list_2)):
        n_list[-4] = 'Ṽ' + ('M'*(i_mult_m-5))
    if n_list[-4] == '9':
        n_list[-4] = 'MẊ'


    if any(n_list[-5] == x for x in (list_1)):
        n_list[-5] = 'Ẋ' * i_mult_xalt
    if n_list[-5] == '5':
        n_list[-5] = 'ẊĹ'
    if any(n_list[-5] == x for x in (list_2)):
        n_list[-5] = 'Ĺ' + ('Ẋ'*(i_mult_xalt))
    if n_list[-5] == '9':
        n_list[-5] = 'ẊĆ'


    if any(n_list[-6] == x for x in (list_1)):
        n_list[-6] = 'Ć' * i_mult_calt
    if n_list[-6] == '4':
        n_list[-6] = 'ĆḊ'
    if any(n_list[-6] == x for x in (list_2)):
        n_list[-6] = 'Ḋ' + ('Ć'*(i_mult_calt))
    if n_list[-6] == '9':
        n_list[-6] = 'ĆḾ'


    if any(n_list[-7] == x for x in ('1','2','3','4','5','6','7','8','9')):
        n_list[-7] = 'Ḿ' * i_mult_malt
    



        
        
    
    #print(n_list)
    n_list_no_zero = n_list.remove('0')

    n_str_new = "".join(n_list)
    print(n_str_new)


for i in range(10000000):
    num_to_rome_v2(i)
