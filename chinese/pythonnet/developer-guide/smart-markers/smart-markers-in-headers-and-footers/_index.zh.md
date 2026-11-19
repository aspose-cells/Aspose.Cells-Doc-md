---
title: 页眉页脚中的智能标记 | Aspose.Cells for Python via .NET
linktitle: 页眉和页脚智能标记 | Aspose.Cells
description: 在 Aspose.Cells for Python via .NET 中，使用自定义 ICellsDataTable 实现或 JSON 数据源，并通过双尖括号语法和 WorkbookDesigner.enable_header_footer_markers 开关在页眉和页脚放置智能标记占位符，还可以通过数据 URI 绑定图片。
keywords: Aspose.Cells, 智能标记, 页眉, 页脚, 页眉页脚标记, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, 自定义数据表, 数据绑定, 图片, 数据 URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /zh/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
页眉和页脚通常包含报告元数据，如报告标题、报告期间、作者和部门。当这些信息已经存在于用于填充工作簿的数据源中时，手动重复输入会造成不必要的冗余。  
经典智能标记语法 `&=Source.Field` 只在工作表正文单元格中解析。如果通过 `page_setup.set_header` 或 `page_setup.set_footer` 在页眉或页脚中放置经典标记，它会保持为文字，因为页眉页脚字符串不在 `workbook_designer.process()` 扫描的工作表单元格网格内。  
从 **Aspose.Cells for Python via .NET 26.11** 开始，`workbook_designer.enable_header_footer_markers` 开关（默认 `False`）使 `process()` 能解析写在页眉页脚字符串中的 `<<Source.Field>>` 占位符——在调用 `process()` 前将其设为 `True`。页眉页脚占位符使用与正文标记相同的数据源。  
每个页眉和页脚包含三个可寻址的部分：
- 部分 `0` 为左侧部分。
- 部分 `1` 为居中部分。
- 部分 `2` 为右侧部分。  
使用 `page_setup.set_header(section, value)` 和 `page_setup.set_footer(section, value)` 写入这些部分。处理后，可通过 `page_setup.get_header(section)` 和 `page_setup.get_footer(section)` 获取完整文本。

{{% alert color="primary" %}}
`<<Source.Field>>` 之类的占位符会将字段值作为文本插入到相应的部分字符串中。使用 `(picture)` 后缀并提供数据-URI 值即可绑定图片。
{{% /alert %}}

## **使用自定义数据表启用页眉/页脚标记**
在 **Aspose.Cells for Python via .NET 26.11** 中，使用以下步骤通过自定义表格数据源解析页眉和页脚占位符：
1. 创建一个 `Workbook` 并获取索引为 `0` 的第一个 `Worksheet`。  
2. 使用 `page_setup.set_header` 和 `page_setup.set_footer` 在所需的页眉和页脚部分写入 `<<Source.Field>>` 占位符。  
3. 定义一个实现 `ICellsDataTable` 的小类，以公开表格行数据——列名、行数以及具有 `before_first()`、`next()` 和 `__getitem__` 索引器的游标——并使用与占位符前缀匹配的源名称。例如，源名称 `node` 对应占位符 `<<node.Name>>`。纯 Python 类或字典列表在此平台上无法绑定；必须使用 `ICellsDataTable` 实现的自定义对象作为数据源。  
4. 为工作簿创建一个 `WorkbookDesigner`。  
5. 在处理前将 `designer.enable_header_footer_markers` 设为 `True`。  
6. 使用 `designer.set_data_source("node", table)` 附加表格和源名称。  
7. 调用 `designer.process()`。  
8. 处理完成后，页眉或页脚文本中不再出现占位符。使用 `get_header` 和 `get_footer` 获取完整的部分字符串。

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **使用 JSON 数据源**
当报告数据已经是 JSON 格式时，可使用 JSON 替代自定义 `ICellsDataTable`。调用 `workbook_designer.set_json_data_source(name, json)` 来附加数据源。  
`name` 参数的作用与表格数据使用的源名称相同。例如，名称 `node` 对应占位符 `<<node.Company>>` 和 `<<node.Title>>`。  
直接向 `set_json_data_source` 传递行数据：
- 支持行数组，例如包含一个或多个行对象的 JSON 数组。  
- 也可以直接传递单个行对象。  
- 请勿将行包装在命名的顶层键下，如 `{"rows":[...]}`。此包装不是此工作流期望的行导向输入形状。  
同一个 JSON 源可以在同一次 `process()` 调用中同时填充两种标记样式。它能够解析工作表正文单元格中的经典 `&=` 标记以及页眉页脚部分中的双尖括号 `<<>>` 占位符。仍需启用 `enable_header_footer_markers` 才能解析页眉页脚占位符。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **开关与多行源语义**
`enable_header_footer_markers` 默认 `False`，该开关仅控制页眉页脚的 `<<Source.Field>>` 占位符。当开关关闭时，`process()` 仍会解析正文单元格中的经典 `&=` 标记，但页眉或页脚中的 `<<Source.Field>>` 占位符会保持为文字。  
页眉或页脚的每个部分是一段字符串，而非重复的带。若数据源包含多行，第一行提供页眉和页脚的值。解析后，这些值会成为普通的页眉或页脚文本。它们在调用 `save` 后仍保留在工作簿中，并在再次加载已保存的工作簿时仍然存在。  
下面的示例使用相同的多行表格数据源创建两个工作簿，以对比关闭和开启行为。`plain_designer` 保持占位符不变，而 `enabled_designer` 使用第一行解析占位符。

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **将图片绑定到页眉或页脚**
`(picture)` 后缀会将图像绑定到页眉或页脚的某个部分。写入 `<<node.logo(picture)>>` 来指示图像出现位置，并提供以数据 URI 形式的字段值——前缀为 `data:image/png;base64,`，后跟图像字节的 Base64 文本。仅提供 Base64 字符串而不含 `data:` 前缀无法嵌入图像。  
`process()` 完成后：
1. 占位符被替换为 `&G`，即标准的页眉页脚图片代码。因为标记成为部分字符串中的代码，它可以出现在更长文本中，如 `Logo: <<node.logo(picture)>>`。  
2. 图像字节作为媒体部件嵌入工作簿，关联到该工作表的页眉/页脚绘图层，因此在打印时图片会随页眉或页脚一起显示。

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

打印出的 `&G` 是 Excel 在渲染页眉时解释的图片代码——`logo.png` 的字节已存入 `HeaderFooterPicture.xlsx`，并在打印时替代代码显示为图像。  
要使用页眉页脚智能标记，在左、居中、右三个页眉或页脚部分使用 `set_header` 和 `set_footer` 写入 `<<Source.Field>>` 占位符。调用 `process()` 前，将 `WorkbookDesigner` 的 `enable_header_footer_markers` 设为 `True`，并通过 `set_data_source("node", table)`（自定义 `ICellsDataTable` 实现）或 `set_json_data_source(name, json)` 提供数据源。使用 `get_header` 和 `get_footer` 读取完成的部分。相同的数据源可在一次处理过程中同时为正文标记和页眉页脚占位符提供数据。通过在占位符后添加 `(picture)` 并提供数据-URI 值，可在部分中绑定图片。

## 相关文章
- [SmartMarker 单元格数组渲染](/cells/zh/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}