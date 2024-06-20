---
title: Ajouter un filigrane WordArt à la feuille de calcul dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

Utilisez WordArt pour ajouter des effets de texte spéciaux aux feuilles de calcul. Par exemple, étirez un titre sur le dessus du fichier, décorez du texte et faites en sorte que le texte s'adapte à une forme prédéfinie, ou appliquez du texte à une feuille Excel en tant que filigrane en arrière-plan. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans les feuilles de calcul pour ajouter une décoration.

{{% /alert %}}

L'exemple suivant montre comment ajouter une forme WordArt pour définir un filigrane en arrière-plan pour une feuille de calcul.

Après l'exécution du code, le fichier de sortie contient un filigrane WordArt rouge pâle.

**Le fichier de sortie** 

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

## **Télécharger le code source d'exemple**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Télécharger un exemple en cours d'exécution**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
