import re

my_pattern = r"It's such a lovely day today.|Some weather we're having today, huh\?|Maybe today's just not my day."
my_regex = re.compile(my_pattern)
# Is there a actual regex pattern (instead of 3 different literals) that would match these, and more sentences?  Chat GPT doesn't think so and returned my solution to me as its own solution!
