---
title: Inserimento ed eliminazione di righe e colonne in PHP
type: docs
weight: 60
url: /it/java/inserting-and-deleting-rows-and-columns-in-php/
---
## **Aspose.Cells - Gestione Righe/Colonne**
### **Inserimento di una riga**
Inserisci una riga in qualsiasi posizione chiamando il metodo insertRows della raccolta Cells. Il metodo insertRows accetta l'indice della riga in cui verrà inserita la nuova riga come primo argomento e il numero di righe da inserire come secondo argomento.

**Codice PHP**

{{< highlight "php" >}}

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
### **Inserimento di più righe**
Per inserire più righe nel foglio di lavoro, chiama il metodo insertRows della raccolta Cells. Il metodo InsertRows accetta due parametri:

- Indice di riga, l'indice della riga da cui verranno inserite le nuove righe.
- Numero di righe, numero totale di righe da inserire.

**Codice PHP**

{{< highlight "php" >}}

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
### **Eliminazione di una riga**
Per eliminare una riga in qualsiasi posizione, chiama il metodo deleteRows della raccolta Cells. Il metodo DeleteRows accetta due parametri:

- Indice di riga, l'indice della riga da cui verranno eliminate le righe.
- Numero di righe, numero totale di righe che devono essere eliminate.

**Codice PHP**

{{< highlight "php" >}}

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
### **Eliminazione di più righe**
Per eliminare più righe da un foglio di lavoro, chiama il metodo deleteRows della raccolta Cells. Il metodo DeleteRows accetta due parametri:

- Indice di riga, l'indice della riga da cui verranno eliminate le righe.
- Numero di righe, numero totale di righe che devono essere eliminate.

**Codice PHP**

{{< highlight "php" >}}

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
### **Inserimento di una colonna**
Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo insertColumns della raccolta Cells. Il metodo insertColumns accetta due parametri:

- Indice colonna, l'indice della colonna da cui verrà inserita la colonna
- Numero di colonne, numero totale di colonne da inserire

**Codice PHP**

{{< highlight "php" >}}

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
### **Eliminazione di una colonna**
Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiama il metodo deleteColumns della raccolta Cells. Il metodo deleteColumns accetta i seguenti parametri:

- Indice colonna, l'indice della colonna da cui verrà eliminata la colonna.
- Numero di colonne, numero totale di colonne che devono essere eliminate.
- Shift celle, parametro booleano per indicare se spostare le celle a sinistra dopo la cancellazione.

**Codice PHP**

{{< highlight "php" >}}

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
## **Scarica il codice in esecuzione**
 Scaricamento**Gestione righe/colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
