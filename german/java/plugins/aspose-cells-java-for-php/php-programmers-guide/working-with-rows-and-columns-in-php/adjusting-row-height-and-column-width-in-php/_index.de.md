---
title: Anpassen der Zeilenhöhe und Spaltenbreite in PHP
type: docs
weight: 10
url: /de/java/adjusting-row-height-and-column-width-in-php/
---
## **Aspose.Cells – Anpassen der Zeilenhöhe und Spaltenbreite**
### **Einstellen der Zeilenhöhe**
Es ist möglich, die Höhe einer einzelnen Zeile festzulegen, indem die Methode setRowHeight der Sammlung Cells aufgerufen wird. Die setRowHeight-Methode übernimmt die folgenden Parameter:

- **Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- **Zeilenhöhe**, die Zeilenhöhe, die auf die Zeile angewendet werden soll.

**PHP-Code**

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
### **Einstellen der Spaltenbreite**
Legen Sie die Breite einer Spalte fest, indem Sie die Methode setColumnWidth der Sammlung Cells aufrufen. Die setColumnWidth-Methode übernimmt die folgenden Parameter:

- **Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

**PHP-Code**

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
## **Laufcode herunterladen**
Download**Zeilenhöhe und Spaltenbreite anpassen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
