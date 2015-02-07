from __future__ import unicode_literals

"""Read the public suffix list and strip out comments and blank lines.

Bleach uses the public suffix list (see effective_tld_names.dat) from the
Mozilla project. The list is licensed under the Mozilla Public License. See the
file for details.

"""

import os
import six


def clean_tld(tld):
    if six.PY2:
        tld = tld.decode('utf-8')
    tld = tld.strip()
    if tld.startswith(('//', '!')):  # Comments and exclusions
        return None
    if tld.startswith('*'):  # Wildcards
        tld = tld.lstrip('*.')
    return tld


def get_tlds():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'effective_tld_names.dat')
    with open(path) as fp:
        raw_tlds = [clean_tld(tld) for tld in fp.readlines()]
    return [tld for tld in raw_tlds if tld]
