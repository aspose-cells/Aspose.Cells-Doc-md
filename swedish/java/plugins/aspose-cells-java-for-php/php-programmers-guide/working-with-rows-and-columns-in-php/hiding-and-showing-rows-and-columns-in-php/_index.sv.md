---
title: Dölja och visa rader och kolumner i PHP
type: docs
weight: 50
url: /sv/java/hiding-and-showing-rows-and-columns-in-php/
description: "Lär dig hur du döljer och visar rader och kolumner genom API:erna Aspose.Cells for PHP via Java."
keywords: How to Hide and Show Rows and Columns in PHP, Hide Rows or Columns using PHP, PHP Show Rows or Columns. 
---
##  **Aspose.Cells for PHP - Kontrollera synligheten för rader och kolumner**
###  **Hur man döljer rader och kolumner i PHP**
Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna HideRow och HideColumn i samlingen Cells. Båda metoderna tar rad/kolumnindex som en parameter för att dölja den specifika raden eller kolumnen.

**PHP-kod**

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
###  **Hur man visar rader och kolumner med PHP**
Utvecklare kan visa alla dolda rader eller kolumner genom att anropa metoderna UnhideRow och UnhideColumn i samlingen Cells. Båda metoderna tar två parametrar:

- **Rowor kolumnindex**indexet för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd**- radhöjden eller kolumnbredden som tilldelats raden eller kolumnen efter att den har visats.

**PHP-kod**

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
##  **Ladda ner Running Code**
 Ladda ner**Kontrollera synligheten för rader och kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
