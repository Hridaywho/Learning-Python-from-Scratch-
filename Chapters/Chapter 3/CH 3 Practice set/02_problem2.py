letter = ''' Dear <|name|>,
            You are selected!       
            <|Date|>'''

print(letter.replace("<|name|>", "Harry").replace("<|Date|>", "24 September 2050"))

# output
# Dear Harry,
#          You are selected!       
#           24 September 2050           