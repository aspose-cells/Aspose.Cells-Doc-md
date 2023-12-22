---
title: إدراج وحذف الصفوف والأعمدة في PHP
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns-in-php/
description: تعرف على كيفية إدراج وحذف الصفوف والأعمدة من خلال واجهات برمجة التطبيقات Aspose.Cells for PHP via Java.
keywords: How to Insert and Delete Rows and Columns in PHP, Insert Rows and Columns using PHP, PHP Delete Rows and Columns, Insert Rows or Columns with PHP, Delete Rows or Columns via PHP.
---
##  **Aspose.Cells - إدارة الصفوف والأعمدة**
###  **إدراج صف**
قم بإدراج صف في أي مكان عن طريق استدعاء الأسلوب InsertRows للمجموعة Cells. تأخذ طريقة InsertRows فهرس الصف الذي سيتم إدراج الصف الجديد فيه كوسيطة أولى، وعدد الصفوف التي سيتم إدراجها كوسيطة ثانية.

**كود PHP**

{{< highlight "php" >}}

 public static function insert_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Row.xls");

    print "Insert Row Successfully." . PHP_EOL;

}  

{{< /highlight >}}
###  **إدراج صفوف متعددة**
لإدراج صفوف متعددة في ورقة العمل، اتصل بأسلوب InsertRows للمجموعة Cells. يأخذ الأسلوب InsertRows معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم إدراج الصفوف الجديدة منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

**كود PHP**

{{< highlight "php" >}}

 public static function insert_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,10);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Multiple Rows.xls");

    print "Insert Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
###  **حذف صف**
لحذف صف في أي مكان، اتصل بأسلوبdeleteRows للمجموعة Cells. تأخذ طريقة RemoveRows معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب حذفها.

**كود PHP**

{{< highlight "php" >}}

 public static function delete_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 3rd row from the worksheet

    $worksheet->getCells()->deleteRows(2,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Row.xls");

    print "Delete Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
###  **حذف صفوف متعددة**
لحذف صفوف متعددة من ورقة عمل، قم باستدعاء الأسلوبdeleteRows للمجموعة Cells. تأخذ طريقة RemoveRows معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب حذفها.

**كود PHP**

{{< highlight "php" >}}

 public static function delete_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 10 rows from the worksheet starting from 3rd row

    $worksheet->getCells()->deleteRows(2,10,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Multiple Rows.xls");

    print "Delete Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
###  **إدراج عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء الأسلوب InsertColumns للمجموعة Cells. تأخذ طريقة InsertColumns معلمتين:

- فهرس العمود، فهرس العمود الذي سيتم إدراج العمود منه
- عدد الأعمدة، إجمالي عدد الأعمدة التي يجب إدراجها

**كود PHP**

{{< highlight "php" >}}

 public static function insert_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a column into the worksheet at 2nd position

    $worksheet->getCells()->insertColumns(1,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Column.xls");

    print "Insert Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
###  **حذف عمود**
لحذف عمود من ورقة العمل في أي مكان، اتصل بالطريقةdeleteColumns للمجموعة Cells. تأخذ طريقةdeleteColumns المعلمات التالية:

- فهرس العمود، فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة، إجمالي عدد الأعمدة التي يجب حذفها.
- تحويل الخلايا، معلمة منطقية للإشارة إلى ما إذا كان سيتم نقل الخلايا المتبقية بعد الحذف.

**كود PHP**

{{< highlight "php" >}}

 public static function delete_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting a column from the worksheet at 2nd position

    $worksheet->getCells()->deleteColumns(1,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Column.xls");

    print "Delete Column Successfully." . PHP_EOL;

}  

{{< /highlight >}}
##  **تحميل كود التشغيل**
 تحميل**إدارة الصفوف/الأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
