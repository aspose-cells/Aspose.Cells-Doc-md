---
title: Автоматическая подгонка строк и столбцов в PHP
type: docs
weight: 20
url: /ru/java/autofit-rows-and-columns-in-php/
---

## **Aspose.Cells - Автоподбор строк и столбцов**
### **Автоподбор строки**
Самым простым способом автоматического изменения ширины и высоты строки является вызов метода autoFitRow класса Worksheet. Метод autoFitRow принимает индекс строки (столбец для изменения размера) в качестве параметра.

**PHP-код**

{{< highlight php >}}

 public static function autofit_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 3rd row of the worksheet

    $worksheet->autoFitRow(2);

    # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

    # cells (from 1st to 9th column) within the row

    #$worksheet->autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Row.xls");

    print "Autofit Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Автоподбор столбца**
Самым простым способом автоматического изменения ширины и высоты столбца является вызов метода autoFitColumn класса Worksheet. Метод autoFitColumn принимает индекс столбца (столбец, который требуется изменить) в качестве параметра.

**PHP-код**

{{< highlight php >}}

 public static function autofit_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 4th column of the worksheet

    $worksheet->autoFitColumn(3);

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #$worksheet->autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Column.xls");

    print "Autofit Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Автоподбор строк и столбцов (Aspose.Cells)** с любого из перечисленных ниже сайтов социальной разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
