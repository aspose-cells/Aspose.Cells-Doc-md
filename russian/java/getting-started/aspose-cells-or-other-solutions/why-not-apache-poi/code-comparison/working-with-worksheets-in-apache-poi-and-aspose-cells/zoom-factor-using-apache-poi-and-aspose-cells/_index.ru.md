---
title: Коэффициент масштабирования с использованием Apache POI и Aspose.Cells
type: docs
weight: 70
url: /ru/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Коэффициент масштабирования**
Microsoft Excel предоставляет функцию, которая позволяет пользователям устанавливать масштаб рабочего листа или коэффициент масштабирования. Эта функция помогает пользователям просматривать содержимое рабочего листа в уменьшенном или увеличенном виде.

Aspose.Cells предоставляет класс Workbook, который представляет файл Microsoft Excel. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет широкий набор свойств и методов для управления рабочими листами. Чтобы установить коэффициент масштабирования рабочего листа, используйте метод setZoom класса Worksheet.

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS — HSSF XSSF — Коэффициент масштабирования**
Apache POI предоставляет функцию масштабирования методом Sheet.setZoom().

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
