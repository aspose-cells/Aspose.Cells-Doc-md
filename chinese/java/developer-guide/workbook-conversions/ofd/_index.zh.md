---
title: 将 Excel 转换为 OFD 格式
linktitle: 将 Excel 转换为 OFD 格式
description: Aspose.Cells 是一个用于处理电子表格文件的 Java 库，支持将 Excel 工作簿转换为 OFD（开放版式文档）格式。本文演示如何使用 Aspose.Cells 创建 Excel 内容并将其导出为 OFD，以及如何将现有的 Excel 文件转换为 OFD。
keywords: Aspose.Cells, Java 库, 电子表格, Excel 转 OFD, OFD 转换, SaveFormat.Ofd, 开放版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值直接将 Excel 工作簿转换为 OFD（Open Fixed-layout Document，开放版式文档）格式。生成的 OFD 文档保留了工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框和数字格式。这使得 Aspose.Cells 适用于需要固定版式输出的归档、打印、监管申报和政府提交等场景。

{{% /alert %}}
## **简介**
OFD（Open Fixed-layout Document，开放版式文档）是中国用于以固定、基于页面的版式表示数字文档的国家标准（GB/T 33190-2016）。在源文档的视觉外观必须与原始创建时完全一致的使用场景中，它扮演着与 PDF 类似的角色。OFD 在中华人民共和国的政府提交、监管申报、电子发票和长期归档中得到了广泛采用。

在需要将电子表格内容作为只读、布局锁定的文档（而非可编辑的电子表格）进行分发的场景中，将 Excel 工作簿转换为 OFD 是一个常见的需求。示例包括向客户发送最终发票、归档季度财务报告，或将预算电子表格提交给监管机构。Aspose.Cells 通过 `SaveFormat.Ofd` 枚举值满足这一需求，该枚举值直接将工作簿写入 OFD，无需中间转换步骤。OFD 输出保留了单元格值、合并区域、字体、颜色、边框、数字格式以及在工作簿上配置的页面设置选项。

{{% alert color="primary" %}}

Aspose.Cells 生成的 OFD 输出保留了源工作簿的可见布局，包括单元格内容、合并单元格、列宽和行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会在固定版式输出中呈现。在工作表上配置的纸张大小、方向和打印区域等页面设置选项会影响生成的 OFD 文档的布局。

{{% /alert %}}
## **创建 Excel 工作簿并保存为 OFD**
Aspose.Cells 允许您以编程方式构建工作簿，向其填充数据，然后使用 `SaveFormat.Ofd` 枚举将其直接保存为 OFD 格式。下面的示例从头开始创建一张发票。它添加公司徽标、抬头信息、收款方区域、明细项和计算出的合计金额，然后将工作簿导出为 OFD 文档。
### **构建带徽标的发票**
该示例通过在左上角插入徽标图像来构建发票工作表，填写公司名称和联系信息，在合并的单元格中添加“INVOICE”标题，记录发票号码和日期，列出收款方客户，构建包含描述、数量、单价和总价列的明细项表格，并使用单元格公式计算小计、税款和总计。粗体标题、价格货币格式、边框和列宽等格式通过 `Style` 和 `Font` 对象应用。最后，使用 `SaveFormat.Ofd` 将工作簿保存为 `.ofd` 扩展名。

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// 创建一个新的工作簿
Workbook workbook = new Workbook();

// 获取第一个工作表
Worksheet worksheet = workbook.getWorksheets().get(0);

// 设置列宽
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// 插入公司标志
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// 公司名称和联系信息
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// INVOICE 标题 - 合并单元格
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// 发票编号和日期
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// 收款方信息
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// 物料明细表头
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// 带边框的货币样式
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// 描述/数量单元格的普通边框样式
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// 物料明细行
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// 小计、税金、合计
worksheet.getCells().get("B24").putValue("Subtotal:");
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// 合计值的粗体 + 货币样式
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// 合计标签的粗体样式
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// 将工作簿另存为 OFD 文件
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **将现有的 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘加载现有的 Excel 工作簿，并将其直接导出为 OFD 格式。这对于批量转换管道、归档工作流以及源工作簿由其他工具生成、仅需要重新输出为固定版式文档的场景非常有用。下面的示例加载现有的 `.xlsx` 工作簿，从其单元格中读取数据，应用可选的页面设置调整，然后将结果保存为 OFD 文档。

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// 从磁盘打开现有 Excel 工作簿
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) 读取并显示所选单元格的值，以确认文件已加载
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) 遍历 Worksheets 集合以枚举可用的工作表
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) （可选）更新时间戳单元格以反映转换
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// 在数据块顶部追加一个汇总标题行
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) 在工作表上配置 PageSetup 属性
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) （可选）为 OFD 输出设置打印区域
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) 将工作簿另存为 OFD 文件
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **相关文章**
- [将 Excel 文件拆分为多个文件](/cells/zh/java/splitting-excel-files-into-multiple-files/)
- [在单元格中插入图片](/cells/zh/java/inserting-an-image-into-a-cell/)
- [读取和写入 DBF 文件](/cells/zh/java/dbf/)
- [在 Aspose.Cells for Java 中将迷你图转换为图像和 HTML](/cells/zh/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}