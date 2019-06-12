# Copyright (C) 2012-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

class MainParams(bitcoin.core.CoreChainParams):
    MESSAGE_START = b'\x2d\x3f\xa2\xf5'
    DEFAULT_PORT = 51314
    RPC_PORT = 51315
    DNS_SEEDS = (('martexcoin.org', 'seed.martexcoin.org'),
                 ('martexcoin.org', 'seed1.martexcoin.org'),
                 ('martexcoin.org', 'seed2.martexcoin.org'),
                 ('martexcoin.org', 'seed3.martexcoin.org'),
                 ('martexcoin.org', 'seed4.martexcoin.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':50,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}

"""
class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x70\x35\x22\x05'
    DEFAULT_PORT = 41314
    RPC_PORT = 41315
    DNS_SEEDS = (('martexcoin.org', 'seed.martexcoin.org'),
                 ('martexcoin.org', 'seed1.martexcoin.org'),
                 ('martexcoin.org', 'seed2.martexcoin.org'),
                 ('martexcoin.org', 'seed3.martexcoin.org'),
                 ('martexcoin.org', 'seed4.martexcoin.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
"""
"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
#    elif name == 'testnet':
#        params = bitcoin.core.coreparams = TestNetParams()
#    elif name == 'regtest':
#        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
