import pytest

import uniplot.analysis
import uniplot.parse


TEST_UNIPROT="./resource/uniprot_sprot_small.xml.gz"

def test_average():
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 303
