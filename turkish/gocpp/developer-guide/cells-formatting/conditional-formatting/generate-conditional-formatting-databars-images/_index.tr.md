---
title: Koşullu Biçimlendirme ile DataBars Görüntüleri Oluştur
linktitle: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
description: Aspose.Cells, veri çubuğu ve resimlerin koşullu biçimlendirmeyle oluşturulmasına imkan sağlayan C++ kütüphanesidir. Bu, hücrelerin değerine göre hücrenin görünümünü özelleştirmeye olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak koşullu biçimlendirme veri çubukları ve resimleri nasıl oluşturulacağını tanıtacaktır.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Veri Çubukları, Görüntüler, Elektronik Tablolar
type: docs
weight: 40
url: /tr/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Bazen Koşullu Biçimlendirme DataBar'ların görüntülerini oluşturmanız gerekebilir. Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) yöntemini kullanarak bu görüntüleri oluşturabilirsiniz. Bu makale, Aspose.Cells kullanarak DataBar görüntüsünün nasıl oluşturulacağını gösterir.

{{% /alert %}}

Aşağıdaki örnek kod, C1 hücresinin Veri Çubuğu görüntüsünü üretir. İlk olarak, hücrenin biçim koşulu nesnesine erişir ve ardından bu nesneden, [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) nesnesine erişerek ve onun [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) metodunu kullanarak hücrenin resmini oluşturur. Son olarak, resmi diske kaydeder.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
