import re

def split_blocks(markdown_text):
    split_text = markdown_text.split("\n\n")
    
    #Remove empty lines
    for row in split_text:
        if row == "" or row == "\n":
            split_text.remove(row)

    #Return stripped blocks   
    return list(map(lambda x: x.strip(), split_text))

def block_to_block_type(block):
    if re.search(r'^#{1,6}\s{1}[\s\w]+$', block, re.IGNORECASE):
        return('heading')
    if re.search(r'^`{3}[\s\S]*`{3}$', block, re.IGNORECASE):
        return('code')
    if re.search(r'^(>.*)(\n>.*)*$', block, re.IGNORECASE):
        return('quote')
    if re.search(r'^[*-] .*(\n[*-] .*)*$', block, re.IGNORECASE):
        return('unordered list')
    if re.search(r'^(\d+)\. ', block):
        lines = block.split('\n')            
        expected_number = 1
        for line in lines:
            match = re.match(r'^(\d+)\. ', line)
            if match:
                current_number = int(match.group(1))
                if current_number != expected_number:
                    return('normal')
                expected_number = current_number + 1
            else:
                return('normal')
        return('ordered list')
    return('normal')
        
# def main():
#     input = "1. First item\n2. Second item"
#     print(f"Result: {block_to_block_type(input)}")


# if __name__ == '__main__':
#     main()
