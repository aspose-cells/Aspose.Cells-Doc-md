---
title: Golang kullanarak C++ ile HTML ye kaydederken CrossHideRight ile Üzerine Çıkarılan İçeriği Gizleme
linktitle: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: C++ ile Aspose.Cells kullanarak HTML ye kaydederken üstü örtülü içeriği gizlemek için CrossHideRight kullanın.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, hücre dizeleri için farklı çapraz tipe belirleyebilirsiniz. Varsayılan olarak, Aspose.Cells Microsoft Excel'e uygun HTML üretir, ancak çapraz tipi [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype) olarak değiştirirseniz, hücreyle örtüşen veya üst üste binen hücre dizelerinin sağ tarafındaki tüm dizeleri gizler.

## **HTML'ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716894.xlsx) yükler ve [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/)'ı [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) olarak ayarladıktan sonra [çıktı HTML'sine](64716893.zip) kaydeder. Ekran görüntüsü, [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)'nin varsayılan çıkıştan çıktı HTML'sini nasıl etkilediğini açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
