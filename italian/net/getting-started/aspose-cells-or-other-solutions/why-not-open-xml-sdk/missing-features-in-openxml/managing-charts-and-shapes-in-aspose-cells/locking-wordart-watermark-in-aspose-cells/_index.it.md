---
title: Blocco Filigrana WordArt in Aspose.Cells
type: docs
weight: 40
url: /it/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Le API di Aspose.Cells consentono di aggiungere filigrane WordArt nel foglio di lavoro in modo che il WordArt diventi un oggetto che può essere spostato e posizionato nel foglio di lavoro. È inoltre possibile bloccare l'oggetto WordArt per qualsiasi interazione come modifica, spostamento e selezione. Questo articolo spiega l'uso del metodo Shape.SetLockedProperty per bloccare alcuni aspetti della filigrana.

{{% /alert %}} 

Le API di Aspose.Cells consentono di bloccare alcuni aspetti della filigrana in modo che l'interazione dell'utente possa essere limitata o completamente bloccata. Il seguente frammento di codice dimostra l'uso dell'API Aspose.Cells for .NET per bloccare la selezione, lo spostamento, la modifica e il ridimensionamento della filigrana creando un foglio di calcolo da zero.

**C#**

{{< highlight csharp >}}

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Scarica Esempio in Esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
