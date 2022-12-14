---
title: Çıktı PDF'sinde ve görüntüde dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 110
url: /tr/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Olası Kullanım Senaryoları**

Bir hücre metin veya dize içeriyorsa ancak hücrenin genişliğinden daha büyükse, sonraki sütundaki sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı PDF/Görüntü olarak kaydettiğinizde, çapraz türü belirterek bu taşmayı kontrol edebilirsiniz.[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)numaralandırma. Aşağıdaki değerlere sahiptir

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): MS Excel gibi görüntüleme, bir sonraki hücreye bağlıdır. Bir sonraki hücre boşsa, dize kesişir veya kesilir.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Dizeyi MS Excel dışa aktaran PDF/Resim gibi görüntüleyin

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Diğer hücreleri geçerek tüm metni görüntüleyin ve çapraz hücrelerin metnini geçersiz kılın

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Yalnızca hücre genişliği içindeki dize görüntüleniyor.

## **TextCrossType kullanarak çıktı PDF/Görüntüsünde dizenin nasıl çaprazlanacağını belirtin**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı belirterek PDF/Görüntü biçiminde kaydeder.[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)Örnek Excel dosyası ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
