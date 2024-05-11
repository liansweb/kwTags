from keywordsMap import KEYWORDS

# 文件路径
file_path = 'urlExample.sample'


def read_file(file_path):
    """
    读取文件内容
    """
    with open(file_path, "r") as f:
        return f.read().splitlines()


class SplitQueryResult:
    """
    分析URL参数结果
    """
    def __init__(self, message='', code=0, parameters=''):
        self.message = message
        self.code = code
        self.parameters = parameters


def split_query(url):
    """
    分析URL参数
    """
    # 如果url中不存在'?'符号，则返回无参数的结果
    if '?' not in url:
        return SplitQueryResult('No parameters found', 404)
    else:
        # 如果url中存在'?'符号，则提取参数部分
        return SplitQueryResult('Parameters successfully extracted', 200, url.split('?', 1)[1])


class SplitQueryKeysResult:
    """
    分析URL参数键结果
    """
    def __init__(self, message='', code=0, keys=None):
        self.message = message
        self.code = code
        self.keys = keys or []


def split_query_keys(parameters):
    """
    分析URL参数键
    """
    # 如果参数字符串以'&'开头，则去掉开头的'&'
    if parameters.startswith('&'):
        parameters = parameters[1:]
    # 提取参数字符串中的所有键
    keys = [pair.split('=', 1)[0] for pair in parameters.split('&')]
    return SplitQueryKeysResult('Keys successfully extracted', 200, keys)


def key_map_tags(keys):
    """
    根据关键字映射标签
    """
    tags_found = set()
    for key in keys:
        for keyword_pattern, keyword_data in KEYWORDS.items():
            # 如果键与关键字模式匹配，则添加对应的标签
            if keyword_pattern.search(key):
                tags_found.update(keyword_data['tags'])
                break
    return list(tags_found)


def main():
    """
    程序主函数
    """
    urls = read_file(file_path)
    url_tags_dict = {}
    for url in urls:
        # 分析URL参数
        query_result = split_query(url)
        # 如果参数分析失败，则跳过本次循环
        if query_result.code != 200:
            continue
        # 分析URL参数键
        keys_result = split_query_keys(query_result.parameters)
        # 根据参数键映射标签
        tags = key_map_tags(keys_result.keys)
        # 提取URL路径部分
        path = url.split('?', 1)[0]
        # 将URL路径与标签关联起来
        url_tags_dict[path] = {
            'keys':keys_result.keys,
            'tags':tags
        }

    print(url_tags_dict)


if __name__ == '__main__':
    main()

