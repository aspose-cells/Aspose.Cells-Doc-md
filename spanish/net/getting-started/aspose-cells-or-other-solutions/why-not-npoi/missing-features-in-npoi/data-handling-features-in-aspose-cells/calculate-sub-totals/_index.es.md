---
title: Calcular Subtotales
type: docs
weight: 10
url: /es/net/calculate-sub-totals/
---

## **Aspose.Cells - Calcular Subtotales**
Puedes crear automáticamente subtotales para cualquier valor que se repita en una hoja de cálculo. Aspose.Cells proporciona funciones de API que te ayudan a agregar subtotales a las hojas de cálculo de forma programática.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Calcular Subtotales** desde cualquiera de los sitios de código social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Para más detalles, visita [Creando Subtotales](/cells/es/net/creating-subtotals/).

{{% /alert %}}
