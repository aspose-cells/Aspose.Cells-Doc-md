---
title: نسخ ونقل الأوراق العمل في PHP
type: docs
weight: 10
url: /ar/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - نسخ ونقل أوراق العمل**
### **نسخ أوراق العمل داخل دفتر عمل**
لنسخ ورق عمل باستخدام **Aspose.Cells for Java في PHP**، اتصل بطريقة **copy_worksheet** في وحدة **copyworksheets**. يمكنك رؤية مثال على الكود أدناه.

**كود PHP**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **نقل ورقات العمل داخل كتاب عمل**
لنقل ورقة العمل باستخدام **Aspose.Cells for Java في PHP**، اتصل بطريقة **move_worksheet** في وحدة **copyworksheets**. يمكنك رؤية مثال على الكود أدناه.

**كود PHP**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **نسخ ونقل أوراق العمل (Aspose.Cells)** من أي مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
