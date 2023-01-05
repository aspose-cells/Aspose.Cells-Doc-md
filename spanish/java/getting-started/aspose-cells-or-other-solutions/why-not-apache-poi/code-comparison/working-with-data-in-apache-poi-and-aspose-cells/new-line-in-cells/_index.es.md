---
title: Nueva Linea en Cells
type: docs
weight: 30
url: /es/java/new-line-in-cells/
---
## **Aspose.Cells - Nueva Línea en Cells**
Para garantizar que se pueda leer el texto de una celda, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, cuyos saltos de línea explícitos los colocan exactamente donde los desea.

Para ajustar texto en una celda, use el método Style.setTextWrapped.

**Java**

{{< highlight "java" >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Nueva línea en Cells**
CellStyle.setWrapText debe ser verdadero para el texto ajustado.

**Java**

{{< highlight "java" >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

 Para más detalles, visite[Saltos de línea y ajuste de texto](/java/line-breaks-and-text-wrapping).

{{% /alert %}}
