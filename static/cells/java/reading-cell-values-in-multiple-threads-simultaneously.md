##Reading Cell Values in Multiple Threads Simultaneously
Learn how to Read Cell Values in Multiple Threads Simultaneously with Aspose.Cells for Java APIs.
Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.
## **How to Read Cell Values in Multiple Threads Simultaneously with Aspose.Cells for Java**
To read cell values in more than one thread simultaneously, set [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) to **true**. If you do not, you might get the wrong cell values. Please note, some features such as formatting cell values are not supported for multiple-threads. So MultiThreadReading only enable you to access cell's original data only. In multiple-threads environment if you try to get cell's formatted value, such as by Cell.getStringValue() for numeric values, you may get unexpected result or exception.
The following code:
1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.
If you comment this line:
testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);
then the following message is displayed:
if (s.equals("R" + row + "C" + col)!=true)
{
System.out.println("This message box will show up when cells read values are incorrect.");
}
Otherwise, the program runs without showing any message which means all values read from cells are correct.
