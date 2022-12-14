---
title: تعيين ناحية الطباعة
type: docs
weight: 40
url: /ar/java/set-print-area/
---
## **Aspose.Cells - تعيين ناحية الطباعة**
بشكل افتراضي ، تدمج منطقة الطباعة فقط جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين إنشاء منطقة طباعة معينة من ورقة العمل.

لتحديد منطقة طباعة معينة ، استخدم ملف[اعداد الصفحة](/java/pagesetup)طريقة setPrintArea للفئة. قم بتعيين نطاق خلايا يحدد منطقة الطباعة لهذه الخاصية.

**Java**

{{< highlight "java" >}}

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
## **Apache POI SS - HSSF XSSF - ضبط منطقة الطباعة**
تتوفر طريقة Workbook.setPrintArea لتعيين خصائص الصفحة الخاصة بمنطقة الطباعة.

**Java**

{{< highlight "java" >}}

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / workbook / setprintarea)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ضبط خيارات الطباعة](/cells/ar/java/page-setup-features/#setting-print-options).

{{% /alert %}}
