---
title: 页眉和页脚中的智能标记 | Aspose.Cells for Python via Java
linktitle: 页眉和页脚智能标记 | Aspose.Cells
description: 在 Aspose.Cells for Python via Java 中，使用双尖括号语法和 WorkbookDesigner.setEnableHeaderFooterMarkers 开关，将 Smart Marker 占位符放置在页面页眉和页脚中，使用表格行或 JSON 数据源，并通过数据 URI 绑定图片。
keywords: Aspose.Cells, Aspose.Cells for Python via Java, 智能标记, 页眉, 页脚, 页眉页脚标记, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, 自定义数据表, 数据绑定, 图片, data URI, Python via Java
type: docs
weight: 196
url: /zh/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
页面页眉和页脚通常包含报告元数据，如报告标题、报告期间、作者和部门。当这些信息已经存在于用于填充工作簿的数据源中时，手动重复会导致不必要的冗余。  
经典的 Smart Marker 语法 `&=Source.Field` 仅在工作表主体单元格中处理。如果通过 `PageSetup.setHeader` 或 `PageSetup.setFooter` 在页眉或页脚中放置经典标记，它将保持为字面文本，因为页眉和页脚字符串不在 `WorkbookDesigner.process()` 扫描的工作表单元格网格中。  
从 **Aspose.Cells for Python via Java 26.11** 开始，`WorkbookDesigner.setEnableHeaderFooterMarkers` 开关（默认 `False`）使 `process()` 能解析写在页眉和页脚字符串中的 `<<Source.Field>>` 占位符——在调用 `process()` 之前将其设为 `True`。页眉和页脚占位符使用与主体标记相同的数据源。  

每个页眉和页脚包含三个可寻址的节：  
- 节 `0` 是左侧节。  
- 节 `1` 是居中节。  
- 节 `2` 是右侧节。  

使用 `PageSetup.setHeader(int section, str value)` 和 `PageSetup.setFooter(int section, str value)` 写入这些节。处理完成后，使用 `PageSetup.getHeader(int section)` 和 `PageSetup.getFooter(int section)` 获取完整的文本。

{{% alert color="primary" %}}
占位符例如 `<<Source.Field>>` 会将字段值作为文本插入到节字符串中。图片可通过 `(picture)` 后缀和 data-URI 值进行绑定。
{{% /alert %}}

## **使用自定义数据表启用页眉/页脚标记**
在 **Aspose.Cells for Python via Java 26.11** 中，使用以下步骤解析页眉和页脚占位符：  
1. 创建 `Workbook` 并使用 `workbook.getWorksheets().get(0)` 获取索引为 `0` 的第一个 `Worksheet`。  
2. 使用 `worksheet.getPageSetup().setHeader(section, value)` 和 `worksheet.getPageSetup().setFooter(section, value)` 将 `<<Source.Field>>` 占位符写入所需的页眉和页脚节。  
3. 定义一个实现 `ICellsDataTable` 的小类，以公开表格行数据——列名、行数以及具有 `beforeFirst()`、`next()` 和 `get()` 的游标，并使用与占位符前缀匹配的源名称。例如，名为 `node` 的源对应占位符 `<<node.Name>>`。普通 Python 类或字典列表在此平台上 **无法** 绑定；`ICellsDataTable` 实现才是自定义对象数据源。  
4. 为工作簿创建 `WorkbookDesigner`。  
5. 在处理之前调用 `designer.setEnableHeaderFooterMarkers(True)`。  
6. 使用 `designer.setDataSource("node", table)` 附加表格并指定源名称。  
7. 调用 `designer.process()`。  
8. 处理完成后，页眉或页脚文本中已不再出现占位符。使用 `worksheet.getPageSetup().getHeader(section)` 和 `worksheet.getPageSetup().getFooter(section)` 读取完整的节字符串。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **使用 JSON 数据源**
当报告数据已经是 JSON 格式时，可使用 JSON 代替自定义 `ICellsDataTable`。调用 `designer.setJsonDataSource(name, json)` 附加源。  
`name` 参数的作用与表格数据使用的源名称相同。例如，名称 `node` 对应占位符 `<<node.Company>>` 和 `<<node.Title>>`。  
直接将行数据传递给 `setJsonDataSource`：  
- 支持行数组，如包含一个或多个行对象的 JSON 数组。  
- 也可以直接传递单个行对象。  
- 请勿将行包装在命名的顶层键下，例如 `{"rows":[...]}`。此包装不是此工作流期望的面向行的输入形状。  

同一个 JSON 源可以在同一次 `process()` 调用中同时填充两种标记样式。它既可以解析工作表主体单元格中的经典 `&=` 标记，也可以解析页眉和页脚节中的双尖括号 `<<>>` 占位符。仍需启用 `setEnableHeaderFooterMarkers` 才能解析页眉和页脚占位符。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **开关和多行源语义**
页眉和页脚标记开关默认是 `False`，`designer.setEnableHeaderFooterMarkers(True)` 仅控制页眉和页脚的 `<<Source.Field>>` 占位符。当开关关闭时，`process()` 仍会解析经典 `&=` 主体标记，但页眉或页脚中的 `<<Source.Field>>` 占位符仍为字面文本。  
页眉或页脚节是一个字符串，而不是可重复的段。若数据源包含多行，第一行提供页眉和页脚的值。解析后，这些值成为普通的页眉或页脚文本。保存工作簿 (`workbook.save(...)`) 后，它们仍然保存在工作簿中，重新加载时仍然存在。  
下面的示例创建了两个工作簿，使用相同的多行表格数据源，以对比关闭和开启行为。`plainDesigner` 保持占位符不变，而 `enabledDesigner` 使用第一行解析它。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **在页眉或页脚中绑定图片**
`(picture)` 后缀可将图片绑定到页眉或页脚节。写入 `<<node.logo(picture)>>` 并提供字段值为 data URI——前缀 `data:image/png;base64,` 后跟图片字节的 Base64 文本。解码后的图片会作为 `byte[]` 数组处理。没有 `data:` 前缀的纯 Base64 字符串无法嵌入图片。  
`process()` 之后：  
1. 占位符被替换为 `&G`，即标准的页眉和页脚图片代码。因为标记变成了节字符串中的代码，它可以位于更长的文本中，例如 `Logo: <<node.logo(picture)>>`。  
2. 图片字节作为媒体部件嵌入工作簿，附加到该工作表的页眉/页脚绘图层上，因而在打印时图片会随页眉或页脚一起打印。

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

打印出的 `&G` 是 Excel 在渲染页眉时解释的图片代码——`logo.png` 的字节现在位于 `HeaderFooterPicture.xlsx` 中，图片会在代码位置显示。  
要使用页眉和页脚智能标记，只需使用 `setHeader` 和 `setFooter` 将 `<<Source.Field>>` 占位符写入左、中、右节。调用 `designer.setEnableHeaderFooterMarkers(True)` 再调用 `process()`，并通过 `designer.setDataSource("node", table)`（自定义 `ICellsDataTable` 实现）或 `designer.setJsonDataSource(name, json)` 提供值。使用 `getHeader` 与 `getFooter` 读取完成的节。相同的数据源可以在一次处理过程中同时填充主体标记和页眉/页脚占位符。通过 `(picture)` 后缀加上 data-URI 值，可将图片绑定到节中。

## 相关文章
- [SmartMarker 单元格数组渲染](/cells/zh/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}