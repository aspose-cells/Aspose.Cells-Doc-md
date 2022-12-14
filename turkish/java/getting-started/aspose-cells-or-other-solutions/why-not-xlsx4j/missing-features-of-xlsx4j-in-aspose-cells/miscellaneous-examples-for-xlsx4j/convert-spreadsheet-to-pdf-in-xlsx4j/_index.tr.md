---
title: Elektronik Tabloyu xlsx4j'de PDF'ye Dönüştür
type: docs
weight: 10
url: /tr/java/convert-spreadsheet-to-pdf-in-xlsx4j/
---
## **Aspose.Cells - XLS'yi PDF'ye dönüştür**
PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde standart bir format olarak yaygın şekilde kullanılmaktadır. Yazılım geliştiricilerinden genellikle Microsoft Excel dosyalarını kolayca PDF belgelerine dönüştürmenin bir yolunu bulmaları istenir. Aspose.Cells bu özelliği destekler.

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Save the document in PDF format

workbook.save(dataDir + "AsposeConvert.pdf", SaveFormat.PDF);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/converter/converttoformats/AsposeConverter.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Excel'i PDF Dosyalarına Dönüştürme](/java/converting-excel-to-pdf-files).

{{% /alert %}}
