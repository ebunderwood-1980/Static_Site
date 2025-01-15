


def split_blocks(markdown_text):
    split_text = markdown_text.split("\n\n")
    
    #Remove empty lines
    for row in split_text:
        if row == "" or row == "\n":
            split_text.remove(row)

    #Return stripped blocks   
    return list(map(lambda x: x.strip(), split_text))
    
