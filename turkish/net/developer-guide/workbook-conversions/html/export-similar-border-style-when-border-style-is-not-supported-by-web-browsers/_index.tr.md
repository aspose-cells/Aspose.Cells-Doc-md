---
title: Kenarlık Stili Web Tarayıcıları tarafından desteklenmediğinde benzer Kenarlık Stilini dışa aktarın
type: docs
weight: 70
url: /tr/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel, Web Tarayıcıları tarafından desteklenmeyen bazı kesikli kenarlık türlerini destekler. Böyle bir Excel dosyasını Aspose.Cells kullanarak HTML'e dönüştürdüğünüzde, bu tür kenarlıklar kaldırılır. Ancak Aspose.Cells, bu tür sınırları görüntülemeyi de destekleyebilir.[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) Emlak. Lütfen değerini şu şekilde ayarlayın:**doğru**ve desteklenmeyen kenarlıklar da HTML dosyasına aktarılacaktır.

## **Kenarlık Stili Web Tarayıcıları tarafından desteklenmediğinde benzer Kenarlık Stilini dışa aktarın**

Aşağıdaki örnek kod,[örnek excel dosyası](64716806.xlsx) aşağıdaki ekran görüntüsünde gösterildiği gibi bazı desteklenmeyen kenarlıklar içerir. Ekran görüntüsü ayrıca etkisini göstermektedir[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)içindeki mülk[çıkış HTML](64716804.zip).

![yapılacaklar:resim_alternatif_metin](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
