---
title: تقسيم الإشرطة في PHP
type: docs
weight: 70
url: /ar/java/split-panes-in-php/
---

## **Aspose.Cells - تقسيم الألواح**
لتقسيم الإشرطة باستخدام **Aspose.Cells Java for PHP** ، قم ببساطة باستدعاء وحدة **SplitPanes**.

**كود PHP**

{{< highlight php >}}

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
## **تحميل رمز التشغيل**
تنزيل **تقسيم الألواح (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
