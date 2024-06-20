---
title: Stil ile Aralık Verileri Kopyalama
type: docs
weight: 340
url: /tr/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Yalnızca Aralık Verisini Kopyala](/cells/tr/java/copy-range-data-only/) bir hücre aralığından diğerine veri kopyalamanın nasıl yapıldığını açıklar. Aspose.Cells ayrıca biçimlendirme ile birlikte bir aralığı kopyalayabilir. Bu makalede nasıl yapıldığını açıklar.

{{% /alert %}} 
## **Yalnızca Aralık Verisiyle Kopyala**
Aspose.Cells, aralıklarla çalışmak için [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)) gibi çeşitli sınıflar ve yöntemler sağlar.

Bu örnek:

1. Bir çalışma kitabı oluşturur.
1. İlk çalışma sayfasındaki bir dizi hücreye veri doldurur.
1. Bir aralık oluşturur.
1. Belirli biçimlendirme özniteliklerine sahip bir stil nesnesi oluşturur.
1. Stil veri aralığına uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralıktan biçimlendirmeyle veri kopyalarını ikinci aralığa kopyalar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

