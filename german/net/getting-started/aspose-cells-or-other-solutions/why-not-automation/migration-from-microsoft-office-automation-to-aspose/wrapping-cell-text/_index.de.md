---
title: Text in Zelle umbrechen
type: docs
weight: 130
url: /de/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

Durch Umbruch wird das Lesen erleichtert: Eine Zelle mit umbrochenem Text passt sich an, um den Text so zu erweitern, dass er nicht über anderen Zellen angezeigt wird.

Mit Aspose.Cells for .NET können Entwickler die meisten Aufgaben in ihren Anwendungen ausführen, die Benutzer mit Microsoft Excel ausführen können, einschließlich des Umbruchs von Text in Zellen. Dieser Artikel erklärt, wie dies funktioniert und vergleicht die Aufgabe mit VSTO und Aspose.Cells. Aspose.Cells ist optimiert für effizientes Codieren und funktioniert ohne Microsoft Automation.

{{% /alert %}}

## **Text in Zelle umbrechen**

Um ein Arbeitsblatt mit zwei Zellen zu erstellen, eine mit umgebrochenem Text und eine ohne:

1. Richten Sie das Arbeitsblatt ein:
   1. Ein Arbeitsbuch erstellen.
   1. Greifen Sie auf das erste Arbeitsblatt zu.
1. Text hinzufügen:
   1. Fügen Sie Text zur Zelle A1 hinzu.
   1. Fügen Sie Text in Zelle A5 ein.
1. Speichern Sie die Tabelle.

Die unten stehenden Codebeispiele zeigen, wie diese Schritte mithilfe von [VSTO](/cells/de/net/wrapping-cell-text/) entweder mit C# oder Visual Basic durchgeführt werden können. Codebeispiele, die zeigen, wie das Gleiche mithilfe von [Aspose.Cells for .NET](/cells/de/net/wrapping-cell-text/) und wieder entweder mit C# oder Visual Basic gemacht wird, folgen unmittelbar danach.

Wenn Sie den Code ausführen, entsteht eine Tabelle mit zwei Zellen, eine mit nicht umschlossenem und eine mit umschlossenem Text:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **Zelletext umschließen mit VSTO**

**C#**

{{< highlight csharp >}}

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

### **Zelletext umschließen mit Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
