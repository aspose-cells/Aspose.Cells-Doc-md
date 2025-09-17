##Reading Cell Values in Multiple Threads Simultaneously
Learn how to read cell values in multiple threads simultaneously through the Aspose.Cells for Node.js via C++ API.
Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.
To read cell values in more than one thread simultaneously, set [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) to **true**. If you do not, you might get the wrong cell values.
The following code:
1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.
If you comment this line:
testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);
then the following message is displayed:
if (s !== "R" + row + "C" + col)
{
console.log("This message box will show up when cells read values are incorrect.");
}
Otherwise, the program runs without showing any message which means all values read from cells are correct.
