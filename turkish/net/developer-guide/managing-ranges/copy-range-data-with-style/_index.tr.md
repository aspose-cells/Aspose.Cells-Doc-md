---
title: Aralık Verilerini Tarzla Kopyala
type: docs
weight: 610
url: /tr/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Yalnızca Aralık Verilerini Kopyala](/cells/tr/net/copy-range-data-only/) verilerin bir hücre aralığından başka bir aralığa nasıl kopyalanacağını açıkladı. Spesifik olarak, kopyalanan hücrelere yeni bir stil seti uygulandı. Aspose.Cells, biçimlendirmeyle tamamlanmış bir aralığı da kopyalayabilir. Bu makale nasıl yapılacağını açıklıyor.

{{% /alert %}}

Aspose.Cells, aralıklarla çalışmak için bir dizi sınıf ve yöntem sağlar, örneğin,[**Aralık Oluştur()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) ve[**UygulaStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Bu örnek:

1. Bir çalışma kitabı oluşturur.
1. İlk çalışma sayfasındaki birkaç hücreyi verilerle doldurur.
1.  oluşturur[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  oluşturur[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) belirtilen biçimlendirme özniteliklerine sahip nesne.
1. Stili veri aralığına uygular.
1. İkinci bir hücre aralığı oluşturur.
1. Birinci aralıktaki biçimlendirmeli verileri ikinci aralığa kopyalar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
