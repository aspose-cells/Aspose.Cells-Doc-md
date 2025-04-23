---
title: Отображение и скрытие вкладок рабочей книги в xlsx4j
type: docs
weight: 40
url: /ru/java/display-and-hide-tabs-of-workbook-in-xlsx4j/
---

## **Aspose.Cells - Отображение и скрытие вкладок рабочей книги**
Aspose.Cells предоставляет класс Workbook, который представляет собой файл Microsoft Excel. Класс Workbook предоставляет широкий спектр свойств и методов для управления файлом Excel. Для управления видимостью вкладок в файле Excel разработчики могут использовать метод setShowTabs класса Workbook.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)
{{< app/cells/assistant language="java" >}}
