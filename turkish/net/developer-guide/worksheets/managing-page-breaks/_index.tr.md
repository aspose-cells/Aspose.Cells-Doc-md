---
title: Sayfa Sonlarını Yönetme
type: docs
weight: 30
url: /tr/net/managing-page-breaks/
description: Bu makalede örnek kod sağlanır ve C# API veya .NET Kitaplığı kullanılarak Excel çalışma sayfalarında programlı olarak sayfa sonlarının nasıl ekleneceği, sayfa sonlarının nasıl temizleneceği veya belirli sayfa sonlarının nasıl silineceği açıklanır.
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
---
{{% alert color="primary" %}}

Tanıma göre sayfa sonu, bir metin akışında bir sayfanın bittiği ve bir sonrakinin başladığı bir yerdir. Microsoft Excel, kullanıcıların bir çalışma sayfasının seçilen herhangi bir hücresine sayfa sonları eklemesine izin verir.

Yazdırma sırasında sayfa sonunun eklendiği, sayfanın sonlandırıldığı ve sayfa sonundan sonra kalan verilerin sonraki sayfada yazdırıldığı hücrenin konumu. Basit bir ifadeyle, sayfa sonları, çalışma sayfanızı belirtimlerinize göre birden çok sayfaya böler. Aspose.Cells'i kullanarak çalışma zamanında çalışma sayfalarınıza da sayfa sonları ekleyebilirsiniz. Aspose.Cells, geliştiricilerin iki tür sayfa sonu eklemesine olanak tanır:

- Yatay sayfa sonu
- Dikey sayfa sonu

Tartışmanın geri kalanında, Aspose.Cells'i kullanarak çalışma sayfalarınıza nasıl yatay veya dikey sayfa sonları ekleyebileceğinizi açıklayacağız.

{{% /alert %}}

##  **Sayfa Sonları**

Aspose.Cells bir sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bir Excel dosyasını temsil eden sınıf. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class, bir çalışma sayfasını yönetmek için kullanılan çok çeşitli özellikler ve yöntemler sağlar.

Sayfa sonlarını eklemek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Yatay Sayfa Sonları**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) Ve[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)özellikler.

 bu[**Yatay Sayfa Sonları**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) Ve[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)özellikler, birkaç sayfa sonu içerebilen koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa sonlarını yönetmek için çeşitli yöntemler içerir.

###  **Sayfa Sonları Ekleme**

 Bir çalışma sayfasına sayfa sonu eklemek için belirtilen hücreye dikey ve yatay sayfa sonları ekleyin.[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) Ve[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) yöntemler. Her biri**Eklemek** method break eklenmesi gereken hücrenin adını alır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

Sayfa sonu önizleme veya baskı önizleme modlarında, bu sayfa sonlarının nasıl çalıştığını görebilirsiniz.

{{% /alert %}}

###  **Tüm Sayfa Sonlarını Temizleme**

 Bir çalışma sayfasındaki tüm sayfa sonlarını temizlemek için[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) Ve[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) koleksiyonlar'[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)yöntemler.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

###  **Belirli Sayfa Sonunu Kaldırma**

 Belirli bir sayfa sonunu kaldırmak için[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) Ve[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) yöntemler. Her biri**KaldırAt**method kaldırılmak üzere olan sayfa sonunun indeksini alır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

##  **bilmek önemli**

 ayarladığınızda**Sayfalara Sığdır** özellikler (yani[**Sayfalara SığdırUzun**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) Ve[**Sayfalara SığdırGeniş**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) sayfa yapısı ayarlarında, sayfa sonu ayarları etkilenir, bu nedenle, çalışma sayfasını yazdırırsanız, sayfa sonu ayarları, yine de ayarlanmış olmasına rağmen dikkate alınmaz.
