import os
import subprocess

import pytest

from flanker import flanker


cwd = os.getcwd()
data_dir = 'tests/data'  # Test from project root

def run(cmd, cwd=cwd):  # Helper for CLI testing
    return subprocess.run(cmd,
                          cwd=cwd,
                          shell=True,
                          check=True,
                          universal_newlines=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)

def test_cli_blactxm():
	run('flanker -i RHB02-C01_4.fasta -g CTX-M', cwd=data_dir)
	run('rm RHB02-C01_4_blaCTX-M-55_1_1000_both_flank.fasta RHB02-C01_4.fasta_resfinder', cwd=data_dir)  # Tidy up
