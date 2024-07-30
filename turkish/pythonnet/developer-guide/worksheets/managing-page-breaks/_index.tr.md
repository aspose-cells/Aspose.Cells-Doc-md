---
title: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/python-net/managing-page-breaks/
description: Bu makale, Aspose.Cells for Python via .NET API lerini kullanarak Excel çalışma sayfalarında sayfa sonları eklemeyi, sayfa sonlarını temizlemeyi veya belirli sayfa sonlarını programatik olarak nasıl sileceğinizi sağlar.
keywords: Python Excel Kütüphanesi, Python sayfa sonları, Python da excel sayfa sonları, Python da sayfa sonunu silme.
---

{{% alert color="primary" %}}

Tanıma göre, bir sayfa kesmesi, metin akışının bir sayfanın bittiği ve diğerinin başladığı yeridir. Microsoft Excel kullanıcılarına herhangi bir seçili hücreye sayfa kesmeleri eklemelerine izin verir.

Sayfa sonunun eklenen hücrenin konumu, sayfanın bittiği ve sayfa sonrası verilerin bir sonraki sayfada yazdırıldığı yerdir. Basitçe söylemek gerekirse, sayfa sonları çalışma sayfanızı belirtilen özelliklerinize göre birden fazla sayfaya böler. Aspose.Cells for Python via .NET kullanarak çalışma sayfalarınıza çalışma zamanında sayfa sonları da ekleyebilirsiniz. Aspose.Cells for Python via .NET, iki tür sayfa sonu eklemeyi sağlar:

- Yatay sayfa kesmesi
- Dikey sayfa kesmesi

Gerçekleşen tartışmanın geri kalanında, Aspose.Cells for Python via .NET kullanarak çalışma sayfalarınıza yatay veya dikey sayfa sonları nasıl ekleyebileceğinizi açıklayacağız.

{{% /alert %}}

## **Sayfa Sonları**

Aspose.Cells for Python via .NET, bir Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfasını yönetmek için kullanılan geniş bir özellik ve yöntem yelpazesi sağlar.

Sayfa kırıklarını eklemek için, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) ve [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) özelliklerini kullanın.

[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) ve [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) özellikleri, birkaç sayfa kırığı içerebilen koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa kırıklarını yönetmek için birçok yöntem içerir.

## **Sayfa Sonları Nasıl Eklenir**

Bir çalışma sayfasına sayfa sonu eklemek için, belirtilen hücreye dikey ve yatay sayfa sonları eklemek için [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) ve [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str) yöntemlerini çağırarak bunu yapabilirsiniz. Her **ekle** yöntemi, sonun nerede eklenmesi gerektiğinin hücre adını alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

Sayfa kesmeleri önizleme veya yazdırma önizleme modlarında, bu sayfa kesmelerinin nasıl çalıştığını görebilirsiniz.

{{% /alert %}}


## **Bilinmesi Gerekenler**

**Sayfa Yerleşimi Ayarları** (yani [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) ve [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) ayarlandığında, sayfa kırığı ayarları etkilenir, bu nedenle çalışma sayfasını yazdırırsanız, sayfa kırığı ayarları dikkate alınmasa da hala ayarlıdır.
