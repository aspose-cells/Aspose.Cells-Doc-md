---
title: Trabajar con fuentes en Apache POI y Aspose.Cells
type: docs
weight: 30
url: /es/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Trabajar con fuentes**
Aspose.Cells proporciona una clase,[Libro de trabajo](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)que representa un archivo de Excel Microsoft. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)clase. La clase Worksheet proporciona una colección Cells. Cada elemento de la colección Cells representa un objeto de la[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)clase.

**Java**

{{< highlight "java" >}}

 //Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Setting the font name to "Courier New"

Style style = cell.getStyle();

Font font = style.getFont();

font.setName("Courier New");

font.setSize(24);

font.setBold(true);

font.setUnderline(FontUnderlineType.SINGLE);

font.setColor(Color.getBlue());

font.setStrikeout(true);

//font.setSubscript(true);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Trabajo con fuentes**
Apache POI SS proporciona una clase de fuente para establecer varias configuraciones de fuente.

**Java**

{{< highlight "java" >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

 Para más detalles, visite[Tratar con la configuración de fuentes](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
