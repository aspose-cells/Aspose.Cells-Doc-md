---
title: Çıkış HTML sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin
type: docs
weight: 140
url: /tr/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Olası Kullanım Senaryoları**

Hücre metni veya dizesi var ancak hücrenin genişliğinden daha büyük ise, dize, bir sonraki sütunda bulunan hücre boş veya boşsa taşar. Excel dosyanızı HTML olarak kaydettiğinizde, taşmayı belirterek bu taşmayı kontrol edebilirsiniz. Bunun için [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) numaralı numaralandırma kullanılır. Aşağıdaki değerlere sahiptir

- **HtmlCrossType.DEFAULT**: MS Excel gibi gösterir, sonraki hücreye bağlıdır. Eğer sonraki hücre boşsa, metin çaprazlar veya kesilir.

- **HtmlCrossType.MS_EXPORT**: MS Excel'in HTML'ye dışa aktarımını gösterir.

- **HtmlCrossType.CROSS**: HTML çapraz dizesini gösterir, büyük HTML dosyalarının oluşturulma performansı **Default** veya **FitToCell** değerine kıyasla onda birden fazla olur.

- **HtmlCrossType.CROSS_HIDE_RIGHT**: HTML çapraz dizesini gösterir ve metinlerin üst üste binmesi durumunda sağdaki metni gizler.

- **HtmlCrossType.FIT_TO_CELL**: Sadece hücre genişliği içinde dizgenin görüntülenmesi.

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

Aşağıdaki örnek kod, [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) özelliğini belirterek [örnek Excel dosyasını](51740732.xlsx) yükler ve HTML formatında kaydeder. Bu kodla oluşturulan [çıktı HTML'leri](51740734.zip) indirin. Örnek Excel dosyası, çıktı HTML üzerindeki [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) değerlerinin etkisini gösteren bu ekran görüntüsünde gösterildiği gibi kırmızı renkle çerçevelenmiş bir resim içermektedir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
