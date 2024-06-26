---
title: WordArt Wasserzeichen zu Arbeitsblatt in Aspose.Cells hinzufügen
type: docs
weight: 20
url: /de/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

Verwenden Sie WordArt, um spezielle Texteffekte zu Tabellenkalkulationen hinzuzufügen. Zum Beispiel können Sie einen Titel über die Oberseite der Datei strecken, Text dekorieren und Text an eine Excel-Tabelle als Hintergrund-Wasserzeichen anwenden. Das WordArt wird zu einem Objekt, das Sie in Tabellenkalkulationen verschieben oder platzieren können, um Dekoration hinzuzufügen.

{{% /alert %}}

Das folgende Beispiel zeigt, wie ein WordArt-Objekt hinzugefügt wird, um ein Hintergrundwasserzeichen für ein Arbeitsblatt festzulegen.

Nach Ausführen des Codes enthält die Ausgabedatei ein blasses rotes WordArt-Wasserzeichen.

**Die Ausgabedatei** 

![todo:image_alt_text](picture1.png)

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Worksheet.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = System.Drawing.Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}

## **Beispielcode herunterladen**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Laufendes Beispiel herunterladen**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
