---
title: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin
type: docs
weight: 120
url: /tr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aspose.Cells için Python via .NET API ile çıktı PDF ve görüntüde dize geçişini nasıl yapılacağını öğrenin.
keywords: Python da Çıktı PDF ve Görüntüde Dize Geçişi
---

## **Olası Kullanım Senaryoları**

Bir hücre metin veya dize içeriyorsa, ancak hücrenin genişliğinden daha büyükse, o zaman dize sonraki sütunda bulunan hücre boş veya boşsa taşar. Excel dosyanızı PDF/Görüntü olarak kaydettiğinizde, [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/) numaralama değerini kullanarak bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerlere sahiptir:

- **TextCrossType.DEFAULT**: Bir sonraki hücreye bağlı olarak MS Excel gibi metni gösterir. Eğer bir sonraki hücre boşsa, dize taşar veya kırpılır.

- **TextCrossType.CROSS_KEEP**: Diziyi MS Excel'e benzer şekilde PDF/Görüntüye aktarır.

- **TextCrossType.CROSS_OVERRIDE**: Tüm metni gösterirken diğer hücreleri taşar ve taşan hücrelerin metnini geçersiz kılar.

- **TextCrossType.STRICT_IN_CELL**: Sadece hücre genişliği içindeki dizeyi gösterir.

## **PDF/Görüntüde dizeyi nasıl geçeceğinizi belirtin, TextCrossType kullanarak.**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/) belirterek onu PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki linklerden indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Örnek Kod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
