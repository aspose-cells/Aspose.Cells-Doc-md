---
title: Копирование строк и столбцов в PHP
type: docs
weight: 30
url: /ru/java/copying-rows-and-columns-in-php/
---
## **Aspose.Cells - Копирование строк и столбцов**
### **Копирование строк**
Aspose.Cells предоставляет метод copyRow класса Cells. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод copyRow принимает следующие параметры:

- исходный объект Cells,
- индекс исходной строки и
- индекс строки назначения.

**PHP-код**

{{< highlight "php" >}}

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
### **Копирование столбцов**
Aspose.Cells предоставляет метод copyColumn класса Cells, этот метод копирует все типы данных, включая формулы — с обновленными ссылками — и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

Метод copyColumn принимает следующие параметры:

- исходный объект Cells,
- индекс исходного столбца и
- индекс столбца назначения.

**PHP-код**

{{< highlight "php" >}}

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
## **Скачать рабочий код**
Скачать**Копирование строк и столбцов (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
