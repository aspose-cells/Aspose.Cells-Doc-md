---
title: Wortkunst Wasserzeichen zur Tabelle hinzufügen mit Aspose.Cells
type: docs
weight: 10
url: /de/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - Wortkunst-Wasserzeichen zur Tabelle hinzufügen**
Verwenden Sie WordArt, um spezielle Texteffekte in Tabellenkalkulationen hinzuzufügen. Zum Beispiel, einen Titel über die Oberseite der Datei strecken, Text dekorieren und ihn an eine voreingestellte Form anpassen oder als Hintergrundwasserzeichen auf ein Excel-Blatt anwenden. Die WordArt wird zu einem Objekt, das Sie in Tabellenkalkulationen bewegen oder positionieren können, um Dekorationen hinzuzufügen.

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Wortkunst-Wasserzeichen zur Tabelle hinzufügen](/cells/de/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
