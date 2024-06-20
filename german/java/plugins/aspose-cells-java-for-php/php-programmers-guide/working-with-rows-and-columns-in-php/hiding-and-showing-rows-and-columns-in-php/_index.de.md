---
title: Zeilen und Spalten in PHP ausblenden und anzeigen
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns-in-php/
description: Erfahren Sie, wie Sie Zeilen und Spalten über die Aspose.Cells for PHP via Java APIs ausblenden und anzeigen können.
keywords: Wie man Zeilen und Spalten in PHP ausblendet und anzeigt, Zeilen oder Spalten in PHP ausblenden, PHP Zeilen oder Spalten anzeigen. 
---

## **Aspose.Cells for PHP - Steuern der Sichtbarkeit von Zeilen & Spalten**
### **Wie man in PHP Zeilen und Spalten ausblendet**
Entwickler können eine Zeile oder Spalte verbergen, indem sie die Methoden HideRow und HideColumn der Cells-Sammlung aufrufen. Beide Methoden nehmen den Zeilen-/Spaltenindex als Parameter, um die spezifische Zeile oder Spalte zu verbergen.

**PHP-Code**

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
### **Wie man in PHP Zeilen und Spalten anzeigt**
Entwickler können eine versteckte Zeile oder Spalte wieder anzeigen, indem sie die Methoden UnhideRow und UnhideColumn der Cells-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Anzeigen zugewiesen wird.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Laden Sie die Steuerung der Sichtbarkeit von Zeilen & Spalten (Aspose.Cells) von einer der unten genannten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
