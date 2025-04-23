---
title: تحديد منطقة الطباعة
type: docs
weight: 40
url: /ar/java/set-print-area/
---

## **Aspose.Cells - تحديد منطقة الطباعة**
بشكل افتراضي، تشمل منطقة الطباعة فقط جميع مناطق ورق العمل التي تحتوي على بيانات. يمكن للمطورين إنشاء منطقة طباعة محددة لورق العمل.

لتحديد منطقة طباعة محددة، استخدم طريقة setPrintArea فئة PageSetup. قم بتعيين نطاق الخلايا الذي يحدد منطقة الطباعة لهذه الخاصية.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - تعيين منطقة الطباعة**
تتوفر طريقة Workbook.setPrintArea لتعيين خصائص الصفحة لمنطقة الطباعة

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تعيين خيارات الطباعة](/cells/ar/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
