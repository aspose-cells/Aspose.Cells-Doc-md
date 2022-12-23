---
title: Grafikleri Özelleştirme
type: docs
weight: 40
url: /tr/net/customizing-charts/
---
{{% alert color="primary" %}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar grafikleri tartıştığımızda, standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlar, birkaç özellik ayarlar ve grafik, varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilerin kendi biçim ayarlarıyla grafikler oluşturmasına olanak tanıyan özel grafikler oluşturmayı da destekler.

Geliştiriciler, Aspose.Cells'i kullanarak çalışma zamanında özel grafikler oluşturabilir.

 Grafik, bir veri serisinden oluşur. Aspose.Cells'deki her veri serisi, bir[**Dizi**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesne oysa[**Seri Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesne koleksiyonu olarak hizmet eder[**Dizi**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)nesneler. Geliştiriciler, özel bir grafik oluştururken, farklı veri serileri için farklı türde grafikler kullanma özgürlüğüne sahiptir.[**Seri Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)nesne).

Aşağıdaki örnek kod, özel grafiklerin nasıl oluşturulacağını gösterir. Bu örnekte, birinci veri serisi için bir sütun grafiği ve ikinci seri için bir çizgi grafiği kullanacağız. Sonuç olarak, çalışma sayfasına bir çizgi grafiğiyle birlikte bir sütun grafiği ekliyoruz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Şu anda Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığını grafiklerini birleştiren özel grafikleri destekler, ancak gelecek sürümlerde daha fazla grafik desteklenecektir.

{{% /alert %}}
