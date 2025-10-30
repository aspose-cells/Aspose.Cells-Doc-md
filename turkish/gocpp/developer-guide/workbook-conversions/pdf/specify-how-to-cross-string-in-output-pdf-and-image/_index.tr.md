---
title: Çıktı PDF ve resimdeki metinleri nasıl geçeceğinizi Golang ile C++ kullanarak belirtin
linktitle: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin
type: docs
weight: 120
url: /tr/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aspose.Cells for C++ kullanarak PDF ve görüntü çıktılarında metin taşmasını nasıl kontrol edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir hücredeki metin veya dize, hücrenin genişliğinden büyükse, diğer hücre boşsa veya null ise, dize taşar. Excel dosyanızı PDF veya Görüntüye kaydederken, [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) enum'ını kullanarak çapraz tipi belirterek bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerleri vardır:

- **TextCrossType.Default**: MS Excel gibi metni gösterir, bu, bir sonraki hücreye bağlıdır. Bir sonraki hücre null ise, dize çaprazlar veya kesilir.

- **TextCrossType.CrossKeep**: MS Excel'den PDF/Görüntü aktarırken dizeyi gösterir.

- **TextCrossType.CrossOverride**: Diğer hücreleri çaprazlayarak tüm metni gösterir ve çaprazlanan hücrelerin metnini üzerine yazar.

- **TextCrossType.StrictInCell**: Sadece hücre genişliği içinde metni görüntüler.

## **PDF/Görüntüde dizeyi nasıl geçeceğinizi belirtin, TextCrossType kullanarak.**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) belirterek PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki linklerden indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Örnek Kod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}
