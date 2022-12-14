---
title: Arbeitsblätter in einer Arbeitsmappe ein- und ausblenden
type: docs
weight: 80
url: /de/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

Wenn Sie Kunden Arbeitsmappen präsentieren oder eine Präsentation halten, kann es hilfreich sein, Arbeitsblätter in einer Arbeitsmappe auszublenden. Ein strukturierter Ansatz für die Tabellenkalkulationsmodellierung legt nahe, dass Daten, Formeln und Visualisierungen wie Diagramme auf separaten Blättern aufbewahrt werden. Dieser Ansatz hält das Layout sauber und einfach und erleichtert die Navigation in der Arbeitsmappe. Beim Präsentieren von Ergebnissen möchten Sie möglicherweise die Daten oder Formelblätter ausblenden, um Ablenkungen zu vermeiden.

Benutzer, die in Microsoft Excel arbeiten, können Arbeitsblätter einfach ein- und ausblenden (anzeigen). Die gleichen Funktionen stehen Entwicklern zur Verfügung, die mit Excel-Tabellen programmieren. Es gibt verschiedene Möglichkeiten, mit Tabellenkalkulationen innerhalb von Softwareanwendungen zu arbeiten. Eine Methode ist die Verwendung von VSTO, eine andere ist Aspose.Cells for .NET.

{{% /alert %}}

## **Arbeitsblätter ein- und ausblenden**

 Dieser Artikel vergleicht[versteckt](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) und[Einblenden](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) Arbeitsblätter mit[VSTO](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) , entweder mit C# oder Visual Basic, um dieselbe Aufgabe auszuführen[Aspose.Cells](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/), wiederum entweder mit C# oder Visual Basic. Mit Aspose.Cells können Sie arbeiten, ohne dass Microsoft Excel installiert ist.

Die Schritte zum Ausblenden eines Arbeitsblatts sind:

1. Öffne einen Ordner.
1. Holen Sie sich ein Arbeitsblatt.
1. Blenden Sie das Arbeitsblatt aus.
1. Speicher die Datei.

 Zu[einblenden](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) wieder ein Arbeitsblatt, schalten Sie einfach die Sichtbarkeit für das ausgeblendete Blatt ein.

 Die folgenden Codebeispiele zeigen zunächst, wie ein Arbeitsblatt ausgeblendet wird. Die ersten Muster zeigen den Prozess mit[VSTO](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) , entweder mit C# oder Visual Basic, im Vergleich zur Verwendung von[Aspose.Cells](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/), wiederum entweder mit C# oder Visual Basics.

 Der zweite Satz von Codebeispielen zeigt die Zeile, die zum Einblenden des Arbeitsblatts verwendet wird[VSTO](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/) oder[Aspose.Cells](/cells/de/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Arbeitsblätter ausblenden**

Unten finden Sie Codebeispiele für VSTO und Aspose.Cells, die veranschaulichen, wie ein Arbeitsblatt in einer Arbeitsmappe ausgeblendet wird.

### **Ausblenden von Arbeitsblättern mit VSTO**

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


### **Ausblenden von Arbeitsblättern mit Aspose.Cells for .NET**

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

## **Arbeitsblätter einblenden**

Unten finden Sie Codebeispiele für VSTO und Aspose.Cells, die veranschaulichen, wie ein Arbeitsblatt in einer Arbeitsmappe eingeblendet wird.

### **Einblenden eines Arbeitsblatts mit VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Einblenden eines Arbeitsblatts mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
