+++
title = "Get Text of Specific Cell" 
description = "" 
weight = 16801 
+++

Aspose.Cells for .NET : Get Text of Specific Cell  

# Aspose.Cells for .NET : Get Text of Specific Cell


### VSTO

{{< code lang="cs" >}}
//Instantiate the Application object.
Excel.Application excelApp = Application;

//Specify the template excel file path.
string myPath = "Get Text of Specific Cell.xlsx";

//Open the excel file.
Microsoft.Office.Interop.Excel.Workbook ThisWorkbook = excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
	  Missing.Value, Missing.Value,
	  Missing.Value, Missing.Value,
	  Missing.Value, Missing.Value,
	  Missing.Value, Missing.Value,
	  Missing.Value, Missing.Value,
	  Missing.Value, Missing.Value);

String res = "";
res = ThisWorkbook.Worksheets["Sheet1"].Range("A1").Text;

MessageBox.Show(res);

//Save the file.
excelApp.ActiveWorkbook.Save();

excelApp.Quit();
{{< /code >}}

### Aspose

{{< code lang="cs" >}}
//Specify the excel file path.
string myPath = "Get Text of Specific Cell.xlsx";

//Instantiating a Workbook object
Workbook workbook = new Workbook(myPath);

//Get worksheet
Worksheet worksheet = workbook.Worksheets[0];

String res = "";
res= worksheet.Cells["A1"].Value.ToString();

Console.Write(res);

Console.ReadKey();

{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposevsto.codeplex.com/downloads/get/1459779)
*   [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Get.Text.of.Specific.Cell.Aspose.Cells.zip)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/wiki/Get%20Text%20of%20Specific%20Cell)

