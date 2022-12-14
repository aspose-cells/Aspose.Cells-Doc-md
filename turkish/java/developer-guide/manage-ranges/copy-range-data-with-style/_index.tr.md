---
title: Aralık Verilerini Tarzla Kopyala
type: docs
weight: 340
url: /tr/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[Yalnızca Aralık Verilerini Kopyala](/cells/tr/java/copy-range-data-only/) verilerin bir hücre aralığından başka bir aralığa nasıl kopyalanacağını açıkladı. Aspose.Cells, biçimlendirmeyle tamamlanmış bir aralığı da kopyalayabilir. Bu makale nasıl yapılacağını açıklıyor.

{{% /alert %}} 
## **Aralık Verilerini Tarzla Kopyala**
Aspose.Cells, aralıklarla çalışmak için bir dizi sınıf ve yöntem sağlar, örneğin,[aralık oluştur()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [Stil Bayrağı](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [ApplyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), vb.

Bu örnek:

1. Bir çalışma kitabı oluşturur.
1. İlk çalışma sayfasındaki birkaç hücreyi verilerle doldurur.
1. Bir aralık oluşturur.
1. Belirtilen biçimlendirme niteliklerine sahip bir stil nesnesi oluşturur.
1. Stili veri aralığına uygular.
1. İkinci bir hücre aralığı oluşturur.
1. Birinci aralıktaki biçimlendirmeli verileri ikinci aralığa kopyalar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

