---
title: Разделение панелей в Apache POI и Aspose.Cells
type: docs
weight: 70
url: /ru/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Разделенные панели**
Aspose.Cells предоставляет класс Workbook, который представляет файл Microsoft Excel. Класс Workbook предоставляет широкий набор свойств и методов для управления файлами Excel. Чтобы реализовать разделенные представления, используйте метод split класса Worksheet. Чтобы удалить разделенные панели, используйте метод removeSplit.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS — HSSF и XSSF — разделенные панели**
Функциональность разделенных панелей может быть достигнута с помощью метода createSplitPane при использовании Apache POI SS (HSSF и XSSF) API.

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Разделить панели](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
