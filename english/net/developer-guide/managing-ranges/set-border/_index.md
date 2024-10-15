---
title: Set Range Border
type: docs
weight: 600
url: /net/set-range-border/
---

## **Possible Usage Scenarios**
When you want to set the border for Range, you don't need to set each cell individually. You can set the border on the range. Aspose.Cells offers this feature.
This article provides a sample code that uses Aspose.Cells to set range border.

## **Set Range border in Excel**
To set the border of a range in Excel, you can follow these steps:
1. Select the range of cells that you want to apply the border to.
2. In the "Home" tab of the ribbon, locate the "Font" group.
3. Within the "Font" group, click on the "Borders" drop-down button.
<br>
<img src="border.png" />
4. Choose the type of border that you want to apply from the options in the drop-down menu. You can choose from preset border styles or customize your own border.
5. Once you have selected the desired border style, the border will be applied to the selected range of cells.

## **Set Range border using Aspose.Cells**
This example shows how to:

1. Create a workbook.
1. Add data to cells in the first worksheet.
1. Create a [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Set inner border of Range.
1. Set outer border of Range.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}
{{< app/cells/assistant language="csharp" >}}