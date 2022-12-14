---
title: Belge Çalışma Kitabını ve Çalışma Sayfası Özelliklerini Excel'de HTML dönüştürmesine dışa aktarma
type: docs
weight: 50
url: /tr/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel dosyası, Microsoft Excel veya Aspose.Cells kullanılarak HTML'ye dışa aktarıldığında, aşağıdaki ekran görüntüsünde gösterildiği gibi çeşitli Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini de dışa aktarır. ayarlayarak bu özellikleri dışa aktarmaktan kaçınabilirsiniz.[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)ve[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)olarak**yanlış**. Bu özelliklerin varsayılan değeri**doğru**. Aşağıdaki ekran görüntüsü, bu özelliklerin dışa aktarılan HTML'de nasıl göründüğünü gösterir.

![yapılacaklar:resim_alternatif_Metin](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excel'deki Belge, Çalışma Kitabı ve Çalışma Sayfası Özelliklerini HTML'ye dönüştürme**

Aşağıdaki örnek kod,[örnek excel dosyası](61767784.xlsx)HTML'ye dönüştürür ve Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmaz.[çıktı HTML'si](61767783.zip).

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
