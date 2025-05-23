---
title: Låsa WordArt vattenstämpel i Aspose.Cells
type: docs
weight: 40
url: /sv/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells API:er tillåter att lägga till WordArt-vattenstämplar på arbetsbladet på ett sätt att WordArt blir ett objekt som du kan flytta och placera på arbetsbladet. Det är också möjligt att låsa WordArt-objektet för interaktioner som redigering, flyttning och val. Den här artikeln förklarar användningen av Shape.SetLockedProperty-metoden för att låsa några aspekter av vattenstämpeln.

{{% /alert %}} 

Aspose.Cells API:er tillåter att låsa vissa aspekter av vattenstämpeln så att användarinteraktionen kan vara begränsad eller helt blockerad. Följande kodsnutt demonstrerar användningen av Aspose.Cells for .NET API:et för att låsa val, rörelse, redigering och omformning av vattenstämpeln genom att skapa ett kalkylblad från grunden.

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
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Ladda ner exempel på körning**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
