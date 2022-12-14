---
title: Infoga och ta bort rader och kolumner i PHP
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns-in-php/
---
## **Aspose.Cells - Hantera rader/kolumner**
### **Infoga en rad**
Infoga en rad på valfri plats genom att anropa metoden insertRows i samlingen Cells. Metoden insertRows tar indexet för raden där den nya raden kommer att infogas som det första argumentet, och antalet rader som ska infogas som det andra argumentet.

**PHP-kod**

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
### **Infoga flera rader**
Om du vill infoga flera rader i kalkylbladet anropar du metoden insertRows i samlingen Cells. Metoden InsertRows tar två parametrar:

- Radindex, indexet för raden varifrån de nya raderna kommer att infogas.
- Antal rader, totalt antal rader som behöver infogas.

**PHP-kod**

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
### **Ta bort en rad**
För att ta bort en rad på valfri plats, anropa metoden deleteRows för samlingen Cells. Metoden DeleteRows tar två parametrar:

- Radindex, indexet för raden där raderna kommer att tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**PHP-kod**

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
### **Ta bort flera rader**
Om du vill ta bort flera rader från ett kalkylblad anropar du metoden deleteRows i samlingen Cells. Metoden DeleteRows tar två parametrar:

- Radindex, indexet för raden där raderna kommer att tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**PHP-kod**

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
### **Infoga en kolumn**
Utvecklare kan också infoga en kolumn i kalkylbladet var som helst genom att anropa metoden insertColumns i samlingen Cells. metoden insertColumns tar två parametrar:

- Kolumnindex, indexet för den kolumn varifrån kolumnen kommer att infogas
- Antal kolumner, totalt antal kolumner som behöver infogas

**PHP-kod**

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
### **Ta bort en kolumn**
För att ta bort en kolumn från kalkylbladet på valfri plats, anropa metoden deleteColumns i samlingen Cells. Metoden deleteColumns använder följande parametrar:

- Kolumnindex, indexet för den kolumn där kolumnen kommer att tas bort.
- Antal kolumner, totalt antal kolumner som behöver raderas.
- Skift celler, boolesk parameter för att indikera om cellerna ska flyttas åt vänster efter radering.

**PHP-kod**

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
## **Ladda ner Running Code**
 Ladda ner**Hantera rader/kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
