---
title: Arbeitsblätter in einer Arbeitsmappe ausblenden und einblenden
type: docs
weight: 80
url: /de/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

Beim Präsentieren von Arbeitsmappen für Kunden oder bei einer Präsentation kann es nützlich sein, Arbeitsblätter in einer Arbeitsmappe auszublenden. Ein strukturierter Ansatz zur Modellierung von Tabellenkalkulationen legt nahe, dass Daten, Formeln und Visualisierungen wie Diagramme auf separaten Blättern aufbewahrt werden. Dieser Ansatz hält das Layout sauber und einfach und erleichtert die Navigation in der Arbeitsmappe. Wenn Sie Ergebnisse präsentieren, möchten Sie möglicherweise die Daten- oder Formelblätter ausblenden, um Ablenkungen zu vermeiden.

Benutzer, die mit Microsoft Excel arbeiten, können Arbeitsblätter ganz einfach ausblenden und dann wieder einblenden. Die gleichen Funktionen stehen auch Entwicklern zur Verfügung, die mit Excel-Tabellenkalkulationen programmieren. Es gibt verschiedene Möglichkeiten, mit Tabellenkalkulationen aus Softwareanwendungen heraus zu arbeiten. Eine Methode besteht darin, VSTO zu verwenden, eine andere ist Aspose.Cells for .NET.

{{% /alert %}}

## **Arbeitsblätter ausblenden und einblenden**

In diesem Artikel werden [Ausblenden](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) und [Einblenden](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) von Arbeitsblättern mit [VSTO](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/), unter Verwendung von entweder C# oder Visual Basic, verglichen, um dieselbe Aufgabe mit [Aspose.Cells](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) mit wiederum entweder C# oder Visual Basic durchzuführen. Aspose.Cells ermöglicht es Ihnen, ohne Microsoft Excel zu arbeiten.

Die Schritte zum Ausblenden eines Arbeitsblatts lauten:

1. Öffnen Sie eine Datei.
1. Holen Sie sich ein Arbeitsblatt.
1. Blenden Sie das Arbeitsblatt aus.
1. Speichern Sie die Datei.

Um das Arbeitsblatt wieder [einzublenden](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/), schalten Sie einfach die Sichtbarkeit für das ausgeblendete Blatt um.

Die nachfolgenden Codebeispiele zeigen zuerst, wie man ein Arbeitsblatt ausblendet. Die ersten Beispiele zeigen den Prozess mit [VSTO](/cells/de/net/Arbeitsblätter-in-einer-Arbeitsmappe-ausblenden-und-einblenden/), entweder in C# oder Visual Basic, im Vergleich zur Verwendung von [Aspose.Cells](/cells/de/net/Arbeitsblätter-in-einer-Arbeitsmappe-ausblenden-und-einblenden/), wiederum unter Verwendung von C# oder Visual Basics.

Die zweite Gruppe von Codebeispielen zeigt die Zeile, die zum Einblenden des Arbeitsblatts in [VSTO](/cells/de/net/Arbeitsblätter-in-einer-Arbeitsmappe-ausblenden-und-einblenden/) oder [Aspose.Cells](/cells/de/net/Arbeitsblätter-in-einer-Arbeitsmappe-ausblenden-und-einblenden/) verwendet wird.

## **Ausblenden von Arbeitsblättern**

Im Folgenden sind Codebeispiele für VSTO und Aspose.Cells aufgeführt, die zeigen, wie ein Arbeitsblatt in einem Workbook ausgeblendet wird.

### **Arbeitsblätter ausblenden mit VSTO**

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


### **Arbeitsblätter mit Aspose.Cells for .NET ausblenden**

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

## **Arbeitsblätter wieder einblenden**

Nachfolgend finden Sie Codedemonstrationen für VSTO und Aspose.Cells, die zeigen, wie ein Arbeitsblatt in einer Arbeitsmappe eingeblendet wird.

### **Ein Arbeitsblatt mit VSTO wieder einblenden**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Ein Arbeitsblatt mit Aspose.Cells for .NET wieder einblenden**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
