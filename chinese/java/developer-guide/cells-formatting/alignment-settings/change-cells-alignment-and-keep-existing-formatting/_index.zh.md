---
title: 更改单元格对齐方式并保持现有格式
type: docs
weight: 260
url: /zh/java/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

有时，您想要更改多个单元格的对齐方式，但又想保留现有的格式。Aspose.Cells允许您使用 [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) 属性进行操作。如果将其设置为 **true**，则对齐方式的更改将生效，否则不会生效。请注意，作为参数传递给 [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) 方法的是 [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) 对象，该方法实际上将格式应用于单元格范围。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载了[示例Excel文件](67338592.xlsx)，创建了范围并在水平和垂直方向上进行了居中对齐，同时保留了现有的格式。以下屏幕截图比较了示例Excel文件和[输出Excel文件](67338591.xlsx)，显示了所有单元格的现有格式都相同，只是单元格现在在水平和垂直方向上都居中对齐。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
{{< app/cells/assistant language="java" >}}
