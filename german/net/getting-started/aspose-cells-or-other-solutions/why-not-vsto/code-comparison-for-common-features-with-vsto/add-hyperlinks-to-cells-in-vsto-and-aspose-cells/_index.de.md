---
title: Hyperlinks zu Zellen in VSTO und Aspose.Cells hinzufügen
type: docs
weight: 20
url: /de/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

Um Hyperlinks zu Zellen in einer Tabelle hinzuzufügen, befolgen Sie die folgenden Schritte:

1. Richten Sie das Arbeitsblatt ein: 
   1. Instanziieren Sie ein Application-Objekt (nur VSTO).
   1. Fügen Sie ein Arbeitsbuch hinzu.
   1. Holen Sie sich das erste Blatt.
   1. Fügen Sie Text zu den Zellen hinzu, zu denen Sie einen Hyperlink hinzufügen möchten.
1. Fügen Sie einen Hyperlink hinzu.
1. Speichern Sie das Dokument.

Diese Schritte sind in den unten stehenden Codebeispielen dargestellt. Das erste Beispiel zeigt, wie Sie VSTO verwenden können, entweder mit C#, um einen Hyperlink zu einer Zelle hinzuzufügen. Die folgenden Beispiele zeigen, wie Sie dasselbe mit Aspose.Cells for .NET tun, wiederum unter Verwendung von C#.

Die Codesamples generieren eine Excel-Datei, die einen Hyperlink in Zelle A1 im ersten Arbeitsblatt enthält.

![todo:image_alt_text](picture1.png)

Ein Hyperlink wird zu Zelle A1 hinzugefügt.

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
