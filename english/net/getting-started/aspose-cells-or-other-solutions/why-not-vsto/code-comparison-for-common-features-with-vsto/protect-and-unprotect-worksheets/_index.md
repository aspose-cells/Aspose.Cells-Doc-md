---
title: Protect and unProtect Worksheets
type: docs
weight: 190
url: /net/protect-and-unprotect-worksheets-with-vsto/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Excel.Application excelApp = Application;

//Specify the template excel file path.

string myPath = "Protect and unProtect Worksheets.xlsx";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Protect the worksheet specifying a password with Structure and Windows attributes.

((Excel.Worksheet)excelApp.ActiveSheet).Protect("thispassword",

	missing, missing, missing, missing, missing, missing, missing, missing,

	missing, missing, missing, missing, true, missing, missing);

//Unprotect the worksheet specifying its password.

((Excel.Worksheet)excelApp.ActiveSheet).Unprotect("thispassword");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 //Specify the template excel file path.

string myPath = "Protect and unProtect Worksheets.xlsx";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the worksheet specifying a password with Structure and Windows attributes.

workbook.Worksheets[workbook.Worksheets.ActiveSheetIndex].Protect(ProtectionType.All, "thispassword", "");

//Unprotect the worksheet specifying its password.

workbook.Worksheets[workbook.Worksheets.ActiveSheetIndex].Unprotect("thispassword");

//Save As the excel file.

workbook.Save(myPath);


{{< /highlight >}}
## **Download Sample Code**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protect.and.unProtect.Worksheets.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/p/asposevsto/wiki/Home/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/wiki/Protect%20and%20unProtect%20Worksheets)
{{< app/cells/assistant language="csharp" >}}
