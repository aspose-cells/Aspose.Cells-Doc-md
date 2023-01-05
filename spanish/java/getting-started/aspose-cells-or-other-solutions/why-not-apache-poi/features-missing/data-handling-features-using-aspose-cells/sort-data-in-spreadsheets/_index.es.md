---
title: Ordenar datos en hojas de cálculo
type: docs
weight: 70
url: /es/java/sort-data-in-spreadsheets/
---
## **Aspose.Cells - Ordenar datos en hojas de cálculo**
{{% alert color="primary" %}} 

Para ordenar los datos en la hoja de cálculo usando Aspose.Cells, simplemente invoque el método DataSorter.sorter() después de configurar algunas propiedades fáciles de configurar del área de la celda.

El código Java se menciona a continuación.

{{% /alert %}} 

Ordenar datos usando Aspose.Cells

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
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Ordenar datos](/java/sort-data) , o[Clasificación de datos](/cells/es/java/data-sorting).

{{% /alert %}}
