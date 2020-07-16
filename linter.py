"""This module exports the Solhint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Solhint(NodeLinter):
    """Solhint class delegate call to solhint tool and return result back."""

    cmd = 'solhint -f stylish '
    regex = r'^\s+(?P<line>\d+):(?P<col>\d+)\s+((?P<error>error)|(?P<warning>warning))\s+(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'solidity'
    error_stream = util.STREAM_BOTH
    defaults = {
        'selector': 'source.solidity'
    }
