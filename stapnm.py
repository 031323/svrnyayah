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

anukrmni = []

def krmh(fn):
	for i, a in enumerate(anukrmni):
		if a[0] == fn:
			return i
	return -1

def anukrmh(fn):
	k = krmh(fn)
	if k == -1:
		with open('prkrnani/' + fn) as f:
			i = len(anukrmni)
			anukrmni.append([fn, ('' if fn == 'index' else f'<h3>{fn}</h3>') + f.read() + '<hr>'])
			for l in re.findall('\([^\)]*\)', anukrmni[i][1]):
				ln = [w.strip() for w in l[1:-1].split(', ')]
				href, ls = (ln[1], '↗') if '.' in ln[1] else (ln[1] + '.html', '')
				anukrmni[i][1] = anukrmni[i][1].replace(l, f'<a href="{href}">{ln[0] + ls}</a>')
				if not ls:
					anukrmni[anukrmh(ln[1])][1] += '' if fn == 'index' else f'<a href="{fn}.html">{fn}</a><br>'
		return i
	else:
		return k

anukrmh('index')

for a in anukrmni:
	fn = a[0]
	s = a[1]
	with open(stlm + '/' + fn + '.html', 'w') as of:
		lekym = nidrsh
		for r in [['प्र॒क॒र॒ण॒ना॒म', ('' if fn == 'index' else fn + ' | ') + 'स्व॒र॒न्या॒याः'], ['त॒त्त्वम्', s]]:
			lekym = lekym.replace('[' + r[0] + ']', r[1])
		of.write(lekym)