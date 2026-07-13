---
title: 将 Excel 转换为 OFD 格式
linktitle: 将 Excel 转换为 OFD 格式
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库，支持将 Excel 工作簿转换为 OFD（Open Fixed-layout Document，开放式版式文档）格式。本文演示如何使用 Aspose.Cells 创建 Excel 内容并将其导出为 OFD，以及如何将现有 Excel 文件转换为 OFD。
keywords: Aspose.Cells, Node.js 库, 电子表格, Excel 转 OFD, OFD 转换, SaveFormat.Ofd, 版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值直接将 Excel 工作簿转换为 OFD（Open Fixed-layout Document，开放式版式文档）格式。生成的 OFD 文档会保留工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框以及数字格式。这使得 Aspose.Cells 适用于需要版式固定输出的归档、打印、监管申报以及政府提交等业务流程。

{{% /alert %}}
## **简介**
OFD（Open Fixed-layout Document，开放式版式文档）是中国的一项国家标准（GB/T 33190-2016），用于以固定的、基于页面的版式表示数字文档。在源文档的视觉外观必须与原始内容完全一致的使用场景中，OFD 扮演着与 PDF 类似的角色。OFD 在中华人民共和国广泛应用于政府提交、监管申报、电子发票以及长期归档等场景。

在需要将电子表格内容以只读的、版式锁定的文件形式分发（而非作为可编辑的电子表格）时，将 Excel 工作簿转换为 OFD 是一种常见需求。例如向客户发送已定稿的发票、归档季度财务报告，或向监管机构提交预算电子表格等。Aspose.Cells 通过 `SaveFormat.Ofd` 枚举值满足此需求，该值可直接将工作簿写入 OFD，无需中间转换步骤。OFD 输出会保留单元格值、合并区域、字体、颜色、边框、数字格式以及工作簿上配置的页面设置选项。

{{% alert color="primary" %}}

Aspose.Cells 生成的 OFD 输出会保留源工作簿的可见布局，包括单元格内容、合并单元格、列宽和行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会在版式固定输出中呈现。工作表上配置的页面设置选项（如纸张大小、方向和打印区域）会影响最终 OFD 文档的布局。

{{% /alert %}}
## **创建 Excel 工作簿并另存为 OFD**
Aspose.Cells 允许您以编程方式构建工作簿，向其中填充数据，然后使用 `SaveFormat.Ofd` 枚举直接将其保存为 OFD 格式。以下示例从零开始创建一张发票。它添加公司徽标、表头信息、账单接收方信息、明细项以及计算得出的总计金额，然后将工作簿导出为 OFD 文档。
### **构建带徽标的发票**
该示例通过在左上角插入徽标图像来构建发票工作表，填入公司名称和联系信息，在合并的单元格中添加"INVOICE"标题，记录发票编号和日期，列出账单接收方客户，构建包含描述、数量、单价和总计列的明细项表，并使用单元格公式计算小计、税额和总计金额。粗体表头、价格的货币格式、边框和列宽等格式通过 `Style` 和 `Font` 对象应用。最后，工作簿使用 `SaveFormat.Ofd` 以 `.ofd` 扩展名保存。

```javascript
let dataDir = "C:\\Temp\\";

// 创建一个新的工作簿
let workbook = new AsposeCells.Workbook();

// 获取第一个工作表
let worksheet = workbook.getWorksheets().get(0);

// 设置列宽
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// 插入公司徽标
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// 公司名称和联系信息
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// 发票标题 - 合并单元格
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// 发票编号和日期
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// 收款方信息
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// 明细项目表头
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
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// 带边框的货币样式
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// 描述/数量单元格的普通边框样式
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// 明细项目行
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
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

// 小计、税额、总计
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// 总计值的粗体+货币样式
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// 总计标签的粗体样式
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// 将工作簿保存为 OFD 文件
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **将现有 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘加载现有的 Excel 工作簿，并直接将其导出为 OFD 格式。这对于批量转换流水线、归档工作流以及源工作簿由其他工具生成、仅需重新输出为版式固定文件的场景非常有用。以下示例加载现有的 `.xlsx` 工作簿，从单元格中读取数据，应用可选的页面设置调整，并将结果保存为 OFD 文档。

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) 读取并显示所选单元格的值，以确认文件已加载
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) 遍历 Worksheets 集合以枚举可用的工作表
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) （可选）更新时间戳单元格以反映转换操作
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// 在数据块顶部追加一个汇总标题行
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) 在工作表上配置 PageSetup 属性
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) （可选）为 OFD 输出设置打印区域
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) 将工作簿另存为 OFD 文件
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **相关文章**
- [Splitting Excel Files into Multiple Files](/cells/zh/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Inserting an Image into a Cell](/cells/zh/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/zh/nodejs-cpp/dbf/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Node.js via C++](/cells/zh/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}