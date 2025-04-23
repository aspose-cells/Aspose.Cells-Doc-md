---
title: Lägg till Word Art vattenstämpel i arbetsbok med Aspose.Cells
type: docs
weight: 10
url: /sv/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - Lägg till Word Art-vattenstämpel i arbetsbok**
Använd WordArt för att lägga till speciella texteffekter i kalkylblad. Till exempel, sträck en titel överst på filen, dekorera text och få texten att passa en förinställd form, eller applicera text på ett Excel-ark som en bakgrundsvattenstämpel. WordArt blir en objekt som du kan flytta eller positionera i kalkylblad för att lägga till dekoration.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

För mer information, besök [Lägg till WordArt-vattenstämpel i arbetsblad](/cells/sv/java/lagg-till-wordart-vattenstampel-i-arbetsblad).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
