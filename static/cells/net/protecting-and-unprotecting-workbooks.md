##Protecting and Unprotecting Workbooks
To prevent someone from accidentally or deliberately changing, moving, or deleting worksheets, you can protect workbook elements with or without a password. To protect a workbook's structure so that worksheets in the workbook can't be moved, deleted, hidden, unhidden, or renamed, and new worksheets can't be inserted, specify the ProtectionType as Structure.
To protect Windows so that they are the same size and position each time the workbook is opened, specify the ProtectionType as Windows. In this article, we show how to [protect](https://docs.aspose.com/cells/net/protecting-and-unprotecting-workbooks/) and [unprotect](https://docs.aspose.com/cells/net/protecting-and-unprotecting-workbooks/) workbooks using VSTO and Aspose.Cells for .NET to let you compare the two methods.
Aspose.Cells works independently of Microsoft Office Automation and is developed to be easy to use and produce neat code.
Protecting a workbook does not stop users from editing cells. To protect the data, you must protect the worksheets.
## **Protecting a Workbook**
To open an existing Microsoft Excel file, protect the workbook with structure and Windows attributes and save the file.
Below are parallel code snippets for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB) that show how to protect a workbook.
### **VSTO**
**C#**
.......
using Microsoft.VisualStudio.Tools.Applications.Runtime;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using System.Reflection;
.......
//Instantiate the Application object.
Excel.Application excelApp = new Excel.ApplicationClass();
//Specify the template excel file path.
string myPath = @"d:\test\MyBook.xls";
//Open the excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value);
//Protect the workbook specifying a password with Structure and Windows attributes.
excelApp.ActiveWorkbook.Protect("007", true, true);
//Save the file.
excelApp.ActiveWorkbook.Save();
//Quit the Application.
excelApp.Quit();
### **Aspose.Cells for .NET**
**C#**
.......
using Aspose.Cells;
.......
//Specify the template excel file path.
string myPath = @"d:\test\MyBook.xls";
//Instantiate a new Workbook.
//Open the excel file.
Workbook workbook = new Workbook(myPath);
//Protect the workbook specifying a password with Structure and Windows attributes.
workbook.Protect(ProtectionType.All,"007");
//Save As the excel file.
workbook.Save(@"d:\test\MyBook.xls");
## **Unprotecting a Workbook**
To unprotect a workbook, use the following lines of code for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**
//Unprotect the workbook specifying its password.
excelApp.ActiveWorkbook.Unprotect("007");
### **Aspose.Cells for .NET**
**C#**
//Unprotect the workbook specifying its password.
workbook.Unprotect("007");
