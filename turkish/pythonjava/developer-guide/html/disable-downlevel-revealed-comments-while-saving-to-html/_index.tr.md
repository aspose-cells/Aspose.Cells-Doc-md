---
title: HTML ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak
type: docs
weight: 20
url: /tr/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak**
Excel dosyası HTML'e dönüştürüldüğünde, Aspose.Cells çıktı HTML dosyasına Aşağı Düzeyde Açığa Çıkarılmış Koşullu Yorumlar ekler. Bu koşullu yorumlar genellikle eski Internet Explorer sürümleri ile ilgilidir ve modern tarayıcılarda gereksizdir. Aşağı Düzeyde Açığa Çıkarılmış Koşullu Yorumlar hakkında ek bilgi için lütfen aşağıdaki bağlantıyı ziyaret edin

[Koşullu yorum - Aşağı Düzeyde Açığa Çıkarılmış Koşullu Yorum](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aşağı Düzeyde Açığa Çıkarılmış Koşullu Yorumları kaldırmak için, Aspose.Cells [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) özelliğini sağlar. [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) özelliğini **True** olarak ayarlamak, çıktı HTML dosyasındaki Aşağı Düzeyde Açığa Çıkarılmış Koşullu Yorumları kaldıracaktır.

Aşağıda, çıktı HTML dosyasındaki kaldırılacak Aşağı Düzeyde Açığa Çıkarılmış Koşullu Yorumları gösteren resim

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
