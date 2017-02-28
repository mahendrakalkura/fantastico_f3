from __future__ import absolute_import, division, print_function

from ansible.plugins.lookup import LookupBase

__metaclass__ = type

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, terms, **kwargs):
        document_roots = []
        for term in terms:
            document_roots.append(term['document_root'])
        return self._flatten(document_roots)
