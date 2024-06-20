---
title: Çıkış HTML sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin
type: docs
weight: 140
url: /tr/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Olası Kullanım Senaryoları**

Hücre metni veya dizesi mevcut olmasına rağmen hücrenin genişliğinden büyükse, dize sonraki sütunun boş veya null olması durumunda taşar. Excel dosyanızı HTML olarak kaydederken, taşmayı [0] numaralı numaralandırma ile belirterek kontrol edebilirsiniz. Şu değerlere sahiptir

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): MS Excel'e benzer şekilde görüntülenir, bu değer sonraki hücreye bağlıdır. Eğer sonraki hücre boşsa, dize taşar veya kısaltılır.

- {0}: Dizeyi, HTML olarak görüntüleyin, büyük HTML dosyaları oluşturmak için {1} veya {2} değerlerine ayarlamaktan on kat daha hızlıdır.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): HTML olarak dizeyi geçiş yapın ve metinlerin örtüştüğü durumlarda sağdaki metni gizleyin.

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Hücre genişliği içindeki dizeyi yalnızca görüntüleyin.

Çıktı HTML'sinde dizeyi enine nasıl geçeceğinizi HtmlCrossType kullanarak belirtin

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

Aşağıdaki örnek kod, yüklenecek olan [örnek Excel dosyasını](51740747.xlsx) yüklüyor ve bu kod ile oluşturulan [çıktı HTML](51740745.zip) dosyalarını indirmenizi sağlar. Örnek Excel dosyası, şu ekran görüntüsünde gösterildiği gibi kırmızı renkle çerçevelenmiş bir resim içermektedir ve bu resmin çıktı HTML üzerinde [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) değerlerinin etkisini göstermektedir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
