import pandas as pd


class AvitoParser:

    def __init__(self, filepath):
        self.filepath = filepath

    def get_price_list_from_file(self) -> list:
        print("========", len(self.filepath) * "=", "========")
        print("========", self.filepath, "========")
        print("========", len(self.filepath) * "=", "========")

        all_strings = []

        try:
            with open(self.filepath, encoding='utf-8') as file:
                all_strings = file.readlines()
        except FileNotFoundError:
            print("Невозможно открыть ресурс")
        except:
            print("Ошибка при работе с ресурсом")

        strings_in_pane = self.trim_usefull_info(all_strings)

        list_of_prices_not_cut = str(strings_in_pane).split('itemProp="price" content="')
        list_of_prices = [x.split('"')[0] for x in list_of_prices_not_cut][1:]

        print("Количество лотов в файле:", len(list_of_prices))
        print("Сырые цены:", list_of_prices)

        return [int(x) for x in list_of_prices]

    def trim_usefull_info(self, all_strings):
        # Поиск начала фрагмента
        for n, x in enumerate(all_strings):
            # if x.find('<div class="items-items-kAJAg items-gallery-UDPbE" data-marker="catalog-serp">') > -1:
            if x.find('<div class="items-items-kAJAg') > -1:
                # print("Начало фрагмента: " + str(n))
                strings_in_pane = all_strings[n:]
                break
        # Поиск конца фрагмента
        for n, x in enumerate(strings_in_pane):
            if x.find('<div class="items-items-kAJAg">') > -1:
                # print("Конец фрагмента: " + str(n))
                strings_in_pane = strings_in_pane[0:n]
                break
        return strings_in_pane

