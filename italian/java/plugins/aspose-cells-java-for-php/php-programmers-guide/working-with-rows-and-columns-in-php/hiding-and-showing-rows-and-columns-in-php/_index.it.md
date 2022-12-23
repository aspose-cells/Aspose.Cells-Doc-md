---
title: Nascondere e mostrare righe e colonne in PHP
type: docs
weight: 50
url: /it/java/hiding-and-showing-rows-and-columns-in-php/
---
## **Aspose.Cells - Controllo della visibilità di righe e colonne**
### **Nascondere righe e colonne**
Gli sviluppatori possono nascondere una riga o una colonna chiamando rispettivamente i metodi HideRow e HideColumn della raccolta Cells. Entrambi i metodi accettano l'indice riga/colonna come parametro per nascondere la riga o colonna specifica.

**Codice PHP**

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
### **Visualizzazione di righe e colonne**
Gli sviluppatori possono visualizzare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi UnhideRow e UnhideColumn della raccolta Cells. Entrambi i metodi accettano due parametri:

- **Indice riga o colonna**- l'indice di una riga o di una colonna utilizzato per mostrare la riga o la colonna specifica.
- **Altezza riga o larghezza colonna**- l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo che è stata mostrata.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
 Scaricamento**Controllo della visibilità di righe e colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
