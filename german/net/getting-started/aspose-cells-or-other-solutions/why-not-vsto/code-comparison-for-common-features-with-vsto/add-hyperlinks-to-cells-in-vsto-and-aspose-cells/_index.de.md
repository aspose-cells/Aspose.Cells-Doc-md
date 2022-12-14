---
title: Fügen Sie Hyperlinks zu Cells in VSTO und Aspose.Cells hinzu
type: docs
weight: 20
url: /de/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
Führen Sie die folgenden Schritte aus, um Hyperlinks zu Zellen in einer Tabelle hinzuzufügen:

1.  Erstellen Sie das Arbeitsblatt:
 1. Instanziieren Sie ein Anwendungsobjekt. (Nur VSTO.)
 1. Fügen Sie eine Arbeitsmappe hinzu.
 1. Holen Sie sich das erste Blatt.
 1. Fügen Sie Text zu den Zellen hinzu, denen Sie einen Hyperlink hinzufügen möchten.
1. Hyperlinks hinzufügen.
1. Speichern Sie das Dokument.

Diese Schritte werden in den folgenden Codebeispielen gezeigt. Das erste Beispiel zeigt, wie VSTO mit C# verwendet wird, um einer Zelle einen Hyperlink hinzuzufügen. Die folgenden Beispiele zeigen, wie man dasselbe mit Aspose.Cells for .NET macht, wiederum mit C#.

Die Codebeispiele generieren eine Excel-Datei mit einem Hyperlink in Zelle A1 auf dem ersten Arbeitsblatt.

![todo: Bild_alt_Text](picture1.png)

Zelle A1 wird ein Hyperlink hinzugefügt.

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Beispielcode herunterladen**

- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Quellenschmiede](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/herunterladen)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).Postleitzahl)
