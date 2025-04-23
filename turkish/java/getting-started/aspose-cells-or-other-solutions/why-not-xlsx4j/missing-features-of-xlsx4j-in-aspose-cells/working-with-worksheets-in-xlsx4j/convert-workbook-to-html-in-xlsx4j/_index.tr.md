---
title: xlsx4j de Çalışma Kitabını HTML e Dönüştürme
type: docs
weight: 10
url: /tr/java/convert-workbook-to-html-in-xlsx4j/
---

## **Aspose.Cells - Çalışma Kitabını HTML'e Dönüştürme**
Aspose.Cells API'leri elektronik tabloları HTML formatına dışa aktarma desteği sağlar. Bu amaçla **Aspose.Cells**, geliştiricilere çıktı HTML'nin birkaç yönünü kontrol etmelerine olanak tanıyan **HtmlSaveOptions** sınıfını kullanır.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Excel Dosyalarını HTML'e Dönüştürme](/cells/tr/java/converting-workbook-to-different-formats/) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
