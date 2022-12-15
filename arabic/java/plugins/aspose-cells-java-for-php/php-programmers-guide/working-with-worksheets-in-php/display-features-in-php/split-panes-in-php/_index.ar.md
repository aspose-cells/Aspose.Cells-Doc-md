---
title: تقسيم الأجزاء في Php
type: docs
weight: 70
url: /ar/java/split-panes-in-php/
---
## **Aspose.Cells - تقسيم الأجزاء**
 لتقسيم الأجزاء باستخدام**Aspose.Cells Java for PHP** ، ببساطة استدعاء**SplitPanes** وحدة.

**كود PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**تقسيم الأجزاء (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
