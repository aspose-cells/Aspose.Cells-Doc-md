---
title: HTML'e kaydederken Alt Seviye Açığa Çıkan Yorumları devre dışı bırakın
type: docs
weight: 20
url: /tr/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **HTML'e kaydederken Alt Seviye Açığa Çıkan Yorumları devre dışı bırakın**
Excel dosyası HTML'e dönüştürüldüğünde, Aspose.Cells, çıktı HTML dosyasına Alt Düzeyde ortaya çıkan koşullu yorumlar ekler. Bu koşullu yorumlar çoğunlukla Internet Explorer'ın eski sürümleriyle ilgilidir ve modern tarayıcılarda ilgisizdir. Alt seviye tarafından açıklanan koşullu yorumlar hakkında ek bilgi için lütfen aşağıdaki bağlantıyı ziyaret edin

[Koşullu yorum - Alt seviye tarafından açıklanan koşullu yorum](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells, Alt Seviye tarafından açıklanan koşullu yorumları kaldırmak için şunları sağlar:[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)Emlak. ayarlamak[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) mülkiyet**Doğru**çıktı HTML dosyasındaki Alt düzey tarafından açıklanan koşullu yorumları kaldıracaktır.

Aşağıdaki görüntü, HTML çıktı dosyasında kaldırılacak olan Alt Düzeyde ortaya çıkan koşullu yorumları göstermektedir.

![yapılacaklar:resim_alternatif_metin](Disable-Downlevel-Revealed-Comments.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
