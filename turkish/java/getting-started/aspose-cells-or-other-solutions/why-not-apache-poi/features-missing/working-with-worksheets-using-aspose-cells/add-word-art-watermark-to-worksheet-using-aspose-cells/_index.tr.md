---
title: Aspose.Cells Kullanarak Elektronik Tabloya Word Art Filigran Ekleme
type: docs
weight: 10
url: /tr/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - Elektronik Tabloya Word Art Filigran Ekleme**
Elektronik tablolara özel metin efektleri eklemek için WordArt'ı kullanın. Örneğin, başlığı dosyanın üst kısmına yayabilir, metni süsleyebilir ve metni önceden ayarlanmış bir şekle sığdırabilir veya metni bir Excel tablosuna arkaplan filigranı olarak uygulayabilirsiniz. WordArt, elektronik tablolara dekorasyon eklemek için hareket ettirebileceğiniz veya konumlandırabileceğiniz bir nesne haline gelir.

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
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Çalışma Sayfasına Kelime Sanatı Filigranı Ekle](/cells/tr/java/çalışma-sayfasına-kelime-sanatı-filigranı-ekle) sayfasını ziyaret edin.

{{% /alert %}}
