---
title: Ein- und Ausblenden von Zeilen und Spalten in PHP
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns-in-php/
description: Erfahren Sie, wie Sie Zeilen und Spalten über die APIs Aspose.Cells for PHP via Java ein- und ausblenden.
keywords: How to Hide and Show Rows and Columns in PHP, Hide Rows or Columns using PHP, PHP Show Rows or Columns. 
---
##  **Aspose.Cells for PHP – Steuern der Sichtbarkeit von Zeilen und Spalten**
###  **So verbergen Sie Zeilen und Spalten in PHP**
Entwickler können eine Zeile oder Spalte ausblenden, indem sie die Methoden HideRow bzw. HideColumn der Sammlung Cells aufrufen. Beide Methoden verwenden den Zeilen-/Spaltenindex als Parameter, um die spezifische Zeile oder Spalte auszublenden.

**PHP-Code**

{{< highlight "php" >}}

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
###  **So zeigen Sie Zeilen und Spalten mit PHP an**
Entwickler können jede ausgeblendete Zeile oder Spalte einblenden, indem sie die Methoden UnhideRow bzw. UnhideColumn der Sammlung Cells aufrufen. Beide Methoden benötigen zwei Parameter:

- **Zeilen- oder Spaltenindex**– der Index einer Zeile oder Spalte, der zur Anzeige der jeweiligen Zeile oder Spalte verwendet wird.
- **Zeilenhöhe oder Spaltenbreite**– die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach der Anzeige zugewiesen wird.

**PHP-Code**

{{< highlight "php" >}}

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
##  **Laden Sie Running Code herunter**
 Herunterladen**Steuern der Sichtbarkeit von Zeilen und Spalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
