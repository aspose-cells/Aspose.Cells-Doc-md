---
title: Kopieren von Zeilen und Spalten in PHP
type: docs
weight: 30
url: /de/java/copying-rows-and-columns-in-php/
---

## **Aspose.Cells - Kopieren von Zeilen und Spalten**
### **Kopieren von Zeilen**
Aspose.Cells bietet die Methode copyRow der Klasse Cells. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, versteckte Zellen, Bilder und andere Zeichenobjekte von der Quellzeile in die Zielzeile.

Die Methode copyRow erhält die folgenden Parameter:

- das Quell-Cells-Objekt,
- den Index der Quellzeile, und
- den Index der Zielzeile.

**PHP-Code**

{{< highlight php >}}

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
### **Spalten kopieren**
Aspose.Cells bietet die Methode copyColumn der Klasse Cells. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln - mit aktualisierten Verweisen - und Werten, Kommentaren, Zellformate, versteckte Zellen, Bilder und andere Zeichenobjekte von der Quellspalte in die Zielspalte.

Die Methode copyColumn erhält die folgenden Parameter:

- das Quell-Cells-Objekt,
- Quellspaltenindex, und
- der Zielspaltenindex.

**PHP-Code**

{{< highlight php >}}

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
## **Laufenden Code herunterladen**
Das Kopieren von Zeilen und Spalten (Aspose.Cells) von einer der unten genannten sozialen Codierungsseiten herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
