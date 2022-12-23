---
title: Trier les données en xlsx4j
type: docs
weight: 60
url: /fr/java/sort-data-in-xlsx4j/
---
## **Aspose.Cells - Trier les données**
Pour trier les données dans une feuille de calcul à l'aide de Aspose.Cells, appelez simplement la méthode DataSorter.sorter() après avoir défini quelques propriétés faciles à définir de la zone de cellule.
Le code Java est mentionné ci-dessous :

**Java**

{{< highlight "java" >}}

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

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/sortdata/AsposeDataSort.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Trier les données](/java/sort-data) ou alors[Tri des données](/cells/fr/java/data-sorting).

{{% /alert %}}
