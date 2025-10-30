---
title: Çıktı HTML sinde string nasıl çapraz geçirileceğini HtmlCrossType kullanarak belirtin, Golang ve C++ ile
linktitle: Çıktı HTML’sinde HtmlCrossType ayarlayın
type: docs
weight: 140
url: /tr/go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for C++ kullanarak HTML çıktısında metin taşmasını kontrol etmeyi öğrenin; HtmlCrossType ile.
---

## **Olası Kullanım Senaryoları**

 Bir hücre, hücre genişliğinden daha büyük metin veya dize içeriyorsa, dize taşar; eğer sonraki hücre boşsa veya yoksa. Excel dosyanızı HTML’ye kaydederken, [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) enumerasyonu kullanarak çapraz tipi belirterek bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerleri içerir:

- **HtmlCrossType.Default**: MS Excel gibi görüntüle, bir sonraki hücreye bağlıdır. Eğer bir sonraki hücre boşsa, dize taşır veya kırpılır.

- **HtmlCrossType.MSExport**: Diziyi MS Excel'in HTML olarak dışa aktarması gibi görüntüle.

- **HtmlCrossType.Cross**: HTML çapraz dizisini görüntüle, büyük HTML dosyaları oluşturma performansı, Değerin Varsayılana veya Hücreye Sığdırmak olarak ayarlanmasından on kat daha hızlı olacaktır.

- **HtmlCrossType.FitToCell**: Dizeyi yalnızca hücre genişliği içinde gösterir.

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](51740732.xlsx) yükler ve farklı [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) değerleri belirterek HTML formatında kaydeder. Lütfen bu kod ile üretilen [çıktı HTML'leri](51740734.zip) indirin. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkli çerçeve ile sınırlanmış bir resmi içerir ve bu ekran görüntüsü, [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) değerlerinin çıktı HTML'sine etkisini gösterir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}
