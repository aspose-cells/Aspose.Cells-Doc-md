---
title: 从源工作表复制页面设置设置到目标工作表的可能使用场景
type: docs
weight: 80
url: /zh/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: 本文介绍如何使用 Aspose.Cells for Python via .NET 样例代码，将源工作表的页面设置复制到目标工作表。
keywords: Python Excel 库，Python 复制页面设置，将页面设置复制到目标工作表。
---

## **可能的使用场景**

当向工作簿添加新工作表时，它会包含默认的 *页面设置*。有时需要将设置信息（[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)）从一个工作表转移到另一个工作表。本文件解释如何使用 Aspose.Cells for Python via .NET API 来复制页面设置。

## **将源工作表中的页面设置复制到目标工作表**

以下示例代码说明了如何使用[**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions)方法从一个工作表复制*页面设置*到另一个工作表。请查看以下示例代码及其控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **控制台输出**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
