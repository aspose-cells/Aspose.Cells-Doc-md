---
title: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydettiğinizde, hücre dizeleri için farklı cross türlerini belirtebilirsiniz. Varsayılan olarak Aspose.Cells, HTML'yi Microsoft Excel'e göre oluşturur, ancak çapraz türü [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) şeklinde değiştirildiğinde, hücre dizeleriyle örtüşen veya üst üste gelen hücre dizesinin sağ tarafındaki tüm dizesleri gizler.

## **HTML'ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716894.xlsx) yükler ve [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) öğesini [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) olarak ayarladıktan sonra onu [çıktı HTML'sine](64716893.zip) kaydeder. Ekran görüntüsü, nasıl etkilediğini varsayılan çıkış HTML'sinden açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
