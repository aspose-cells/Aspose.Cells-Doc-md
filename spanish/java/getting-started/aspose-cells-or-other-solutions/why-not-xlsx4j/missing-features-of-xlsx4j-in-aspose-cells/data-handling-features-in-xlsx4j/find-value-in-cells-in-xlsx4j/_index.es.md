---
title: Buscar valor en Cells en xlsx4j
type: docs
weight: 30
url: /es/java/find-value-in-cells-in-xlsx4j/
---
## **Aspose.Cells - Buscar valor en Cells**
En Microsoft Excel, los usuarios pueden buscar celdas que contengan datos específicos. Por ejemplo, hacer clic en**Editar**y luego**Encontrar**abre el cuadro de diálogo Buscar. Los usuarios ingresan un valor y hacen clic**DE ACUERDO**para buscarlo Excel resalta los campos coincidentes.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Buscar o buscar datos](/cells/es/java/find-or-search-data).

{{% /alert %}}
