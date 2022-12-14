---
title: Trier des données dans des feuilles de calcul
type: docs
weight: 70
url: /fr/java/sort-data-in-spreadsheets/
---
## **Aspose.Cells - Trier les données dans les feuilles de calcul**
{{% alert color="primary" %}} 

Pour trier les données dans une feuille de calcul à l'aide de Aspose.Cells, appelez simplement la méthode DataSorter.sorter() après avoir défini quelques propriétés faciles à définir de la zone de cellule.

Le code Java est mentionné ci-dessous.

{{% /alert %}} 

Trier les données en utilisant Aspose.Cells

**Java**

{{< highlight "java" >}}

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
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Trier les données](/java/sort-data) , ou[Tri des données](/cells/fr/java/data-sorting).

{{% /alert %}}
