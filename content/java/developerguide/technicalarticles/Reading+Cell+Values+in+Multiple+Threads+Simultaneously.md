+++
title = "Reading Cell Values in Multiple Threads Simultaneously" 
description = "" 
weight = 12357 
+++

Aspose.Cells for Java : Reading Cell Values in Multiple Threads Simultaneously  

# Aspose.Cells for Java : Reading Cell Values in Multiple Threads Simultaneously


Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

To read cell values in more than one thread simultaneously, set [Worksheet.getCells().setMultiThreadReading()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#MultiThreadReading) to **true**. If you do not, you might get the wrong cell values.

The following code:

1.  Creates a workbook.
2.  Adds a worksheet.
3.  Populates the worksheet with string values.
4.  It then creates two threads that simultaneously read values from random cells.  
    If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.

If you comment this line:

{{< code lang="cs" >}}
testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);
{{< /code >}}

then the following message is displayed:

{{< code lang="cs" >}}
if (s.equals("R" + row + "C" + col)!=true)
{
    System.out.println("This message box will show up when cells read values are incorrect.");
}
{{< /code >}}

Otherwise, the program runs without showing any message which means all values read from cells are correct.


