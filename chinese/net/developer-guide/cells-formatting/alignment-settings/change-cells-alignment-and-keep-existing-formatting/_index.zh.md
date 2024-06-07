---
title: 更改单元格对齐方式并保留现有格式
description: 使用Aspose.Cells库更改单元格对齐方式并保留现有格式
keywords: Aspose.Cells, C#, 单元格对齐, 保留现有格式
type: docs
weight: 340
url: /zh/net/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

有时，您想更改多个单元格的对齐方式，但又希望保留现有格式。Aspose.Cells允许您使用 [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) 属性来执行此操作。如果将其设置为**true**，则将进行对齐方式的更改，否则不会。请注意，向 [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) 方法传递 [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象，该方法实际上将应用格式化到一系列单元格中。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载了[示例Excel文件](67338585.xlsx)，创建了范围并使其在水平和垂直方向上居中对齐，并保持现有格式不变。以下屏幕截图比较了示例Excel文件和[输出的Excel文件](67338586.xlsx)，显示所有单元格的现有格式相同，除了现在单元格在水平和垂直方向上均居中对齐。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
