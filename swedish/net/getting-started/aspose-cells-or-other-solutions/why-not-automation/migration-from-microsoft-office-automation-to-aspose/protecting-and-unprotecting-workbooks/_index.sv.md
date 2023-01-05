---
title: Skydda och avskydda arbetsböcker
type: docs
weight: 20
url: /sv/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

För att förhindra att någon av misstag eller avsiktligt ändrar, flyttar eller tar bort kalkylblad kan du skydda arbetsbokselement med eller utan lösenord. För att skydda en arbetsboks struktur så att kalkylblad i arbetsboken inte kan flyttas, raderas, gömmas, döljas eller bytas namn, och nya kalkylblad inte kan infogas, anger du ProtectionType som Structure.

 För att skydda Windows så att de har samma storlek och position varje gång arbetsboken öppnas, ange ProtectionType som Windows. I den här artikeln visar vi hur du[skydda](/cells/sv/net/protecting-and-unprotecting-workbooks/) och[oskydda](/cells/sv/net/protecting-and-unprotecting-workbooks/) arbetsböcker med VSTO och Aspose.Cells for .NET för att låta dig jämföra de två metoderna.

Aspose.Cells fungerar oberoende av Microsoft Office Automation och är utvecklad för att vara enkel att använda och producera snygg kod.

Att skydda en arbetsbok hindrar inte användare från att redigera celler. För att skydda data måste du skydda arbetsbladen.

{{% /alert %}} 
## **Skydda en arbetsbok**
För att öppna en befintlig Microsoft Excel-fil, skydda arbetsboken med struktur och Windows-attribut och spara filen.

Nedan finns parallella kodavsnitt för VSTO (C#, VB) och Aspose.Cells for .NET (C#, VB) som visar hur man skyddar en arbetsbok.
### **VSTO**
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

//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

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



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......


//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

workbook.Protect(ProtectionType.All,"007");

//Save As the excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}
## **Ta bort skyddet av en arbetsbok**
För att avskydda en arbetsbok, använd följande kodrader för VSTO (C#, VB) och Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
