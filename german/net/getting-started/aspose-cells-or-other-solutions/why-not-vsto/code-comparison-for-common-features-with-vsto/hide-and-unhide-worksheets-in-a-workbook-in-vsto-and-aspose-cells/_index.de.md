---
title: Arbeitsblätter in einem Workbook in VSTO und Aspose.Cells ausblenden und einblenden
type: docs
weight: 140
url: /de/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

Dieser Artikel vergleicht das Ausblenden und Einblenden von Arbeitsblättern mit VSTO unter Verwendung von C# oder Visual Basic mit der Ausführung derselben Aufgabe mit Aspose.Cells unter Verwendung von C# oder Visual Basic. Aspose.Cells ermöglicht es Ihnen, auch ohne Microsoft Excel installiert zu arbeiten.

Die Schritte zum Ausblenden eines Arbeitsblatts lauten:

1. Öffnen Sie eine Datei.
1. Holen Sie sich ein Arbeitsblatt.
1. Blenden Sie das Arbeitsblatt aus.
1. Speichern Sie die Datei.
   Um ein Arbeitsblatt erneut anzuzeigen, schalten Sie einfach die Sichtbarkeit für das versteckte Arbeitsblatt um.

Die unten stehenden Codebeispiele zeigen zunächst, wie man ein Arbeitsblatt ausblendet. Die ersten Beispiele zeigen den Prozess mit VSTO unter Verwendung von C#, im Vergleich zur Verwendung von Aspose.Cells, erneut unter Verwendung von C#.

Die zweite Reihe von Codebeispielen zeigt die Zeile, die zum Einblenden des Arbeitsblatts in VSTO oder Aspose.Cells verwendet wird.
## **Ausblenden von Arbeitsblättern**
Im Folgenden sind Codebeispiele für VSTO und Aspose.Cells aufgeführt, die zeigen, wie ein Arbeitsblatt in einem Workbook ausgeblendet wird.
### **VSTO**
{{< highlight csharp >}}

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
{{< highlight csharp >}}

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
## **Arbeitsblatt ausblenden**
Nachfolgend finden Sie Codedemonstrationen für VSTO und Aspose.Cells, die zeigen, wie ein Arbeitsblatt in einer Arbeitsmappe eingeblendet wird.
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
