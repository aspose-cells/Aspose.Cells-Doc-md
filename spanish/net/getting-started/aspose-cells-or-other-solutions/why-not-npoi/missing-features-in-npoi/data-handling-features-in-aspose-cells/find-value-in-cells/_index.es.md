---
title: Encuentra Valor en Cells
type: docs
weight: 20
url: /es/net/find-value-in-cells/
---
## **Aspose.Cells - Buscar valor en Cells**
En Microsoft Excel, los usuarios pueden buscar celdas que contengan datos específicos. Por ejemplo, hacer clic en**Editar**y entonces**Encontrar**abre el cuadro de diálogo Buscar. Los usuarios ingresan un valor y hacen clic**OK**para buscarlo Excel resalta los campos coincidentes.

**C#**

{{< highlight "cs" >}}

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
## **Descargar código de ejecución**
 Descargar**Encuentra Valor en Cells** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Buscar o buscar datos](/cells/es/net/find-or-search-data/).

{{% /alert %}}
