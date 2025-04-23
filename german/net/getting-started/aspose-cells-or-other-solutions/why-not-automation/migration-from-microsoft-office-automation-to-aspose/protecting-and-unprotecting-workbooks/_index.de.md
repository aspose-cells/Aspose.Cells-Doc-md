---
title: Arbeitsmappen schützen und schützen aufheben
type: docs
weight: 20
url: /de/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

Um zu verhindern, dass jemand Arbeitsblätter versehentlich oder absichtlich ändert, verschiebt oder löscht, können Sie Arbeitsmappenelemente mit oder ohne Kennwort schützen. Um die Struktur einer Arbeitsmappe zu schützen, damit Tabellenblätter in der Arbeitsmappe nicht verschoben, gelöscht, ausgeblendet, eingeblendet oder umbenannt und keine neuen Tabellenblätter eingefügt werden können, geben Sie den ProtectionType als Struktur an.

Um Windows zu schützen, sodass sie jedes Mal, wenn die Arbeitsmappe geöffnet wird, die gleiche Größe und Position haben, geben Sie den ProtectionType als Windows an. In diesem Artikel zeigen wir, wie man Arbeitsmappen mit VSTO und Aspose.Cells for .NET [schützt](/cells/de/net/protecting-and-unprotecting-workbooks/) und [entsperrt](/cells/de/net/protecting-and-unprotecting-workbooks/), um Ihnen zu ermöglichen, die beiden Methoden zu vergleichen.

Aspose.Cells funktioniert unabhängig von der Microsoft Office-Automatisierung und ist darauf ausgelegt, einfach zu bedienen zu sein und sauberen Code zu erzeugen.

Das Schützen einer Arbeitsmappe verhindert nicht, dass Benutzer Zellen bearbeiten. Um die Daten zu schützen, müssen Sie die Arbeitsblätter schützen.

{{% /alert %}} 
## **Schützen einer Arbeitsmappe**
Um eine vorhandene Microsoft Excel-Datei zu öffnen, schützen Sie die Arbeitsmappe mit Struktur- und Windows-Attributen und speichern Sie die Datei.

Nachfolgend finden Sie parallele Code-Schnipsel für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB), die zeigen, wie man eine Arbeitsmappe schützt.
### **VSTO**
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

{{< highlight csharp >}}

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
## **Entsperren einer Arbeitsmappe**
Um eine Arbeitsmappe zu entsperren, verwenden Sie die folgenden Codezeilen für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
