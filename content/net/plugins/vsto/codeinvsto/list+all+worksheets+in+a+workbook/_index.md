---
title : "List All Worksheets in a Workbook" 
description : "" 
weight : 16804 
toc : false
type: docs
url: /net/plugins/vsto/codeinvsto/list+all+worksheets+in+a+workbook/
---

# Aspose.Cells for .NET : List All Worksheets in a Workbook


### VSTO

{{< code lang="cs" >}}
	Excel.Application excelApp = Application;

	//Specify the template excel file path.
	string myPath = "List All Worksheets in a Workbook.xlsx";

	//Open the excel file.
	Microsoft.Office.Interop.Excel.Workbook ThisWorkbook = excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
		  Missing.Value, Missing.Value,
		  Missing.Value, Missing.Value,
		  Missing.Value, Missing.Value,
		  Missing.Value, Missing.Value,
		  Missing.Value, Missing.Value,
		  Missing.Value, Missing.Value);
	ListSheets(ThisWorkbook);

}
private void ListSheets(Microsoft.Office.Interop.Excel.Workbook workbook)
{
	int index = 0;

	Excel.Range rng = this.Application.get_Range("A1", missing);

	foreach (Excel.Worksheet displayWorksheet in workbook.Worksheets)
	{
		rng.get_Offset(index, 0).Value2 = displayWorksheet.Name;
		index++;
	}
}
{{< /code >}}

### Aspose

{{< code lang="cs" >}}
static void Main(string[] args)
{
	string myPath = "List All Worksheets in a Workbook.xlsx";
	Workbook workbook = new Workbook(myPath);

	ListSheets(workbook);
}

private static void ListSheets(Workbook workbook)
{
	int index=0;
	Worksheet thisWorksheet = workbook.Worksheets[0];
	foreach (Worksheet worksheet in workbook.Worksheets)
	{
		thisWorksheet.Cells[index, 0].Value = worksheet.Name;
		index++;
	}
}
{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposevsto.codeplex.com/downloads/get/1459775)
*   [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/List.All.Worksheets.in.a.Workbook.Aspose.Cells.zip)
*   [Sourceforge](https://sourceforge.net/p/asposevsto/wiki/Home/)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/wiki/List%20All%20Worksheets%20in%20a%20Workbook)

