---
title: HtmlCrossType kullanarak çıktı HTML'sinde dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 140
url: /tr/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Olası Kullanım Senaryoları**

Hücre metin veya dize içeriyorsa ancak hücrenin genişliğinden daha büyükse, sonraki sütundaki bir sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı HTML'ye kaydettiğinizde, çapraz türü belirterek bu taşmayı kontrol edebilirsiniz.[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)numaralandırma. Aşağıdaki değerlere sahiptir

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Bir sonraki hücreye bağlı olan MS Excel gibi görüntüleyin. Bir sonraki hücre boşsa, dize kesişir veya kesilir.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Dizeyi MS Excel dışa aktarma HTML'si gibi görüntüleyin.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : HTML çapraz dizesini görüntüle, büyük HTML dosyaları oluşturma performansı, değeri olarak ayarlamaktan on kat daha hızlı olacaktır.[**VARSAYILAN**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) veya[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): HTML çapraz dizesini görüntüleyin ve metinler çakıştığında doğru dizeyi gizleyin.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): Yalnızca hücrenin genişliği içindeki dize görüntüleniyor.

## **HtmlCrossType kullanarak çıktı HTML'sinde dizenin nasıl çaprazlanacağını belirtin**

Aşağıdaki örnek kod,[örnek excel dosyası](51740747.xlsx)ve farklı belirterek HTML biçiminde kaydeder.[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Lütfen indirin[çıktı HTML'si](51740745.zip) Bu kodla oluşturulan dosyalar. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkle çevrelenmiş görüntüyü içerir.[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)çıkış HTML'sindeki değerler.

![yapılacaklar:resim_alternatif_Metin](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
