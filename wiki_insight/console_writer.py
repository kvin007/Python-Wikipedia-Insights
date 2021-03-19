
def write_language_domain(langs_and_domains):
    print('Language and Domain count\n')
    print("Period\t\tLanguage\tDomain\t\tViewCount\n")
    for ld in langs_and_domains:
        print(f'{get_hour_format(ld[0])}\t\t{ld[1]}\t\t{ld[2]}\t\t{ld[3]}\n')
    print('\n')


def write_page_titles(page_titles):
    print('Language page max view count\n')
    print("Period\t\tPage\t\tViewCount\n")
    for pt in page_titles:
        print(f'{get_hour_format(pt[0])}\t\t{pt[1]}\t{pt[2]}\n')
    print('\n')


def get_hour_format(hour):
    h = int(hour)
    if h >= 13:
        return f'{h - 12}PM'
    elif h == 12:
        return '12AM'
    else:
        return f'{h}AM'
