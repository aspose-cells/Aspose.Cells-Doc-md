---
title: 更改单元格对齐方式并保持现有格式
linktitle: 更改单元格对齐方式并保持现有格式
description: 使用Aspose.Cells库在Node.js中通过C++改变单元格对齐方式并保持现有格式
keywords: Aspose.Cells，Node.js via C++，单元格对齐，保持现有格式
type: docs
weight: 340
url: /zh/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **可能的使用场景**

有时，你想更改多个单元格的对齐方式，但又想保持现有格式。Aspose.Cells for Node.js via C++允许你使用 [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-) 方法实现。如果设置为 **true**，对齐方式的更改将生效，否则不变。请注意，[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)对象作为参数传递给 [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) 方法，后者会将格式应用于一系列单元格。

## **更改单元格对齐方式并保留现有格式**

以下示例代码加载了示例Excel文件(67338585.xlsx)，创建范围并将其在水平和垂直方向上居中对齐，并保持现有格式不变。以下屏幕截图比较了示例Excel文件和输出Excel文件(67338586.xlsx)，并显示了所有单元格的现有格式相同，只是单元格现在在水平和垂直方向上都居中对齐。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
