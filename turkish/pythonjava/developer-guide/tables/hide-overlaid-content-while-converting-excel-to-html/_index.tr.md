---
title: Excel i HTML ye dönüştürürken üst üste binmiş içeriği gizleyin
type: docs
weight: 40
url: /tr/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Excel'i HTML'ye dönüştürürken üst üste binmiş içeriği gizleyin**
Excel dosyanızı HTML'ye kaydederken, hücre dizeleri için farklı çapraz tipler belirtebilirsiniz. Varsayılan olarak Aspose.Cells, Microsoft Excel'e uygun olarak HTML oluşturur, ancak [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)’ı [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) olarak değiştirdiğinizde; hücre dizesiyle çakışan veya üzerine binen hücre dizesinin sağ tarafındaki tüm dizesini gizler.

Aşağıdaki örnek kod, [örnek Excel dosyasını](sampleHidingOverlaidContentWithCrossHideRight.xlsx) yükler ve [çıkış HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)’e [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)'ı [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) olarak ayarladıktan sonra kaydeder. Ekran görüntüsü [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)'ın varsayılan çıkıştan çıkış HTML'ini nasıl etkilediğini açıklar.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
