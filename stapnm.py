import sys
from os import listdir
import re

nidrsh = open('nidrsh.html').read()

for fn in listdir('prkrnani'):
	with open('prkrnani/' + fn) as f:
		with open(sys.argv[1] + '/' + fn + '.html', 'w') as of:
			lekym = nidrsh

			s = ('' if fn == 'index' else f'<h2>{fn}</h2>') + f.read()
			for l in re.findall('\([^\)]*\)', s):
				ln = l[1:-1].replace(' ', '').split(',')
				href, ls = (ln[1], '↗') if '.' in ln[1] else (ln[1] + '.html', '')
				s = s.replace(l, f'<a href="{href}">{ln[0] + ls}</a>')

			for r in [['प्र॒क॒र॒ण॒ना॒म', 'स्व॒र॒बो॒धः' + ('' if fn == 'index' else ' | ' + fn)], ['त॒त्त्वम्', s]]:
				lekym = lekym.replace('[' + r[0] + ']', r[1])
			of.write(lekym)