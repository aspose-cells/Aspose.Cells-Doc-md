---
title: Lägga till hyperlänkar till celler i VSTO och Aspose.Cells
type: docs
weight: 20
url: /sv/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

För att lägga till hyperlänkar till celler i ett kalkylblad, följ följande steg:

1. Ställ in kalkylbladet: 
   1. Instantiera en Application-objekt. (Endast VSTO)
   1. Lägg till en arbetsbok.
   1. Hämta det första arket.
   1. Lägg till text i cellerna som du kommer att lägga till en hyperlänk till.
1. Lägg till hyperlänk.
1. Spara dokumentet.

Dessa steg visas i kodexemplen nedan. Det första exemplet visar hur man använder VSTO med antingen C# för att lägga till en hyperlänk till en cell. Exemplen som följer visar hur man gör samma sak med hjälp av Aspose.Cells for .NET, igen med C#.

Kodexemplen genererar en Excelfil med en hyperlänk i cell A1 på det första arket.

![todo:image_alt_text](picture1.png)

En hyperlänk läggs till cell A1.

## **VSTO**

{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 //Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Ladda ned provkoden**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
