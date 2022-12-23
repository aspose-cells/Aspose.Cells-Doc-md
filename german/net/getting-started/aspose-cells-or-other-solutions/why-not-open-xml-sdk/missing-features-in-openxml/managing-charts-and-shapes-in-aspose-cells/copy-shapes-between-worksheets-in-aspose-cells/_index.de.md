---
title: Kopieren Sie Formen zwischen Arbeitsblättern in Aspose.Cells
type: docs
weight: 30
url: /de/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

Manchmal müssen Sie Elemente auf einem Arbeitsblatt, z. B. Bilder, Diagramme und andere Zeichenobjekte, zwischen Arbeitsblättern kopieren. Aspose.Cells unterstützt diese Funktion. Diagramme, Bilder und andere Objekte können mit höchster Präzision kopiert werden.

In diesem Artikel erfahren Sie ausführlich, wie Sie Formen zwischen Arbeitsblättern kopieren. Zur Veranschaulichung erstellt es eine Konsolenanwendung in Visual Studio.Net, kopiert Bilder, Diagramme und andere Zeichenobjekte zwischen Arbeitsblättern mit Aspose.Cells.

{{% /alert %}} 

Unten ist der Code zum Kopieren eines Diagramms von einem Arbeitsblatt in ein anderes

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Notiz:** Weitere Informationen zum Kopieren mehrerer Formen finden Sie unter[Hier](/cells/de/net/copy-shapes-between-worksheets/)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Laufendes Beispiel herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
