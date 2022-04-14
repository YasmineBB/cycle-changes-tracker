

        
def pain_exp():

    """
    Asks the user if they have experienced this level of pain before in order to log to the worksheet.
    """
    global pain_exp_before
    pain_exp_before = typingInput(Fore.LIGHTMAGENTA_EX + 'Have you experienced this level of pain before? Y/N \n\n' + Fore.RESET)
    # print(pain_exp_before)
    while True:
        
        if pain_exp_before == 'y' or pain_exp_before == 'Y' or pain_exp_before == 'n' or pain_exp_before == 'N':
          print('     ')
          typingPrint("Okay. We've logged this for you.\n\n")
          print(pain_exp_before)
          return on_period_flow_level()
          break
        else:
          typingPrint(f'{pain_exp_before} is not a valid input! Please enter either Y or N...\n\n')
          continue
        
    return pain_exp_before