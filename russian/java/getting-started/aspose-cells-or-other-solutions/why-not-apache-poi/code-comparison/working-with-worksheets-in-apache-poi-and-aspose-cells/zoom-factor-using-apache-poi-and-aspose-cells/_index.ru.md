---
title: Фактор масштабирования с использованием Apache POI и Aspose.Cells
type: docs
weight: 70
url: /ru/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Масштабный коэффициент**
Microsoft Excel предоставляет функцию, позволяющую пользователям установить масштабный фактор или масштабирование листа. Эта функция помогает пользователям просматривать содержимое листа в меньшем или большем масштабе.

Aspose.Cells предоставляет класс Workbook, который представляет файл Microsoft Excel. Класс Workbook содержит WorksheetCollection, которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом Worksheet. Класс Worksheet предоставляет широкий спектр свойств и методов для управления листами. Для установки коэффициента масштабирования листа используйте метод setZoom класса Worksheet.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Коэффициент масштабирования**
Apache POI предоставляет метод Sheet.setZoom(), позволяющий использовать функцию масштабирования.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
