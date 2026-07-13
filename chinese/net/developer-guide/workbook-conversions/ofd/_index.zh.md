---
title: 将 Excel 转换为 OFD 格式
linktitle: 将 Excel 转换为 OFD 格式
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，支持将 Excel 工作簿转换为 OFD（开放式固定版式文档）格式。本文演示如何使用 Aspose.Cells 创建 Excel 内容并将其导出为 OFD，以及如何将现有 Excel 文件转换为 OFD。
keywords: Aspose.Cells, .NET 库, 电子表格, Excel 转 OFD, OFD 转换, SaveFormat.Ofd, 固定版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值将 Excel 工作簿直接转换为 OFD（开放式固定版式文档）格式。生成的 OFD 文档可保留工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框以及数字格式。这使得 Aspose.Cells 适用于需要固定版式输出的归档、打印、监管申报以及政府提交等场景。

{{% /alert %}}
## **简介**
OFD（开放式固定版式文档）是中国的一项国家标准（GB/T 33190-2016），用于以固定的、基于页面的版式表示数字文档。它的作用类似于 PDF，适用于必须精确保持源文档视觉外观的使用场景。OFD 在中华人民共和国广泛应用于政府申报、监管备案、电子发票以及长期归档等领域。

在需要将电子表格内容作为只读、版式锁定的文档分发（而不是作为可编辑的电子表格）时，将 Excel 工作簿转换为 OFD 是一种常见的需求。例如向客户交付已定稿的发票、归档季度财务报告或向监管机构提交预算电子表格。Aspose.Cells 通过 `SaveFormat.Ofd` 枚举值满足此需求，该值可以将工作簿直接写入 OFD，无需中间转换步骤。OFD 输出可保留单元格值、合并区域、字体、颜色、边框、数字格式以及在工作簿上配置的页面设置选项。

{{% alert color="primary" %}}

Aspose.Cells 生成的 OFD 输出可保留源工作簿的可见布局，包括单元格内容、合并单元格、列宽和行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会在固定版式输出中呈现。工作表上配置的页面设置选项（例如纸张大小、方向和打印区域）会影响最终 OFD 文档的布局。

{{% /alert %}}
## **创建 Excel 工作簿并另存为 OFD**
Aspose.Cells 允许您以编程方式构建工作簿，向其中填充数据，然后使用 `SaveFormat.Ofd` 枚举直接将其保存为 OFD 格式。以下示例从头开始创建一张发票。它添加公司徽标、抬头信息、收款方区域、明细行以及计算后的合计金额，然后将工作簿导出为 OFD 文档。
### **构建带徽标的发票**
该示例通过在左上角插入徽标图像来构建发票工作表，填写公司名称和联系方式，在合并单元格中添加 "INVOICE" 标题，记录发票编号和日期，列出收款方客户信息，构建包含描述、数量、单价和合计列的明细表，并使用单元格公式计算小计、税款和总计。通过 `Style` 和 `Font` 对象应用粗体表头、价格货币格式、边框以及列宽等格式设置。最后，使用 `SaveFormat.Ofd` 将工作簿保存为 `.ofd` 扩展名的文件。

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// 创建一个新的工作簿
Workbook workbook = new Workbook();

// 获取第一个工作表
Worksheet worksheet = workbook.Worksheets[0];

// 设置列宽
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// 插入公司标志
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// 公司名称和联系信息
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// 发票标题 - 合并单元格
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// 发票编号和日期
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// 收款方信息
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// 订单项表头
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// 带边框的货币样式
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// 描述/数量单元格的普通边框样式
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// 订单项行
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// 小计、税款、总计
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// 总计值的粗体 + 货币样式
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// 总计标签的粗体样式
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// 将工作簿保存为 OFD 文件
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **将现有 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘加载现有 Excel 工作簿，并将其直接导出为 OFD 格式。这对于批量转换流水线、归档工作流以及源工作簿由其他工具生成且仅需重新发布为固定版式文档的场景非常有用。以下示例加载现有 `.xlsx` 工作簿，读取其单元格中的数据，应用可选的页面设置调整，并将结果保存为 OFD 文档。

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// 从磁盘打开一个现有的 Excel 工作簿
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) 读取并显示选定单元格的值，以确认文件已加载
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) 遍历 Worksheets 集合以枚举可用的工作表
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) 可选择地更新时间戳单元格以反映转换操作
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// 在数据块顶部插入一个汇总标题行
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) 在工作表上配置 PageSetup 属性
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) 可选择地为 OFD 输出设置打印区域
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) 将工作簿保存为 OFD 文件
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **相关文章**
- [拆分 Excel 文件为多个文件](/cells/zh/net/splitting-excel-files-into-multiple-files/)
- [在单元格中插入图像](/cells/zh/net/inserting-an-image-into-a-cell/)
- [读取和写入 DBF 文件](/cells/zh/net/dbf/)
- [在 Aspose.Cells for .NET 中将迷你图转换为图像和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}