---
title: Kenar Boşluklarını Ayarlama
type: docs
weight: 20
url: /tr/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiricilerin, yazdırma sürecini kontrol etmek için çalışma sayfaları için sayfa kurulum ayarlarını yapılandırması gerekebilir. Bu konuda, sayfa kenar boşluklarını yapılandırmak için Aspose.Cells'in nasıl kullanılacağı anlatılmaktadır.

{{% /alert %}}

## **Kenar Boşluklarını Ayarlama**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

 bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf sağlar[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) bir çalışma sayfası için sayfa düzeni seçeneklerini ayarlamak için kullanılan özellik. bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) öznitelik bir nesnedir[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) geliştiricilerin yazdırılan bir çalışma sayfası için farklı sayfa düzeni seçenekleri belirlemesine olanak tanıyan sınıf. bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)class, sayfa düzeni seçeneklerini ayarlamak için kullanılan çeşitli özellikler ve yöntemler sağlar.

### **Sayfa Kenar Boşlukları**

 kullanarak sayfa kenar boşluklarını (sol, sağ, üst, alt) ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)sınıf üyeleri. Sayfa kenar boşluklarını belirtmek için kullanılan yöntemlerden birkaçı aşağıda listelenmiştir:

- [**sol kenar boşluğu**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**sağ kenar boşluğu**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Üst boşluk**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Alt Marj**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Sayfada Ortala**

Bir sayfada bir şeyi yatay ve dikey olarak ortalamak mümkündür. Bunun için bazı yararlı üyeler var.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) sınıf,[**MerkezYatay**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) ve[**MerkezDikey**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Üstbilgi ve Altbilgi Kenar Boşlukları**

 ile üstbilgi ve altbilgi kenar boşluklarını ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) gibi sınıf üyeleri[**Başlık Marjı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) ve[**Altbilgi Kenar Boşluğu**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
