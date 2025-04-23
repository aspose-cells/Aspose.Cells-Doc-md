---
title: Daten in Tabellenblättern sortieren
type: docs
weight: 70
url: /de/java/sort-data-in-spreadsheets/
---

## **Aspose.Cells - Daten in Tabellenblättern sortieren**
{{% alert color="primary" %}} 

Um Daten in Tabellenblatt mit Aspose.Cells zu sortieren, rufen Sie einfach die Methode DataSorter.sorter() auf und setzen Sie einige leicht zu setzende Eigenschaften des Zellbereichs.

Der Java-Code ist unten aufgeführt.

{{% /alert %}} 

Daten mit Aspose.Cells sortieren

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Daten sortieren](/java/sort-data) oder [Daten sortieren](/cells/de/java/data-sorting).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
