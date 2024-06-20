---
title: Trabajar con colores en Apache POI y Aspose.Cells
type: docs
weight: 20
url: /es/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Trabajar con colores**
Aspose.Cells proporciona una clase, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). La clase Worksheet proporciona una colección de Celdas. Cada elemento en la colección de Celdas representa un objeto de la clase [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells proporciona el método setStyle en la clase Cell que se utiliza para establecer el formato de una celda. Además, el objeto Style de la clase Style se puede usar para configurar la configuración de fuente.

**Java**

{{< highlight java >}}

 //Accessing cell from the worksheet

Cell cell = cells.get("B2");

Style style = cell.getStyle();

//Setting the foreground color to yellow

style.setBackgroundColor(Color.getYellow());

//Setting the background pattern to vertical stripe

style.setPattern(BackgroundType.VERTICAL_STRIPE);

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.fromArgb(212,213,0);

workbook.changePalette(color,55);

//Accessing cell from the worksheet

cell = cells.get("B3");

//Adding some value to the cell

cell.setValue("Hello Aspose!");

//Setting the custom color to the font

style = cell.getStyle();

Font font = style.getFont();

font.setColor(color);

cell.setStyle(style);


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Trabajar con colores**
La clase CellStyle está disponible para establecer la configuración de fondo y patrón de relleno.

**Java**

{{< highlight java >}}

 // Aqua background

CellStyle style = wb.createCellStyle();

style.setFillBackgroundColor(IndexedColors.AQUA.getIndex());

style.setFillPattern(CellStyle.BIG_SPOTS);

Cell cell = row.createCell((short) 1);

cell.setCellValue("X");

cell.setCellStyle(style);

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.createCellStyle();

style.setFillForegroundColor(IndexedColors.ORANGE.getIndex());

style.setFillPattern(CellStyle.SOLID_FOREGROUND);

cell = row.createCell((short) 2);

cell.setCellValue("X");

cell.setCellStyle(style);

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

Para más detalles, visite [Colores y patrones de fondo](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
