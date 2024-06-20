---
title: Autoadatta righe e colonne in PHP
type: docs
weight: 20
url: /it/java/autofit-rows-and-columns-in-php/
---

## **Aspose.Cells - Adattamento automatico delle righe e delle colonne**
### **Adatta automaticamente la riga**
Il modo più diretto per dimensionare automaticamente la larghezza e l'altezza di una riga è chiamare il metodo autoFitRow della classe Worksheet. Il metodo autoFitRow prende come parametro l'indice della riga da ridimensionare.

**Codice PHP**

{{< highlight php >}}

 public static function autofit_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 3rd row of the worksheet

    $worksheet->autoFitRow(2);

    # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

    # cells (from 1st to 9th column) within the row

    #$worksheet->autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Row.xls");

    print "Autofit Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Adatta automaticamente la colonna**
Il modo più semplice per dimensionare automaticamente la larghezza e l'altezza di una colonna è chiamare il metodo autoFitColumn della classe Worksheet. Il metodo autoFitColumn prendere l'indice della colonna da ridimensionare come parametro.

**Codice PHP**

{{< highlight php >}}

 public static function autofit_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 4th column of the worksheet

    $worksheet->autoFitColumn(3);

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #$worksheet->autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Column.xls");

    print "Autofit Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Adatta automaticamente righe e colonne (Aspose.Cells)** da uno dei seguenti siti di social coding:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
