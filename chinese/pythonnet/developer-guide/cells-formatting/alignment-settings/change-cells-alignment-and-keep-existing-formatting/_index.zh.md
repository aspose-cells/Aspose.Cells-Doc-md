---
title: 更改单元格对齐方式并保持现有格式
description: 使用Aspose.Cells for Python via .NET库更改单元格对齐方式并保留现有格式
keywords: Aspose.Cells for Python via .NET，Python单元格对齐，保留现有格式
type: docs
weight: 340
url: /zh/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

 有时，你想同时更改多个单元格的对齐方式，又希望保持已有格式。Aspose.Cells for Python via .NET允许你使用[**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments)属性实现。如果将其设置为**true**，则对齐方式的更改会生效，否则不变。请注意，[**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)对象作为参数传递给[**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style)方法，该方法实际应用格式到一范围单元格。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载了示例Excel文件(67338585.xlsx)，创建范围并将其在水平和垂直方向上居中对齐，并保持现有格式不变。以下屏幕截图比较了示例Excel文件和输出Excel文件(67338586.xlsx)，并显示了所有单元格的现有格式相同，只是单元格现在在水平和垂直方向上都居中对齐。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
