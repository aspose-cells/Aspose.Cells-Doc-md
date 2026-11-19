---
title: 页眉和页脚中的智能标记 | Aspose.Cells .NET
linktitle: 页眉和页脚智能标记 | Aspose.Cells
description: 在页面页眉和页脚中放置 Smart Marker 占位符，使用双尖括号语法和 WorkbookDesigner.EnableHeaderFooterMarkers 开关，并通过 DataTable 或 JSON 数据源进行绑定，还可通过数据 URI 绑定图片，适用于 Aspose.Cells for .NET。
keywords: Aspose.Cells, 智能标记, 页眉, 页脚, 页眉页脚标记, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, 数据绑定, 图片, data URI, C#
type: docs
weight: 196
url: /zh/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
页面页眉和页脚通常包含报告元数据，例如报告标题、报告期间、作者和部门。当这些信息已经存在于用于填充工作簿的数据源中时，手动重复会产生不必要的冗余。
经典的 Smart Marker 语法 `&=Source.Field` 只在工作表主体单元格中处理。如果通过 `PageSetup.SetHeader` 或 `PageSetup.SetFooter` 在页眉或页脚中放置经典标记，它将保持为文字，因为页眉和页脚字符串不在 `WorkbookDesigner.Process()` 扫描的工作表单元格网格中。
自 **Aspose.Cells for .NET 26.11** 起，默认 `false` 的 `WorkbookDesigner.EnableHeaderFooterMarkers` 开关可使 `Process()` 解析写在页眉和页脚字符串中的 `<<Source.Field>>` 占位符——在调用 `Process()` 前将其设为 `true`。页眉和页脚占位符使用与正文标记相同的数据源。
每个页眉和页脚包含三个可寻址的部分：
- 部分 `0` 为左侧部分。
- 部分 `1` 为居中部分。
- 部分 `2` 为右侧部分。
使用 `PageSetup.SetHeader(int section, string value)` 和 `PageSetup.SetFooter(int section, string value)` 写入这些部分。处理后，使用 `PageSetup.GetHeader(int section)` 和 `PageSetup.GetFooter(int section)` 获取完成的文本。

{{% alert color="primary" %}}
类似 `<<Source.Field>>` 的占位符会将字段值以文本形式插入到部分字符串中。图片可通过 `(picture)` 后缀和 data-URI 值进行绑定。
{{% /alert %}}

## **使用 DataTable 启用页眉/页脚标记**
在 **Aspose.Cells for .NET 26.11** 中使用 `DataTable` 解析页眉和页脚占位符的顺序如下：
1. 创建 `Workbook` 并获取索引为 `0` 的首个 `Worksheet`。
2. 使用 `PageSetup.SetHeader` 和 `PageSetup.SetFooter` 将 `<<Source.Field>>` 占位符写入所需的页眉和页脚部分。
3. 创建一个表名与占位符使用的源前缀相匹配的 `DataTable`。例如，名为 `node` 的表对应占位符 `<<node.Name>>`。
4. 为工作簿创建 `WorkbookDesigner`。
5. 在处理之前将 `designer.EnableHeaderFooterMarkers` 设为 `true`。
6. 使用 `designer.SetDataSource(table)` 附加该表。
7. 调用 `designer.Process()`。
8. 处理完成后，页眉或页脚文本中不再出现占位符。使用 `GetHeader` 和 `GetFooter` 获取完成的部分字符串。

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **使用 JSON 数据源**
当报告数据已以 JSON 格式提供时，可使用 JSON 替代 `DataTable`。调用 `WorkbookDesigner.SetJsonDataSource(string name, string json)` 附加数据源。
`name` 参数的作用与 `DataTable` 的表名相同。例如，名称 `node` 对应占位符 `<<node.Company>>` 和 `<<node.Title>>`。
直接向 `SetJsonDataSource` 传递行数据：
- 支持包含一个或多个行对象的 JSON 数组。
- 也可直接传入单个行对象。
- 不要在顶层使用诸如 `{"rows":[...]}` 的命名键包装行。此包装不是此工作流期望的面向行的输入结构。
同一个 JSON 源可以在同一次 `Process()` 调用中同时为两种标记样式提供数据。它可以解析工作表主体单元格中的经典 `&=` 标记以及页眉和页脚部分中的 `<<>>` 占位符。仍需启用 `EnableHeaderFooterMarkers` 才能解析页眉和页脚占位符。

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **开关与多行源语义**
`EnableHeaderFooterMarkers` 默认 `false`，该开关仅控制页眉和页脚的 `<<Source.Field>>` 占位符。开关关闭时，`Process()` 仍会解析经典的 `&=` 正文标记，但页眉或页脚中的 `<<Source.Field>>` 占位符会保持为文字。
页眉或页脚部分是一个字符串，而不是可重复的带。若数据源包含多行，则第一行提供页眉和页脚的值。解析后，这些值会变为普通的页眉或页脚文本。保存工作簿后，它们仍然保留在工作簿中，重新加载时仍然可见。
下面的示例创建了两个工作簿，使用相同的多行 `DataTable`，以对比未启用和已启用的行为。`plainDesigner` 保持占位符不变，而 `enabledDesigner` 使用第一行进行解析。

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **将图片绑定到页眉或页脚**
`(picture)` 后缀可将图像绑定到页眉或页脚部分。写入 `<<node.logo(picture)>>` 指定图片出现的位置，并提供字段值为 data URI——即前缀 `data:image/png;base64,` 加上图像字节的 Base64 文本。没有 `data:` 前缀的纯 Base64 字符串不会嵌入图像。
`Process()` 后：
1. 占位符被替换为 `&G`，即标准的页眉和页脚图片代码。由于标记成为部分字符串中的代码，它可以嵌入更长的文本，例如 `Logo: <<node.logo(picture)>>`。
2. 图像字节作为媒体部件嵌入工作簿，附加到该工作表的页眉/页脚绘图层中，因此在打印时图片会随页眉或页脚一起打印。

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

打印出的 `&G` 是 Excel 在呈现页眉时解释的图片代码——`logo.png` 的字节现在位于 `HeaderFooterPicture.xlsx` 中，图像将替代代码显示在相应位置。
要使用页眉和页脚智能标记，请使用 `SetHeader` 和 `SetFooter` 将 `<<Source.Field>>` 占位符写入左、居中和右页眉或页脚部分。在调用 `Process()` 前将 `WorkbookDesigner` 的 `EnableHeaderFooterMarkers` 设为 `true`，并通过 `SetDataSource(DataTable)` 或 `SetJsonDataSource` 提供值。使用 `GetHeader` 和 `GetFooter` 读取完成的部分。相同的数据源可在一次处理过程中同时填充正文标记和页眉/页脚占位符。通过在字段后添加 `(picture)` 后缀并提供 data-URI 值，可将图像绑定到相应部分。

## 相关文档
- [SmartMarker 单元格数组渲染](/cells/zh/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}