---
title: Hitta specifik ordhändelse
type: docs
weight: 120
url: /sv/net/find-specific-word-occurrence/
---

## **VSTO Excel**
{{< highlight csharp >}}

 Excel.Application excelApp = Application;

//Specify the template excel file path.

string myPath = "List All Worksheets in a Workbook.xls";

//Open the excel file.

Microsoft.Office.Interop.Excel.Workbook ThisWorkbook = excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

	  Missing.Value, Missing.Value,

	  Missing.Value, Missing.Value,

	  Missing.Value, Missing.Value,

	  Missing.Value, Missing.Value,

	  Missing.Value, Missing.Value,

	  Missing.Value, Missing.Value);

Excel.Worksheet Worksheet = ThisWorkbook.Worksheets["Sheet1"];

findNow(Worksheet, "test");

//Save the file.

excelApp.ActiveWorkbook.Save();

excelApp.Quit();


{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 static void Main(string[] args)

{

	//Instantiate a new Workbook.

	Workbook workbook = new Workbook();

	//Specify the template Excel file path.

	string myPath = "Book1.xls";

	//Open the Excel file.

	workbook.Open(myPath);

	//Get the first sheet.

	Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

	findNow(objSheet, "test");

	workbook.Save(myPath);

}

private static void findNow(Worksheet objSheet, string textToFind)

{

	//Get Cells collection

	Cells cells = objSheet.Cells;

	//Instantiate FindOptions Object

	FindOptions findOptions = new FindOptions();

	//Create a Cells Area

	CellArea ca = new CellArea();

	ca.StartRow = 8;

	ca.StartColumn = 2;

	ca.EndRow = 17;

	ca.EndColumn = 13;

	//Set cells area for find options

	findOptions.SetRange(ca);

	//Set searching properties

	findOptions.SearchNext = true;

	findOptions.SeachOrderByRows = true;

	findOptions.LookInType = LookInType.Values;

	//Find the cell with 0 value

	Cell cell = cells.Find(textToFind, null, findOptions);

	Console.WriteLine(cell.StringValue);

}


{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Find.Specific.Word.Occurrence.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/p/asposevsto/wiki/Home/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/wiki/Find%20Specific%20Word%20Occurrence)
{{< app/cells/assistant language="csharp" >}}
