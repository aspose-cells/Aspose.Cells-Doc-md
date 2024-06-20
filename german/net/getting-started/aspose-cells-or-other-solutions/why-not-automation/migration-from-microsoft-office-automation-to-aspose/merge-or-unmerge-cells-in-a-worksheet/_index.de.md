---
title: Zusammenführen oder Aufteilen von Zellen in einem Arbeitsblatt
type: docs
weight: 40
url: /de/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Beim Arbeiten mit Arbeitsblättern müssen Sie häufig einen Titel/Überschrift in einer einzelnen Zelle erstellen, der über dem Arbeitsblatt steht. Möglicherweise erstellen Sie eine Rechnung und möchten weniger Spalten für die Gesamt- oder Zusammenfassungswerte. Wenn Sie eine Zelle aus zwei oder mehr Zellen erstellen möchten, müssen Sie die Zellen zusammenführen. Wir führen die Aufgabe unabhängig mit VSTO und Aspose.Cells for .NET durch.

{{% /alert %}}

## **Beschreibung**

Öffnen Sie eine vorhandene Excel-Datei, führen Sie einige Zellen im ersten Arbeitsblatt in der Arbeitsmappe zusammen und speichern Sie die Excel-Datei.

## **Zellen zusammenführen**

Im Folgenden finden Sie parallele Code-Schnipsel für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

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

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the range of cells i.e.., A1:C1.

Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.

rng1.Merge(Missing.Value);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

rng1.Merge();

//Save the file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Aufteilen der Zellen**

Um die Zelle(n) aufzuteilen, verwenden Sie die folgenden Codezeilen für VSTO (C#, VB) und Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
