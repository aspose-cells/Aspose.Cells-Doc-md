---
title: Работа со шрифтами в Apache POI и Aspose.Cells
type: docs
weight: 30
url: /ru/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Работа со шрифтами**
Aspose.Cells предоставляет класс,[Рабочая тетрадь](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)который представляет собой файл Excel Microsoft. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)учебный класс. Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет собой объект[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)учебный класс.

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
## **Apache POI SS — HSSF XSSF — Работа со шрифтами**
Apache POI SS предоставляет класс Font для установки различных параметров шрифта.

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
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Работа с настройками шрифта](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
