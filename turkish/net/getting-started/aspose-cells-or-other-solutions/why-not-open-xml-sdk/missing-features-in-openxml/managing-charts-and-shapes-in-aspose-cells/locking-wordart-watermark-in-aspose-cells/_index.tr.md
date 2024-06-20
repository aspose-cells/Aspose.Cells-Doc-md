---
title: Aspose.Cells te Kelime Sanatı Filigran Kilitleme
type: docs
weight: 40
url: /tr/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells API'leri, çalışma sayfasına Kelime Sanatı filigranları eklemenize olanak tanırken, Kelime Sanatı'nın düzenleme, hareket ve seçme gibi etkileşimlerine kilitlenmesine de olanak tanır. Bu makale, Shape.SetLockedProperty yönteminin kullanımını, bir filigranın bazı yönlerini kilitlemek için açıklar.

{{% /alert %}} 

Aspose.Cells API'ları, kullanıcı etkileşiminin sınırlı veya tamamen engellenmiş olmasını sağlamak için filigranın belirli yönlerini kilitlemeye olanak tanır. Aşağıdaki kod parçacığı, Aspose.Cells for .NET API'sinin kullanımını göstererek filigranın seçim, hareket, düzenleme ve yeniden boyutlandırmayı kilitler ve sıfırdan bir elektronik tablo oluşturur.

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
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Örnek Çalışmayı İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
