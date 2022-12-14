---
title: Aspose.Cells kullanarak Çalışma Kitabını HTML'ye dönüştürün
type: docs
weight: 20
url: /tr/java/convert-workbook-to-html-using-aspose-cells/
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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Excel Dosyalarını HTML'ye Dönüştürme](/cells/tr/java/converting-workbook-to-different-formats/).

{{% /alert %}}
