---
title: Yalnızca Aralık Verilerini Kopyala
type: docs
weight: 330
url: /tr/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

Bazen, bir hücre aralığından diğerine veri kopyalamak isteyebilirsiniz ve sadece veriyi, biçimlendirmeyi değil. Aspose.Cells, bu özelliği [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)) yöntemi ile sunar.

{{% /alert %}} 
## **Yalnızca Aralık Verisini Kopyala**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Bir aralık oluştur.
1. Belirtilen biçimlendirme özniteliklerine sahip bir stil nesnesi oluşturun.
1. Stil biçimlendirmesini aralığa uygular.
1. Başka bir hücre aralığı oluşturun.
1. İlk aralığın verisini [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)) yöntemini kullanarak ikinci aralığa kopyalayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
