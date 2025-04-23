---
title: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin
type: docs
weight: 120
url: /tr/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Olası Kullanım Senaryoları**

Bir hücre metin veya dize içeriyorsa, ancak hücrenin genişliğinden daha büyükse, o zaman dize sonraki sütunda bulunan hücre boş veya boşsa taşar. Excel dosyanızı PDF/Görüntü olarak kaydettiğinizde, [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype) numaralama değerini kullanarak bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerlere sahiptir:

- **TextCrossType.Default**: MS Excel gibi metin görüntüler, bu sonraki hücreye bağlıdır. Eğer sonraki hücre boşsa, dize taşar veya kısaltılır.

- **TextCrossType.CrossKeep**: Dizeyi MS Excel olarak dışa aktarır.

- **TextCrossType.CrossOverride**: Tüm metni diğer hücreleri taşıyarak ve taşan hücrelerin metnini geçersiz kılarak görüntüler.

- **TextCrossType.StrictInCell**: Sadece hücre genişliği içinde metni görüntüler.

## **PDF/Görüntüde dizeyi nasıl geçeceğinizi belirtin, TextCrossType kullanarak.**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype) belirterek onu PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki linklerden indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Örnek Kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
