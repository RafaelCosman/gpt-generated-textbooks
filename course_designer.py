from agent_helper_functions import ask

def outliner(topic):
    query = f"""
Please outline the 6-12 top-level sections for a course on {topic}.
These points are numbered 1., 2., 3., etc.

Outline:

"""

    output = ask(query)
    print(f"Outliner output for topic {topic}:")
    print(output)

    return output

def suboutliner(topic, outline, section):
    query = f"""
We are designing a course on {topic}. The overall outline is:

{outline}

Your job is to write the outline for section {section}.
- This outline can include anywhere from 3-10 sub-points.
- These sub-points should be enumerated A., B., C., etc. and should not have sub-sub-points within them.

{section} Outline:

"""

    output = ask(query)
    print(f"\n{section}")
    print(output)

    return output

def writer(topic, outline, section, section_outline, subsection):
    query = f"""
We are designing a course on {topic}. The overall outline is:

{outline}

The outline for section {section} is

{section_outline}

Your job is to write subsection {subsection}.
- This subsection could be anywhere from a few paragraphs to several pages of text.
- Please include details, examples, and practice problems where appropriate.
- Please use markdown wherever you can, including code blocks (```js), bulleted lists (- item), enumerated lists (1. item), bold, italics, sub-sub-headings (### heading) and more.

{subsection} Content:

"""

    output = ask(query)
    print(f"\n## {subsection}\n")
    print(output)

    return output

# This function runs the other three
if __name__ == "__main__":
    topic = input("What topic would you like a textbook on? ")
    outline = outliner(topic)

    section_and_outlines = [(section, suboutliner(topic, outline, section)) for section in outline.splitlines()]

    for (section, section_outline) in section_and_outlines:
        print()
        print("#", section)
        print()
        written_texts = [(section, subsection, writer(topic, outline, section, section_outline, subsection)) for subsection in section_outline.splitlines()]
