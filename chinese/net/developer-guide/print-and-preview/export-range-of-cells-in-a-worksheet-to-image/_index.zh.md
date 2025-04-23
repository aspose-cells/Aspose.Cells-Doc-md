---
title: 导出工作表中的单元格范围为图像
type: docs
weight: 60
url: /zh/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **可能的使用场景**

您可以使用 Aspose.Cells 制作工作表的图像。但是，有时您只需将工作表中的一定范围的单元格导出为图像。本文解释了如何实现这一点。

## **导出工作表中的单元格范围为图像**

要对一个范围进行图像化处理，将打印区域设置为所需的范围，然后将所有边距设置为 0。还需将 [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) 设置为 **true**。以下代码将图像化范围 D8:G16。以下是 [示例 Excel 文件](47153160.xlsx) 的屏幕截图，以及代码中使用的图像。您可以使用任何 Excel 文件尝试此代码。

## **示例 Excel 文件及其导出图像的屏幕截图**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

执行该代码仅创建范围 D8:G16 的图像。

**![todo:image_alt_text](Output-Image.png)**

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
