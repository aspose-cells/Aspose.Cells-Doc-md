---
title: Reading Cell Values in Multiple Threads Simultaneously
linktitle: Multiple Threads
type: docs
weight: 1100
url: /java/reading-cell-values-in-multiple-threads-simultaneously/
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) to **true**. If you do not, you might get the wrong cell values. Please note, some features such as formatting cell values are not supported for multiple-threads. So MultiThreadReading only enable you to access cell's original data only. In multiple-threads environment if you try to get cell's formatted value, such as by Cell.getStringValue() for numeric values, you may get unexpected result or exception.

The following code:

1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
   If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.

If you comment this line:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

then the following message is displayed:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Otherwise, the program runs without showing any message which means all values read from cells are correct.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
