---
title: Justera radhöjd och kolumnbredd i PHP
type: docs
weight: 10
url: /sv/java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - Justera radhöjd och kolumnbredd**
### **Ange radhöjden**
Det är möjligt att ange höjden för en enskild rad genom att anropa samlingen för 'cells' 'setRowHeight' -metoden.

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

**PHP-kod**

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
### **Ange kolumnbredden**
Ange bredden på en kolumn genom att anropa samlingen 'cells' 'setColumnWidth' -metoden.

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Justera radhöjd och kolumnbredd (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
