---
title: Dölj och visa kalkylblad i en arbetsbok
type: docs
weight: 80
url: /sv/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

När du presenterar arbetsböcker för kunder, eller gör en presentation, kan det vara användbart att dölja arbetsblad i en arbetsbok. Ett strukturerat tillvägagångssätt för kalkylbladsmodellering föreslår att data, formler och visualiseringar som diagram hålls på separata ark. Detta tillvägagångssätt håller layouten ren och enkel och gör arbetsboken lättare att navigera. När du presenterar resultat kanske du vill dölja data eller formelblad för att undvika distraktion.

Användare som arbetar i Microsoft Excel kan enkelt dölja och sedan visa (visa) kalkylblad. Samma funktioner är tillgängliga för utvecklare som programmerar med Excel-kalkylblad. Det finns olika sätt att arbeta med kalkylblad inifrån mjukvaruapplikationer. En metod är att använda VSTO, en annan är Aspose.Cells för .NET.

{{% /alert %}}

## **Dölja och visa arbetsblad**

 Den här artikeln jämför[gömmer sig](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) och[gömmer upp sig](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) arbetsblad med[VSTO](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) , med antingen C# eller Visual Basic, för att utföra samma uppgift med[Aspose.Cells](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/)återigen med antingen C# eller Visual Basic. Aspose.Cells låter dig arbeta utan Microsoft Excel installerat.

Stegen för att dölja ett kalkylblad är:

1. Öppna en fil.
1. Skaffa ett arbetsblad.
1. Göm kalkylbladet.
1. Spara filen.

 Till[dölja](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) ett kalkylblad igen, slå helt enkelt på synlighet för det dolda arket.

 Kodexemplen nedan visar först hur man döljer ett kalkylblad. De första proverna visar processen med[VSTO](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) , med antingen C# eller Visual Basic, jämfört med att använda[Aspose.Cells](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/), återigen med antingen C# eller Visual Basics.

 Den andra uppsättningen kodexempel visar raden som används för att visa kalkylbladet i[VSTO](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/) eller[Aspose.Cells](/cells/sv/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Döljer arbetsblad**

Nedan finns kodexempel för VSTO och Aspose.Cells som illustrerar hur man döljer ett kalkylblad i en arbetsbok.

### **Dölja arbetsblad med VSTO**

**C#**

{{< highlight "csharp" >}}



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


### **Döljer kalkylblad med Aspose.Cells för .NET**

**C#**

{{< highlight "csharp" >}}



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

## **Visar arbetsblad**

Nedan finns kodexempel för VSTO och Aspose.Cells som illustrerar hur man visar ett kalkylblad i en arbetsbok.

### **Visa ett kalkylblad med VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Visa ett kalkylblad med Aspose.Cells för .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
