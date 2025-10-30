---
title: Tarayıcılar tarafından desteklenmeyen Kenar Çizgisi Stili ile benzer Kenar Çizgisi Stilini C++ ve Golang kullanarak dışa aktar
linktitle: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar
type: docs
weight: 70
url: /tr/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Web tarayıcıları tarafından desteklenmeyen kenar stillerini Aspose.Cells kullanarak Golang ile nasıl dışa aktaracağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, web tarayıcıları tarafından desteklenmeyen bazı çizgili sınır türlerini destekler. Böyle bir Excel dosyasını Aspose.Cells kullanarak HTML'ye dönüştürürken, bu sınırlar kaldırılır. Ancak, Aspose.Cells `[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)` özelliği ile bu sınırların da gösterilmesini destekleyebilir. Lütfen değeri **true** olarak ayarlayın ve desteklenmeyen sınırlar da HTML dosyasına dışa aktarılacaktır.

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**

Aşağıdaki örnek kod, desteklenmeyen bazı sınırları içeren [örnek Excel dosyasını](64716806.xlsx) yükler ve aşağıdaki ekran görüntüsünde gösterildiği gibi, `[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)` özelliğinin etkisini gösterir. Ayrıca ekran görüntüsü, [çıkış HTML'sinde](64716804.zip) `[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)` özelliğinin etkisini detaylandırır.

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
