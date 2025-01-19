import re

def split_blocks(markdown_text):
    split_text = markdown_text.split("\n\n")
    
    #Remove empty lines
    for row in split_text:
        if row == "" or row == "\n":
            split_text.remove(row)

    #Return stripped blocks   
    return list(map(lambda x: x.strip(), split_text))

def block_to_block_type(markdown_blocks):
    results = []
    for block in markdown_blocks:
        if re.search(r'^#{1,6}\s{1}[\s\w]+$', block, re.IGNORECASE):
            results.append('h')
        elif re.search(r'^`{3}[\s\S]*`{3}$', block, re.IGNORECASE):
            results.append('c')
        elif re.search(r'^(>.*)(\n>.*)*$', block, re.IGNORECASE):
            results.append('q')
        elif re.search(r'^[*|\-] .*(\n[*|\-] .*)*$', block, re.IGNORECASE):
            results.append('u')
        elif re.search(r'^(\d+)\. ', block):
            lines = block.split('\n')            
            print(lines)
            expected_number = 0
            for line in lines:
                match = re.match(r'^(\d+)\. ', line)
                if match:
                    current_number = int(match.group(1))
                    if current_number != expected_number + 1:
                        results.append(None)
                        break
                    expected_number = current_number
                else:
                    results.append(None)
                    break
            results.append('o')
        else:
            results.append(None)
    return results
        
# def main():
#     input = "1. First Item\n2. Second Item"
#     print(f"Result: {block_to_block_type([input])}")


# if __name__ == '__main__':
#     main()
