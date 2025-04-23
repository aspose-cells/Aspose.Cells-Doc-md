---
title: Rahmen zu Zellen in einem Arbeitsblatt in VSTO und Aspose.Cells hinzufügen
type: docs
weight: 10
url: /de/net/add-borders-to-cells-in-a-worksheet-in-vsto-and-aspose-cells/
---

Um Rahmen zu Zellen in einem Tabellenblatt hinzuzufügen, befolgen Sie die folgenden Schritte:

1. Richten Sie das Arbeitsblatt ein: 
   1. Ein Application-Objekt instanziieren (nur VSTO)
   1. Ein Arbeitsbuch hinzufügen
   1. Das erste Blatt abrufen
   1. Fügen Sie Text zu den Zellen hinzu, zu denen Sie Rahmen hinzufügen möchten
1. Füge Rahmen hinzu: 
   1. Definieren Sie einen Bereich
   1. Wenden Sie einen Rahmenstil auf den Bereich an
   1. Wiederholen Sie dies für jeden Bereich und jeden Rahmenstil, den Sie einstellen möchten. Dieses Beispiel wendet Haarlinien, dünnen, mittleren und dicken Linien an
1. Beenden: 
   1. Passen Sie die Spalte, in der die Zellen stehen, an, um den Text ordentlich anzupassen
   1. Speichern Sie das Dokument

Diese Schritte sind im folgenden Code dargestellt. Die ersten Codebeispiele zeigen, wie man sie mit VSTO entweder in C# oder Visual Basic implementiert. Nach den VSTO-Beispielen folgen Beispiele, die zeigen, wie man dieselben Schritte mithilfe von Aspose.Cells for .NET ausführt, wiederum entweder in C# oder Visual Basic. Die Aspose.Cells-Codebeispiele sind viel kürzer, da Aspose.Cells für effizientes Codieren optimiert ist.

Der Code generiert eine Excel-Datei mit einer Anzahl von Zellen auf dem ersten Blatt, von denen jede einen anderen Rahmen hat:

![todo:image_alt_text](picture1.png)

Zellen mit angewendeten Rahmen.
## **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;

//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;

//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;

//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;

//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();

//Save the excel file.

objBook.SaveAs("ApplyBorders.xls",

            Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Type.Missing);

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];

//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

 Aspose.Cells.Range _range;

 _range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

 _range.SetOutlineBorders(CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("ApplyBorders.xls");


{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Borders.to.Cells.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
