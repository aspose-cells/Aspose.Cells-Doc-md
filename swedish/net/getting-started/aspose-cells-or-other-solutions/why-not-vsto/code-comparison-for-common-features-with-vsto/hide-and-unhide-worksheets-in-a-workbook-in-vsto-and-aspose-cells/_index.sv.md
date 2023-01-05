---
title: Dölj och visa kalkylblad i en arbetsbok i VSTO och Aspose.Cells
type: docs
weight: 140
url: /sv/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
Den här artikeln jämför att dölja och ta fram kalkylblad med VSTO, med antingen C# eller Visual Basic, med att utföra samma uppgift med Aspose.Cells, återigen med antingen C# eller Visual Basic. Aspose.Cells låter dig arbeta utan Microsoft Excel installerat.

Stegen för att dölja ett kalkylblad är:

1. Öppna en fil.
1. Skaffa ett arbetsblad.
1. Göm kalkylbladet.
1. Spara filen.
 För att visa ett kalkylblad igen, aktivera bara synligheten för det dolda bladet.

Kodexemplen nedan visar först hur man döljer ett kalkylblad. De första exemplen visar processen med VSTO, med antingen C#, jämfört med att använda Aspose.Cells, återigen med antingen C#.

Den andra uppsättningen kodexempel visar raden som används för att visa kalkylbladet i VSTO eller Aspose.Cells.
## **Döljer arbetsblad**
Nedan finns kodexempel för VSTO och Aspose.Cells som illustrerar hur man döljer ett kalkylblad i en arbetsbok.
### **VSTO**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **Ta fram arbetsblad**
Nedan finns kodexempel för VSTO och Aspose.Cells som illustrerar hur man visar ett kalkylblad i en arbetsbok.
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Ladda ner provkod**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).blixtlås)
