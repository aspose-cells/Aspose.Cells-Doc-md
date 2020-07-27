+++
title = "Protecting and Unprotecting Workbooks in VSTO and Aspose.Cells" 
description = "" 
weight = 16808 
+++

Aspose.Cells for .NET : Protecting and Unprotecting Workbooks in VSTO and Aspose.Cells  

# Aspose.Cells for .NET : Protecting and Unprotecting Workbooks in VSTO and Aspose.Cells


To open an existing Microsoft Excel file, protect the workbook with structure and Windows attributes and save the file.

Below are parallel code snippets for VSTO (C#) and Aspose.Cells for .NET (C#) that show how to protect a workbook.

## VSTO

**Protecting Workbook**

{{< code lang="cs" >}}
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
{{< /code >}}

**UnProtecting Workbook**

{{< code lang="cs" >}}
 //Unprotect the workbook specifying its password.
  excelApp.ActiveWorkbook.Unprotect("007");
{{< /code >}}

## Aspose.Cells

**Protecting Workbook**

{{< code lang="cs" >}}
//Specify the template excel file path.
   string myPath = "Book1.xls";

//Instantiate a new Workbook.
//Open the excel file.
   Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.
   workbook.Protect(ProtectionType.All, "007");

//Save As the excel file.
   workbook.Save("MyBook.xls");
{{< /code >}}

**UnProtecting Workbook**

{{< code lang="cs" >}}
//Unprotect the workbook specifying its password.
  workbook.Unprotect("007");
{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposevsto.codeplex.com/downloads/get/1459787)
*   [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
*   [Sourceforge](http://goo.gl/JH1J2I)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20(Aspose.Cells).zip)

