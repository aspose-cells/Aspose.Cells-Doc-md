---
title: Verrouillage du filigrane WordArt dans Aspose.Cells
type: docs
weight: 40
url: /fr/net/locking-wordart-watermark-in-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells Les API permettent d'ajouter des filigranes WordArt sur la feuille de calcul de manière à ce que le WordArt devienne un objet que vous pouvez déplacer et positionner sur la feuille de calcul. Il est également possible de verrouiller l'objet WordArt pour toute interaction telle que l'édition, le mouvement et la sélection. Cet article explique l'utilisation de la méthode Shape.SetLockedProperty pour verrouiller certains aspects du filigrane.

{{% /alert %}} 

Les API Aspose.Cells permettent de verrouiller certains aspects du filigrane afin que l'interaction de l'utilisateur puisse être limitée ou complètement bloquée. L'extrait de code suivant illustre l'utilisation de Aspose.Cells for .NET API pour verrouiller la sélection, le mouvement, l'édition et le redimensionnement du filigrane en créant une feuille de calcul à partir de zéro.

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
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Télécharger l'exemple d'exécution**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
