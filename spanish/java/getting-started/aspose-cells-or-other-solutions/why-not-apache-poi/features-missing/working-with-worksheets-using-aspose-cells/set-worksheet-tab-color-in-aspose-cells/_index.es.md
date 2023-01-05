---
title: Establecer el color de la pestaña de la hoja de trabajo en Aspose.Cells
type: docs
weight: 90
url: /es/java/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Establecer el color de la pestaña de la hoja de trabajo**
Aspose.Cells le permite cambiar el color de las pestañas individuales de la hoja de trabajo para que se destaquen del resto. Por ejemplo, puede hacer que Gastos sea rojo, Ventas verde, Activos azul, etc.
#### **Configuración del color de la pestaña de la hoja de trabajo con Microsoft Excel**
1. Haga clic con el botón derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de trabajo actual.
1. Seleccione**color de pestaña**.
1. Seleccione un color de la paleta.
1. Hacer clic**DE ACUERDO**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Establecer el color de la pestaña de la hoja de trabajo](/java/set-worksheet-tab-color).

{{% /alert %}}
