---
title: Verileri Filtreleme
type: docs
weight: 100
url: /tr/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** kullanıcılar için Otomatik Filtreleme ve Özel Veri Filtreleme özellikleri sağlar. Bu özellikleri kullanarak, çalışma sayfasından yalnızca bir listede görüntülemek istediğiniz öğeleri seçmenin bir yolunu bulabilirsiniz. Ayrıca, bir listedeki öğeleri belirlenen kriterlere göre filtrelemenize izin verilir. Otomatik Filtreleme / Özel Veri Filtreleme özelliği ile metin, sayı veya tarihleri filtreleyebilirsiniz.

 Kullanabilirsiniz**Otomatik Filtreyi Etkinleştir** Boole özniteliği**RowFilterSettings** GridDesktop denetimi için Otomatik Filtre özelliğini etkinleştirmek için sınıf. Sınıfın kullanabileceğiniz başka bazı özellikleri vardır, örneğin**Üst bilgi satırı** , **Satırı Başlat** ve**EndRow**başlık, başlangıç ve bitiş satır dizinlerini belirtmek için. bu**kriterler** özelliği, özel filtreleme ölçütlerini ayarlamak için kullanılır. Sınıfın ayrıca adında bir yöntemi vardır.**Filtre Satırları** verilen kriterlere göre filtrelenmiş satırları almak için.

 RowFilter'daki "içerir" tipi arama (büyük/küçük harfe duyarsız) özniteliği GridDesktop tarafından da desteklenir. Kullanabilirsin**Olguyu Yoksay** mülkiyet**Izgara Sütunu** ihtiyacınıza yönelik büyük/küçük harf duyarlılığı özniteliğini belirtmek için class. adlı bir özelliği de kullanabilirsiniz.**IsStartWithCriteria** nın-nin**Izgara Sütunu** RowFilter'ın bir sütunda StartWith ölçütünü kullanıp kullanmadığını belirtmek için sınıf; özelliğin varsayılan değeri false olarak ayarlanmıştır.

{{% /alert %}} 
## **Verileri Filtreleme**
Bu örnekte hem Otomatik Filtreleme hem de Özel Veri Filtreleme özelliklerini uyguluyoruz. GridDesktop'ta bazı veri listesini dolduruyoruz, Otomatik Filtreleme özelliğini etkinleştiriyoruz ve ardından bazı kriterlere göre filtrelenmiş satırları aratıyoruz.
### **Otomatik filtre**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Özel Veri Filtresi**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
