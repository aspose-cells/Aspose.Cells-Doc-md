---
title: Ein und Löschen von Zeilen und Spalten in PHP
type: docs
weight: 60
url: /de/java/inserting-and-deleting-rows-and-columns-in-php/
description: Erfahren Sie, wie Sie Zeilen und Spalten durch die Aspose.Cells für PHP via Java APIs einfügen und löschen.
keywords: Wie man Zeilen und Spalten in PHP einfügt und löscht, Zeilen und Spalten mit PHP einfügt, PHP Zeilen und Spalten löscht, Zeilen oder Spalten mit PHP einfügt, Zeilen oder Spalten über PHP löscht.
---

## **Aspose.Cells - Verwalten von Zeilen/Spalten**
### **Einlegen einer Zeile**
Fügen Sie eine Zeile an einer beliebigen Stelle ein, indem Sie die Methode insertRows der Cells-Sammlung aufrufen. Die Methode insertRows nimmt den Index der Zeile, in die die neue Zeile eingefügt werden soll, als ersten Argument und die Anzahl der einzufügenden Zeilen als zweites Argument.

**PHP-Code**

{{< highlight php >}}

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
### **Einfügen mehrerer Zeilen**
Um mehrere Zeilen in das Arbeitsblatt einzufügen, rufen Sie die Methode insertRows der Cells-Sammlung auf. Die Methode insertRows nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, Gesamtanzahl der Zeilen, die eingefügt werden müssen.

**PHP-Code**

{{< highlight php >}}

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
### **Löschen einer Zeile**
Um eine Zeile an einer beliebigen Stelle zu löschen, rufen Sie die Methode deleteRows der Cells Sammlung auf. Die deleteRows Methode nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, Gesamtanzahl der Zeilen, die gelöscht werden müssen.

**PHP-Code**

{{< highlight php >}}

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
### **Mehrere Zeilen löschen**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode deleteRows der Cells Sammlung auf. Die deleteRows Methode nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, Gesamtanzahl der Zeilen, die gelöscht werden müssen.

**PHP-Code**

{{< highlight php >}}

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
### **Einfügen einer Spalte**
Entwickler können auch eine Spalte in das Arbeitsblatt an einer beliebigen Stelle einfügen, indem sie die insertColumns Methode der Cells Sammlung aufrufen. Die insertColumns Methode nimmt zwei Parameter:

- Spaltenindex, der Index der Spalte, von der die Spalte eingefügt werden soll.
- Anzahl der Spalten, Gesamtanzahl der Spalten, die eingefügt werden müssen.

**PHP-Code**

{{< highlight php >}}

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
### **Löschen einer Spalte**
Um eine Spalte aus dem Arbeitsblatt an einer beliebigen Stelle zu löschen, rufen Sie die Methode deleteColumns der Cells Sammlung auf. Die deleteColumns Methode nimmt die folgenden Parameter:

- Spaltenindex, der Index der Spalte, von der die Spalte gelöscht werden soll.
- Anzahl der Spalten, Gesamtanzahl der Spalten, die gelöscht werden müssen.
- Zellen verschieben, Boolescher Parameter, um anzuzeigen, ob die Zellen nach dem Löschen nach links verschoben werden sollen.

**PHP-Code**

{{< highlight php >}}

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
## **Laufenden Code herunterladen**
**Zeilen/Spalten verwalten (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
