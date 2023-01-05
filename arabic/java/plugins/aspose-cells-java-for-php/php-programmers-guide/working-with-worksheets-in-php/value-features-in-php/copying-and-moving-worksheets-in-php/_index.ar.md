---
title: نسخ أوراق العمل ونقلها في Php
type: docs
weight: 10
url: /ar/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells - نسخ أوراق العمل ونقلها**
### **نسخ أوراق العمل داخل مصنف**
 لنسخ ورقة العمل باستخدام**Aspose.Cells for Java في PHP** ، مكالمة**نسخة_ورقة عمل** طريقة**أوراق العمل** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود PHP**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **انقل أوراق العمل داخل مصنف**
 لنقل ورقة العمل باستخدام**Aspose.Cells for Java في PHP** ، مكالمة**نقل ورقة العمل** طريقة**أوراق العمل** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود PHP**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**نسخ أوراق العمل ونقلها (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
