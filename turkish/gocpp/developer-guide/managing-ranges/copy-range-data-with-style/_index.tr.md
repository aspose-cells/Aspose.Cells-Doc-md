---
title: Stil ile Aralık Verisini Kopyala (C++)
linktitle: Stil ile Aralık Verileri Kopyalama
type: docs
weight: 610
url: /tr/go-cpp/copy-range-data-with-style/
description: Excel dosyalarında hücre stilleri de dahil olmak üzere aralık verisini kopyalayın, Aspose.Cells for C++ ile.
---

{{% alert color="primary" %}}

[Sadece Kopyala Aralığı Verisi](/cells/tr/cpp/copy-range-data-only/) nasıl hücre verilerini aralıklar arasında kopyalayacağınızı açıkladı. Bu makale, Aspose.Cells for C++ kullanarak biçimlendirme stillerini koruyarak hücre aralıklarını nasıl kopyalayacağınızı gösterir.

{{% /alert %}}

Aspose.Cells, [**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) ve [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) dahil olmak üzere aralıklarla çalışma için sınıf ve metodlar sağlar.

Bu örnek şu işlemleri gösterir:

1. Bir çalışma kitabı oluştur
1. Hücreleri veri ile doldurun
1. Bir [**Range**](https://reference.aspose.com/cells/go-cpp/range/) oluşturun
1. Bir [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesi oluşturun ve yapılandırın
1. Aralığa stiller uygulayın
1. İkinci bir aralık oluşturun
1. Biçimlendirilmiş verileri aralıklar arasında kopyalayın

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}
