---
title: Establecer el color de la pestaña de la hoja de cálculo en Aspose.Cells
type: docs
weight: 20
url: /es/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Establecer el color de la pestaña de la hoja de cálculo**
Aspose.Cells te permite cambiar el color de las pestañas individuales de las hojas de cálculo para hacerlas más destacadas. Por ejemplo, puedes hacer que Gastos sean rojos, Ventas verdes, Activos azules, etc.
### **Establecer el color de la pestaña de la hoja de cálculo con Microsoft Excel**
1. Haz clic derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de cálculo actual.
1. Selecciona **Color de pestaña**.
1. Selecciona un color de la paleta.
1. Haz clic en **Aceptar**.

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Establecer el color de la pestaña de la hoja de cálculo** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Para más detalles, visita [Establecer el color de la pestaña de la hoja de cálculo](/cells/es/net/set-worksheet-tab-color/).

{{% /alert %}}
