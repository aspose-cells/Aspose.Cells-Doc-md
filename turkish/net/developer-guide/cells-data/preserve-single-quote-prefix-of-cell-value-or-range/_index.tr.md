---
title: Cell Değeri veya Aralığının Tek Alıntı Önekini Koru
type: docs
weight: 310
url: /tr/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Cell Değeri veya Aralığının Tek Alıntı Önekini Aspose.Cells for .NET API aracılığıyla nasıl koruyacağınızı öğrenin.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **Olası Kullanım Senaryoları**

Başında kesme işareti veya tek tırnak işareti olan hücrenin içine bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, aşağıdaki ekran görüntüsünde gösterildiği gibi baştaki kesme işaretini veya tek tırnak işaretini bir formül çubuğunda görüntüler.

![yapılacak şey:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells aynı zamanda Microsoft Excel gibi baştaki kesme işaretini veya tek tırnak işaretini de gizler ancak[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) gibi**doğru** o hücre için. Hücrenin boş bir stilini ayarlarsanız, o zaman[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) olur**YANLIŞ** Tekrar. Bu sorunla başa çıkmak için Aspose.Cells şunları sağlar:[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) özellik, ayarlandığında**false**, bu durumda [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) hiç güncellenmez ve eski değeri korunur . Bunun anlamı, [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) özelliğinin eski değeri **true** ise, bu **doğru kalacak** ve eski değer *yanlış** ise *yanlış** olarak kalacaktır.

##  **Cell Değeri veya Aralığının Tek Alıntı Önekini Koru**

Aşağıdaki örnek kod, kullanımını açıklamaktadır.[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)Daha önce açıklandığı gibi mülk. Lütfen kodun içindeki yorumları okuyun ve daha fazla yardım için aşağıda verilen kodun konsol çıktısına bakın.

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **Konsol Çıkışı**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
