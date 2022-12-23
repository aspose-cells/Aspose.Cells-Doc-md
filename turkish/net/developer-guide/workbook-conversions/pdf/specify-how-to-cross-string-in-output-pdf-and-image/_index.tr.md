---
title: PDF çıktısında ve görüntüde dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 120
url: /tr/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Olası Kullanım Senaryoları**

Bir hücre metin veya dize içeriyorsa ancak hücrenin genişliğinden daha büyükse, sonraki sütundaki bir sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı PDF/Image içine kaydettiğinizde, çapraz türü belirterek bu taşmayı kontrol edebilirsiniz.[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)numaralandırma. Aşağıdaki değerlere sahiptir

- **TextCrossType.Default**: Bir sonraki hücreye bağlı olan metni MS Excel gibi görüntüleyin. Bir sonraki hücre boşsa, dize kesişir veya kesilir.

- **TextCrossType.CrossKeep**: Dizeyi, PDF/Resim dışa aktaran MS Excel gibi görüntüleyin

- **TextCrossType.CrossOverride**: Diğer hücreleri geçerek tüm metni görüntüleyin ve çapraz hücrelerin metnini geçersiz kılın

- **TextCrossType.StrictInCell**: Dizeyi yalnızca hücrenin genişliği içinde görüntüleyin.

## **TextCrossType kullanarak PDF/Image çıktısında dizenin nasıl çaprazlanacağını belirtin**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı belirterek PDF/Görüntü biçiminde kaydeder.[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Örnek Excel dosyası ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Basit kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
