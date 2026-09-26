---  
title: Reading Cell Values in Multiple Threads Simultaneously with Golang via C++  
linktitle: Multiple Threads  
type: docs  
weight: 1800  
url: /go-cpp/reading-cell-values-in-multiple-threads-simultaneously/  
description: Learn how to read cell values in multiple threads simultaneously through the Aspose.Cells for Go via Go API.  
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells Go Multiple Threads, Read data in Multiple Threads  
---  

{{% alert color="primary" %}}  

Reading cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.  

{{% /alert %}}  

To read cell values in more than one thread simultaneously, set [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/go-cpp/cells/getmultithreadreading/) to **true**. If you do not, you might get incorrect cell values.  

The following code:  

1. Creates a workbook.  
2. Adds a worksheet.  
3. Populates the worksheet with string values.  
4. Creates two threads that simultaneously read values from random cells. If the values read are correct, nothing happens. If the values read are incorrect, a message is displayed.  

If you comment this line:  

{{< highlight go >}}  
testWorkbook.get_Worksheets().Get(0).get_Cells().set_MultiThreadReading(true);  
{{< /highlight >}}  

then the following message is displayed:  

{{< highlight go >}}  
if (s != "R" + row + "C" + col)  
{  
    MessageBox::Show("This message box will show up when the cell values read are incorrect.");  
}  
{{< /highlight >}}  

Otherwise, the program runs without showing any message, which means all values read from cells are correct.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MultipleThreads.go" >}}  
{{< app/cells/assistant language="go" >}}
