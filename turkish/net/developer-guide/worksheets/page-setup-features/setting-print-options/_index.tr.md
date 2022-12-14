---
title: Yazdırma Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/net/setting-print-options/
---
{{% alert color="primary" %}}

Microsoft Excel'in sayfa ayarı ayarları, kullanıcıların çalışma sayfası sayfalarının nasıl yazdırılacağını denetlemesine olanak tanıyan çeşitli yazdırma seçenekleri (sayfa seçenekleri olarak da anılır) sağlar.

{{% /alert %}}

## **Yazdırma Seçeneklerini Ayarlama**

Bu yazdırma seçenekleri, kullanıcıların şunları yapmasına olanak tanır:

- Çalışma sayfasında belirli bir yazdırma alanı seçin.
- Başlıkları yazdırın.
- Kılavuz çizgilerini yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Yazdırma hücresi hataları.
- Sayfa sıralamasını tanımlayın.

 Aspose.Cells, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler, Excel tarafından sunulan özellikleri kullanarak bu seçenekleri çalışma sayfaları için kolayca yapılandırabilir.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)sınıf. Bu özelliklerin nasıl kullanıldığı aşağıda daha ayrıntılı olarak tartışılmaktadır.

### **Yazdırma Alanını Ayarla**

Varsayılan olarak, yazdırma alanı, çalışma sayfasının veri içeren tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir yazdırma alanını oluşturabilir.

 Belirli bir yazdırma alanı seçmek için[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**Alanı yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)Emlak. Bu özelliğe yazdırma alanını tanımlayan bir hücre aralığı atayın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Baskı Başlıklarını Ayarla**

 Aspose.Cells, yazdırılan bir çalışma sayfasının tüm sayfalarında yinelenecek satır ve sütun başlıkları belirlemenizi sağlar. Bunu yapmak için[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**Başlık Sütunlarını Yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) ve[**YazdırBaşlıkSatırları**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)özellikleri.

Tekrarlanacak satır veya sütunlar, satır veya sütun numaraları geçirilerek tanımlanır. Örneğin, satırlar $1:$2 olarak tanımlanır ve sütunlar $A:$B olarak tanımlanır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Diğer Yazdırma Seçeneklerini Ayarlayın**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class ayrıca genel yazdırma seçeneklerini aşağıdaki gibi ayarlamak için birkaç başka özellik daha sağlar:

- [**Kılavuz Çizgilerini Yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)kılavuz çizgilerinin yazdırılıp yazdırılmayacağını tanımlayan bir Boolean özelliği.
- [**Baskı Başlıkları**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): Satır ve sütun başlıklarının yazdırılıp yazdırılmayacağını tanımlayan bir Boolean özelliği.
- [**Siyah ve beyaz**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): çalışma sayfasının siyah beyaz modda yazdırılıp yazdırılmayacağını tanımlayan bir Boolean özelliği.
- [**Yorumları Yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): yazdırma yorumlarının çalışma sayfasında mı yoksa çalışma sayfasının sonunda mı görüntüleneceğini tanımlar.
- [**Taslağı Yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): sayfanın grafiksiz yazdırılıp yazdırılmayacağını tanımlayan bir boolean özelliği..
- [**Yazdırma Hataları**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): hücre hatalarının görüntülenen, boş, kısa çizgi veya N/A olarak yazdırılıp yazdırılmayacağını tanımlar.

 ayarlamak için[**Yorumları Yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) ve[**Yazdırma Hataları**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) özellikler, Aspose.Cells ayrıca iki numaralandırma sağlar,[**YazdırYorum Türü**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , ve[**Yazdırma HatalarıTürü**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) atanacak önceden tanımlanmış değerleri içeren[**Yorumları Yazdır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) ve[**Yazdırma Hataları**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)sırasıyla özellikler.

 Önceden tanımlanmış değerler,[**YazdırYorum Türü**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)numaralandırma açıklamalarıyla birlikte aşağıda listelenmiştir.

|**Yorum Türlerini Yazdır**|**Tanım**|
|:- |:- |
|Yerinde Yazdır|Yorumların çalışma sayfasında görüntülendiği şekilde yazdırılacağını belirtir.|
|YazdırYorum Yok|Yorumların yazdırılmayacağını belirtir.|
|PrintSheetEnd|Çalışma sayfasının sonunda yorumların yazdırılacağını belirtir.|

 Önceden tanımlanmış değerler[**Yazdırma HatalarıTürü**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)numaralandırma açıklamalarıyla birlikte aşağıda listelenmiştir.



|**Yazdırma Hatası Türleri**|**Tanım**|
|:- |:- |
|Yazdırma HatalarıBoş|Hataların yazdırılmayacağını belirtir.|
|PrintErrorsTire|Hataların "--" olarak yazdırılacağını belirtir.|
|Görüntülenen Yazdırma Hataları|Hataların görüntülendiği şekilde yazdırılacağını belirtir.|
|Yazdırma HatalarıNA|Hataların "#N/A" olarak yazdırılacağını belirtir.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Sayfa Sırasını Ayarla**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)sınıf sağlar[**Emir**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)çalışma sayfanızın birden çok sayfasının yazdırılmasını sıralamak için kullanılan özellik. Sayfaları aşağıdaki gibi sıralamak için iki olasılık vardır.

- **Aşağı ve yukarı:** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya doğru yazdırır.
- **Sonra aşağı:** aşağıdaki sayfaları yazdırmadan önce sayfaları soldan sağa yazdırır.

 Aspose.Cells bir numaralandırma sağlar,[**BaskıSiparişTürü**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)önceden tanımlanmış tüm sipariş türlerini içerir.

 Önceden tanımlanmış değerler[**BaskıSiparişTürü**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)numaralandırma aşağıda listelenmiştir.

|**Yazdırma Sırası Türleri**|**Tanım**|
|:- |:- |
|AşağıSonraÜzeri|Baskı sırasını aşağı ve yukarı olarak temsil eder.|
|YukarıSonraAşağı|Baskı sırasını aşağı ve yukarı olarak temsil eder.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
