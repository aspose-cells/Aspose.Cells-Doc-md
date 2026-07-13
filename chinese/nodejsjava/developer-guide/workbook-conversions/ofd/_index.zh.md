---
title: 将 Excel 转换为 OFD 格式
linktitle: 将 Excel 转换为 OFD 格式
description: Aspose.Cells for Node.js via Java 是一个用于处理电子表格文件的电子表格库，支持将 Excel 工作簿转换为 OFD（Open Fixed-layout Document，开放版式文档）格式。本文演示了如何创建 Excel 内容并将其导出为 OFD，以及如何使用 Aspose.Cells 将现有的 Excel 文件转换为 OFD。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, Excel 转 OFD, OFD 转换, SaveFormat.Ofd, 固定版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值将 Excel 工作簿直接转换为 OFD（Open Fixed-layout Document，开放版式文档）格式。生成的 OFD 文档保留了工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框以及数字格式。这使得 Aspose.Cells 适用于需要固定版式输出的归档、打印、监管申报以及政府提交等工作流程。

{{% /alert %}}
## **简介**
OFD（Open Fixed-layout Document，开放版式文档）是中国用于以固定、基于页面的版式表示数字文档的国家标准（GB/T 33190-2016）。在源文档的视觉外观必须与原始所见完全一致的使用场景中，它扮演着与 PDF 类似的角色。OFD 在中华人民共和国的政府提交、监管申报、电子发票以及长期归档等领域被广泛采用。

在需要将电子表格内容作为只读的、版式锁定的文档分发（而非可编辑的电子表格）的场景中，将 Excel 工作簿转换为 OFD 是一项常见需求。例如，向客户发送最终发票、归档季度财务报告，或将预算电子表格提交给监管机构。Aspose.Cells 通过 `SaveFormat.Ofd` 枚举值满足这一需求，可将工作簿直接写入 OFD，无需中间转换步骤。OFD 输出保留了工作簿中的单元格值、合并区域、字体、颜色、边框、数字格式以及页面设置选项。

{{% alert color="primary" %}}

Aspose.Cells 生成的 OFD 输出保留了源工作簿的可见布局，包括单元格内容、合并单元格、列宽以及行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会在固定版式输出中呈现。在工作表上配置的页面设置选项（例如纸张大小、方向以及打印区域）会影响生成的 OFD 文档的版式。

{{% /alert %}}
## **创建 Excel 工作簿并保存为 OFD**
Aspose.Cells 允许您通过编程方式构建工作簿，向其中填充数据，然后使用 `SaveFormat.Ofd` 枚举直接将其保存为 OFD 格式。下面的示例从头开始创建一张发票。它添加了公司徽标、抬头信息、收票方信息、明细项目以及计算出的合计金额，然后将工作簿导出为 OFD 文档。
### **构建带徽标的发票**
该示例通过在左上角插入徽标图像来构建发票工作表，填充公司名称和联系方式，在合并的单元格中添加"INVOICE"（发票）标题，记录发票编号和日期，列出收票方客户，构建包含描述、数量、单价和合计列的明细项目表，并使用单元格公式计算小计、税金和总计。通过 `Style` 和 `Font` 对象应用粗体标题、价格货币格式、边框以及列宽等格式。最后，使用 `SaveFormat.Ofd` 将工作簿以 `.ofd` 扩展名保存。

```javascript
let dataDir = "C:\\Temp\\";

// Create a new Workbook
let workbook = new AsposeCells.Workbook();

// Obtain the first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Set column widths
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Line items header
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Currency style with borders
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Plain border style for description/quantity cells
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Line items rows
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Bold + currency style for total values
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Bold style for total labels
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **将现有的 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘加载现有的 Excel 工作簿，并将其直接导出为 OFD 格式。这对于批量转换流水线、归档工作流程以及源工作簿由其他工具生成而只需重新输出为固定版式文档的场景非常有用。下面的示例加载一个现有的 `.xlsx` 工作簿，从其单元格中读取数据，应用可选的页面设置调整，然后将结果保存为 OFD 文档。

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// 从磁盘打开一个已存在的 Excel 工作簿
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) 读取并显示选定单元格的值，以确认文件已加载
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) 遍历 Worksheets 集合以枚举可用的工作表
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) 可选地更新时间戳单元格以反映转换操作
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// 在数据块的顶部添加一个汇总标题行
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) 在工作表上配置 PageSetup 属性
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) 可选地为 OFD 输出设置打印区域
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) 将工作簿另存为 OFD 文件
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **相关文章**
- [将 Excel 文件拆分为多个文件](/cells/zh/nodejs-java/splitting-excel-files-into-multiple-files/)
- [在单元格中插入图片](/cells/zh/nodejs-java/inserting-an-image-into-a-cell/)
- [读写 DBF 文件](/cells/zh/nodejs-java/dbf/)
- [在 Aspose.Cells for Node.js via Java 中将迷你图转换为图像和 HTML](/cells/zh/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}