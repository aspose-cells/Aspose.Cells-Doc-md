---
title: Regolazione dell altezza della riga e della larghezza della colonna in PHP
type: docs
weight: 10
url: /it/java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - Regolazione dell'altezza della riga e della larghezza della colonna**
### **Impostazione dell'altezza della riga**
È possibile impostare l'altezza di una singola riga chiamando il metodo setRowHeight della collezione Cells. Il metodo setRowHeight richiede i seguenti parametri:

- **Indice di riga**, l'indice della riga a cui si sta modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

**Codice PHP**

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
### **Impostazione della larghezza della colonna**
Imposta la larghezza di una colonna chiamando il metodo setColumnWidth della collezione Cells. Il metodo setColumnWidth richiede i seguenti parametri:

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.
- **Larghezza di colonna**, la larghezza desiderata della colonna.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Regolazione dell'altezza della riga e della larghezza della colonna (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale citati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
