---
title: Разделить панели в Apache POI и Aspose.Cells
type: docs
weight: 70
url: /ru/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Разделить панели**
Aspose.Cells предоставляет класс Workbook, который представляет файл Microsoft Excel. Класс Workbook предоставляет широкий спектр свойств и методов для управления файлами Excel. Для реализации разделенных видов используйте метод split класса Worksheet. Для удаления разделенных панелей используйте метод removeSplit.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Разделить панели**
Функциональность разделения панелей может быть достигнута с использованием метода createSplitPlane при использовании API Apache POI SS (HSSF & XSSF)

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Раздел разделения окон](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
