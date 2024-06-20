---
title: تناسب الصف والعمود تلقائيًا
type: docs
weight: 10
url: /ar/java/auto-fit-row-and-column/
description: تعلم كيفية تناسب الصف والعمود من خلال واجهة برمجة التطبيقات Aspose.Cells for Java.
keywords: كيفية تناسب الصف والعمود في جافا، تناسب بيانات الصف في جدول العمل باستخدام جافا، تناسب بيانات العمود في جافا. 
---

## **كيفية ضبط تلقائي للصف والعمود باستخدام Aspose.Cells for Java**
أبسط طريقة لتحديد عرض وارتفاع صف بشكل تلقائي هي استدعاء الطريقة autoFitRow في ورقة العمل. تأخذ طريقة autoFitRow مؤشر الصف (الصف الذي سيتم تغيير حجمه) كمعلمة.

**يرجى ملاحظة:** إذا كنت ترغب في ضبط صفوف وأعمدة تلقائيًا في جداول بيانات Excel باستخدام Java، يرجى زيارة [ضبط تلقائي للصفوف والأعمدة](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - ضبط تلقائي للصف والعمود**
Apache POI SS - HSSF و XSSF يوفر Sheet.autoSizeColumn لضبط الأعمدة تلقائيًا

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
