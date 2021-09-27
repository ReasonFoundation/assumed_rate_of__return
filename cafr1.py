import re
import glob

def clean_key(key):
    """ Clean the key words"""
    key = key.replace(',', '').replace('\n', ' ').replace('\t', ' ').replace('  ', ' ').strip()
    return key


def update_dict(dd, result, reverse=False):
    """ Update key - values extracted to a dictionary"""
    global all_keys
    for k, v in result:
        if reverse:
            k, v = v, k
        k = clean_key(k)
        all_keys.add(k)

        if k not in dd:
            dd[k] = [v]
        else:
            dd[k].append(v)
    return dd

all_dicts = []

# create a set
all_keys = set()

def get_inv_rate_return(textfolder):
    """Extracting the number of interest using regular expression with different keywords
    Return a dictionary """
    for filename in glob.glob(textfolder):
        text = open(filename).read()
        # split the whole text into lines
        lines = text.lower().strip().split('\n')
        lines = [x.strip() for x in lines]
        lines = [x for x in lines if len(x) > 0]

        for position, line in enumerate(lines):

            # keyword: investment rate of return
            result1 = re.findall(r"(investment\s*rate\s*of\s*return).*(\d+\.\d+).*%", line)
            result1b = re.findall(r"(investment\s*rate\s*of\s*return).*(\d+\.\d+).*percent", line)
            result1c = re.findall(r"(investment\s*rate\s*of\s*return).*\d+\.\d+.*(\d+\.\d+)", line)

            # keyword: net of (something) investment
            result2 = re.findall(r"(\d+\.\d+\s*%),?\s+(net\s*of.+investment)", line)
            result2b = re.findall(r"(\d+\.\d+\s*percent),?\s+.*(net\s*of.+investment)", line)
            result2c = re.findall(r"(net\s*of\s*investment).*(\d+\.\d+\s*percent)", line)

            # keyword: discount rate
            result3 = re.findall(r"(discount\s*rate).*\s*(\d+\.\d+\s*%)", line)
            result3b = re.findall(r"(discount\s*rate).*\s*(\d+\.\d+\s*percent)", line)

            # keyword: opeb plan
            result4 = re.findall(r"(\d+\.\d+\s*%).+(opeb\splan)", line)
            result4b = re.findall(r"(\d+\.\d+\s*percent).+(opeb\splan)", line)


            for result in (result1, result1b, result1c, result2, result2b, result2c, result3, result3b, result4, result4b):
                if result != []:
                    # get 2 lines before and 2 lines after the line that contains keywords
                    context = lines[position - 2: position + 2]
                    context = ' '.join(context)
                    filename = filename.replace('2020.txt', '')
                    dictdata = {
                        'file': filename,
                        'context': context
                    }

                    update_dict(dictdata, result1)
                    update_dict(dictdata, result1b)
                    update_dict(dictdata, result2, reverse=True)
                    update_dict(dictdata, result2b, reverse=True)
                    update_dict(dictdata, result2c)
                    update_dict(dictdata, result3)
                    update_dict(dictdata, result3b)
                    update_dict(dictdata, result4, reverse=True)
                    update_dict(dictdata, result4b, reverse=True)

                    all_dicts.append(dictdata)


    return(all_dicts)



result = get_inv_rate_return('MI2020/*.txt')

all_keys = ['file'] + list(all_keys) +['context']
with open('output1.csv', 'w') as f:
    f.write(','.join(all_keys) + '\n')
    for dd in result:
        tmp = []
        for k in all_keys:
            if k in dd:
                tmp.append(f'"{dd[k]}"')
            else:
                tmp.append('""')

        f.write(','.join(tmp) + '\n')



if __name__ == '__main__':
    pass


