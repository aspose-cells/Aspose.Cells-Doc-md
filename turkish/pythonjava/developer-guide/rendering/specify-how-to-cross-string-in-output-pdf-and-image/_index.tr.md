---
title: Çıktı PDF'sinde ve görüntüde dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 20
url: /tr/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Çıktı PDF'sinde ve görüntüde dizenin nasıl çaprazlanacağını belirtin**
 Bir hücre, hücrenin genişliğinden daha büyük metin veya dize içerdiğinde, sonraki sütundaki bir sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı PDF/Görüntü olarak kaydettiğinizde, çapraz türü belirterek bu taşmayı kontrol edebilirsiniz.[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) numaralandırma. Aşağıdaki değerlere sahiptir

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): MS Excel gibi görüntüleme, bir sonraki hücreye bağlıdır. Bir sonraki hücre boşsa, dize kesişir veya kesilir.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): PDF/Görüntü dışa aktaran MS Excel'e benzer dizeyi görüntüleyin
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE): Diğer hücreleri geçerek tüm metni görüntüleyin ve çapraz hücrelerin metnini geçersiz kılın
- [TextCrossType.STRICT_İÇİNDE_HÜCRE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL)Yalnızca hücrenin genişliği içindeki dize görüntüleniyor.

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı TextCrossType belirterek PDF/Görüntü biçiminde kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
