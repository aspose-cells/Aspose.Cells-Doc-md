---
title: Ajouter un filigrane WordArt au graphique dans Aspose.Cells
type: docs
weight: 10
url: /fr/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

Vous pouvez utiliser WordArt pour ajouter des effets de texte spéciaux aux feuilles de calcul. Par exemple, étirez un titre, décorez du texte, adaptez le texte à une forme prédéfinie ou appliquez le texte affecté à la zone de traçage d'un graphique en tant que filigrane. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans vos feuilles de calcul pour ajouter de la décoration.

{{% /alert %}} 

L'exemple suivant montre comment ajouter une forme WordArt en tant que filigrane pour la zone de traçage d'un graphique existant. L'exemple utilise un modèle de fichier Excel qui contient déjà le graphique.

**Le fichier d'entrée** 

![tâche : image_autre_texte](picture1.png)

**Le fichier de sortie**

![tâche : image_autre_texte](picture2.png)

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";

//Open the existing excel file.

Workbook workbook = new Workbook(FileName);

//Get the chart in the first worksheet.

Aspose.Cells.Charts.Chart chart = workbook.Worksheets[0].Charts[0];

//Add a WordArt watermark (shape) to the chart's plot area.

Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the transparency.

wordArtFormat.Transparency = 0.9;

//Get the line format and make it invisible.

Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the excel file.

workbook.Save(FileName);

{{< /highlight >}}

## **Télécharger l'exemple de code**

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Télécharger l'exemple d'exécution**

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
