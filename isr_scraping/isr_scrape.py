## -- IMPORTS

from bs4 import BeautifulSoup
import numpy as np
from urllib.requests import urlopen


## -- FUNCTIONS

def isr_author_list(url, isr_str, outfile):
    """ Writes a file of authors for each ISR.

    Parameters
    ----------
    url : str
        The url where the ISRs are located.
    isr_str : str
        The str used to isolate ISRs.
    outfile : str
        What to name the file written out.
    """

    html = ulropen(url).read()
    lines = BeautifulSoup(html, 'lxml').findAll('li')
    lines = [str(line) for lin in lines]
    isr_bool = [isr_str in line for line in lines]
    isrs = np.array(lines)[isr_bool]

    authors = [elem.split('<br/>')[-1].split('<span class="small_font")')[0] for elem in isrs]

    author_str_out = '\n'.join(authors)
    
    with open(outfile, 'w') as f:
        f.write(author_str_out)


