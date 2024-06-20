---
title: 页面设置  自适应页面设置
type: docs
weight: 30
url: /zh/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - 页面设置 - 自适应页面设置**
要将工作表内容适配到特定页数，使用 [PageSetup](/cells/zh/java/page-setup-fit-to-page-setting/) 类的 setFitToPagesTall 和 setFitToPagesWide 方法。这些方法也用于调整工作表。

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Excel file

WorksheetCollection worksheets = workbook.getWorksheets();

int sheetIndex = worksheets.add();

Worksheet sheet = worksheets.get(sheetIndex);

PageSetup pageSetup = sheet.getPageSetup();

// Setting the number of pages to which the length of the worksheet will

// be spanned

pageSetup.setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned

pageSetup.setFitToPagesWide(1);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - 页面设置 - 自适应页面设置**
Apache POI SS 使用 setFitHeight 和 setFitWidth 方法进行自适应页面设置。

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

有关详细信息，请访问 [设置页面选项](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options)。

{{% /alert %}}
