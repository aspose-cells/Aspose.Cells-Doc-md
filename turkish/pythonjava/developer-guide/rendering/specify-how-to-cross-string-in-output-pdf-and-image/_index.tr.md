---
title: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin
type: docs
weight: 20
url: /tr/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Çıktı PDF ve görüntülerde metin geçişini belirle**
Bir hücre metni veya dizesi, hücre genişliğinden daha büyükse ve bir sonraki sütundaki hücre boş veya null ise, dize taşar. Excel dosyanızı PDF/Görüntü olarak kaydettiğinizde, [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) numaralandırmasını kullanarak bu taşmayı kontrol edebilirsiniz.

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): MS Excel gibi görüntüler, bir sonraki hücreye bağlıdır. Eğer bir sonraki hücre boşsa, dize taşar veya kısaltılır.
- [TextCrossType.CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): PDF/Görüntü şeklinde taşma benzeri dizeyi görüntüler.
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE): Tüm metni diğer hücrelerin üzerinden keserek ve taşarak metnin üzerine yazarak görüntüler.
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): Sadece hücre genişliği içerisindeki dizeyi görüntüler.

Aşağıdaki örneğin kodu, örnek Excel dosyasını yükler ve farklı TextCrossType belirterek PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
