---
title: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar
type: docs
weight: 70
url: /tr/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, Web Tarayıcıları tarafından desteklenmeyen bazı türde kesikli kenarlar destekler. Aspose.Cells kullanarak bu tür bir Excel dosyasını HTML'e dönüştürdüğünüzde, bu tür kenarlar kaldırılır. Bununla birlikte, Aspose.Cells, bu tür kenarları [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) özelliğini kullanarak göstermeyi de destekler. Lütfen değerini **true** olarak ayarlayın ve desteklenmeyen kenarlar da HTML dosyasına dışa aktarılacaktır.

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**

Aşağıdaki örneğin kodu, aşağıdaki ekran görüntüsünde gösterildiği gibi desteklenmeyen bazı kenarlıkları içeren [örnek Excel dosyasını](64716806.xlsx) yükler. Ekran görüntüsü, [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) özelliğinin [çıkış HTML'sinin](64716804.zip) içindeki etkisini daha ayrıntılı olarak açıklar.

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
