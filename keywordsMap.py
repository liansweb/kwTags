import re


KEYWORDS = {
    re.compile(r'[\w]*down[\w]*'): {'tags': [ 'download_any_file', 'directory_traversal']},
    re.compile(r'[\w]*file[\w]*'): {'tags': [ 'lfi', 'ssrf','rfi', 'download_any_file', 'directory_traversal']},
    re.compile(r'[\w]*path[\w]*'): {'tags': [ 'lfi', 'ssrf','download_any_file', 'directory_traversal']},
    re.compile(r'[\w]*page[\w]*'): {'tags': [ 'directory_traversal']},
    re.compile(r'[\w]*url[\w]*'): {'tags': [ 'rfi', 'download_any_file', 'directory_traversal']},
    re.compile(r'[\w]*feed[\w]*'): {'tags': [ 'rfi','ssrf']},
    re.compile(r'[\w]*name[\w]*'): {'tags': [ 'lfi','download_any_file']},
}

