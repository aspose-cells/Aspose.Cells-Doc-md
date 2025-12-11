---
title: Working with Fonts in Apache POI and Aspose.Cells
type: docs
weight: 30
url: /java/working-with-fonts-in-apache-poi-and-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Working with Fonts**
Aspose.Cells provides a class, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) that represents a Microsoft Excel file. The Workbook class contains a WorksheetCollection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) class. **The** Worksheet class provides a Cells collection. Each item in the Cells collection represents an object of the [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) class.

**Java**

{{< highlight java >}}

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

## **Apache POI SS - HSSF XSSF - Working with Fonts**
Apache POI SS provides Font class to set various Font settings.

**Java**

{{< highlight java >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style, so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

For more details, visit [Dealing with Font Settings](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
