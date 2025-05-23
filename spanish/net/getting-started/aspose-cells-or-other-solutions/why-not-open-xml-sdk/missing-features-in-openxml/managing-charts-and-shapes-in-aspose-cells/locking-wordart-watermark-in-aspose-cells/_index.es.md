---
title: Bloquear una Marca de Agua de WordArt en Aspose.Cells
type: docs
weight: 40
url: /es/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Los APIs de Aspose.Cells permiten agregar marcas de agua de WordArt en la hoja de cálculo de manera que el WordArt se convierta en un objeto que se puede mover y posicionar en la hoja de cálculo. También es posible bloquear el objeto WordArt para cualquier interacción, como la edición, el movimiento y la selección. Este artículo explica el uso del método Shape.SetLockedProperty para bloquear algunos aspectos de la marca de agua.

{{% /alert %}} 

Los APIs de Aspose.Cells permiten bloquear ciertos aspectos de la marca de agua para que la interacción del usuario pueda ser limitada o completamente bloqueada. El siguiente fragmento de código demuestra el uso del API Aspose.Cells for .NET para bloquear la selección, el movimiento, la edición y el redimensionamiento de la marca de agua mediante la creación de una hoja de cálculo desde cero.

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
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Descargar Ejemplo en Ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
