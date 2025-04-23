---
title: إعادة ترتيب الصفحات ضمن الدفتر
type: docs
weight: 50
url: /ar/java/re-order-sheets-within-workbook/
---

## **Aspose.Cells - إعادة ترتيب الصفحات ضمن الدفتر**
توفر Aspose.Cells طريقة تسمى Worksheet.moveTo() مستخدمة لنقل ورقة عمل إلى موقع آخر في نفس جدول البيانات.

**Java**

{{< highlight java >}}

 //Create a new Workbook.

Workbook workbook = new Workbook();

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet worksheet1 = worksheets.get(0);

Worksheet worksheet2 = worksheets.add("Sheet2");

Worksheet worksheet3 = worksheets.add("Sheet3");

//Move Sheets with in Workbook.

worksheet2.moveTo(0);

worksheet1.moveTo(1);

worksheet3.moveTo(2);

//Save the excel file.

workbook.save(dataDir + "AsposeMoveSheet.xls");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - إعادة ترتيب الصفحات ضمن الدفتر**
توفر Apache POI طريقة Workbook.setSheetOrder() لتعيين أوراق عمل بالترتيب المطلوب.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

wb.createSheet("third sheet");

wb.setSheetOrder("second sheet", 0);

wb.setSheetOrder("new sheet", 1);

wb.setSheetOrder("third sheet", 2);

FileOutputStream fileOut = new FileOutputStream(dataDir + "Apache_Reordered.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/reordersheets)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [نسخ ونقل الأوراق العمل](/cells/ar/java/copying-and-moving-worksheets).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
