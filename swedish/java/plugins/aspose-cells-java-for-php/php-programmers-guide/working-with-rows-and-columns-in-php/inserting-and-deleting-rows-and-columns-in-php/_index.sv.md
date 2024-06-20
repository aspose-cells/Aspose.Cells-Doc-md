---
title: Infoga och ta bort rader och kolumner i PHP
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns-in-php/
description: Lär dig hur man infogar och tar bort rader och kolumner genom Aspose.cells för PHP via Java API er.
keywords: Hur man infogar och tar bort rader och kolumner i PHP, infoga rader och kolumner med hjälp av PHP, ta bort rader och kolumner med PHP, infoga rader eller kolumner med PHP, ta bort rader eller kolumner via PHP.
---

## **Aspose.Cells - Hantera rader/kolumner**
### **Infoga en rad**
Infoga en rad på valfri plats genom att anropa insertRows metoden i Cells-kollektionen. insertRows metoden tar indexet för raden där den nya raden ska infogas som första argument, och antalet rader som ska infogas som andra argument.

**PHP-kod**

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
### **Infoga flera rader**
För att infoga flera rader i arket, anropa insertRows metoden i Cells-kollektionen. InsertRows metoden tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, totalt antal rader som behöver infogas.

**PHP-kod**

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
### **Ta bort en rad**
För att ta bort en rad på valfri plats, anropa deleteRows metoden i Cells-kollektionen. DeleteRows metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**PHP-kod**

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
### **Ta bort flera rader**
För att ta bort flera rader från ett kalkylblad, anropa deleteRows metoden i Cells-kollektionen. DeleteRows metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**PHP-kod**

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
### **Infoga en kolumn**
Utvecklare kan också infoga en kolumn i arbetsbladet på valfri plats genom att anropa metoden insertColumns i Cells-samlingen. insertColumns-metoden tar två parametrar:

- Kolumnindex, index av kolumn där kolumnen ska infogas
- Antal kolumner, totalt antal kolumner som behöver infogas

**PHP-kod**

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
### **Ta bort en kolumn**
För att ta bort en kolumn från arbetsbladet på valfri plats, anropas deleteColumns-metoden i Cells-samlingen. deleteColumns-metoden tar följande parametrar:

- Kolumnindex, index av kolumn där kolumnen ska tas bort.
- Antal kolumner, totalt antal kolumner som behöver tas bort.
- Skifta celler, en boolesk parameter för att indikera om cellerna ska skiftas åt vänster efter borttagning.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ned **Hantering av rader/kolumner (Aspose.Cells)** från någon av de nämnda sociala kodsajterna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
