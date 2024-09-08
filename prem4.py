def minimize_ticket_price(ticket_price, k):
    stack = []
    n = len(ticket_price)

  
    for digit in ticket_price:
  
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    
    stack = stack[:-k] if k else stack


    final_price = ''.join(stack).lstrip('0')
    
 
    return final_price if final_price else '0'


ticket_price = input().strip()
k = int(input().strip())

print(minimize_ticket_price(ticket_price, k))