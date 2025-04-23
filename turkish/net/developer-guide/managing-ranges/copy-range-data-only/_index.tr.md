---
title: Yalnızca Aralık Verilerini Kopyala
type: docs
weight: 600
url: /tr/net/copy-range-data-only/
---

{{% alert color="primary" %}}

Bazen, verileri bir hücre aralığından başka bir hücre aralığına kopyalamak isteyebilirsiniz, sadece verileri ve biçimlendirmeyi kopyalayarak. Aspose.Cells bu özelliği sunar.

Bu makale, Aspose.Cells'i veri aralığını kopyalamak için kullanan bir örnek kod sunmaktadır.

{{% /alert %}}

Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Bir [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) oluşturma.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi oluşturur.
1. Stil biçimlendirmesini aralığa uygular.
1. Başka bir hücre aralığı oluşturun.
1. İlk aralığın verilerini bu ikinci aralığa kopyalayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
