+++
title = "Sort Data in xlsx4j" 
description = "" 
weight = 20669 
+++

Aspose.Cells for Java : Sort Data in xlsx4j  

# Aspose.Cells for Java : Sort Data in xlsx4j


## Aspose.Cells - Sort Data

To sort data in spreadsheet using Aspose.Cells, simply invoke the `DataSorter.sorter()` method after setting few easy to set properties of cell area.  
Java code is mentioned below:

**Java**

{{< code lang="java" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook(dataDir + "AsposeDataInput.xls");

//Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.getWorksheets().get(0);

//Get the cells collection in the sheet
Cells cells = worksheet.getCells();

//Obtain the DataSorter object in the workbook
DataSorter sorter = workbook.getDataSorter();

//Set the first order
sorter.setOrder1(SortOrder.ASCENDING);

//Define the first key.
sorter.setKey1(0);

//Set the second order
sorter.setOrder2(SortOrder.ASCENDING);

//Define the second key
sorter.setKey2(1);

//Create a cells area (range).
CellArea ca = new CellArea();

//Specify the start row index.
ca.StartRow = 1;
//Specify the start column index.
ca.StartColumn = 0;
//Specify the last row index.
ca.EndRow = 9;
//Specify the last column index.
ca.EndColumn = 2;

//Sort data in the specified data range (A2:C10)
sorter.sort(cells, ca);

//Saving the excel file
workbook.save(dataDir + "AsposeSortedData_Out.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/sortdata/AsposeDataSort.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/sortdata/AsposeDataSort.java)

For more details, visit [Sort Data](http://docs.aspose.com:8082/docs/display/cellsjava/Sort+Data) or [Data Sorting](http://docs.aspose.com:8082/docs/display/cellsjava/Data+Sorting).

