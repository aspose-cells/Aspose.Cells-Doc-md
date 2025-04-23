---
title: Establecer el color de la pestaña de la hoja de cálculo en xlsx4j
type: docs
weight: 60
url: /es/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - Establecer el color de la pestaña de la hoja de cálculo**
Aspose.Cells te permite cambiar el color de las pestañas individuales de las hojas de cálculo para hacerlas más destacadas. Por ejemplo, puedes hacer que Gastos sean rojos, Ventas verdes, Activos azules, etc.
### **Establecer el color de la pestaña de la hoja de cálculo con Microsoft Excel**
1. Haz clic derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de cálculo actual.
1. Selecciona **Color de pestaña**.
1. Selecciona un color de la paleta.
1. Haz clic en **Aceptar**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Establecer color de pestaña de hoja de trabajo](/java/set-worksheet-tab-color).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
