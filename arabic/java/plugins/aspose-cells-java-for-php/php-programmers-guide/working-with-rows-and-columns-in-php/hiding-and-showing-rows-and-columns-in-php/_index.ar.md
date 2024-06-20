---
title: إخفاء وإظهار الصفوف والأعمدة في PHP
type: docs
weight: 50
url: /ar/java/hiding-and-showing-rows-and-columns-in-php/
description: تعلم كيفية إخفاء وإظهار الصفوف والأعمدة من خلال Aspose.Cells لواجهات برمجة التطبيقات via Java لبرمجة PHP.
keywords: كيفية إخفاء وإظهار الصفوف والأعمدة في PHP، إخفاء الصفوف أو الأعمدة باستخدام PHP، PHP إظهار الصفوف أو الأعمدة. 
---

## **Aspose.Cells للـ PHP - التحكم في رؤية الصفوف والأعمدة**
### **كيفية إخفاء الصفوف والأعمدة في PHP**
يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق HideRow و HideColumn لمجموعة Cells على التوالي. تأخذ كلا الطريقتين فهرس الصف/العمود كمعلمة لإخفاء الصف أو العمود المعين.

**كود PHP**

{{< highlight php >}}

 public static function hide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Hiding the 3rd row of the worksheet

    $cells->hideRow(2);

    # Hiding the 2nd column of the worksheet

    $cells->hideColumn(1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Hide Rows And Columns.xls");

    print "Hide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **كيفية عرض الصفوف والأعمدة باستخدام PHP**
يمكن للمطورين إظهار أي صف أو عمود مخفي عن طريق استدعاء طرق UnhideRow و UnhideColumn لمجموعة Cells على التوالي. تأخذ كلا الطريقتين معلمين:

- **فهرس الصف أو العمود** - فهرس صف أو عمود يُستخدم لإظهار الصف أو العمود المعين.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين بعد إظهاره.

**كود PHP**

{{< highlight php >}}

 public static function unhide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Unhiding the 3rd row and setting its height to 13.5

    $cells->unhideRow(2,13.5);

    # Unhiding the 2nd column and setting its width to 8.5

    $cells->unhideColumn(1,8.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Unhide Rows And Columns.xls");

    print "Unhide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **التحكم في رؤية الصفوف والأعمدة (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
