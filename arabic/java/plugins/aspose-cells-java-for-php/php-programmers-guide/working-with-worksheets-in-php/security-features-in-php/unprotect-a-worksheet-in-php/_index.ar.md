---
title: قم بإلغاء حماية ورقة العمل في Php
type: docs
weight: 20
url: /ar/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells - إلغاء حماية ورقة العمل**
 لحماية ورقة العمل باستخدام**Aspose.Cells Java for PHP** ، مكالمة**unotect_worksheet** طريقة**الحماية** وحدة.

**كود PHP**

{{< highlight "php" >}}

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
## **تحميل كود الجري**
تحميل**إلغاء حماية ورقة العمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
