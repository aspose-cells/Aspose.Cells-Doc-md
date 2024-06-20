---
title: إلغاء حماية ورقة العمل في PHP
type: docs
weight: 20
url: /ar/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - إلغاء حماية ورقة عمل**
لحماية ورقة العمل باستخدام **Aspose.Cells Java for PHP**, اتصل بطريقة **unprotect_worksheet** في وحدة **protection**.

**كود PHP**

{{< highlight php >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **إلغاء حماية ورقة العمل (Aspose.Cells)** من أي مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
