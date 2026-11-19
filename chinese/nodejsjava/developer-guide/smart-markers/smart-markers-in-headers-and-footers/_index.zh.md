---
title: 页眉和页脚中的智能标记 | Aspose.Cells for Node.js via Java
linktitle: 页眉和页脚智能标记 | Aspose.Cells for Node.js via Java
description: 在 Aspose.Cells for Node.js via Java 中，使用双尖括号语法和 WorkbookDesigner.setEnableHeaderFooterMarkers 开关，将 Smart Marker 占位符放置在页眉和页脚中，使用 JSON 数据源，并通过 data URI 绑定图片。
keywords: Aspose.Cells for Node.js via Java, 智能标记, 页眉, 页脚, 页眉页脚标记, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, JSON 行, 数据绑定, 图片, data URI, JavaScript
type: docs
weight: 196
url: /zh/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
页眉和页脚通常包含报告元数据，例如报告标题、报告期间、作者和部门。当这些信息已经存在于用于填充工作簿的数据源中时，手动重复它们会导致不必要的重复。  
经典的 Smart Marker 语法 `&=Source.Field` 只能在工作表正文单元格中处理。如果通过 `PageSetup.setHeader` 或 `PageSetup.setFooter` 将经典标记放置在页眉或页脚中，它将保持原始文字，因为页眉页脚字符串不在 `WorkbookDesigner.process()` 扫描的工作表单元格网格中。  
从 **Aspose.Cells for Node.js via Java 26.11** 开始，`WorkbookDesigner.setEnableHeaderFooterMarkers` 设置（默认值为 `false`）使 `process()` 能够解析写在页眉页脚区域字符串中的 `<<Source.Field>>` 占位符。请在调用 `process()` 之前调用 `designer.setEnableHeaderFooterMarkers(true)`。页眉页脚占位符使用与正文标记相同的数据源。  
每个页眉和页脚包含三个可寻址的区段：
- 区段 `0` 为左侧区段。
- 区段 `1` 为中间区段。
- 区段 `2` 为右侧区段。
使用 `PageSetup.setHeader(int section, String value)` 和 `PageSetup.setFooter(int section, String value)` 来写入这些区段。处理完成后，使用 `PageSetup.getHeader(int section)` 和 `PageSetup.getFooter(int section)` 获取生成的文本。

{{% alert color="primary" %}}
诸如 `<<Source.Field>>` 的占位符会将字段值以文本形式插入区段字符串中。图片可通过 `(picture)` 后缀和 data-URI 值进行绑定。
{{% /alert %}}

## **使用 JSON 行数据启用页眉/页脚标记**
使用以下步骤在 **Aspose.Cells for Node.js via Java 26.11** 中使用 JSON 行数据解析页眉和页脚占位符：
1. 创建一个 `Workbook` 并使用 `workbook.getWorksheets().get(0)` 获取其第一个 `Worksheet`。
2. 使用 `PageSetup.setHeader` 和 `PageSetup.setFooter` 将 `<<Source.Field>>` 占位符写入所需的页眉和页脚区段。
3. 将行数据准备为 JSON 行对象数组，并选择一个与占位符使用的来源前缀相匹配的来源名称。例如，名为 `node` 的来源对应占位符 `<<node.Name>>`。在此平台上，传递给 `setDataSource` 的普通 JavaScript 对象和数组无法绑定——JSON 是受支持的表格形式。
4. 为该工作簿创建一个 `WorkbookDesigner`。
5. 在处理之前调用 `designer.setEnableHeaderFooterMarkers(true)`。
6. 使用 `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')` 附加 JSON。
7. 调用 `designer.process()`。
8. 处理完成后，占位符不再出现在页眉或页脚文本中。使用 `getHeader` 和 `getFooter` 获取生成的区段字符串。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **使用 JSON 数据源**
当报告数据已经以 JSON 形式可用时，只需一次 `setJsonDataSource` 调用即可为所有标记样式提供数据。调用 `WorkbookDesigner.setJsonDataSource(String name, String json)` 来附加数据源。  
`name` 参数是占位符使用的来源名称。例如，名称 `node` 对应占位符 `<<node.Company>>` 和 `<<node.Title>>`。  
直接将行数据传递给 `setJsonDataSource`：
- 支持行数组，例如包含一个或多个行对象的 JSON 数组。
- 也可以直接传递单个行对象。
- 不要在顶层使用命名键（如 `{"rows":[...]}`）包装行。此包装不是该工作流所期望的行导向输入格式。  
单个 JSON 数据源可以在同一次 `process()` 调用中填充两种标记样式。它既可以解析工作表正文单元格中的经典 `&=` 标记，又可以解析页眉页脚区段中的双尖括号 `<<>>` 占位符。仍需调用 `designer.setEnableHeaderFooterMarkers(true)` 才能解析页眉页脚占位符。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **开关和多行来源语义**
`setEnableHeaderFooterMarkers` 默认值为 `false`，该设置仅控制页眉页脚的 `<<Source.Field>>` 占位符。关闭开关时，`process()` 仍会解析正文中的经典 `&=` 标记，但页眉或页脚中的 `<<Source.Field>>` 占位符将保持原始文字。  
页眉或页脚区段是一个字符串，而不是重复的带状区域。如果数据源包含多行，则第一行提供页眉和页脚的值。解析后，这些值成为普通的页眉或页脚文本。调用 `save` 后，它们仍保存在工作簿中，重新加载保存的工作簿时依然存在。  
以下示例使用相同的多行 JSON 数据源创建两个工作簿，以对比关闭和启用时的行为。`plainDesigner` 保持占位符不变，而 `enabledDesigner` 则使用第一行进行解析。

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **在页眉或页脚中绑定图片**
`(picture)` 后缀可将图片绑定到页眉或页脚区段。使用 `<<node.logo(picture)>>` 在希望显示图片的位置写入占位符，并提供 data URI 形式的字段值——前缀为 `data:image/png;base64,`，后跟图片字节的 Base64 文本。缺少 `data:` 前缀的纯 Base64 字符串无法嵌入图片。  
1. 占位符被替换为 `&G`，即标准的页眉页脚图片代码。因为标记变成了区段字符串中的代码，它可以嵌入更长的文本中，例如 `Logo: <<node.logo(picture)>>`。  
2. 图片字节以媒体部件的形式嵌入工作簿，并附加到该工作表的页眉/页脚绘图层中，从而在打印时图片随页眉页脚一起打印。

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

打印出的 `&G` 是 Excel 在渲染页眉时解释的图片代码——`logo.png` 的字节现在存放在 `HeaderFooterPicture.xlsx` 中，图片会在代码位置打印出来。  
要使用页眉页脚智能标记，请使用 `setHeader` 和 `setFooter` 将 `<<Source.Field>>` 占位符写入左、中、右页眉或页脚区段。在调用 `process()` 之前调用 `designer.setEnableHeaderFooterMarkers(true)`，并通过 `designer.setJsonDataSource(name, json)` 提供值。使用 `getHeader` 和 `getFooter` 读取生成的区段。相同的数据源可在一次处理过程中为正文标记和页眉页脚占位符提供数据。使用带有 data-URI 值的 `(picture)` 后缀即可在区段中绑定图片。

## 相关文章
- [SmartMarker 单元格数组渲染](/cells/zh/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}