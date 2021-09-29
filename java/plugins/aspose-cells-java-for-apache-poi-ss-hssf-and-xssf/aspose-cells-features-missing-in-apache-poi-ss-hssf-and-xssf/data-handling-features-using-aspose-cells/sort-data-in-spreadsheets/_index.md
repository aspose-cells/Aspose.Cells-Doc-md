---
title: Sort Data in Spreadsheets
type: docs
weight: 70
url: /java/sort-data-in-spreadsheets/
---

## **Aspose.Cells - Sort Data in Spreadsheets**
{{% alert color="primary" %}} 

To sort data in spreadsheet using Aspose.Cells, simply invoke the DataSorter.sorter() method after setting few easy to set properties of cell area.

Java code is mentioned below.

{{% /alert %}} 

Sort Data using Aspose.Cells

**Java**

{{< highlight java >}}

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

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

For more details, visit [Sort Data](http://docs.aspose.com:8082/docs/display/cellsjava/Sort+Data), or [Data Sorting](http://docs.aspose.com:8082/docs/display/cellsjava/Data+Sorting).

{{% /alert %}}
