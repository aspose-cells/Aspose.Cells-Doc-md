##Reading Cell Values in Multiple Threads Simultaneously
Learn how to read Cell Values in Multiple Threads Simultaneously through the Aspose.Cells for .NET API.
Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.
To read cell values in more than one thread simultaneously, set [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) to **true**. If you do not, you might get the wrong cell values.
The following code:
1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.
If you comment this line:
testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;
then the following message is displayed:
if (s != "R" + row + "C" + col)
{
MessageBox.Show("This message box will show up when cells read values are incorrect.");
}
Otherwise, the program runs without showing any message which means all values read from cells are correct.
