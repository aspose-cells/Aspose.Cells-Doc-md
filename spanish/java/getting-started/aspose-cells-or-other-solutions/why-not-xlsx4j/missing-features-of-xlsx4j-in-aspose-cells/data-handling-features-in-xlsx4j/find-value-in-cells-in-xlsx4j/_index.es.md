---
title: Encontrar Valor en Celdas en xlsx4j
type: docs
weight: 30
url: /es/java/find-value-in-cells-in-xlsx4j/
---

## **Aspose.Cells - Encontrar Valor en Celdas**
En Microsoft Excel, los usuarios pueden buscar celdas que contienen datos específicos. Por ejemplo, al hacer clic en **Editar** y luego en **Buscar**, se abre el cuadro de diálogo de búsqueda. Los usuarios ingresan un valor y hacen clic en **Aceptar** para buscarlo. Excel resalta los campos coincidentes.

**Java**

{{< highlight java >}}

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
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Buscar o Buscar Datos](/cells/es/java/find-or-search-data)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
