---
title: 实现工作表的自定义纸张大小以进行渲染
type: docs
weight: 70
url: /zh/python-net/implement-custom-paper-size-of-worksheet-for-rendering/
description: 本文介绍如何使用 Aspose.Cells for Python via .NET 样例代码，在将 Excel 文件渲染成 PDF 时，设置自定义纸张尺寸。
keywords: Python Excel 库，Python 在导出为 PDF 时设置自定义纸张大小，实现工作表的自定义纸张大小。
---

## **可能的使用场景**

MS Excel 中没有直接创建自定义纸张尺寸的选项，但当将 Excel 文件渲染为 PDF 时，可以设置工作表的自定义纸张尺寸。本文介绍如何使用 Aspose.Cells for Python via .NET API 设置工作表的自定义纸张尺寸。

## **实现工作表的自定义纸张大小以进行渲染**

Aspose.Cells for Python via .NET 允许你实现工作表的自定义纸张尺寸。你可以使用 [**custom_paper_size**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/custom_paper_size/#float-float) 方法配合 [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) 类来指定自定义页面大小。以下示例演示如何为工作簿中的第一个工作表指定自定义纸张尺寸。请同时参考用上述代码生成的[输出 PDF](45056028.pdf)。

## **屏幕截图**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.py" >}}
