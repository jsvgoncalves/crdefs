from os import listdir
from os.path import isfile, join

DIR = 'nodes'
OUTPUT = 'cr-defs.tex'
HEADER = "% !TEX root = main.tex\n\
\\newcommand{\\crnumfmt}[1]{(N = #1)}\n\
\\newcommand{\\crdefs}[2]{\n\
    \\IfEqCase{#1}{\n"
FOOTER = "    }[\\PackageError{crdefs}{Undefined option to crdefs: #1}{}]\n\
}\n"


def from_file(f_name):
    fs = []
    with open(f_name) as f:
        for l in f.readlines():
            # sometimes there's a special char in the beginning of the sentence
            # so `startswith()` doesn't work. regex tbi
            if 'Files\\\\' in l:
                fs.append(l[7:9])
    return fs


def main():
    files = [join(DIR, f) for f in listdir(DIR) if isfile(join(DIR, f))]
    o = []

    for f_name in files:
        d = {'name': f_name, 'files': from_file(f_name)}
        o.append(d)

    with open(OUTPUT, 'w') as f:
        f.write(HEADER)
        for data in o:
            f.write('      {{{}}}{{\\crnumfmt{{{}}}}} \n'.format(
                data['name'][6:-4],
                len(data['files'])))
        f.write(FOOTER)


if __name__ == '__main__':
    main()
