---
title: Aggiungi filigrana Word Art al foglio di lavoro utilizzando Aspose.Cells
type: docs
weight: 10
url: /it/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - Aggiungi filigrana Word Art al foglio di lavoro**
Usa WordArt per aggiungere effetti di testo speciali ai fogli di calcolo. Ad esempio, allunga un titolo nella parte superiore del file, decora il testo e adatta il testo a una forma preimpostata oppure applica il testo a un foglio Excel come filigrana di sfondo. La WordArt diventa un oggetto che puoi spostare o posizionare nei fogli di calcolo per aggiungere decorazioni.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Aggiungi filigrana WordArt al foglio di lavoro](/cells/it/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
