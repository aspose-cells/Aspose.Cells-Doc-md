---
title: How to Check Frozen State without Excel.
linktitle: Frozen State
type: docs
weight: 190
url: /python-net/how-to-check-frozen-state-of-excel-worksheet
description: In this article, you will learn how check frozen state of excel worksheet programmatically using Aspose.Cells for Python via .NET APIs.
keywords: Python Excel Library, Python How to check Frozen State without Excel, Check Frozen State without Excel in Python.
---

## **Introduction**

In this article, we will learn how check frozen state of excel worksheet programmatically. We can simply find whether the worksheet is frozen or splitted in MS Excel. But is there a way to find whether it is frozen or splitted with CSharp. We can simply do it with Aspose.Cells for Python via .NET.

## **How to Check Frozen State**
With Aspose.Cells for Python via .NET, we can check whether the window is frozen and how many rows and columns are locked.

Please use the [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) property to check the state of window panes 
and gets locked rows and columns with  [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) method.
1. Construct Workbook to open the file.
2. Check whether the worksheet is frozen.
3. Gets the locked row and columns

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}