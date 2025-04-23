---
title: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin
type: docs
weight: 110
url: /tr/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Olası Kullanım Senaryoları**

Bir hücre metin veya dize içeriyorsa ancak hücrenin genişliğinden daha büyükse, dize, bir sonraki sütunda bulunan hücre null veya boşsa taşar. Excel dosyanızı PDF/Görsel olarak kaydettiğinizde, bu taşmayı [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) sıralamasını kullanarak kontrol edebilirsiniz. Aşağıdaki değerlere sahiptir

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): MS Excel gibi görüntüleyin, bir sonraki hücreye bağlıdır. Bir sonraki hücre null ise, dize taşacaktır veya kısaltılacaktır.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Dizeyi MS Excel ile benzer şekilde görüntüleyin PDF/Görsel dışa aktarma

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Diğer hücreleri geçerek tüm metni görüntüleyin ve geçilen hücrelerin metnini geçersiz kılın

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Sadece hücre genişliği içinde dizeyi görüntüleme.

## **PDF/Görüntüde dizeyi nasıl geçeceğinizi belirtin, TextCrossType kullanarak.**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) belirterek onu PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki linklerden indirilebilir:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
