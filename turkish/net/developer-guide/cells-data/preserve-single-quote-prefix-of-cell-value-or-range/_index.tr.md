---
title: Cell Değerinin veya Aralığının Tek Alıntı Ön Ekini Koru
type: docs
weight: 310
url: /tr/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Olası Kullanım Senaryoları**

Kesme işareti veya tek tırnak işareti bulunan hücrenin içine bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda baştaki kesme işaretini veya tek tırnak işaretini görüntüler.

![yapılacaklar:resim_alternatif_metin](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells ayrıca Microsoft Excel gibi önde gelen kesme işaretini veya tek alıntıyı gizler, ancak[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) olarak**doğru** o hücre için Hücre için boş bir stil ayarlarsanız, o zaman[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) olur**YANLIŞ** Yeniden. Bu sorunu çözmek için Aspose.Cells,[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) özellik, ayarlandığında**YANLIŞ** , o zamanlar[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)hiç güncellenmez ve eski değeri korunur. Bunun anlamı, eğer eski değer[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)mülkiyet oldu**doğru** , kalacak**doğru** ve eğer eski değer**YANLIŞ** , kalacak**YANLIŞ**.

## **Cell Değerinin veya Aralığının Tek Alıntı Ön Ekini Koru**

 Aşağıdaki örnek kod, kullanımını açıklar[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)özelliği daha önce açıklandığı gibi. Lütfen kodun içindeki yorumları okuyun ve daha fazla yardım için aşağıda verilen kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
