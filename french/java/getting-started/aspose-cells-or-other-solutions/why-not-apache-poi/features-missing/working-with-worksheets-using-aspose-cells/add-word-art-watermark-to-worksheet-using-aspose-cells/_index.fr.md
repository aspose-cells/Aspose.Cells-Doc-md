---
title: Ajouter un filigrane Word Art à la feuille de calcul à l aide d Aspose.Cells
type: docs
weight: 10
url: /fr/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - Ajouter un filigrane Word Art à la feuille de calcul**
Utilisez WordArt pour ajouter des effets spéciaux de texte aux feuilles de calcul. Par exemple, étirez un titre sur le dessus du fichier, décorez du texte et ajustez du texte à une forme prédéfinie, ou appliquez du texte à une feuille Excel en tant que filigrane de fond. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans les feuilles de calcul pour ajouter de la décoration.

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add Watermark

Shape wordart = sheet.getShapes().addTextEffect(MsoPresetTextEffect.TEXT_EFFECT_1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the shape's fill format

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency

wordArtFormat.setTransparency(0.9);

//Make the line invisible

wordart.setHasLine(false);

//Save the file

workbook.save(dataDir + "AsposeWatermark_Out.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Ajouter un filigrane WordArt à la feuille de calcul](/cells/fr/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
