---
title: تجميع الصفوف والأعمدة وإلغاء تجميعها في PHP
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns-in-php/
---
## **Aspose.Cells - إدارة المجموعة للصفوف والأعمدة**
### **تجميع الصفوف والأعمدة**
من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء التابعين groupRows و groupColumns للمجموعة Cells. تأخذ كلتا الطريقتين المعلمات التالية:

- أول صف / فهرس العمود ، أول صف أو عمود في المجموعة.
- فهرس الصف / العمود الأخير ، الصف أو العمود الأخير في المجموعة.
- مخفي ، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف / الأعمدة بعد التجميع أم لا.

**كود PHP**

{{< highlight "php" >}}

 public static function group_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true

    $cells->groupRows(0,5,true);

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true

    $cells->groupColumns(0,2,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Group Rows And Columns.xls");

    print "Group Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **فك تجميع الصفوف والأعمدة**
قم بفك تجميع الصفوف أو الأعمدة المجمعة عن طريق استدعاء أساليب UngroupRows و UngroupColumns للمجموعة Cells. تأخذ كلتا الطريقتين نفس المعلمات:

- الصف الأول أو فهرس العمود ، الصف / العمود الأول المراد فك تجميعه.
- فهرس الصف أو العمود الأخير ، الصف / العمود الأخير المراد فك تجميعه.

**كود PHP**

{{< highlight "php" >}}

 public static function ungroup_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Group Rows And Columns.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Ungrouping first six rows (from 0 to 5)

    $cells->ungroupRows(0,5);

    # Ungrouping first three columns (from 0 to 2)

    $cells->ungroupColumns(0,2);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Ungroup Rows And Columns.xls");

    print "Ungroup Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**تجميع وفك تجميع الصفوف والأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
