---
title: Sperren des WordArt-Wasserzeichens in Aspose.Cells
type: docs
weight: 40
url: /de/net/locking-wordart-watermark-in-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells APIs ermöglichen das Hinzufügen von WordArt-Wasserzeichen auf dem Arbeitsblatt, sodass die WordArt zu einem Objekt wird, das Sie auf dem Arbeitsblatt verschieben und positionieren können. Es ist auch möglich, das WordArt-Objekt für jede Interaktion wie Bearbeiten, Verschieben und Auswählen zu sperren. In diesem Artikel wird die Verwendung der Shape.SetLockedProperty-Methode erläutert, um einige Aspekte des Wasserzeichens zu sperren.

{{% /alert %}} 

Aspose.Cells APIs ermöglichen es, bestimmte Aspekte des Wasserzeichens zu sperren, sodass die Benutzerinteraktion eingeschränkt oder vollständig blockiert werden kann. Das folgende Code-Snippet demonstriert die Verwendung von Aspose.Cells for .NET API zum Sperren der Auswahl, Bewegung, Bearbeitung und Größenänderung des Wasserzeichens durch Erstellen einer Tabelle von Grund auf neu.

**C#**

{{< highlight "csharp" >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Laufendes Beispiel herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
