---
title: Aspose.Cells te Çalışma Sayfasına Kelime Sanatı Filigran Ekle
type: docs
weight: 20
url: /tr/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

WordArt'ı kullanarak elektronik tablolara özel metin efektleri ekleyin. Örneğin, başlığı dosyanın üst kısmına uzatın, metni süsleyin ve metni önceden ayarlanmış bir şekle uygun hale getirin veya metni bir Excel çalışma sayfasına arka plan filigranı olarak uygulayın. WordArt, elektronik tablolara dekorasyon eklemek için taşıyabileceğiniz bir nesne haline gelir.

{{% /alert %}}

Aşağıdaki örnek, bir çalışma sayfası için arka plan filigranı olarak bir WordArt şekli eklemenin nasıl yapıldığını göstermektedir.

Kod çalıştırıldıktan sonra çıktı dosyası soluk kırmızı bir WordArt filigranı içerir.

**Çıkış dosyası** 

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

## **Örnek Kod İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Örnek Çalışmayı İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
