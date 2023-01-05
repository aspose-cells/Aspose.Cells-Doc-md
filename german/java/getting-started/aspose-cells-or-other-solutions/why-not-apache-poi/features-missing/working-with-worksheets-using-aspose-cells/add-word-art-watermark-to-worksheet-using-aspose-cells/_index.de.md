---
title: Fügen Sie dem Arbeitsblatt Word Art Watermark mit Aspose.Cells hinzu
type: docs
weight: 10
url: /de/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - Fügen Sie dem Arbeitsblatt ein Word Art-Wasserzeichen hinzu**
Verwenden Sie WordArt, um Tabellenkalkulationen spezielle Texteffekte hinzuzufügen. Ziehen Sie beispielsweise einen Titel über den oberen Rand der Datei, dekorieren Sie Text und passen Sie Text an eine voreingestellte Form an oder wenden Sie Text als Hintergrundwasserzeichen auf eine Excel-Tabelle an. Die WordArt wird zu einem Objekt, das Sie verschieben oder in Tabellenkalkulationen positionieren können, um Dekoration hinzuzufügen.

**Java**

{{< highlight "java" >}}

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
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[WordArt-Wasserzeichen zum Arbeitsblatt hinzufügen](/cells/de/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
