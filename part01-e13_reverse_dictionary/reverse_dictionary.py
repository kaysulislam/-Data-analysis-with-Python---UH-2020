#!/usr/bin/env python3

def reverse_dictionary(d):
    empty_dict = {}
    for key, value in d.items():
        for items in value:
            new_item = {items: [key]}
            if(items not in empty_dict.keys()):
                empty_dict.update(new_item)
            elif(items in empty_dict.keys()):
                empty_dict[str(items)].append(key)
    return empty_dict


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa',
                                         'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
