---
title: 从源工作表复制页面设置设置到目标工作表的可能使用场景
type: docs
weight: 80
url: /zh/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: 本文解释了如何使用Aspose.Cells for Python via .NET的示例代码，以程序方式从源工作表复制页面设置到目标工作表。
keywords: Python Excel库，Python复制页面设置，将页面设置复制到目标工作表的Python
---

## **可能的使用场景**

当向工作簿添加新工作表时，它包含默认的*页面设置*。有时，您需要从一个工作表传输设置([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup))到另一个工作表。本文解释了如何使用Aspose.Cells for Python via .NET的API从一个工作表复制页面设置到另一个工作表。

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
