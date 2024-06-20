---
title: Dölj och Visa kalkylblad i en arbetsbok
type: docs
weight: 80
url: /sv/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

När man presenterar arbetsböcker för kunder, eller håller en presentation, kan det vara användbart att dölja kalkylblad i en arbetsbok. En strukturerad metod för kalkylmodellering föreslår att data, formler och visualiseringar som diagram hålls på separata blad. Denna metod håller layouten ren och enkel och gör arbetsboken lättare att navigera. När resultaten presenteras kan du vilja dölja data- eller formelbladen från syn för att undvika distraktion.

Användare som arbetar i Microsoft Excel kan enkelt dölja och sedan visa (visa) kalkylblad. Samma funktioner är tillgängliga för utvecklare som programmerar med Excel-kalkylblad. Det finns olika sätt att arbeta med kalkylblad från inom programvaruapplikationer. En metod är att använda VSTO, en annan är Aspose.Cells for .NET.

{{% /alert %}}

## **Dölja och Visa kalkylblad**

Den här artikeln jämför [dölja](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) och [visa](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) kalkylblad med [VSTO](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/), med antingen C# eller Visual Basic, för att utföra samma uppgift med [Aspose.Cells](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/), igen med antingen C# eller Visual Basic. Aspose.Cells låter dig arbeta utan Microsoft Excel installerat.

Stegen för att dölja ett arbetsblad är:

1. Öppna en fil.
1. Hämta ett arbetsblad.
1. Dölj arbetsbladet.
1. Spara filen.

För att [visa](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) ett arbetsblad igen, växlar du helt enkelt synligheten för det dolda arket.

Kodexemplen nedan visar först hur man döljer ett arbetsblad. De första exemplen visar processen med [VSTO](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/), genom att använda antingen C# eller Visual Basic, jämfört med att använda [Aspose.Cells](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/), igen med antingen C# eller Visual Basics.

Den andra uppsättningen kodexempel visar den rad som används för att visa det dolda arket i [VSTO](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) eller [Aspose.Cells](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Dölja Arbetsblad**

Här nedan finns kodexempel för VSTO och Aspose.Cells som illustrerar hur man döljer ett arbetsblad i en arbetsbok.

### **Dölja Ark med VSTO**

**C#**

{{< highlight csharp >}}



.......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......



//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



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

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Dölja Ark med Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Visa Ark**

Här nedan finns kodexempel för VSTO och Aspose.Cells som illustrerar hur man avmarkerar ett arbetsblad i en arbetsbok.

### **Visa ett ark med VSTO**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Visa ett ark med Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
