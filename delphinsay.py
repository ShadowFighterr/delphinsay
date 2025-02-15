def delphinsay(message):
    dolphin = r"""
    .
    .
    .
    Dolphin."""
    border_length = len(message) + 4
    top_border = "_" * border_length
    bottom_border = "-" * border_length

    # Build the text box
    text_box = f"""
{top_border}
< {message} >
{bottom_border}
"""

    print(text_box)
    print(dolphin)


delphinsay(input())
