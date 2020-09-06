import sys
import os
import re
import shutil
from pathlib import Path

stlm = sys.argv[1]

stlpdm = Path(stlm)
if stlpdm.exists() and stlpdm.is_dir():
	shutil.rmtree(stlm)
os.mkdir(stlm)
shutil.copyfile('style.css', stlm + '/style.css')

nidrsh = open('nidrsh.html').read()

for fn in os.listdir('prkrnani'):
	with open('prkrnani/' + fn) as f:
		with open(stlm + '/' + fn + '.html', 'w') as of:
			lekym = nidrsh

			s = ('' if fn == 'index' else f'<h2>{fn}</h2>') + f.read()
			for l in re.findall('\([^\)]*\)', s):
				ln = l[1:-1].replace(' ', '').split(',')
				href, ls = (ln[1], '↗') if '.' in ln[1] else (ln[1] + '.html', '')
				s = s.replace(l, f'<a href="{href}">{ln[0] + ls}</a>')

			for r in [['प्र॒क॒र॒ण॒ना॒म', 'स्व॒र॒बो॒धः' + ('' if fn == 'index' else ' | ' + fn)], ['त॒त्त्वम्', s]]:
				lekym = lekym.replace('[' + r[0] + ']', r[1])
			of.write(lekym)