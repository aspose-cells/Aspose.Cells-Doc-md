---
title: Aggiungere un watermark WordArt al foglio di lavoro in Aspose.Cells
type: docs
weight: 20
url: /it/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

Usa WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, distendi un titolo sulla parte superiore del file, decora il testo e fai adattare il testo a una forma preimpostata, o applica il testo a un foglio di Excel come un watermark di sfondo. Il WordArt diventa un oggetto che puoi spostare o posizionare nei fogli di calcolo per aggiungere decorazioni.

{{% /alert %}}

L'esempio seguente mostra come aggiungere una forma WordArt per impostare un watermark di sfondo per un foglio di lavoro.

Dopo aver eseguito il codice, il file di output contiene un watermark WordArt rosso pallido.

**Il file di output 

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

## **Scarica il codice di esempio**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Scarica Esempio in Esecuzione**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
