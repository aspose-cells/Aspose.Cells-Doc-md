---
title: Reading Cell Values in Multiple Threads Simultaneously
linktitle: Multiple Threads
type: docs
weight: 1800
url: /net/reading-cell-values-in-multiple-threads-simultaneously/
description: Learn how to read cell values in multiple threads simultaneously through the Aspose.Cells for .NET API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) to **true**. If you do not, you might get incorrect cell values.

The following code:

1. Creates a workbook.  
2. Adds a worksheet.  
3. Populates the worksheet with string values.  
4. It then creates two threads that simultaneously read values from random cells.  
   If the values read are correct, nothing happens. If the values read are incorrect, a message is displayed.

If you comment this line:

{{< highlight csharp >}}
testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;
{{< /highlight >}}

then the following message is displayed:

{{< highlight csharp >}}
if (s != "R" + row + "C" + col)
{
    MessageBox.Show("This message box will show up when cell values read are incorrect.");
}
{{< /highlight >}}

Otherwise, the program runs without showing any message, which means that all values read from the cells are correct.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
