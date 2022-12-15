---
title: Ordina i dati nei fogli di calcolo
type: docs
weight: 70
url: /it/java/sort-data-in-spreadsheets/
---
## **Aspose.Cells - Ordina i dati nei fogli di calcolo**
{{% alert color="primary" %}} 

Per ordinare i dati nel foglio di calcolo utilizzando Aspose.Cells, è sufficiente richiamare il metodo DataSorter.sorter() dopo aver impostato alcune proprietà facili da impostare dell'area della cella.

Il codice Java è menzionato di seguito.

{{% /alert %}} 

Ordina i dati utilizzando Aspose.Cells

**Giava**

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Ordina dati](/java/sort-data) , o[Ordinamento dei dati](/cells/it/java/data-sorting).

{{% /alert %}}
