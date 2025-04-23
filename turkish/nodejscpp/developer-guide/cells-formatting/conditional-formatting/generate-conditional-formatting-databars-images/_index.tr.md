---
title: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
linktitle: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma yapan Node.js kütüphanesidir. Koşullu biçimlendirilmiş veri çubukları ve resimlerin oluşturulmasını destekleyerek, kullanıcıların hücre değerlerine göre elektronik tablonun gösterimini özelleştirmesine olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak koşullu biçimlendirilmiş veri çubukları ve resimler oluşturmayı tanıtacaktır.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Veri Çubukları, Resimler, Elektronik Tablolar, Node.js C++ ile
type: docs
weight: 40
url: /tr/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Bazen Koşullu Biçimlendirme DataBar'ların görüntülerini oluşturmanız gerekebilir. Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) yöntemini kullanarak bu görüntüleri oluşturabilirsiniz. Bu makale, Aspose.Cells kullanarak DataBar görüntüsünün nasıl oluşturulacağını gösterir.

{{% /alert %}}

Aşağıdaki örnek kod, C1 hücresinin Veri Çubuğu görüntüsünü üretir. İlk olarak, hücrenin biçim koşulu nesnesine erişir ve ardından bu nesneden, [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) nesnesine erişerek ve onun [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) metodunu kullanarak hücrenin resmini oluşturur. Son olarak, resmi diske kaydeder.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

