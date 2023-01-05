---
title: Работа с границами в Apache POI и Aspose.Cells
type: docs
weight: 10
url: /ru/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Работа с границами**
Aspose.Cells предоставляет класс,[Рабочая тетрадь](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)который представляет собой файл Excel Microsoft. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)учебный класс. Класс Worksheet предоставляет коллекцию Cells. Каждый элемент коллекции Cells представляет собой объект[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)учебный класс.

Aspose.Cells предоставляет метод setStyle в[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)класс, используемый для установки стиля форматирования ячейки. Кроме того, объект Style[Стиль](http://docs.aspose.com:8082/docs/display/cellsjava/Style)используется класс и предоставляет свойства для настройки параметров шрифта.

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
## **Apache POI SS — HSSF XSSF — Работа с границами**
Класс CellStyle предоставляет функции для установки параметров границ с использованием Apache POI SS — HSSF и XSSF.

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
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Добавление границ к Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
