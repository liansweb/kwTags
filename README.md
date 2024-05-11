# kwTags
实现keywords与Web攻击的对应关系

## 解释
对于Url，通过正则匹配，提示keywords与Web攻击的对应关系。
```
    例如：path ==> lfi, download_any_file, directory_traversal
```

## 功能
- [ ] 实现为`BurpSuite`插件 
- [ ] 针对`Tags`给出测试方法
- [ ] 针对`Tags`提供可配合攻击链
- [ ] 补充`Keywords`识别种类
- [ ] 补充`Keywords`识别方法（keys匹配+value特征匹配）

## TODO

- [ ] 论证实用性

## 示例
```python
{
	'/include/thumb.php': {
		'keys': ['dir'],
		'tags': []
	},
	'/api/geojson': {
		'keys': ['url'],
		'tags': ['download_any_file', 'rfi', 'directory_traversal']
	},
	'/common/download/resource': {
		'keys': ['resource'],
		'tags': []
	},
	'/remote/fgt_lang': {
		'keys': ['lang'],
		'tags': []
	},
	'/server/node_upgrade_srv.js': {
		'keys': ['action', 'firmware'],
		'tags': []
	},
	'/download.do': {
		'keys': ['file'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/seeyon/webmail.do': {
		'keys': ['method', 'filename', 'filePath'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/public/index.php/material/Material/_download_imgage': {
		'keys': ['media_id', 'picUrl'],
		'tags': []
	},
	'/backup/auto.php': {
		'keys': ['password', 'path'],
		'tags': ['lfi', 'ssrf', 'download_any_file', 'directory_traversal']
	},
	'/rewrite': {
		'keys': ['x'],
		'tags': []
	},
	'/': {
		'keys': ['file'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/NCFindWeb': {
		'keys': ['service', 'filename'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/prod-api/common/download/resource': {
		'keys': ['name'],
		'tags': ['lfi', 'download_any_file']
	},
	'/hrm/hrm_e9/orgChart/js/jquery/plugins/jqueryFileTree/connectors/jqueryFileTree.jsp': {
		'keys': ['dir'],
		'tags': []
	},
	'/+CSCOT+/oem-customization': {
		'keys': ['app', 'type', 'platform', 'resource-type', 'name'],
		'tags': ['lfi', 'download_any_file']
	},
	'/onecluster.jsp': {
		'keys': ['cluster', 'timestamp', 'isTMP'],
		'tags': []
	},
	'/systemLog/downFIle.php': {
		'keys': ['_JD_ID', 'fileName'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/e-mobile/App/Init.php': {
		'keys': ['weiApi', 'sessionkey', 'm'],
		'tags': []
	},
	'/i3geo/exemplos/codemirror.php': {
		'keys': ['page'],
		'tags': ['directory_traversal']
	},
	'/wp-json/lp/v1/courses/archive-course': {
		'keys': ['template_pagination_path'],
		'tags': ['lfi', 'ssrf', 'download_any_file', 'directory_traversal']
	},
	'/wp-content/plugins/usc-e-shop/functions/progress-check.php': {
		'keys': ['progressfile'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/events': {
		'keys': ['a'],
		'tags': []
	},
	'/index.php': {
		'keys': ['q'],
		'tags': []
	},
	'/wxjsapi/saveYZJFile': {
		'keys': ['fileName', 'downloadUrl'],
		'tags': ['lfi', 'download_any_file', 'ssrf', 'rfi', 'directory_traversal']
	},
	'/photo/combine.php': {
		'keys': ['type', 'g'],
		'tags': []
	},
	'/include/js/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/libs/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/lib/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/min/index.php': {
		'keys': ['f'],
		'tags': []
	},
	'/minify/min/index.php': {
		'keys': ['f'],
		'tags': []
	},
	'/libs/js/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/lib/js/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/js/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/contrib/extjs//examples/feed-viewer/feed-proxy.php': {
		'keys': ['feed'],
		'tags': ['ssrf', 'rfi']
	},
	'/ui/vcav-bootstrap/rest/vcav-providers/provider-logo': {
		'keys': ['url'],
		'tags': ['download_any_file', 'rfi', 'directory_traversal']
	},
	'/render': {
		'keys': ['url'],
		'tags': ['download_any_file', 'rfi', 'directory_traversal']
	}
}
```
