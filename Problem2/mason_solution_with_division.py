def get_product_other_elements(list):
    total_product = 1
    new_list = []
    for num in list:
        total_product = total_product*num
    for num in list:
        new_num = total_product/num
        new_list.append(new_num)
    return new_list

get_product_other_elements(int_array)
