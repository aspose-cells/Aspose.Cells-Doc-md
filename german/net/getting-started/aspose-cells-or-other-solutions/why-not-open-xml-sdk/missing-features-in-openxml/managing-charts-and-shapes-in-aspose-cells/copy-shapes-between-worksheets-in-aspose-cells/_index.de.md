---
title: Formen zwischen Arbeitsblättern in Aspose.Cells kopieren
type: docs
weight: 30
url: /de/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

Manchmal müssen Elemente auf einem Arbeitsblatt, z. B. Bilder, Diagramme und andere Zeichenobjekte, zwischen Arbeitsblättern kopiert werden. Aspose.Cells unterstützt diese Funktion. Diagramme, Bilder und andere Objekte können mit höchster Präzision kopiert werden.

Dieser Artikel gibt Ihnen ein detailliertes Verständnis dafür, wie man Formen zwischen Arbeitsblättern kopiert. Zur Veranschaulichung erstellt er eine Konsolenanwendung in Visual Studio.Net, kopiert Bilder, Diagramme und andere Zeichenobjekte zwischen Arbeitsblättern mit Hilfe von Aspose.Cells.

{{% /alert %}} 

Im Folgenden finden Sie den Code zum Kopieren eines Diagramms von einem Arbeitsblatt auf ein anderes.

**C#**

{{< highlight csharp >}}

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

**Hinweis:** Für weitere Details zum Kopieren mehrerer Formen besuchen Sie [hier](/cells/de/net/copy-shapes-between-worksheets/)
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Laufendes Beispiel herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
