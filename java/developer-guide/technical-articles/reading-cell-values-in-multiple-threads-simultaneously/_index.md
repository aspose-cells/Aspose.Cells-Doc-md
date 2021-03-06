---
title: Reading Cell Values in Multiple Threads Simultaneously
type: docs
weight: 110
url: /java/reading-cell-values-in-multiple-threads-simultaneously/
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Worksheet.getCells().setMultiThreadReading()**](https://apireference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) to **true**. If you do not, you might get the wrong cell values.

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

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
