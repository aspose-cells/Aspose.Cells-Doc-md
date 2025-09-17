##Protecting and Unprotecting Workbooks in VSTO and Aspose.Cells
To open an existing Microsoft Excel file, protect the workbook with structure and Windows attributes and save the file.
Below are parallel code snippets for VSTO (C#) and Aspose.Cells for .NET (C#) that show how to protect a workbook.
## **VSTO**
**Protecting Workbook**
//Instantiate the Application object.
Excel.Application excelApp = Application;
//Excel.Application excelApp = Application;
//Specify the template excel file path.
string myPath = "MyBook.xls";
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
**UnProtecting Workbook**
//Unprotect the workbook specifying its password.
excelApp.ActiveWorkbook.Unprotect("007");
## **Aspose.Cells**
**Protecting Workbook**
//Specify the template excel file path.
string myPath = "Book1.xls";
//Instantiate a new Workbook.
//Open the excel file.
Workbook workbook = new Workbook(myPath);
//Protect the workbook specifying a password with Structure and Windows attributes.
workbook.Protect(ProtectionType.All, "007");
//Save As the excel file.
workbook.Save("MyBook.xls");
**UnProtecting Workbook**
//Unprotect the workbook specifying its password.
workbook.Unprotect("007");
## **Download Sample Code**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip)
