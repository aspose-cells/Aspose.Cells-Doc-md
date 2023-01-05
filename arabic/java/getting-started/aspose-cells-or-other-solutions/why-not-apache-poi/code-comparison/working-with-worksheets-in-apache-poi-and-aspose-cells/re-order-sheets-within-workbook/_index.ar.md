---
title: إعادة ترتيب الأوراق داخل المصنف
type: docs
weight: 50
url: /ar/java/re-order-sheets-within-workbook/
---
## **Aspose.Cells - إعادة ترتيب الأوراق داخل المصنف**
يوفر Aspose.Cells طريقة ، Worksheet.moveTo () ، تُستخدم لنقل ورقة العمل إلى مكان آخر في نفس جدول البيانات.

**Java**

{{< highlight "java" >}}

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
## **Apache POI SS - HSSF XSSF - إعادة ترتيب الأوراق داخل المصنف**
يوفر Apache POI طريقة Workbook.setSheetOrder () لتعيين أوراق العمل بالترتيب المطلوب.

**Java**

{{< highlight "java" >}}

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)src / main / java / com / aspose / خلية / أمثلة / featurescomparison / أوراق العمل / أوراق إعادة الطلبات)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[نسخ أوراق العمل ونقلها](/cells/ar/java/copying-and-moving-worksheets).

{{% /alert %}}
