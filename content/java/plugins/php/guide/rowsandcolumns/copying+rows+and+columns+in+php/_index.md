---
title : "Copying Rows and Columns in PHP" 
description : "" 
weight : 20843 
toc : false
type: docs
url: /java/plugins/php/guide/rowsandcolumns/copying+rows+and+columns+in+php/
---

# Aspose.Cells for Java : Copying Rows and Columns in PHP


## Aspose.Cells - Copying Rows and Columns

##### Copying Rows

Aspose.Cells provides the`copyRow`method of the`Cells`class. This method copies all types of data including formulas, values, comments, cell formats, hidden cells, images and other drawing objects from the source row to the destination row.

The`copyRow`method takes the following parameters:

*   the source`Cells`object,
*   the source row index, and
*   the destination row index.

**PHP Code**

{{< code lang="cs" >}}
public static function copy_rows($dataDir)
{

    # Instantiating a Workbook object by excel file path
    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file
    $worksheet = $workbook->getWorksheets()->get(0);

    # Copy the second row with data, formattings, images and drawing objects
    # to the 12th row in the $worksheet->
    $worksheet->getCells()->copyRow($worksheet->getCells(),1,11);

    # Saving the modified Excel file in default (that is Excel 2003) format
    $workbook->save($dataDir . "Copy Rows.xls");

    print "Copy Rows Successfully." . PHP_EOL;

}
{{< /code >}}

##### Copying Columns

Aspose.Cells provides the`copyColumn`method of the`Cells`class, this method copies all types of data, including formulas - with updated references - and values, comments, cell formats, hidden cells, images and other drawing objects from the source column to the destination column.

The`copyColumn`method takes the following parameters:

*   the source`Cells`object,
*   source column index, and
*   the destination column index.

**PHP Code**

{{< code lang="cs" >}}
public static function copy_columns($dataDir)
{

    # Instantiating a Workbook object by excel file path
    $workbook = new Workbook();

    # Accessing the first worksheet in the Excel file
    $worksheet = $workbook->getWorksheets()->get(0);

    # Put some data into header rows (A1:A4)
    $i = 0;
    while($i < 5)
    {
        $worksheet->getCells()->get($i, 0)->setValue("Header Row #$i");
        $i++;

    }


    # Put some detail data (A5:A999)
    $i = 5;
    while ($i < 1000) {

        $worksheet->getCells()->get($i, 0)->setValue("Detail Row #$i");
        $i++;
    }

    # Create another Workbook.
    $workbook1 = new Workbook();

    # Get the first worksheet in the book.
    $worksheet1 = $workbook1->getWorksheets()->get(0);

    # Copy the first column from the first worksheet of the first workbook into
    # the first worksheet of the second workbook.
    $worksheet1->getCells()->copyColumn($worksheet->getCells(),0,2);

    # Autofit the column.
    $worksheet1->autoFitColumn(2);

    # Saving the modified Excel file in default (that is Excel 2003) format
    $workbook->save($dataDir . "Copy Columns.xls");

    print "Copy Columns Successfully." . PHP_EOL;

}
{{< /code >}}

## Download Running Code

Download **Copying Rows and Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)

