---
title: 使用Apache POI和Aspose.Cells缩放因子
type: docs
weight: 70
url: /zh/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 缩放因子**
Microsoft Excel提供了一个功能，允许用户设置工作表的缩放或比例因子。此功能帮助用户以较小或较大的视图查看工作表内容。

Aspose.Cells提供了一个表示Microsoft Excel文件的类Workbook。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了大量用于管理工作表的属性和方法。要设置工作表的缩放因子，请使用Worksheet类的setZoom方法。

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 缩放因子**
Apache POI提供了Sheet.setZoom()方法来使用缩放功能。

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
