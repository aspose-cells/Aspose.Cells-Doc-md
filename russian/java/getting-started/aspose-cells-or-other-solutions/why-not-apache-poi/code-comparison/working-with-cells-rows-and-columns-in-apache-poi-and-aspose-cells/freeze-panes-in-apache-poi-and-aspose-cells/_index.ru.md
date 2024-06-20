---
title: Замораживание областей в Apache POI и Aspose.Cells
type: docs
weight: 80
url: /ru/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Заморозить области**
Aspose.Cells предоставляет класс, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), который представляет файл Microsoft Excel. Класс Workbook содержит коллекцию листов, которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). Класс Worksheet предоставляет широкий спектр свойств и методов для управления листами. Для настройки замораживания областей вызовите метод класса Worksheet freezePanes. Метод FreezePanes принимает следующие параметры:

- **Строка**, индекс строки, с которой начнется закрепление.
- **Столбец**, индекс столбца, с которого начнется закрепление.
- **Закрепленные строки**, количество видимых строк в верхней панели.
- **Закрепленные столбцы**, количество видимых столбцов в левой панели.

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Замораживание областей**
sheet.createFreezePane доступен для достижения функциональности FreezePane при использовании Apache POI SS - HSSF и XSSF

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Замораживание областей](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
