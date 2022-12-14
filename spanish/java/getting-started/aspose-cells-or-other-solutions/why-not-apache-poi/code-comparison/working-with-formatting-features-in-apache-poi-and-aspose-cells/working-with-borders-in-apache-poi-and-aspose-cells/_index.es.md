---
title: Trabajar con bordes en Apache POI y Aspose.Cells
type: docs
weight: 10
url: /es/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Trabajo con bordes**
Aspose.Cells proporciona una clase,[Libro de trabajo](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)que representa un archivo de Excel Microsoft. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)clase. La clase Worksheet proporciona una colección Cells. Cada elemento de la colección Cells representa un objeto de la[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)clase.

Aspose.Cells proporciona el método setStyle en el[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)clase utilizada para establecer el estilo de formato de una celda. Además, el objeto Estilo del[Estilo](http://docs.aspose.com:8082/docs/display/cellsjava/Style)class se utiliza y proporciona propiedades para configurar los ajustes de fuente.

**Java**

{{< highlight "java" >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Trabajo con bordes**
La clase CellStyle proporciona características para establecer la configuración de los bordes usando Apache POI SS - HSSF y XSSF.

**Java**

{{< highlight "java" >}}

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
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

 Para más detalles, visite[Adición de bordes a Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
