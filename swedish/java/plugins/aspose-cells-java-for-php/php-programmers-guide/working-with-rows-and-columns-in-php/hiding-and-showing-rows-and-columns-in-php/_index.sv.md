---
title: Dölja och visa rader och kolumner i PHP
type: docs
weight: 50
url: /sv/java/hiding-and-showing-rows-and-columns-in-php/
description: Lär dig hur man döljer och visar rader och kolumner genom Aspose.cells för PHP via Java API er.
keywords: Hur man döljer och visar rader och kolumner i PHP, dölj rader eller kolumner med hjälp av PHP, PHP Visa rader eller kolumner. 
---

## **Aspose.Cells för PHP - Kontrollera synligheten för rader och kolumner**
### **Hur man döljer rader och kolumner i PHP**
Utvecklare kan dölja en rad eller kolumn genom att anropa HideRow och HideColumn metoderna i Cells-kollektionen respektive. Båda metoderna tar rad/kolumnindexet som parameter för att dölja den specifika raden eller kolumnen.

**PHP-kod**

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
### **Hur man visar rader och kolumner med PHP**
Utvecklare kan återvisa dolda rader eller kolumner genom att anropa UnhideRow och UnhideColumn metoderna i Cells-kollektionen respektive. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjd eller kolumnbredd tilldelad till raden eller kolumnen efter att den visas.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Kontrollera synligheten av rader & kolumner (Aspose.Cells)** från någon av nedanstående sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
