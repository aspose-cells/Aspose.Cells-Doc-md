---
title: Sadece Aralık Verilerini Kopyala, Golang ile C++ kullanarak
linktitle: Yalnızca Aralık Verilerini Kopyala
type: docs
weight: 600
url: /tr/go-cpp/copy-range-data-only/
description: Aspose.Cells ve Golang kullanarak sadece biçimlendirmeyi olmadan alan verisini kopyalamayı öğrenin.
---

{{% alert color="primary" %}}

Bazen, verileri bir hücre aralığından başka bir hücre aralığına kopyalamak isteyebilirsiniz, sadece verileri ve biçimlendirmeyi kopyalayarak. Aspose.Cells bu özelliği sunar.

Bu makale, Aspose.Cells'i veri aralığını kopyalamak için kullanan bir örnek kod sunmaktadır.

{{% /alert %}}

Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Bir [**Range**](https://reference.aspose.com/cells/go-cpp/range/) oluşturma.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesi oluşturur.
1. Stil biçimlendirmesini aralığa uygular.
1. Başka bir hücre aralığı oluşturun.
1. İlk aralığın verilerini bu ikinci aralığa kopyalayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataOnly.go" >}}
