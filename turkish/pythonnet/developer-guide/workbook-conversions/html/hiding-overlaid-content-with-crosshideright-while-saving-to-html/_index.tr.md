---
title: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, hücre dizesi için farklı çapraz türleri belirtebilirsiniz. Varsayılan olarak, Aspose.Cells for Python via .NET, Microsoft Excel'e uygun HTML üretir. Ancak, çapraz türünü [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) olarak değiştirirseniz, hücre metniyle örtüşen veya üst üste binmiş hücre metnlerini gizler.

## **HTML'ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716894.xlsx) yükler ve [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) öğesini [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) olarak ayarladıktan sonra onu [çıktı HTML'sine](64716893.zip) kaydeder. Ekran görüntüsü, nasıl etkilediğini varsayılan çıkış HTML'sinden açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
