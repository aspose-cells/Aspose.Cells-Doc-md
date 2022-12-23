---
title: احتواء تلقائي للصف والعمود
type: docs
weight: 10
url: /ar/java/auto-fit-row-and-column/
---
## **Aspose.Cells - احتواء تلقائي للصف والعمود**
الطريقة الأكثر مباشرة لتغيير حجم عرض الصف وارتفاعه تلقائيًا هي استدعاء طريقة Worksheet.autoFitRow. تأخذ طريقة autoFitRow فهرس صف (للصف المراد تغيير حجمه) كمعامل.

**يرجى الملاحظة:**إذا كنت تريد احتواء الصفوف والأعمدة تلقائيًا في جداول بيانات Excel باستخدام Java ، يرجى زيارة[احتواء تلقائي للصفوف والأعمدة](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

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
## **Apache POI SS - HSSF XSSF - احتواء تلقائي للصف والعمود**
Apache POI SS - يوفر HSSF و XSSF Sheet.autoSizeColumn لملائمة الأعمدة تلقائيًا

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / cellrowscolumns / autofitrowandcolumn)
