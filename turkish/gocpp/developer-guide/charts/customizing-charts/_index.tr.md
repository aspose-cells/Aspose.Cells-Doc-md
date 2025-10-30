---
title: Golang kullanarak C++ ile Grafikler Özelleştirme
linktitle: Grafikleri Özelleştirme
description: Aspose.Cells for C++ te grafiklerin nasıl özelleştirileceğini öğrenin. Rehberimiz, grafik düzenlerini nasıl değiştireceğinizi, veri serilerini ekleyip biçimlendireceğinizi, eksenleri ayarlayacağınızı ve grafiklerin görünümünü ve kullanılabilirliğini artırmak için farklı biçimlendirme seçeneklerini nasıl uygulayacağınızı gösterecek.
keywords: Aspose.Cells for C++, grafikler, özelleştirme, düzenler, veri serileri, eksenler, biçimlendirme, görünüm, kullanılabilirlik.
type: docs
weight: 40
url: /tr/go-cpp/customizing-charts/
---


## **Özel Grafikler Oluşturma**

Şimdiye kadar grafikler hakkında konuşurken, kendi biçim ayarlarına sahip standart grafikleri ele aldık. Sadece veri kaynağını tanımlarız, birkaç özellik ayarları yaparız ve grafik varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilerin kendi biçim ayarlarıyla grafikler oluşturmasına imkan tanıyan özel grafikler oluşturmayı da destekler.

Geliştiriciler, Aspose.Cells kullanarak çalışma zamanında özel grafikler oluşturabilirler.

Bir grafik bir veri serilerinden oluşur. Her veri serisi Aspose.Cells'te bir [**Series**](https://reference.aspose.com/cells/go-cpp/series/) nesnesi tarafından temsil edilir, [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) nesnesi ise [**Series**](https://reference.aspose.com/cells/go-cpp/series/) nesnelerinin bir koleksiyonu olarak görev yapar. Özel bir grafik oluştururken, geliştiriciler, farklı veri serileri için farklı tipte grafikler kullanma özgürlüğüne sahiptir ( [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) nesnesinde toplanan veri serileri).

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

 Şu anda, Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığın grafiklerini birleştiren özel grafiklere destek sağlar. Ancak, gelecekteki sürümlerde daha fazla grafik desteklenecektir.

{{% /alert %}}
