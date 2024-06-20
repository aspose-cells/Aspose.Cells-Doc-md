---
title: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/net/managing-page-breaks/
description: Bu makale, C# API veya .NET Kitaplığı kullanarak Excel çalışma sayfalarına programlı olarak sayfa kırıkları eklemeyi, sayfa kırıklarını temizlemeyi veya belirli sayfa kırıklarını silmeyi nasıl yapacağınızı örnek kodlarla anlatmaktadır.
keywords: c# sayfa kırıkları, excel sayfa kırıkları, sayfa kırığını temizle c#, belirli sayfa kırığı sil c#
---

{{% alert color="primary" %}}

Tanıma göre, bir sayfa kesmesi, metin akışının bir sayfanın bittiği ve diğerinin başladığı yeridir. Microsoft Excel kullanıcılarına herhangi bir seçili hücreye sayfa kesmeleri eklemelerine izin verir.

Sayfa kırığı eklenen hücrenin konumunda, sayfa biter ve sayfa kırığından sonraki veri bir sonraki sayfaya basılırken. Basitçe söylemek gerekirse, sayfa kırıkları çalışma sayfanızı istediğiniz özelliklere göre birden çok sayfaya böler. Ayrıca, Aspose.Cells kullanarak çalışma sayfalarınızda çalışma zamanında sayfa kırıkları ekleyebilirsiniz. Aspose.Cells, geliştiricilere iki tür sayfa kırığı ekleme olanağı sağlar:

- Yatay sayfa kesmesi
- Dikey sayfa kesmesi

Tartışmanın geri kalanında, Aspose.Cells kullanarak çalışma sayfalarınıza yatay veya dikey sayfa kesme nasıl ekleyebileceğinizi açıklayacağız.

{{% /alert %}}

## **Sayfa Sonları**

Aspose.Cells, Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasını yönetmek için kullanılan geniş bir özellik ve yöntem yelpazesi sağlar.

Sayfa kırıklarını eklemek için, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) ve [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) özelliklerini kullanın.

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) ve [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) özellikleri, birkaç sayfa kırığı içerebilen koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa kırıklarını yönetmek için birçok yöntem içerir.

### **Sayfa Kesmeleri Eklemek**

Çalışma sayfasında bir sayfa kırığı eklemek için, [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) ve [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) yöntemlerini kullanarak belirtilen hücrede dikey ve yatay sayfa kırıkları ekleyin. Her **Ekle** yöntemi, kırığın ekleneceği hücrenin adını alır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

Sayfa kesmeleri önizleme veya yazdırma önizleme modlarında, bu sayfa kesmelerinin nasıl çalıştığını görebilirsiniz.

{{% /alert %}}

### **Tüm Sayfa Kesmelerini Temizleme**

Bir çalışma sayfasındaki tüm sayfa kırıklarını temizlemek için, [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) ve [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) koleksiyonlarının [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear) yöntemlerini çağırın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Belirli Sayfa Kesmesini Kaldırma**

Belirli bir sayfa kırığını kaldırmak için, [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat)  ve [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) yöntemlerini kullanın. Her **RemoveAt** yöntemi, kaldırılacak sayfa kırığının indisini alır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Bilinmesi Gerekenler**

**Sayfa Yerleşimi Ayarları** (yani [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) ve [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) ayarlandığında, sayfa kırığı ayarları etkilenir, bu nedenle çalışma sayfasını yazdırırsanız, sayfa kırığı ayarları dikkate alınmasa da hala ayarlıdır.
