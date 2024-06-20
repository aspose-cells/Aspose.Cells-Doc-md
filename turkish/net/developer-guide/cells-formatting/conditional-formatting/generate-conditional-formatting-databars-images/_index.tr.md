---
title: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
description: Aspose.Cells elektronik tablo dosyalarıyla çalışmak için bir .NET kütüphanesidir. Hücrelerin değerlerine göre elektronik tablonun görüntüsünü özelleştirmenize izin veren şartlı biçimlendirilmiş veri çubukları ve görüntülerin oluşturulmasını destekler. Bu makale, Aspose.Cells kütüphanesini kullanarak şartlı biçimlendirilmiş veri çubukları ve görüntüler oluşturmayı anlatacaktır.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Veri Çubukları, Görüntüler, Elektronik Tablolar
type: docs
weight: 40
url: /tr/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Bazen Koşullu Biçimlendirme DataBar'ların görüntülerini oluşturmanız gerekebilir. Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) yöntemini kullanarak bu görüntüleri oluşturabilirsiniz. Bu makale, Aspose.Cells kullanarak DataBar görüntüsünün nasıl oluşturulacağını gösterir.

{{% /alert %}}

Aşağıdaki örnek kod, C1 hücresinin VeriÇubuk görüntüsünü oluşturur. İlk olarak, hücrenin biçimlendirme koşulu nesnesine erişir, ardından bu nesneden [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) nesnesine erişir ve bu nesnenin [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) yöntemini kullanarak hücrenin görüntüsünü oluşturur. Son olarak, görüntüyü diske kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
