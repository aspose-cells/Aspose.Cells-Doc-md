---
title: Golanga via C++ ile Sadece Aralık Stili Kopyala
linktitle: Sadece Aralık Stilini Kopyala
type: docs
weight: 620
url: /tr/go-cpp/copy-range-style-only/
description: Aspose.Cells ve Golang kullanarak Excel de yalnızca aralık stilini nasıl kopyalayacağınızı öğrenin.
---

{{% alert color="primary" %}}

[Yalnızca Aralık Verisini Kopyala](/cells/tr/cpp/copy-range-data-only/) ve [Stil ile Aralık Verisini Kopyala](/cells/tr/cpp/copy-range-data-with-style/) başlıklı makaleler, bir aralıktan veri kopyalama işlemini, kendi başına veya biçimlendirme ile birlikte gösterir. Ayrıca sadece biçimlendirmeyi de kopyalamak mümkündür. İşte detaylar.

{{% /alert %}} 

Bu örnek bir çalışma kitabı oluşturur, veri ile doldurur ve yalnızca bir aralığın stilini kopyalar.

1. Bir aralık oluştur.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesi oluşturur.
1. Stil biçimlendirmesini aralığa uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralığın biçimlendirmesini ikinci aralığa kopyalar.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeStyleOnly.go" >}}
