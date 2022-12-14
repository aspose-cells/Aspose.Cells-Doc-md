---
title: إدراج وحذف الصفوف والأعمدة في PHP
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns-in-php/
---
## **Aspose.Cells - إدارة الصفوف / الأعمدة**
### **إدخال صف**
أدخل صفًا في أي مكان عن طريق استدعاء طريقة insertRows للمجموعة Cells. تأخذ طريقة insertRows فهرس الصف حيث سيتم إدراج الصف الجديد كوسيطة أولى ، وعدد الصفوف التي سيتم إدراجها كوسيطة ثانية.

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
### **إدراج صفوف متعددة**
لإدراج عدة صفوف في ورقة العمل ، قم باستدعاء الأسلوب insertRows للمجموعة Cells. تأخذ طريقة InsertRows معلمتين:

- فهرس الصف ، فهرس الصف حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب إدراجها.

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
### **حذف صف**
لحذف صف في أي مكان ، قم باستدعاء طريقة deleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب حذفها.

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
### **حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل ، قم باستدعاء الأسلوب deleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، إجمالي عدد الصفوف التي يجب حذفها.

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
### **إدخال عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة insertColumns للمجموعة Cells. تأخذ طريقة insertColumns معلمتين:

- فهرس العمود ، فهرس العمود حيث سيتم إدراج العمود
- عدد الأعمدة ، إجمالي عدد الأعمدة التي يجب إدراجها

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
### **حذف عمود**
لحذف عمود من ورقة العمل في أي مكان ، قم باستدعاء طريقة deleteColumns للمجموعة Cells. تأخذ طريقة deleteColumns المعلمات التالية:

- فهرس العمود ، فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة ، إجمالي عدد الأعمدة التي يجب حذفها.
- تحول الخلايا ، المعلمة المنطقية للإشارة إلى ما إذا كان سيتم نقل الخلايا المتبقية بعد الحذف.

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
## **قم بتنزيل كود التشغيل**
 تحميل**إدارة الصفوف / الأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
