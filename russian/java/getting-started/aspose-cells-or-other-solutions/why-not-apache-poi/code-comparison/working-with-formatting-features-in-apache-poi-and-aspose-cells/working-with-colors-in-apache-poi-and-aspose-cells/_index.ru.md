---
title: Работа с Цветами в Apache POI и Aspose.Cells
type: docs
weight: 20
url: /ru/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Работа с Цветами**
Aspose.Cells предоставляет класс, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), который представляет файл Microsoft Excel. Класс Workbook содержит WorksheetCollection, который позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет объект класса [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells предоставляет метод setStyle в классе Cell, который используется для установки форматирования ячейки. Кроме того, объект Style класса Style может быть использован для конфигурации настроек шрифта.

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
## **Apache POI SS - HSSF XSSF - Работа с Цветами**
Класс CellStyle доступен для установки параметров фона и шаблона заливки.

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
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Цвета и Фоновые Шаблоны](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
