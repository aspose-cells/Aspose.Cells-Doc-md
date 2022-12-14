---
title: Justera radhöjd och kolumnbredd i PHP
type: docs
weight: 10
url: /sv/java/adjusting-row-height-and-column-width-in-php/
---
## **Aspose.Cells - Justering av radhöjd och kolumnbredd**
### **Ställa in radhöjden**
Det är möjligt att ställa in höjden på en enda rad genom att anropa Cells-samlingens setRowHeight-metod. Metoden setRowHeight tar följande parametrar:

- **Radindex**, indexet för raden som du ändrar höjden på.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

**PHP-kod**

{{< highlight "php" >}}

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
### **Ställa in kolumnbredden**
Ställ in bredden på en kolumn genom att anropa Cells-samlingens setColumnWidth-metod. Metoden setColumnWidth tar följande parametrar:

- **Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- **Kolumnbredd**, önskad kolumnbredd.

**PHP-kod**

{{< highlight "php" >}}

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
## **Ladda ner Running Code**
Ladda ner**Justera radhöjd och kolumnbredd (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
