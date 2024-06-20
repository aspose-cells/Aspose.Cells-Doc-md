---
title: نسخ الصفوف والأعمدة في PHP
type: docs
weight: 30
url: /ar/java/copying-rows-and-columns-in-php/
---

## **Aspose.Cells - نسخ الصفوف والأعمدة**
### **نسخ الصفوف**
توفر Aspose.Cells طريقة copyRow من فئة Cells. تقوم هذه الطريقة بنسخ جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلية والخلايا المخفية والصور وغيرها من الكائنات الرسومية الأخرى من الصف المصدر إلى الصف الوجهة.

تأخذ طريقة copyRow المعلمات التالية:

- كائن الـCells المصدر،
- فهرس الصف المصدر، و
- فهرس الصف الوجهة.

**كود PHP**

{{< highlight php >}}

 public static function copy_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the $worksheet->

    $worksheet->getCells()->copyRow($worksheet->getCells(),1,11);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Copy Rows.xls");

    print "Copy Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **نسخ الأعمدة**
توفر Aspose.Cells طريقة copyColumn من فئة Cells، هذه الطريقة تقوم بنسخ جميع أنواع البيانات بما في ذلك الصيغ - بالمراجع المحدثة - والقيم والتعليقات وتنسيقات الخلية والخلايا المخفية والصور وغيرها من الكائنات الرسومية الأخرى من العمود المصدر إلى العمود الوجهة.

تأخذ طريقة copyColumn المعلمات التالية:

- كائن الـCells المصدر،
- فهرس العمود المصدر، و
- فهرس العمود الوجهة.

**كود PHP**

{{< highlight php >}}

 public static function copy_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook();

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Put some data into header rows (A1:A4)

    $i = 0;

    while($i < 5)

    {

        $worksheet->getCells()->get($i, 0)->setValue("Header Row #$i");

        $i++;

    }


    # Put some detail data (A5:A999)

    $i = 5;

    while ($i < 1000) {

        $worksheet->getCells()->get($i, 0)->setValue("Detail Row #$i");

        $i++;

    }

    # Create another Workbook.

    $workbook1 = new Workbook();

    # Get the first worksheet in the book.

    $worksheet1 = $workbook1->getWorksheets()->get(0);

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    $worksheet1->getCells()->copyColumn($worksheet->getCells(),0,2);

    # Autofit the column.

    $worksheet1->autoFitColumn(2);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Copy Columns.xls");

    print "Copy Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **نسخ الصفوف والأعمدة (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
