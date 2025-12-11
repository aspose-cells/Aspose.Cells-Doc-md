---
title: How to check Frozen State without Excel.
linktitle: Frozen State
type: docs
weight: 190
url: /net/how-to-check-frozen-state-of-excel-worksheet
description: In this article, you will learn how to check the frozen state of an Excel worksheet programmatically using the C# library with .NET API.

ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to check the frozen state of an Excel worksheet programmatically. We can simply determine whether the worksheet is frozen or split in Microsoft Excel. But is there a way to find whether it is frozen or split using C#? We can do it easily with Aspose.Cells for .NET.

## **Are Window Panes Frozen?**
With Aspose.Cells for .NET, we can check whether the window is frozen and how many rows and columns are locked.

Please use the [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) property to check the state of window panes and get locked rows and columns with the [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/) method.
1. Construct a Workbook to open the file.
2. Check whether the worksheet is frozen.
3. Get the locked rows and columns

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
{{< app/cells/assistant language="csharp" >}}
