import re

def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        content = "Error: Not found"
    else:
        content = file.read()
        file.close()
        with open(path) as f:
            content = f.read().strip('\n')
    finally:
        return content

def parse_template(text):
    '''
    function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
    using regex.
    '''

    regex = re.sub(r'({.*?})',"{}" ,text)
    result =re.findall(r'\{.*?\}', text)
    
    return regex,result

def merge(template,list):
    return template.format(*list)

if __name__ =='__main__':
    print(
    '''
    ****    *****   ****    ****    ****    ****    ****    ****    ****    ****    ****
    *                                                                                  *
    *   Welcome to Madlib Game, You will need to answer some question and just wait the result *
    *                                                                                  *             
    ****    *****   ****    ****    ****    ****    ****    ****    ****    ****    ****
    '''
    )

    text = read_template('madlib_cli/assets/file.txt')
    parse_new_text,res = parse_template(text)
    user_input=[]

    for x in range(res):
        message = input('Enter an {} :'.format(res[x]))
        user_input.append(message)
    final_res= parse_new_text.format(*user_input)
    print(final_res)
    
