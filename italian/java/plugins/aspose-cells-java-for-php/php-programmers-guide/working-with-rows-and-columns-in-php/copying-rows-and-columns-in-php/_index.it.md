---
title: Copiare righe e colonne in PHP
type: docs
weight: 30
url: /it/java/copying-rows-and-columns-in-php/
---
## **Aspose.Cells - Copia di righe e colonne**
### **Copia di righe**
Aspose.Cells fornisce il metodo copyRow della classe Cells. Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla riga di origine alla riga di destinazione.

Il metodo copyRow accetta i seguenti parametri:

- l'oggetto sorgente Cells,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

**Codice PHP**

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
### **Copia di colonne**
Aspose.Cells fornisce il metodo copyColumn della classe Cells, questo metodo copia tutti i tipi di dati, incluse formule - con riferimenti aggiornati - e valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti di disegno dalla colonna di origine alla colonna di destinazione.

Il metodo copyColumn accetta i seguenti parametri:

- l'oggetto sorgente Cells,
- indice della colonna di origine e
- l'indice della colonna di destinazione.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scaricamento**Copia di righe e colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
