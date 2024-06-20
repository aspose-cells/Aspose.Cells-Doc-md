---
title: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, hücre dizeleri için farklı çapraz türleri belirtebilirsiniz. Varsayılan olarak, Aspose.Cells HTML'yi Microsoft Excel'e göre oluşturur, ancak [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) karakterini [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) olarak değiştirdiğinizde, hücre dizesiyle birlikte bindirilmiş veya üst üste binmiş olan hücre dizesinin sağındaki tüm dizeleri gizler.

## **Web Tarayıcıları tarafından desteklenmeyen Birleşik Stil'in benzerini dışa aktar**

Aşağıdaki örnek kod, [sample Excel file](64716916.xlsx) yüklendikten sonra [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) olarak [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) ayarlandıktan sonra onu [output HTML](64716915.zip) olarak kaydeder. Ekran görüntüsü, [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) 'nin varsayılan çıktıdan çıktı HTML'yi nasıl etkilediğini açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
