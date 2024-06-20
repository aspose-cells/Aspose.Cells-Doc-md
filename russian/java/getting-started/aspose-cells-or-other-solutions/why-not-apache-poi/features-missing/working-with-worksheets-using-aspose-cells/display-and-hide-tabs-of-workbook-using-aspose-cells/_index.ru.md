---
title: Показать и скрыть вкладки книги с помощью Aspose.Cells
type: docs
weight: 50
url: /ru/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

