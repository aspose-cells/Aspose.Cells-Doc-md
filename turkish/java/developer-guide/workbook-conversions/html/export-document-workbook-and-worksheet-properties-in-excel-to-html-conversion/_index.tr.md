---
title: Excel den HTML e belge çalışma kitabı ve çalışma sayfası özelliklerini dışa aktar
type: docs
weight: 50
url: /tr/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel dosyası, Microsoft Excel veya Aspose.Cells kullanılarak HTML'e dışa aktarıldığında, aşağıdaki ekran görüntüsünde gösterilen Belge, Çalışma Kitabı ve Çalışsayfa özelliklerinin çeşitli türleri de dışa aktarılır. Bu özelliklerin dışa aktarılmasını, **false** olarak ayarlayarak [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) ve [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) ayarlayarak önleyebilirsiniz. Bu özelliklerin varsayılan değeri **true**'dur. Aşağıdaki ekran görüntüsü, bu özelliklerin dışa aktarılmış HTML'de nasıl göründüğünü göstermektedir.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Belge, Çalışma Kitabı ve Çalışma Sayfası Özelliklerini Excel'den HTML'e Dışa Aktar**

Aşağıdaki örnek kod, [örnek Excel dosyasını](61767784.xlsx) yükler ve HTML'e dönüştürür ve dışa aktarılan HTML'de Belge, Çalışma Kitabı ve Çalışsayfa özelliklerini dışa aktarmaz. ([çıktı HTML](61767783.zip)).

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
{{< app/cells/assistant language="java" >}}
