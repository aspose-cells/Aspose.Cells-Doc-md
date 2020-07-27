+++
title = "Grouping and Ungrouping Rows and Columns in PHP" 
description = "" 
weight = 20844 
+++

Aspose.Cells for Java : Grouping and Ungrouping Rows and Columns in PHP  

# Aspose.Cells for Java : Grouping and Ungrouping Rows and Columns in PHP


## Aspose.Cells - Group Management of Rows & Columns

##### Grouping Rows & Columns

It is possible to group rows or columns by calling the`groupRows`and`groupColumns`methods of the`Cells`collection. Both methods take the following parameters:

*   First row/column index, the first row or column in the group.
*   Last row/column index, the last row or column in the group.
*   Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.

**PHP Code**

{{< code lang="cs" >}}
public static function group_rows_columns($dataDir)
{

    # Instantiating a Workbook object by excel file path
    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file
    $worksheet = $workbook->getWorksheets()->get(0);
    $cells = $worksheet->getCells();;

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true
    $cells->groupRows(0,5,true);

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true
    $cells->groupColumns(0,2,true);

    # Saving the modified Excel file in default (that is Excel 2003) format
    $workbook->save($dataDir . "Group Rows And Columns.xls");

    print "Group Rows And Columns Successfully." . PHP_EOL;

}
{{< /code >}}

##### Ungrouping Rows & Columns

Ungroup grouped rows or columns by calling the`Cells`collection's`UngroupRows`and`UngroupColumns`methods. Both methods take the same parameters:

*   First row or column index, the first row/column to be ungrouped.
*   Last row or column index, the last row/column to be ungrouped.

**PHP Code**

{{< code lang="cs" >}}
public static function ungroup_rows_columns($dataDir)
{

    # Instantiating a Workbook object by excel file path
    $workbook = new Workbook($dataDir . 'Group Rows And Columns.xls');

    # Accessing the first worksheet in the Excel file
    $worksheet = $workbook->getWorksheets()->get(0);
    $cells = $worksheet->getCells();;

    # Ungrouping first six rows (from 0 to 5)
    $cells->ungroupRows(0,5);

    # Ungrouping first three columns (from 0 to 2)
    $cells->ungroupColumns(0,2);

    # Saving the modified Excel file in default (that is Excel 2003) format
    $workbook->save($dataDir . "Ungroup Rows And Columns.xls");

    print "Ungroup Rows And Columns Successfully." . PHP_EOL;

}
{{< /code >}}

## Download Running Code

Download **Group & Ungroup Rows & Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)

