---
title: Stil ile Aralık Verileri Kopyalama
type: docs
weight: 610
url: /tr/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Yalnızca Aralık Verilerini Kopyala](/cells/tr/net/copy-range-data-only/) hücre aralığının verilerini başka bir aralığa kopyalamanın ve kopyalanan hücrelere yeni bir dizi stillerin uygulanmasının nasıl olduğunu açıkladı. Aspose.Cells ayrıca biçimlendirme ile birlikte bir aralığı kopyalayabilir. Bu makalede bunun nasıl olduğu açıklanmaktadır.

{{% /alert %}}

Aspose.Cells, aralıklarla çalışmak için bir dizi sınıf ve yöntem sağlar, örneğin, [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) ve [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Bu örnek:

1. Bir çalışma kitabı oluşturur.
1. İlk çalışma sayfasındaki bir dizi hücreye veri doldurur.
1. Bir [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) oluşturur.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi oluşturur.
1. Stil veri aralığına uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralıktan biçimlendirmeyle veri kopyalarını ikinci aralığa kopyalar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
