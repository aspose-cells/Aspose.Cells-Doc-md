---
title: Çıkış HTML sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin
type: docs
weight: 140
url: /tr/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Olası Kullanım Senaryoları**

Hücre metni veya dizesi var ancak hücrenin genişliğinden daha büyük ise, dize, bir sonraki sütunda bulunan hücre boş veya boşsa taşar. Excel dosyanızı HTML olarak kaydettiğinizde, taşmayı belirterek bu taşmayı kontrol edebilirsiniz. Bunun için [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) numaralı numaralandırma kullanılır. Aşağıdaki değerlere sahiptir

- **HtmlCrossType.Default**: MS Excel gibi görüntüle, bir sonraki hücreye bağlıdır. Eğer bir sonraki hücre boşsa, dize taşır veya kırpılır.

- **HtmlCrossType.MSExport**: Diziyi MS Excel'in HTML olarak dışa aktarması gibi görüntüle.

- **HtmlCrossType.Cross**: HTML çapraz dizisini görüntüle, büyük HTML dosyaları oluşturma performansı, Değerin Varsayılana veya Hücreye Sığdırmak olarak ayarlanmasından on kat daha hızlı olacaktır.

- **HtmlCrossType.FitToCell**: Sadece dizeyi hücre genişliği içinde görüntüle.

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

Aşağıdaki örnek kod, [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) özelliğini belirterek [örnek Excel dosyasını](51740732.xlsx) yükler ve HTML formatında kaydeder. Bu kodla oluşturulan [çıktı HTML'leri](51740734.zip) indirin. Örnek Excel dosyası, çıktı HTML üzerindeki [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) değerlerinin etkisini gösteren bu ekran görüntüsünde gösterildiği gibi kırmızı renkle çerçevelenmiş bir resim içermektedir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
