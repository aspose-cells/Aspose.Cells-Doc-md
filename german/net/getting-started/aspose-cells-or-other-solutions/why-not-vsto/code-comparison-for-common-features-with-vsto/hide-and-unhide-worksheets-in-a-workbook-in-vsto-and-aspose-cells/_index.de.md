---
title: Ausblenden und Einblenden von Arbeitsblättern in einer Arbeitsmappe in VSTO und Aspose.Cells
type: docs
weight: 140
url: /de/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
Dieser Artikel vergleicht das Aus- und Einblenden von Arbeitsblättern mit VSTO unter Verwendung von C# oder Visual Basic mit dem Ausführen derselben Aufgabe mit Aspose.Cells, wiederum unter Verwendung von C# oder Visual Basic. Mit Aspose.Cells können Sie arbeiten, ohne dass Microsoft Excel installiert ist.

Die Schritte zum Ausblenden eines Arbeitsblatts sind:

1. Öffne einen Ordner.
1. Holen Sie sich ein Arbeitsblatt.
1. Blenden Sie das Arbeitsblatt aus.
1. Speicher die Datei.
 Um ein Arbeitsblatt wieder einzublenden, schalten Sie einfach die Sichtbarkeit für das ausgeblendete Blatt ein.

Die folgenden Codebeispiele zeigen zunächst, wie ein Arbeitsblatt ausgeblendet wird. Die ersten Beispiele zeigen den Prozess mit VSTO, wobei entweder C# verwendet wird, im Vergleich zur Verwendung von Aspose.Cells, wiederum mit entweder C#.

Der zweite Satz von Codebeispielen zeigt die Zeile, die zum Einblenden des Arbeitsblatts in VSTO oder Aspose.Cells verwendet wird.
## **Arbeitsblätter ausblenden**
Unten finden Sie Codebeispiele für VSTO und Aspose.Cells, die veranschaulichen, wie ein Arbeitsblatt in einer Arbeitsmappe ausgeblendet wird.
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
## **Einblenden des Arbeitsblatts**
Unten finden Sie Codebeispiele für VSTO und Aspose.Cells, die veranschaulichen, wie ein Arbeitsblatt in einer Arbeitsmappe eingeblendet wird.
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
## **Beispielcode herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Quellenschmiede](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/herunterladen)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).Postleitzahl)
