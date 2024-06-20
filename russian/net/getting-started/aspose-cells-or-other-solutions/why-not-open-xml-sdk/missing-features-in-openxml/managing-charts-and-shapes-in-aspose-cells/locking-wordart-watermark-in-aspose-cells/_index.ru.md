---
title: Блокировка водяного знака WordArt в Aspose.Cells
type: docs
weight: 40
url: /ru/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

API Aspose.Cells позволяют добавлять водяные знаки WordArt на листе таким образом, что WordArt становится объектом, который можно перемещать и позиционировать на листе. Также возможно заблокировать объект WordArt для любых взаимодействий, таких как редактирование, перемещение и выбор. В этой статье объясняется использование метода Shape.SetLockedProperty для блокировки нескольких аспектов водяного знака.

{{% /alert %}} 

API Aspose.Cells позволяет блокировать определенные аспекты водяного знака, чтобы пользовательское взаимодействие могло быть ограничено или полностью заблокировано. Нижеприведенный фрагмент кода демонстрирует использование Aspose.Cells for .NET API для блокировки выбора, перемещения, редактирования и изменения размера водяного знака при создании электронной таблицы с нуля.

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
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Скачать пример выполнения**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
