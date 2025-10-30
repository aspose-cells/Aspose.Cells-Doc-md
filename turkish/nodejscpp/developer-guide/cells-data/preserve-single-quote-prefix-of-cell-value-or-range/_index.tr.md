---
title: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 310
url: /tr/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for Node.js via C++ API kullanarak Hücre Değeri veya Aralık Başlangıç Tırnak Ön Ekini nasıl koruyacağınızı öğrenin.
keywords: Hücre Değeri veya Aralık Node.js de Tek Tırnak Öncüsünü Koru veya Gizle veya Göster Node.js de C++ aracılığıyla
---

## **Olası Kullanım Senaryoları**

Önde gelen tek tırnak ya da tek tırnak işaretli bir hücreye bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, önde gelen tek tırnak ya da tek tırnak işaretini aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda görüntüler.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ ayrıca Microsoft Excel gibi öncü apostrof veya tek tırnak işaretini gizler, ancak [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) hücre için **doğru** olarak ayarlanır. Eğer hücreye boş bir stil ayarlarsanız, o zaman [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) tekrar **yanlış** olur. Bu sorunu çözmek için, Aspose.Cells for Node.js via C++ [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) metodunu sağlar, bu **yanlış** olarak ayarlandığında, [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) hiç güncellenmez ve eski değeri korunur. Bu, [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--)'ün eski değeri **doğru** ise, **doğru** kalacaktır ve eski değeri **yanlış** ise, **yanlış** kalacaktır anlamına gelir.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod, daha önce açıklanan [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) metodunun kullanımını açıklamaktadır. Lütfen kod içindeki yorumları okuyun ve aşağıdaki kodun konsol çıkışını daha fazla yardım için görün.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
