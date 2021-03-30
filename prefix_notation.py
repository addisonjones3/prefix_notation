def parse_prefix_expression(input_string, token_delimiter=' '):

    class ImproperExpression(Exception):
        pass

    class EmptyExpression(Exception):
        pass

    allowed_operators = ['*', '/', '+', '-']
    expression_lists = [s.split(token_delimiter) for s in input_string.split('\n')]

    for z, input_list in enumerate(expression_lists):
        list_len = len(input_list)

        try:
            if list_len == 1:
                if input_list[0] == '':
                    raise EmptyExpression
                else:
                    print(int(input_list[0]))
                continue

            int_count = 0
            op_count = 0
            input_list.reverse()
            processing_list = []

            for i, c in enumerate(input_list):
                if c == '':
                    continue
                elif c not in allowed_operators:
                    processing_list.insert(0, int(c))
                    int_count += 1
                    continue
                else:
                    op_count += 1

                if op_count == int_count:
                    raise ImproperExpression

                elif c == '+':
                    a = processing_list[0] + processing_list[1]

                elif c == '-':
                    a = processing_list[0] - processing_list[1]

                elif c == '*':
                    a = processing_list[0] * processing_list[1]

                elif c == '/':
                    a = float(processing_list[0]) / processing_list[1]

                if i == list_len - 1:
                    print(a)
                else:
                    processing_list = [a, *processing_list[2:]]

        # TODO error handling
        except EmptyExpression:
            print('Statement {0} is empty - passing'.format(z))
            continue
        except ImproperExpression:
            print('Statement {0} does not adhere to proper prefix notation syntax - passing'.format(z))
            continue
        except ZeroDivisionError:
            print('Attempted division by zero for statement {0} - passing'.format(z))
            continue


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        parse_prefix_expression(sys.argv[1])

    elif len(sys.argv) == 3:
        parse_prefix_expression(sys.argv[1], sys.argv[2])

    else:
        raise Exception
