---
title: WordArt Wasserzeichen in Aspose.Cells sperren
type: docs
weight: 40
url: /de/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Die Aspose.Cells-APIs ermöglichen das Hinzufügen von WordArt-Wasserzeichen auf dem Arbeitsblatt in einer Weise, dass das WordArt zu einem Objekt wird, das auf dem Arbeitsblatt bewegt und positioniert werden kann. Es ist auch möglich, das WordArt-Objekt für jegliche Interaktion wie Bearbeiten, Verschieben und Auswahl zu sperren. Dieser Artikel erläutert die Verwendung der Shape.SetLockedProperty-Methode zum Sperren einiger Aspekte des Wasserzeichens.

{{% /alert %}} 

Die Aspose.Cells-APIs ermöglichen das Sperren bestimmter Aspekte des Wasserzeichens, damit die Benutzerinteraktion eingeschränkt oder vollständig blockiert werden kann. Der folgende Codeausschnitt zeigt die Verwendung der Aspose.Cells for .NET-API zum Sperren der Auswahl, Bewegung, Bearbeitung und Größenänderung des Wasserzeichens durch Erstellung einer Tabellenkalkulation von Grund auf.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Locking WordArt Watermark.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Lock Shape Aspects

wordart.IsLocked = true;

wordart.SetLockedProperty(ShapeLockType.Selection, true);

wordart.SetLockedProperty(ShapeLockType.ShapeType, true);

wordart.SetLockedProperty(ShapeLockType.Move, true);

wordart.SetLockedProperty(ShapeLockType.Resize, true);

wordart.SetLockedProperty(ShapeLockType.Text, true);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Laufendes Beispiel herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
