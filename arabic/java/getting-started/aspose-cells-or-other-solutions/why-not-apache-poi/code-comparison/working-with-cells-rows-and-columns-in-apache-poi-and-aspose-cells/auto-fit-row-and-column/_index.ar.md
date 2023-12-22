---
title: الاحتواء التلقائي للصف والعمود
type: docs
weight: 10
url: /ar/java/auto-fit-row-and-column/
description: تعرف على كيفية الاحتواء التلقائي للصف والعمود من خلال Aspose.Cells for Java API.
keywords: How to Autofit Row and Column in Java, Autofit Row Data in workbook using Java, Java Autofit Column Data. 
---
##  **كيفية الاحتواء التلقائي للصف والعمود باستخدام Aspose.Cells for Java**
الطريقة الأكثر مباشرة للتحجيم التلقائي لعرض الصف وارتفاعه هي استدعاء الأسلوب Worksheet.autoFitRow. تأخذ الطريقة autoFitRow فهرس الصف (الصف الذي سيتم تغيير حجمه) كمعلمة.

**يرجى الملاحظة:**إذا كنت تريد الاحتواء التلقائي للصفوف والأعمدة في جداول بيانات Excel باستخدام Java، فيرجى زيارة[الاحتواء التلقائي للصفوف والأعمدة](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
##  **Apache POI SS - HSSF XSSF - التناسب التلقائي للصف والعمود**
Apache POI SS - يوفر HSSF وXSSF Sheet.autoSizeColumn لملاءمة الأعمدة تلقائيًا

**Java**

{{< highlight "java" >}}

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
##  **تحميل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
##  **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/Java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
