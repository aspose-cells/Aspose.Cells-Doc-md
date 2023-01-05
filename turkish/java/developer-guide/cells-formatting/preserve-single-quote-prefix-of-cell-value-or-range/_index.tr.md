---
title: Cell Değerinin veya Aralığının Tek Alıntı Ön Ekini Koru
type: docs
weight: 1900
url: /tr/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Olası Kullanım Senaryoları**

Kesme işareti veya tek tırnak işareti bulunan hücrenin içine bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda baştaki kesme işaretini veya tek tırnak işaretini görüntüler.

![yapılacaklar:resim_alternatif_metin](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells ayrıca Microsoft Excel gibi önde gelen kesme işaretini veya tek alıntıyı gizler, ancak[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) olarak**doğru** o hücre için Hücre için boş bir stil ayarlarsanız, o zaman[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) olur**YANLIŞ** Yeniden. Bu sorunu çözmek için Aspose.Cells,[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) özellik, ayarlandığında**YANLIŞ**, o zamanlar[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)hiç güncellenmez ve eski değeri korunur. Bunun anlamı, eğer eski değer[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)mülkiyet oldu**doğru**, true olarak kalacaktır ve eski değer false ise false olarak kalacaktır.

## **Cell Değerinin veya Aralığının Tek Alıntı Ön Ekini Koru**

Aşağıdaki örnek kod, kullanımını açıklar[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)özelliği daha önce açıklandığı gibi. Lütfen kodun içindeki yorumları okuyun ve daha fazla yardım için aşağıda verilen kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
