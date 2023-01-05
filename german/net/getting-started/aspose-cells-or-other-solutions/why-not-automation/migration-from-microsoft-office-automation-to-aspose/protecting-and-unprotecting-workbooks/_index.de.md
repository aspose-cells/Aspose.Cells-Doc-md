---
title: Arbeitsmappen schützen und Schutz aufheben
type: docs
weight: 20
url: /de/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

Um zu verhindern, dass jemand versehentlich oder absichtlich Arbeitsblätter ändert, verschiebt oder löscht, können Sie Arbeitsmappenelemente mit oder ohne Kennwort schützen. Um die Struktur einer Arbeitsmappe zu schützen, sodass Arbeitsblätter in der Arbeitsmappe nicht verschoben, gelöscht, ausgeblendet, eingeblendet oder umbenannt und keine neuen Arbeitsblätter eingefügt werden können, geben Sie den ProtectionType als Structure an.

 Um Windows so zu schützen, dass sie bei jedem Öffnen der Arbeitsmappe dieselbe Größe und Position haben, geben Sie den ProtectionType als Windows an. In diesem Artikel zeigen wir, wie es geht[beschützen](/cells/de/net/protecting-and-unprotecting-workbooks/) und[entschützen](/cells/de/net/protecting-and-unprotecting-workbooks/) Arbeitsmappen mit VSTO und Aspose.Cells for .NET, damit Sie die beiden Methoden vergleichen können.

Aspose.Cells funktioniert unabhängig von Microsoft Office Automation und wurde entwickelt, um einfach zu verwenden und sauberen Code zu produzieren.

Das Schützen einer Arbeitsmappe hindert Benutzer nicht daran, Zellen zu bearbeiten. Um die Daten zu schützen, müssen Sie die Arbeitsblätter schützen.

{{% /alert %}} 
## **Schützen einer Arbeitsmappe**
Um eine vorhandene Microsoft-Excel-Datei zu öffnen, schützen Sie die Arbeitsmappe mit Struktur- und Windows-Attributen und speichern Sie die Datei.

Nachfolgend finden Sie parallele Codeausschnitte für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB), die zeigen, wie eine Arbeitsmappe geschützt wird.
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
## **Schutz einer Arbeitsmappe aufheben**
Um den Schutz einer Arbeitsmappe aufzuheben, verwenden Sie die folgenden Codezeilen für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB).
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
