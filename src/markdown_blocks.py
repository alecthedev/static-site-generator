block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    return markdown.strip().split("\n\n")


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading

    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    if any(line.startswith(">") for line in lines):
        return block_type_quote

    if any(line.startswith("* ") for line in lines) or any(
        line.startswith("- ") for line in lines
    ):
        return block_type_unordered_list

    if block.startswith("1. "):
        line_num = 1
        for line in lines:
            if not line.startswith(f"{line_num}. "):
                break
            line_num += 1
        return block_type_ordered_list

    return block_type_paragraph
