---
title: Kenarlık Stili Web Tarayıcıları tarafından desteklenmediğinde benzer Kenarlık Stilini dışa aktarın
type: docs
weight: 70
url: /tr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel, Web Tarayıcıları tarafından desteklenmeyen bazı kesikli kenarlık türlerini destekler. Böyle bir Excel dosyasını Aspose.Cells kullanarak HTML'ye dönüştürdüğünüzde, bu tür kenarlıklar kaldırılır. Ancak, Aspose.Cells, benzer sınırları görüntülemeyi de destekleyebilir.[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)Emlak. Lütfen değerini şu şekilde ayarlayın:**doğru**ve desteklenmeyen kenarlıklar da HTML dosyasına aktarılacaktır.

## **Kenarlık Stili Web Tarayıcıları tarafından desteklenmediğinde benzer Kenarlık Stilini dışa aktarın**

Aşağıdaki örnek kod,[örnek excel dosyası](64716832.xlsx)aşağıdaki ekran görüntüsünde gösterildiği gibi bazı desteklenmeyen kenarlıklar içerir. Ekran görüntüsü ayrıca etkisini göstermektedir[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)içindeki mülk[çıktı HTML'si](64716831.zip).

![yapılacaklar:resim_alternatif_Metin](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
