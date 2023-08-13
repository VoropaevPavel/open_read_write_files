with open('recipes.txt', encoding="utf-8") as f:
    cook_book = {}
    for line in f.read().split('\n\n'):
        name, _, *args = line.split('\n')
        d = []
        for arg in args:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
            d.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[name] = d

print(f'cook_book = {cook_book}')
#
# # result = {}
# # def get_shop_list_by_dishes(dishes, person_count):
# #     for dish in dishes:
# #         if dish in cook_book:
# #             for ingredients in cook_book[dish]:
# #                 if ingredients['ingredient_name'] in result:
# #                     result[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
# #                 else:
# #                     result[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': int(ingredients['quantity']) * person_count}
# #
# # get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# # print(result)
#
# import  os
# all_texts = [text_name for text_name in os.listdir() if text_name[0].isdigit()]
#
# def read_write_file(all_texts):
#     files_dict = {}
#     for element in all_texts:
#         with open(element, encoding='utf-8') as text:
#             text = text.read().strip()
#             length_of_text = len(text.split('\n'))
#             files_dict.setdefault(element, [])
#             files_dict[element].extend((length_of_text, text))
#
#     files_dict = dict(sorted(files_dict.items(), key=lambda x: x[1][0]))
#     for key, value in files_dict.items():
#         with open('file_homework.txt', 'a', encoding='utf-8') as file:
#             file.write(f"{key}\n"
#                        f"{value[0]}\n"
#                        f"{value[1]}\n\n"
#                        )
#
# read_write_file(all_texts)