---
title: Zeilenhöhe und Spaltenbreite anpassen in PHP
type: docs
weight: 10
url: /de/java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - Zeilenhöhe und Spaltenbreite anpassen**
### **Einstellen der Zeilenhöhe**
Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen der Methode setRowHeight der Cells-Sammlung festzulegen. Die Methode setRowHeight nimmt die folgenden Parameter an:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

**PHP-Code**

{{< highlight php >}}

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
### **Die Spaltenbreite festlegen**
Rufen Sie die Breite einer Spalte durch Aufrufen der Methode setColumnWidth der Sammlung Cells ein. Die Methode setColumnWidth nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

**PHP-Code**

{{< highlight php >}}

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
## **Laufenden Code herunterladen**
Laden Sie **Anpassung von Zeilenhöhe und Spaltenbreite (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
