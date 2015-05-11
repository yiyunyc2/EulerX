#! /usr/bin/env python

# Euler checker receives a Cleantax file as input
# and reports multiple roots per taxonomy, children with multiple parents, and unmatched leaves
# __author__ = "Parisa Kianmajd"
#__version__ = "1.0.1"


import wizardParser


def main(iFiles):
    inputData = list()
    taxonDict = dict()
    unmatched = dict()
    parents = list()
    leaves = list()
    errors = list()
    for f in iFiles:
        inputData += open(f).readlines()
    for line in inputData:
        if line.startswith('taxonomy'):
           g = line.split(" ")[1]
           if g not in taxonDict:
               taxonDict.update({g:{'parents':[], 'leaves': [], 'arts': []}})
        if line.startswith("("):
            elements = line[1:-2].split(" ")
            parents.append(elements[0])
            for e in elements[1:]:
                if e in leaves:
                    errors.append('Child with multiple parents in taxonomy ' + str(g) + ": " + str(e))
                else:
                    leaves.append(e)
        if line == "\n":
                taxonDict[g]['parents'] += list(set(parents) - set(leaves))
                taxonDict[g]['leaves'] += list(set(leaves) - set(parents))
                leaves = []
        if line.startswith("["):
            art = line[1:-2].split(" ")
            source = art[0].split('.')
            dest = art[2].split('.')
            taxonDict[source[0]]['arts'].append(source[1])
            taxonDict[dest[0]]['arts'].append(dest[1])

    for g in taxonDict:
        if len(taxonDict[g]['parents']) > 1:
            errors.append('Too many roots in taxonomy ' + str(g) + ": " + ', '.join(taxonDict[g]['parents']) + ".")

    for g in taxonDict:
        for c in taxonDict[g]['leaves']:
            if c not in taxonDict[g]['arts']:
                if g not in unmatched:
                    unmatched.update({g:[]})
                unmatched[g].append(c)

    for g in unmatched:
        if len(unmatched[g]) > 0:
            errors.append('There are unmatched leaves in taxonomy ' + str(g) + ": " + ', '.join(unmatched[g]) + ".")
    if len(errors) == 0:
        print "The input is valid"
    else:
        print "Errors in the input:"
        for e in errors:
            print e

# MAIN
if __name__ == '__main__':
    main(wizardParser.args.iFile)