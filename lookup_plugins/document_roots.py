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
        items = []
        for user in terms:
            for domain, document_root in user['domains_and_document_roots'].items():
                items.append({
                    'group': user['username'],
                    'owner': user['username'],
                    'path': document_root,
                })
        return self._flatten(items)
