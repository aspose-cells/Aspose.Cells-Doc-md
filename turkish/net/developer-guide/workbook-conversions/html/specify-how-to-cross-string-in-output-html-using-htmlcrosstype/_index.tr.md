---
title: HtmlCrossType kullanarak HTML çıktısında dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 140
url: /tr/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Olası Kullanım Senaryoları**

Hücre metin veya dize içeriyorsa ancak hücrenin genişliğinden daha büyükse, sonraki sütundaki sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı HTML'e kaydettiğinizde, çapraz türü belirterek bu taşmayı kontrol edebilirsiniz.[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) numaralandırma. Aşağıdaki değerlere sahiptir

- **HtmlCrossType.Default**: MS Excel gibi görüntüleme, bir sonraki hücreye bağlıdır. Bir sonraki hücre boşsa, dize kesişir veya kesilir.

- **HtmlCrossType.MSExport**: Dizeyi, HTML dışa aktaran MS Excel gibi görüntüleyin.

- **HtmlCrossType.Cross**: HTML çapraz dizisini görüntüleyin, büyük HTML dosyaları oluşturma performansı, değeri Varsayılan veya FitToCell olarak ayarlamaktan on kat daha hızlı olacaktır.

- **HtmlCrossType.FitToCell**: Yalnızca hücre genişliği içindeki dize görüntüleniyor.

## **HtmlCrossType kullanarak HTML çıktısında dizenin nasıl çaprazlanacağını belirtin**

 Aşağıdaki örnek kod,[örnek excel dosyası](51740732.xlsx) ve farklı belirterek HTML formatında kaydeder.[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) . Lütfen indirin[çıktı HTML'leri](51740734.zip) bu kod ile oluşturulmuştur. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkle çevrelenmiş görüntüyü içerir.[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) HTML çıkışındaki değerler.

![yapılacaklar:resim_alternatif_metin](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
