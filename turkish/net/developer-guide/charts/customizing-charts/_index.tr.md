---
title: Grafikleri Özelleştirme
description: Aspose.Cells for .NET numaralı telefondan grafikleri nasıl özelleştireceğinizi öğrenin. Kılavuzumuz, grafiklerinizin görünümünü ve kullanılabilirliğini geliştirmek için grafik düzenlerini nasıl değiştireceğinizi, veri serilerini nasıl ekleyip biçimlendireceğinizi, eksenleri nasıl ayarlayacağınızı ve çeşitli biçimlendirme seçeneklerini nasıl uygulayacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /tr/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **Özel Grafikler Oluşturma**

Şu ana kadar grafikleri tartışırken, standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlıyoruz, birkaç özelliği ayarlıyoruz ve grafik varsayılan format ayarlarıyla oluşturuluyor. Ancak Aspose.Cells API'leri aynı zamanda geliştiricilerin kendi format ayarlarıyla grafikler oluşturmasına olanak tanıyan özel grafikler oluşturmayı da destekler.

Geliştiriciler çalışma zamanında Aspose.Cells'i kullanarak özel grafikler oluşturabilir.

 Bir grafik bir veri serisinden oluşur. Aspose.Cells'deki her veri serisi bir ile temsil edilir[**Seri**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesne oysa[**SeriKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesne bir koleksiyon görevi görür[**Seri**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)nesneler. Özel bir grafik oluştururken, geliştiriciler farklı veri serileri için farklı türde grafikler kullanma özgürlüğüne sahiptir (bkz.[**SeriKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)nesne).

Aşağıdaki örnek kod, özel grafiklerin nasıl oluşturulacağını gösterir. Bu örnekte ilk veri serisi için sütun grafiği, ikinci seri için ise çizgi grafiği kullanacağız. Sonuç olarak, çalışma sayfasına çizgi grafikle birleştirilmiş bir sütun grafiği ekliyoruz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Şu anda Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığını grafiklerini birleştiren özel grafikleri desteklemektedir ancak gelecek sürümlerde daha fazla grafik desteklenecektir.

{{% /alert %}}
