---
title: 更改单元格对齐方式并保持现有格式
description: 使用Aspose.Cells库更改单元格对齐方式并保留现有格式
keywords: Aspose.Cells，C#，单元格对齐，保留现有格式
type: docs
weight: 340
url: /zh/net/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

有时，您可能想要更改多个单元格的对齐方式，同时保留现有格式。使用Aspose.Cells可以实现这一点。如果将它设置为True，则对齐方面的更改将发生，否则不会。请注意，[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象作为参数传递给[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)方法，该方法实际上将格式应用于一系列单元格。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载了示例Excel文件(67338585.xlsx)，创建范围并将其在水平和垂直方向上居中对齐，并保持现有格式不变。以下屏幕截图比较了示例Excel文件和输出Excel文件(67338586.xlsx)，并显示了所有单元格的现有格式相同，只是单元格现在在水平和垂直方向上都居中对齐。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
