---
title: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 310
url: /tr/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for .NET API si ile Hücre Değeri veya Aralığının Tek Tırnak Öneki Saklanmış Olarak Korunmasını nasıl öğrenirsiniz.
keywords: Tek Tırnak Öneki ile Hücre Değeri veya Aralığının Saklanması, Önde Gelen tırnak işareti veya tek tırnak işareti gizle, İlk tek tırnak işareti veya tek tırnak işareti göster
---

## **Olası Kullanım Senaryoları**

Önde gelen tek tırnak ya da tek tırnak işaretli bir hücreye bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, önde gelen tek tırnak ya da tek tırnak işaretini aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda görüntüler.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells, Microsoft Excel gibi önde gelen tek tırnak işaretini gizler ancak [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)'yi o hücre için **true** olarak ayarlar. Eğer hücrenin boş bir stili ayarlarsanız, o zaman [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) tekrar **false** olur. Bu sorunla başa çıkmak için Aspose.Cells, [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) özelliğini sağlar; bu **false** olarak ayarlandığında, o zaman [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) hiç güncellenmez ve eski değeri korunur. Bu, [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) özelliğinin eski değeri **true** ise **true** olarak kalır ve eğer eski değeri **false** ise **false** olarak kalır demektir.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod önceden açıklanan [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) özelliğinin kullanımını açıklamaktadır. Yardım için kod içindeki yorumları okuyun ve verilen kodun konsol çıktısını görmek için aşağıdaki kodu inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
