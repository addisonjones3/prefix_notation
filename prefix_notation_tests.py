from prefix_notation import parse_prefix_expression

t0 = '1'  # 1
t1 = '* + 2 3 4'  # 20
t2 = '+ 9 * 2 6'  # 21
t3 = '* + 1 + + 2 3 4 + 5 + 6 7'  # 180
t4 = '/ 3 4'  # .75
comb = '1\n' \
       '* + 2 3 4\n' \
       '+ 9 * 2 6\n' \
       '* + 1 + + 2 3 4 + 5 + 6 7p \n' \
       '/ -3 + 4 5\n' \
       '- -1 1'

comb_same_line = '1\n* + 2 3 4\n+ 9 * 2 6\n* + 1 + + 2 3 4 + 5 + 6 7p \n/ -3 4\n- -1 1'

t_div_0 = '+ 1 1\n' \
          '/ 1 0\n' \
          '\n' \
          '* 3 2\n'

t_mult_0 = '* 2 0'

t_multi_space = '/ 2     2\n' \
                '+ 1   +  4   2'

t_all_issues = '1\n' \
               '* + 2 3 4\n' \
               '+ 9 * 2 6\n' \
               '* + 1 + + 2 3 4 + 5 + 6 7p \n' \
               '/ -3 + 4 5\n' \
               '- -1 1\n' \
               '/ 1 0\n' \
               '* 1 0\n' \
               '\n' \
               '+ + 1 1\n' \
               '+ 1b 2\n' \
               'A A A'

t_tab_delim = '+\t1\t2'

t_bad_char = '+ 1b 2'
t_bad_char2 = 'A 2 4'

# parse_prefix_expression(t0)
# parse_prefix_expression(t1)
# parse_prefix_expression(t2)
# parse_prefix_expression(comb)
# parse_prefix_expression(t0)
# parse_prefix_expression(comb)
# parse_prefix_expression(t_multi_space)
# parse_prefix_expression(t_bad_char2)
parse_prefix_expression(t_all_issues)
# parse_prefix_expression(t_tab_delim, token_delimiter='\t')