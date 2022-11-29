---
title: Page Setup - Fit to Page Setting
type: docs
weight: 30
url: /java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - Page Setup - Fit to Page Setting**
To fit the contents of the worksheet to a specific number of pages, use the [PageSetup](/cells/java/page-setup-fit-to-page-setting/) class' setFitToPagesTall and setFitToPagesWide methods. These methods are also used to scale worksheets.

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
## **Apache POI SS - HSSF & XSSF - Page Setup - Fit to Page Setting**
Apache POI SS uses setFitHeight and setFitWidth methods for fit to page settings.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

For more details, visit [Setting Page Options](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
