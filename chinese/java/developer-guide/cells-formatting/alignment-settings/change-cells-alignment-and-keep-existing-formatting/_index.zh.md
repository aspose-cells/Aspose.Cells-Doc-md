---
title: 更改单元格对齐方式并保留现有格式
type: docs
weight: 260
url: /zh/java/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

有时，您希望更改多个单元格的对齐方式，但也希望保留现有的格式。Aspose.Cells允许您通过[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments)属性来实现。如果将其设置为**true**，则对齐方式的更改将生效，否则不生效。请注意，调用[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))方法时将[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)对象作为参数传递，该方法实际上将格式应用于单元格范围。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载[sample Excel文件](67338592.xlsx)，创建范围并使其水平和垂直居中，并保留现有的格式不变。以下屏幕截图比较了示例Excel文件和[输出Excel文件](67338591.xlsx)，并显示了除了单元格现在水平和垂直居中外，所有单元格的现有格式都是相同的。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
