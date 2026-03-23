Analyze the job posting. Take the skills section and remove elements in the items sections that are the least applicable. Output JSON in the same format as the input JSON.

 - Do not change the ordering of the sections.
 - Do not change the order of the items.
 - Do not change the wording of the items.
 - Only change the "items" section by removing elements that are not applicable.
 - Each section must have at least 2 items, and at most 3.

# Job posting
{{ job_posting }}

# Skills
{{ skills }}
