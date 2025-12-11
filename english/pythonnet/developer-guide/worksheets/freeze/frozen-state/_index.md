---
title: How to Check Frozen State without Excel.
linktitle: Frozen State
type: docs
weight: 190
url: /python-net/how-to-check-frozen-state-of-excel-worksheet
description: In this article, you will learn how to check the frozen state of an Excel worksheet programmatically using Aspose.Cells for Python via .NET APIs.
keywords: Python Excel Library, Python How to check Frozen State without Excel, Check Frozen State without Excel in Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to check the frozen state of an Excel worksheet programmatically. We can simply determine whether the worksheet is frozen or split in MS Excel. But is there a way to find whether it is frozen or split using C#? We can easily do it with Aspose.Cells for Python via .NET.

## **How to Check Frozen State**
With Aspose.Cells for Python via .NET, we can check whether the window is frozen and how many rows and columns are locked.

Please use the [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) property to check the state of window panes and get locked rows and columns with  [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) method.

1. Construct a Workbook to open the file.
2. Check whether the worksheet is frozen.
3. Get the locked rows and columns.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
