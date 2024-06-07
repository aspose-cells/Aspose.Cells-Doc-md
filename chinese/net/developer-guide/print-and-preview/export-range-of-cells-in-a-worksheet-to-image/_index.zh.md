---
title: 将工作表中的一系列单元格导出为图像
type: docs
weight: 60
url: /zh/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **可能的使用场景**

您可以使用Aspose.Cells制作工作表的图像。但是，有时您需要仅将工作表中的一系列单元格导出为图像。本文介绍了如何实现这一点。

## **将工作表中的一系列单元格导出为图像**

要获取范围的图像，请将打印区域设置为所需范围，然后将所有边距设置为0。还将[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet)设置为**true**。以下代码获取范围D8：G16的图像。下面是代码中使用的[示例Excel文件](47153160.xlsx)的屏幕截图。您可以尝试在任何Excel文件中使用该代码。

## **示例Excel文件及其导出图像的屏幕截图**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

执行该代码将仅创建范围D8：G16的图像。

**![todo:image_alt_text](Output-Image.png)**

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
