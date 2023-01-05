---
title: Aspose.Cells'i kullanarak Çalışma Sayfasına Word Art Filigranı ekleyin
type: docs
weight: 10
url: /tr/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - Çalışma Sayfasına Word Art Filigranı Ekle**
Elektronik tablolara özel metin efektleri eklemek için WordArt'ı kullanın. Örneğin, bir başlığı dosyanın üst kısmına uzatın, metni süsleyin ve metni önceden ayarlanmış bir şekle sığdırın veya metni bir Excel sayfasına arka plan filigranı olarak uygulayın. WordArt, dekorasyon eklemek için elektronik tablolarda taşıyabileceğiniz veya konumlandırabileceğiniz bir nesne haline gelir.

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
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Sayfasına WordArt Filigranı Ekleme](/cells/tr/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
