---
title: Hücre Değeri veya Aralığın Tek Tırnak Öneki Koruma ile Golang ile C++
linktitle: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 310
url: /tr/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for C++ API kullanarak Hücre veya Aralıkta Tek Tırnak Ön Ekini Nasıl Koruyacağınızı öğrenin.
keywords: Tek Tırnak Öneki ile Hücre Değeri veya Aralığının Saklanması, Önde Gelen tırnak işareti veya tek tırnak işareti gizle, İlk tek tırnak işareti veya tek tırnak işareti göster
---

## **Olası Kullanım Senaryoları**

Bir hücreye öngörülen apostrof veya tek tırnak işareti ile bazı değerler koyduğunuzda, Microsoft Excel bunları gizler, ancak hücreyi seçtiğinizde, formül çubuğunda önde gelen apostrof veya tek tırnak gösterilir. Aşağıdaki ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells, Microsoft Excel gibi önde gelen apostrof veya tek tırnak işaretini gizler, ancak bu hücre için [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) değerini **doğru** yapar. Eğer hücrenin boş bir stili ayarlanırsa, o zaman [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) tekrar **yanlış** olur. Bu sorunla başa çıkmak için Aspose.Cells, [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) özelliği sağlar, bu ayar **yanlış** yapıldığında, [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) hiç güncellenmez ve eski değeri korunur. Bu, eğer [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) özelliğinin eski değeri **doğru** ise, **doğru** kalacaktır ve eğer eski değer **yanlış** ise, o da **yanlış** kalacaktır.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod, yukarıda açıklanan [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) özelliğinin kullanımını açıklar. Lütfen kod içindeki yorumları okuyun ve aşağıda verilen kodun konsol çıktılarını inceleyerek daha fazla yardım alın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
