---
title: حماية أوراق العمل في Php
type: docs
weight: 10
url: /ar/java/protecting-worksheets-in-php/
---
## **Aspose.Cells - حماية أوراق العمل**
 لحماية ورقة العمل باستخدام**Aspose.Cells Java for PHP** ، مكالمة**حماية_ورقة العمل** طريقة**الحماية** وحدة.

**كود PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");  

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**حماية أوراق العمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
