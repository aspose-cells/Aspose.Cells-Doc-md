---
title: 使用 Apache POI 和 Aspose.Cells 的缩放因子
type: docs
weight: 70
url: /zh/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 缩放系数**
Microsoft Excel 提供了一项功能，允许用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。

Aspose.Cells 提供了一个类 Workbook，它表示一个 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。

工作表由 Worksheet 类表示。 Worksheet 类提供了广泛的属性和方法来管理工作表。要设置工作表的缩放系数，请使用 Worksheet 类的 setZoom 方法。

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 缩放因子**
Apache POI 提供 Sheet.setZoom() 方法利用缩放功能。

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
