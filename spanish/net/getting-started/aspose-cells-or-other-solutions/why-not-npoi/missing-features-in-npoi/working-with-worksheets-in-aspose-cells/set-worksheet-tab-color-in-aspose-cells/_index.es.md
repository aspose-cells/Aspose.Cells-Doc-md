---
title: Establecer el color de la pestaña de la hoja de trabajo en Aspose.Cells
type: docs
weight: 20
url: /es/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Establecer el color de la pestaña de la hoja de trabajo**
Aspose.Cells le permite cambiar el color de las pestañas individuales de la hoja de trabajo para que se destaquen del resto. Por ejemplo, puede hacer que Gastos sea rojo, Ventas verde, Activos azul, etc.
### **Configuración del color de la pestaña de la hoja de trabajo con Microsoft Excel**
1. Haga clic con el botón derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de trabajo actual.
1. Seleccione**color de pestaña**.
1. Seleccione un color de la paleta.
1. Hacer clic**OK**.

**C#**

{{< highlight "cs" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Establecer el color de la pestaña de la hoja de trabajo** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Establecer el color de la pestaña de la hoja de trabajo](/cells/es/net/set-worksheet-tab-color/).

{{% /alert %}}
