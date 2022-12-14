---
title: Çalışma Kitabını xlsx4j'de HTML'ye Dönüştür
type: docs
weight: 10
url: /tr/java/convert-workbook-to-html-in-xlsx4j/
---
## **Aspose.Cells - Çalışma Kitabını HTML'ye Dönüştür**
 Aspose.Cells API'leri, elektronik tabloların HTML biçiminde dışa aktarılması için destek sağlar. Bu amaç için,**Aspose.Cells** kullanır**HtmlKaydetme Seçenekleri** geliştiricilerin çıktı HTML'sinin çeşitli yönlerini kontrol etmesine izin veren sınıf.

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Excel Dosyalarını HTML'ye Dönüştürme](/cells/tr/java/converting-workbook-to-different-formats/).

{{% /alert %}}
