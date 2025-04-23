---
title: Grafikleri Özelleştirme
description: Aspose.Cells for .NET de grafikleri nasıl özelleştireceğinizi öğrenin. Rehberimiz, grafik düzenlerini değiştirme, veri serilerini ekleyip biçimlendirme, ekseni ayarlama ve grafiklerinizin görünümünü ve kullanılabilirliğini artırmak için çeşitli biçimlendirme seçeneklerini uygulama konusunda size rehberlik edecektir.
keywords: Aspose.Cells for .NET, grafik oluşturma, özelleştirme, düzenler, veri serileri, eksenler, biçimlendirme, görünüm, kullanılabilirlik.
type: docs
weight: 40
url: /tr/net/customizing-charts/
---

{{% alert color="primary" %}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar, grafikleri konuşurken, standart format ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlarız, birkaç özellik belirleriz ve grafik, varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri aynı zamanda kendi format ayarlarıyla grafik oluşturmayı destekler.

Geliştiriciler, Aspose.Cells kullanarak çalışma zamanında özel grafikler oluşturabilirler.

Bir grafik bir veri serilerinden oluşur. Her veri serisi Aspose.Cells'te bir [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesnesi tarafından temsil edilir, [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesnesi ise [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesnelerinin bir koleksiyonu olarak görev yapar. Özel bir grafik oluştururken, geliştiriciler, farklı veri serileri için farklı tipte grafikler kullanma özgürlüğüne sahiptir ( [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesnesinde toplanan veri serileri).

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Şu anda Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığılmış grafikleri birleştiren özel grafikleri desteklemektedir, ancak gelecekte daha fazla grafik desteklenecektir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
