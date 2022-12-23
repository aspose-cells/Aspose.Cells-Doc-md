---
title: Заморозить панели в Apache POI и Aspose.Cells
type: docs
weight: 80
url: /ru/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Замораживание панелей**
Aspose.Cells предоставляет класс,[Рабочая тетрадь](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)который представляет собой файл Excel Microsoft. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен[Рабочий лист](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)учебный класс. Класс Worksheet предоставляет широкий набор свойств и методов для управления рабочими листами. Чтобы настроить области закрепления, вызовите метод freezePanes класса Worksheet. Метод FreezePanes принимает следующие параметры:

- **Строка**, индекс строки ячейки, с которой начнется замораживание.
- **Столбец**, индекс столбца ячейки, с которой начнется замораживание.
- **Замороженные строки**, количество видимых строк в верхней панели.
- **Замороженные столбцы**, количество видимых столбцов в левой панели

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS — HSSF XSSF — замораживание областей**
Sheet.createFreezePane доступен для реализации функциональности FreezePane при использовании Apache POI SS — HSSF и XSSF.

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Замерзшие оконные стекла](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
