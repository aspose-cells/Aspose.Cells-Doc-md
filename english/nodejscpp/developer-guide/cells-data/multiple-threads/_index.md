---
title: Reading Cell Values in Multiple Threads Simultaneously
linktitle: Multiple Threads
type: docs
weight: 1800
url: /nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Learn how to read cell values in multiple threads simultaneously through the Aspose.Cells for Node.js via C++ API.
keywords: Read Cell Values in Multiple Threads Simultaneously Node.js via C++, Aspose.Cells C++ Multiple Threads, Read data in Multiple Threads
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) to **true**. If you do not, you might get the wrong cell values.

The following code:

1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
   If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.

If you comment this line:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

then the following message is displayed:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Otherwise, the program runs without showing any message which means all values read from cells are correct.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
