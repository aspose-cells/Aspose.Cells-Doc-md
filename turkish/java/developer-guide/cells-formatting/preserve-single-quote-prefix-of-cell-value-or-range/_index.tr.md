---
title: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 1900
url: /tr/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Olası Kullanım Senaryoları**

Önde gelen tek tırnak ya da tek tırnak işaretli bir hücreye bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, önde gelen tek tırnak ya da tek tırnak işaretini aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda görüntüler.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells, Microsoft Excel gibi öncülük eden apostrof veya tek tırnak işaretini gizler; ancak [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) orada **true** olarak ayarlar. Eğer hücrenin boş bir stilini ayarlarsanız, o zaman [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) yine **false** olur. Bu sorunla başa çıkmak için Aspose.Cells, [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) özelliğini sağlar, **false** olarak ayarlandığında, o zaman [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) hiç güncellenmez ve eski değeri korunur. Demek oluyor ki, [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) özelliğinin eski değeri **true** ise, o öyle kalacaktır ve eğer eski değer **false** ise, o öyle kalacaktır.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod, daha önce açıklandığı gibi [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) özellik kullanımını açıklar. Kod içindeki yorumları okuyun ve daha fazla yardım için verilen kodun konsol çıktısına bakın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
