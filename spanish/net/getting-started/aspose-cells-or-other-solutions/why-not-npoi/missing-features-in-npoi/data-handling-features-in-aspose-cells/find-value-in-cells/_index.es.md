---
title: Encontrar Valor en Celdas
type: docs
weight: 20
url: /es/net/find-value-in-cells/
---

## **Aspose.Cells - Encontrar Valor en Celdas**
En Microsoft Excel, los usuarios pueden buscar celdas que contienen datos específicos. Por ejemplo, al hacer clic en **Editar** y luego en **Buscar**, se abre el cuadro de diálogo de búsqueda. Los usuarios ingresan un valor y hacen clic en **Aceptar** para buscarlo. Excel resalta los campos coincidentes.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Encontrar Valor en Celdas** desde cualquiera de los sitios de código social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Para más detalles, visita [Encontrar o Buscar Datos](/cells/es/net/find-or-search-data/).

{{% /alert %}}
