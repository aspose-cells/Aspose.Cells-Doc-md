---
title: Accessing Worksheet
type: docs
weight: 10
url: /net/accessing-worksheet/
---

{{% alert color="primary" %}} 

A worksheet is an integral part of an Excel file. In fact, an Excel file is composed of one or more worksheets. Each worksheet can be composed of up tp 65,536 rows and 256 columns only. It is the worksheet that holds data in an Excel file.

Aspose.Cells.GridDesktop can create and manipulate existing and new Excel files so there is, of course, a way to access worksheets using Aspose.Cells.GridDesktop. This topic discusses how.

{{% /alert %}} 
## **Using Worksheet Index**
Developers can access an instance of any Worksheet by using the worksheet index of any desired worksheet as shown below in the example. This approach is good for iterating through a number of worksheets in an Excel file.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Using Worksheet Name**
If the name of the worksheet is known, it is possible to access a worksheet using its name as shown below.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accessing an Active Worksheet**
It is possbile that an Excel file will have more than one worksheet. The one htat a user is working on is called the active worksheet. It is possible to access the active sheet.

To access an active worksheet, Aspose.Cells.GridDesktop offers two approaches:
### **Using the AcriveSheetIndex Property**
One way to access an active worksheet using Aspose.Cells.GridDesktop control is to use the GridDesktop control's ActiveSheetIndex property. Using this property, it is possible to get the index of the active worksheet in the Aspose.Cells.GridDesktop control. Then that index can be used to access the worksheet in a traditional manner as shown below.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Using the GetActiveWorksheet Method**
The other approach is to call the GridDesktop control's GetActiveWorksheet method. This method provides a reference of the worksheet that is currently active in Aspose.Cells.GridDesktop control as shown below.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
