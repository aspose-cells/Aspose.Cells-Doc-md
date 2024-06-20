---
title: تثبيت الألواح في PHP
type: docs
weight: 40
url: /ar/java/freeze-panes-in-php/
---

## **Aspose.Cells - تجميد الألواح**
لتثبيت الألواح في مستند جدول البيانات باستخدام **Aspose.Cells Java for PHP**, قم ببساطة بالاستدعاء لوحدة **FreezePanes**.

**كود PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تجميد الألواح (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
