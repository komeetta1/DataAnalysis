import re

import re
str = """He is the president of Russia.
He’s a powerful man1."""
str = """He is the president of Russia.
He’s a powerful man2."""
newstr = re.sub(r'(\b[Hh]e\b)', r'\1 (Putin)', str, 2)
print (newstr)