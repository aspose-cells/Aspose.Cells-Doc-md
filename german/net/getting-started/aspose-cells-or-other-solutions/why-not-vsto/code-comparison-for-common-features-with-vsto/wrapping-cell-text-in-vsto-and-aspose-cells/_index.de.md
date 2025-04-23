---
title: Zelltext in VSTO und Aspose.Cells umbrechen
type: docs
weight: 250
url: /de/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---

Um ein Arbeitsblatt mit zwei Zellen zu erstellen, eine mit umgebrochenem Text und eine ohne:

1. Richten Sie das Arbeitsblatt ein: 
   1. Ein Arbeitsbuch erstellen.
   1. Greifen Sie auf das erste Arbeitsblatt zu.
1. Text hinzufügen: 
   1. Fügen Sie Text zur Zelle A1 hinzu.
   1. Fügen Sie Text in Zelle A5 ein.
1. Speichern Sie die Tabelle.
   Die unten aufgeführten Codebeispiele zeigen, wie Sie diese Schritte mithilfe von VSTO entweder mit C# ausführen können. Codebeispiele, die zeigen, wie Sie dasselbe mit Aspose.Cells for .NET tun können, auch mit C#, folgen unmittelbar danach.

Wenn Sie den Code ausführen, entsteht eine Tabelle mit zwei Zellen, eine mit nicht umschlossenem und eine mit umschlossenem Text:

## **Ausgabe mit VSTO Excel**

![todo:image_alt_text](picture1.png)

## **Ausgabe mit Aspose.Cells for .NET**

![todo:image_alt_text](picture2.png)

## **VSTO**

{{< highlight csharp >}}

 //Access vsto application

Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

//Access workbook

Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

//Access worksheet

Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

//Access vsto worksheet

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

//Place some text in cell A1 without wrapping

Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

cellA1.Value = "Sample Text Unwrapped";

//Place some text in cell A5 with wrapping

Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

cellA5.Value = "Sample Text Wrapped";

cellA5.WrapText = true;

//Save the workbook

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 private static void WrappingCellText()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Place some text in cell A1 without wrapping

	Cell cellA1 = worksheet.Cells["A1"];

	cellA1.PutValue("Some Text Unwrapped");

	//Place some text in cell A5 wrapping

	Cell cellA5 = worksheet.Cells["A5"];

	cellA5.PutValue("Some Text Wrapped");

	Style style = cellA5.GetStyle();

	style.IsTextWrapped = true;

	cellA5.SetStyle(style);

	//Autofit rows

	worksheet.AutoFitRows();

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Beispielcode herunterladen**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
