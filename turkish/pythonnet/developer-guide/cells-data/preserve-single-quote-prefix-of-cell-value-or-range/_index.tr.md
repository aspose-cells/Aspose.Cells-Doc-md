---
title: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 310
url: /tr/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for Python via .NET API si ile bir hücre değerinin veya aralığının tek tek tırnak önekini nasıl koruyacağınızı öğrenin.
keywords: Python Excel Kütüphanesi, Python Hücre Değeri veya Aralığın Başına Tek Tırnak Eklemek, Python Baştaki aposotrof veya tek tırnak işareti gizle, Python Başlıkta aposotrof veya tek tırnak işareti göster
---

## **Olası Kullanım Senaryoları**

Önde gelen tek tırnak ya da tek tırnak işaretli bir hücreye bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, önde gelen tek tırnak ya da tek tırnak işaretini aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda görüntüler.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NET de önde gelen tek tırnak ya da tek tırnak işareti göstermez, ancak o hücre için **true** olarak ayarlar. Eğer hücrenin boş bir stili ayarlarsanız, o zaman **false** hale gelir. Bu sorunla başa çıkmak için, Aspose.Cells for Python via .NET **false** olarak ayarlandığında, [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) hiçbir şekilde güncellenmiyor ve eski değeri korunuyor. Bu, eğer [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) özelliğinin eski değeri **true** ise, o zaman **true** kalacak ve eğer eski değer **false** ise, o zaman **false** kalacaktır.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod önceden açıklanan [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) özelliğinin kullanımını açıklamaktadır. Yardım için kod içindeki yorumları okuyun ve verilen kodun konsol çıktısını görmek için aşağıdaki kodu inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
