def long_repeat(line):
    new_dict={}
    s_count=0
    prev_symbol=''
    if line  == '':
        return 0
    else:
      new_list =list(line)
      for i,item in enumerate(new_list):
          if prev_symbol!='':
              if item == prev_symbol:
                  s_count+=1
                  new_dict[item]=s_count+1
              else:
                  s_count=0
          prev_symbol=item
    if  bool(new_dict):
        return max(new_dict.values())
    else:
        return 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')