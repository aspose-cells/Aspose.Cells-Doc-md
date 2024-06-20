---
title: Trabajando con bordes en Apache POI y Aspose.Cells
type: docs
weight: 10
url: /es/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Trabajando con bordes**
Aspose.Cells proporciona una clase, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). La clase Worksheet proporciona una colección de Celdas. Cada elemento en la colección de Celdas representa un objeto de la clase [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells proporciona el método setStyle en la clase [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) usado para establecer el estilo de formato de una celda. Además, el objeto Style de la clase [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) es utilizado y proporciona propiedades para configurar la configuración de fuente.

**Java**

{{< highlight java >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Trabajando con bordes**
La clase CellStyle proporciona características para establecer la configuración de bordes usando Apache POI SS - HSSF and XSSF.

**Java**

{{< highlight java >}}

 //Setting the line of the top border

style.setBorder(BorderType.TOP_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the bottom border

style.setBorder(BorderType.BOTTOM_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the left border

style.setBorder(BorderType.LEFT_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the right border

style.setBorder(BorderType.RIGHT_BORDER,CellBorderType.THICK,Color.getBlack());

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

Para más detalles, visite [Agregar bordes a las celdas](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
