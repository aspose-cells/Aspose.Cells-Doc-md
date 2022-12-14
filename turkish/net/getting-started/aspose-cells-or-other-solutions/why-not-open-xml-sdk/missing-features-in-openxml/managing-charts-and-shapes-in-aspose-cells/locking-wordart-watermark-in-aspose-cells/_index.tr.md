---
title: Aspose.Cells'de WordArt Filigranını Kilitleme
type: docs
weight: 40
url: /tr/net/locking-wordart-watermark-in-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells API'ler, çalışma sayfasına WordArt filigranları eklemenize olanak tanır; böylece WordArt, çalışma sayfasında hareket ettirebileceğiniz ve konumlandırabileceğiniz bir nesne haline gelir. Düzenleme, hareket ve seçim gibi herhangi bir etkileşim için WordArt nesnesini kilitlemek de mümkündür. Bu makalede, filigranın birkaç özelliğini kilitlemek için Shape.SetLockedProperty yönteminin kullanımı açıklanmaktadır.

{{% /alert %}} 

Aspose.Cells API'ler, kullanıcı etkileşiminin sınırlandırılabilmesi veya tamamen engellenmesi için filigranın belirli yönlerinin kilitlenmesine izin verir. Aşağıdaki kod parçacığı, sıfırdan bir elektronik tablo oluşturarak filigranın seçimini, hareketini, düzenlenmesini ve yeniden boyutlandırılmasını kilitlemek için Aspose.Cells for .NET API kullanımını göstermektedir.

**C#**

{{< highlight "csharp" >}}

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
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **Çalışan Örneği İndirin**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
