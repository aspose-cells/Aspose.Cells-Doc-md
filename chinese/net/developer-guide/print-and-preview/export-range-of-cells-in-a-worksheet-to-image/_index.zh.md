---
title: 将工作表中的 Cells 范围导出到图像
type: docs
weight: 60
url: /zh/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **可能的使用场景**

您可以使用 Aspose.Cells 制作工作表的图像。但是，有时您只需要将工作表中的一系列单元格导出到图像。本文解释了如何实现这一点。

## **将工作表中的 Cells 范围导出到图像**

要拍摄某个范围的图像，请将打印区域设置为所需范围，然后将所有边距设置为 0。同时设置[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet)至**真的** .以下代码获取范围 D8:G16 的图像。下面是截图[示例 Excel 文件](47153160.xlsx)在代码中使用。您可以使用任何 Excel 文件试用该代码。

## **示例 Excel 文件及其导出图像的屏幕截图**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

执行代码仅创建范围 D8:G16 的图像。

**![todo:image_alt_text](Output-Image.png)**

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
