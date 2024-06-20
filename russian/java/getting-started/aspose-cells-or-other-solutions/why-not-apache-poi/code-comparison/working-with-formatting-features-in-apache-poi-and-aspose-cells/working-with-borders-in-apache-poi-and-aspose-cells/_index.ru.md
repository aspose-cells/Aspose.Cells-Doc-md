---
title: Работа с рамками в Apache POI и Aspose.Cells
type: docs
weight: 10
url: /ru/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Работа с рамками**
Aspose.Cells предоставляет класс [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), который представляет файл Microsoft Excel. Класс Workbook содержит Collection, позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). Класс Worksheet предоставляет Collection. Каждый элемент в Collection представляет объект класса [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells предоставляет метод setStyle в классе [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell), используемый для установки форматирования ячейки. Также используется объект [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) класса Style, который предоставляет свойства для настройки параметров шрифта.

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
## **Apache POI SS - HSSF XSSF - Работа с рамками**
Класс CellStyle предоставляет функции для установки настроек рамок с использованием Apache POI SS - HSSF и XSSF.

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
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Добавление Границ к Ячейкам](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
