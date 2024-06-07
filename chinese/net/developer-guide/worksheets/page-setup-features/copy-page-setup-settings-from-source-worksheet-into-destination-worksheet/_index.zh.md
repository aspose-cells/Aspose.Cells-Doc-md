---
title: 将源工作表中的页面设置复制到目标工作表
type: docs
weight: 80
url: /zh/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: 本文说明了如何使用C# API或.NET库样本代码以编程方式将源工作表中的页面设置复制到目标工作表。
keywords: 复制页面设置c#，将页面设置复制到目标工作表c#
---

## **可能的使用场景**

当您向工作簿中添加新工作表时，它包含默认的*页面设置*。有时您需要将一个工作表中的设置([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup))传输到另一个工作表。本文说明了如何使用Aspose.Cells API将一个工作表的页面设置复制到另一个工作表。

## **将源工作表中的页面设置复制到目标工作表**

以下示例代码说明了如何使用[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)方法将一个工作表的*页面设置*从一个工作表复制到另一个。请参阅以下示例代码及其控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **控制台输出**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
