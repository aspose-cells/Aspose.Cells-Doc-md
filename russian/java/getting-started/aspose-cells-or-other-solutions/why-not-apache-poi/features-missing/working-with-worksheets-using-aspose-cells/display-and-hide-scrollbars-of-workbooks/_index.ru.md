---
title: Отображение и скрытие полос прокрутки в книгах Excel
type: docs
weight: 40
url: /ru/java/display-and-hide-scrollbars-of-workbooks/
---

## **Aspose.Cells - Отображение и скрытие полос прокрутки рабочих книг**
Aspose.Cells предоставляет класс **Workbook**, который представляет собой файл Excel. Класс **Workbook** предоставляет широкий спектр свойств и методов для управления файлом Excel. Однако, для управления видимостью полос прокрутки в файле Excel разработчики могут использовать методы **setVScrollBarVisible** и **setHScrollBarVisible** класса **Workbook**.

**Java**

{{< highlight java >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
{{< app/cells/assistant language="java" >}}
