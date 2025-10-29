---
title: 使用 Golang 通过 C++ 改变单元格对齐方式并保持现有格式
description: 使用Aspose.Cells库更改单元格对齐方式并保留现有格式
keywords: Aspose.Cells、C++、单元格对齐、保持现有格式
type: docs
weight: 340
url: /zh/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

 有时，您想要更改多个单元格的对齐方式，但又希望保持现有的格式。Aspose.Cells允许使用[**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/)属性实现这一点。如果将其设置为**true**，对齐变更将生效，否则不变。请注意，[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)对象作为参数传递给[**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)方法，而该方法实际应用格式到一系列单元格。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载了示例Excel文件(67338585.xlsx)，创建范围并将其在水平和垂直方向上居中对齐，并保持现有格式不变。以下屏幕截图比较了示例Excel文件和输出Excel文件(67338586.xlsx)，并显示了所有单元格的现有格式相同，只是单元格现在在水平和垂直方向上都居中对齐。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
