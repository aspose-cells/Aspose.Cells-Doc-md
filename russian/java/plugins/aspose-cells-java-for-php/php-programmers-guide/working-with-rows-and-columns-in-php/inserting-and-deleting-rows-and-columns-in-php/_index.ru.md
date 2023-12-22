---
title: Вставка и удаление строк и столбцов в PHP
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns-in-php/
description: Узнайте, как вставлять и удалять строки и столбцы с помощью API Aspose.Cells for PHP via Java.
keywords: How to Insert and Delete Rows and Columns in PHP, Insert Rows and Columns using PHP, PHP Delete Rows and Columns, Insert Rows or Columns with PHP, Delete Rows or Columns via PHP.
---
##  **Aspose.Cells - Управление строками/столбцами**
###  **Вставка строки**
Вставьте строку в любое место, вызвав метод InsertRows коллекции Cells. Метод InsertRows принимает индекс строки, в которую будет вставлена новая строка, в качестве первого аргумента, а количество строк, которые будут вставлены, в качестве второго аргумента.

**PHP-код**

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
###  **Вставка нескольких строк**
Чтобы вставить несколько строк в лист, вызовите метод InsertRows коллекции Cells. Метод InsertRows принимает два параметра:

- Индекс строки — индекс строки, из которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

**PHP-код**

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
###  **Удаление строки**
Чтобы удалить строку в любом месте, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки — индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**PHP-код**

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
###  **Удаление нескольких строк**
Чтобы удалить несколько строк из листа, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки — индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**PHP-код**

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
###  **Вставка столбца**
Разработчики также могут вставить столбец в лист в любое место, вызвав метод InsertColumns коллекции Cells. Метод InsertColumns принимает два параметра:

- Индекс столбца, индекс столбца, из которого столбец будет вставлен.
- Количество столбцов, общее количество столбцов, которые необходимо вставить

**PHP-код**

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
###  **Удаление столбца**
Чтобы удалить столбец с листа в любом месте, вызовите метод deleteColumns коллекции Cells. Метод deleteColumns принимает следующие параметры:

- Индекс столбца — индекс столбца, из которого столбец будет удален.
- Количество столбцов, общее количество столбцов, которые необходимо удалить.
- Сдвиг ячеек, логический параметр, указывающий, следует ли смещать ячейки, оставшиеся после удаления.

**PHP-код**

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
##  **Загрузить рабочий код**
 Скачать**Управление строками/столбцами (Aspose.Cells)**с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
