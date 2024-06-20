---
title: Nascondere e mostrare righe e colonne in PHP
type: docs
weight: 50
url: /it/java/hiding-and-showing-rows-and-columns-in-php/
description: Scopri come nascondere e mostrare righe e colonne attraverso le API Aspose.Cells per PHP via Java.
keywords: Come nascondere e mostrare righe e colonne in PHP, Nascondi righe o colonne usando PHP, PHP Mostra righe o colonne. 
---

## **Aspose.Cells per PHP - Controllo della visibilità di righe e colonne**
### **Come nascondere righe e colonne in PHP**
Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi HideRow e HideColumn della collezione Cells. Entrambi i metodi accettano l'indice di riga/colonna come parametro per nascondere la riga o colonna specifica.

**Codice PHP**

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
### **Come mostrare righe e colonne utilizzando PHP**
Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi UnhideRow e UnhideColumn della collezione Cells. Entrambi i metodi accettano due parametri:

- **Indice di riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza riga o larghezza colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo che è stata mostrata.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Controllo della visibilità delle righe e delle colonne (Aspose.Cells)** da uno dei siti di codifica sociali di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
