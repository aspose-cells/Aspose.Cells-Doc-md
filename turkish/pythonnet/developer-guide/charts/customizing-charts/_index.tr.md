---
title: Grafikleri Özelleştirme
description: Aspose.Cells for Python via .NET de grafiklerin nasıl özelleştirileceğini öğrenin. Kılavuzumuz, grafik düzenlerini değiştirme, veri serisi ekleme ve biçimlendirme, eksenleri ayarlama ve grafiklerin görünüm ve kullanılabilirliğini artırmak için çeşitli biçimlendirme seçenekleri uygulama konusunda size gösterir.
keywords: Aspose.Cells for Python via .NET, grafikler, özelleştirme, düzenler, veri serileri, eksenler, biçimlendirme, görünüm, kullanılabilirlik.
type: docs
weight: 40
url: /tr/python-net/customizing-charts/
---

{{% alert color="primary" %}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar, grafikler hakkında konuştuğumuzda, standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Sadece veri kaynağını tanımlarız, birkaç özellik ayarları yaparız ve grafik varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells for Python via .NET API'leri, geliştiricilerin kendi biçimlendirme ayarlarıyla grafikler oluşturmasına olanak tanıyan özelleştirilmiş grafikler oluşturmaya da destek sağlar.

Geliştiriciler, Aspose.Cells for Python via .NET kullanarak çalışma zamanında özel grafikler oluşturabilir.

Bir grafik, bir veri serisinden oluşur. Aspose.Cells for Python via .NET'deki her veri serisi, bir [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) nesnesi ile temsil edilirken, [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) nesnesi [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) nesnelerinin koleksiyonu olarak hizmet eder. Özel grafik oluştururken, geliştiriciler farklı veri serileri için farklı grafik türleri kullanma özgürlüğüne sahiptir (bu, [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) nesnesindeki koleksiyonda toplanmıştır).

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

Şu anda Aspose.Cells for Python via .NET sadece pie, çizgi, kolon ve kolon yığın grafikleri kombinasyonunu destekleyen özel grafikler desteklenmektedir; ancak daha fazla grafik türü gelecekteki sürümlerde desteklenecektir.

{{% /alert %}}
