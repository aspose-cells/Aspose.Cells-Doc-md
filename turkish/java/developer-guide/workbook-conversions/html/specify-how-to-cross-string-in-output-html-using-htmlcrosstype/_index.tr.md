---
title: HtmlCrossType kullanarak HTML çıktısında dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 140
url: /tr/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Olası Kullanım Senaryoları**

Hücre metin veya dize içeriyorsa ancak hücrenin genişliğinden daha büyükse, sonraki sütundaki bir sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı HTML'e kaydettiğinizde, çapraz türü belirterek bu taşmayı kontrol edebilirsiniz.[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)numaralandırma. Aşağıdaki değerlere sahiptir

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Bir sonraki hücreye bağlı olan MS Excel gibi görüntüleyin. Bir sonraki hücre boşsa, dize kesişir veya kesilir.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Dizeyi, HTML dışa aktaran MS Excel gibi görüntüleyin.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : HTML çapraz dizisini görüntüleyin, büyük HTML dosyaları oluşturma performansı, değeri olarak ayarlamaktan on kat daha hızlı olacaktır.[**VARSAYILAN**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) veya[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): HTML çapraz dizeyi görüntüleyin ve metinler çakıştığında sağ diziyi gizleyin.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL)Yalnızca hücrenin genişliği içindeki dize görüntüleniyor.

## **HtmlCrossType kullanarak HTML çıktısında dizenin nasıl çaprazlanacağını belirtin**

Aşağıdaki örnek kod,[örnek excel dosyası](51740747.xlsx)ve farklı belirterek HTML formatında kaydeder.[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Lütfen indirin[çıkış HTML](51740745.zip) Bu kodla oluşturulan dosyalar. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkle çevrelenmiş görüntüyü içerir.[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)HTML çıkışındaki değerler.

![yapılacaklar:resim_alternatif_metin](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
