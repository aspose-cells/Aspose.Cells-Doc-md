---
title: 将源工作表中的页面设置设置复制到目标工作表
type: docs
weight: 80
url: /zh/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: 本文介绍如何使用 C# API 或 .NET 库示例代码以编程方式将页面设置设置从源工作表复制到目标工作表。
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **可能的使用场景**

当您将新工作表添加到工作簿时，它包含默认的*页面设置设置*。有时您可能需要传输设置 ([**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)从一个工作表到另一个工作表。本文档说明如何使用 Aspose.Cells API 将页面设置设置从一个工作表复制到另一个工作表。

##  **将源工作表中的页面设置设置复制到目标工作表**

下面的示例代码说明了如何复制*页面设置设置*从一个工作表到另一个使用[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)方法。请参阅以下示例代码及其控制台输出以供参考。

##  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **控制台输出**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
