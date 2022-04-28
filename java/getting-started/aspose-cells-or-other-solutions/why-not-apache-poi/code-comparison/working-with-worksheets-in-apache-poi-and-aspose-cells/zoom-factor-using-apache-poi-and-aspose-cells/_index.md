---
title: Zoom Factor using Apache POI and Aspose.Cells
type: docs
weight: 70
url: /java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Zoom Factor**
Microsoft Excel provides a feature that lets users set a worksheet's zoom or scaling factor. This feature helps users to see the worksheet contents in smaller or larger views.

Aspose.Cells provides a class, Workbook, that represents a Microsoft Excel file. The Workbook class contains a WorksheetCollection that allows access to each worksheet in an Excel file.

A worksheet is represented by the Worksheet class. The Worksheet class provides a wide range of properties and methods for managing worksheets. To set a worksheet's zoom factor, use the Worksheet class' setZoom method.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Zoom Factor**
Apache POI provides Sheet.setZoom() method avail zoom feature.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)

{{% alert color="primary" %}} 

For more details, visit [Zoom Factor](http://docs.aspose.com:8082/docs/display/cellsjava/Zoom+Factor).

{{% /alert %}}
