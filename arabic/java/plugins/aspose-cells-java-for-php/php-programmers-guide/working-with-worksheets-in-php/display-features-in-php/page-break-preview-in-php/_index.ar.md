---
title: معاينة الاستراحة على الصفحة في PHP
type: docs
weight: 60
url: /ar/java/page-break-preview-in-php/
---

## **Aspose.Cells - معاينة كسر الصفحات**
لتعيين ورقة العمل إلى معاينة الاستراحة على الصفحة باستخدام **Aspose.Cells Java for PHP** ، قم ببساطة باستدعاء وحدة **PageBreakPreview**.

**كود PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview

$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **معاينة كسر الصفحات (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
