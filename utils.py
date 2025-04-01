import iconv
import re

def program_name_to_filename(program_name):
    # First iconv UTF-8 -> ASCII//TRANSLIT
    cvt = iconv.open('ASCII//TRANSLIT', 'UTF-8')
    name_iconv = cvt.iconv(program_name.encode('utf-8'))
    # Lowercase
    name_lower = name_iconv.decode('ascii').lower()
    # Remove illegal characters
    name_clean = re.sub(r'[^a-z0-9-]', '', name_lower)

    return name_clean
