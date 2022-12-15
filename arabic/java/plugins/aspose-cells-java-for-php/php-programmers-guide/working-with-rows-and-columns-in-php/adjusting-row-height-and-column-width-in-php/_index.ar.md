---
title: ضبط ارتفاع الصف وعرض العمود في PHP
type: docs
weight: 10
url: /ar/java/adjusting-row-height-and-column-width-in-php/
---
## **Aspose.Cells - ضبط ارتفاع الصف وعرض العمود**
### **ضبط ارتفاع الصف**
من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء طريقة setRowHeight لمجموعة Cells. تأخذ طريقة setRowHeight المعلمات التالية:

- **فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- **ارتفاع الصف**، ارتفاع الصف المراد تطبيقه على الصف.

**كود PHP**

{{< highlight "php" >}}

 public static function set_row_height($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the height of the second row to 13

    $cells->setRowHeight(1, 13);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Row Height.xls");

    print "Set Row Height Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **ضبط عرض العمود**
قم بتعيين عرض العمود عن طريق استدعاء طريقة setColumnWidth للمجموعة Cells. تأخذ طريقة setColumnWidth المعلمات التالية:

- **فهرس العمود**، هو فهرس العمود الذي تقوم بتغيير عرضه.
- **عرض العمود**، عرض العمود المطلوب.

**كود PHP**

{{< highlight "php" >}}

 public static function set_column_width($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the width of the second column to 17.5

    $cells->setColumnWidth(1, 17.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Column Width.xls");

    print "Set Column Width Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**ضبط ارتفاع الصف وعرض العمود (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
