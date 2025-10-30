---
title: Golang kullanarak C++ ile Excel den HTML ye Dönüşümde Belge Çalışma Kitabı ve Çalışma Sayfası Özelliklerini dışa aktar
linktitle: Excel den HTML ye Dönüştürme sırasında Belge Çalışma Kitabı ve Çalışma Sayfası Özelliklerini İhraç Et
type: docs
weight: 50
url: /tr/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye dönüştürürken Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmayı veya aktarmamayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir Microsoft Excel dosyası, Microsoft Excel veya Aspose.Cells kullanılarak HTML'ye aktarıldığında, aşağıdaki ekran görüntüsünde gösterildiği gibi çeşitli Belge, Çalışma Kitabı ve Çalışma Sayfası özellikleri de dışa aktarılır. Bu özellikleri dışa aktarmamayı sağlayabilirsiniz; [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) ve [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) değerlerini **false** olarak ayarlayarak. Bu özelliklerin varsayılan değeri **true**'dur. Aşağıdaki ekran görüntüsü, bu özelliklerin dışa aktarılan HTML'de nasıl göründüğünü gösterir.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excel'de HTML'ye Belge, Çalışma Kitabı ve Çalışma Sayfası Özellikleri Dışa Aktarma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](61767776.xlsx) yükler ve Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmadan HTML'ye dönüştürür [çıktı HTML'si](61767779.zip).

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
