# Copyright (c) 2014 University of California, Davis
# 
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from latent_tax_assumption import *

global config

config = {
    "reasonerDir" : "",
    "reasonerTimeout" :  10,
    "inputLocation" : "",
    "outputDir" : "",
    "inputDir" : "",
    "htmlDir" : "..",
    "inputType" : "",
    "outputType" : "text",
    "outputFile" : "console",
    "taxonomies" : [],
    "species" : [],
    "goals" : [],
    "ltaList" : [],
    "goalTypes" : [],
    "goalRelations" : ["includes","equals","disjoint","overlaps","is_included_in"],
    "ltaString" :"",
    "compression" : False,
    "memory" : False,
    "ltas" :LatentTaxAssumption(),
    "uncertaintyRed" : False,
    "pw" : False,
}



