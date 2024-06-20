---
title: Lägg till WordArt vattenstämpel på arbetsblad i Aspose.Cells
type: docs
weight: 20
url: /sv/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

 Använd WordArt för att lägga till speciella texteffekter till kalkylblad. Till exempel, sträck en rubrik överst på filen, dekorera text och få texten att passa en förinställd form eller applicera text på ett Excel-ark som en bakgrundsvattenstämpel. WordArt blir ett objekt som du kan flytta eller placera i kalkylblad för att lägga till dekoration.

{{% /alert %}}

Följande exempel visar hur man lägger till en WordArt-form för att ställa in en bakgrundsvattenstämpel för ett arbetsblad.

Efter att ha kört koden innehåller utdatafilen en blekröd WordArt-vattenstämpel.

**Utgångsfilen** 

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

## **Ladda ned provkoden**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Ladda ner exempel på körning**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
