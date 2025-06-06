---
title: إعداد الصفحة  ضبط إلى إعداد الصفحة
type: docs
weight: 30
url: /ar/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - إعداد الصفحة - ضبط إلى إعداد الصفحة**
لتناسب محتويات الورقة العمل إلى عدد معين من الصفحات، استخدم فئة [PageSetup](/cells/ar/java/page-setup-fit-to-page-setting/) وطرق setFitToPagesTall و setFitToPagesWide. يتم استخدام هذه الطرق أيضًا لتحديد مقياس الأوراق العمل.

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
## **Apache POI SS - HSSF و XSSF - إعداد الصفحة - ضبط إلى إعداد الصفحة**
تستخدم Apache POI SS طرق setFitHeight و setFitWidth لإعداد تناسب الصفحة.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [ضبط خيارات الصفحة](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
