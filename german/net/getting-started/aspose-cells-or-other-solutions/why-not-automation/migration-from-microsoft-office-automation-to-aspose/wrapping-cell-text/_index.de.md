---
title: Umbruch Cell Text
type: docs
weight: 130
url: /de/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

Das Umbrechen von Text erleichtert das Lesen: Eine Zelle mit umbrochenem Text wird erweitert, um sie an den Text anzupassen, sodass der Text nicht über anderen Zellen angezeigt wird.

Mit Aspose.Cells for .NET können Entwickler die meisten Aufgaben in ihren Anwendungen ausführen, die Benutzer mit Microsoft Excel ausführen können, einschließlich Textumbruch in Zellen. Dieser Artikel erklärt, wie und vergleicht die Aufgabe mit VSTO und Aspose.Cells. Aspose.Cells ist für effizientes Codieren optimiert und funktioniert ohne Microsoft-Automatisierung.

{{% /alert %}}

## **Umbruch Cell Text**

So erstellen Sie ein Arbeitsblatt mit zwei Zellen, eine mit umbrochenem Text und eine ohne:

1. Erstellen Sie das Arbeitsblatt:
 1. Erstellen Sie eine Arbeitsmappe.
 1. Greifen Sie auf das erste Arbeitsblatt zu.
1. Text hinzufügen:
 1. Fügen Sie Text zu Zelle A1 hinzu.
 1. Fügen Sie umgebrochenen Text zu Zelle A5 hinzu.
1. Speichern Sie die Tabelle.

 Die folgenden Codebeispiele zeigen, wie Sie diese Schritte mit ausführen[VSTO](/cells/de/net/wrapping-cell-text/) entweder mit C# oder Visual Basic. Codebeispiele, die zeigen, wie man dasselbe mit macht[Aspose.Cells for .NET](/cells/de/net/wrapping-cell-text/), wiederum mit entweder C# oder Visual Basic folgen unmittelbar danach.

Das Ausführen des Codes führt zu einer Tabelle mit zwei Zellen, eine mit nicht umbrochenem Text und eine mit:

|<p>**Geben Sie den Zellentext mit VSTO aus** </p><p>![todo: Bild_alt_Text](wrapping-cell-text_1.png)</p>|<p>**Zeilenumbruchtext mit Aspose.Cells for .NET ausgeben** </p><p>![todo: Bild_alt_Text](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **Umbruch von Cell Text mit VSTO**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

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

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Umbruch von Cell Text mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

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

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
