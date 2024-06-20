---
title: Veri Filtreleme
type: docs
weight: 100
url: /tr/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop, filtre, veri filtresi, Otomatik Filtreleme, Satır Filtresi
description: Bu makale, GridDesktop ta Çalışma Kitabında veri filtreleme nasıl yapılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop**, kullanıcılar için Otomatik Filtreleme ve Özel Veri Filtreleme özellikleri sağlar. Bu özellikleri kullanarak, istediğiniz öğeleri çalışma kitabından listelemek için bir yol bulabilirsiniz. Dahası, bir listeye göre öğeleri belirli bir kriterlere göre filtrelemek mümkündür. Otomatik Filtreleme / Özel Veri Filtreleme özelliği ile metin, sayılar veya tarihler filtrelenebilir.

GridDesktop kontrolü için Otomatik Filtreleme özelliğini etkinleştirmek için **RowFilterSettings** sınıfının **EnableAutoFilter** Boolean özelliğini kullanabilirsiniz. Sınıfın kullanabileceğiniz diğer özellikleri, örneğin **HeaderRow**, **StartRow** ve **EndRow** başlık, başlangıç ve bitiş satır indekslerini belirtmek için kullanılır. **Criteria** özelliği özel filtreleme kriterlerini belirlemek için kullanılır. Sınıfın **FilterRows** adında verilen kriterlere göre filtrelenmiş satırları almak için bir yöntemi bulunmaktadır.

GridDesktop tarafından "içerir" tipinde arama (büyük/küçük harf duyarlı olmayan) RowFilter özelliği desteklenmektedir. İhtiyacınıza göre harf duyarlılık özelliğini belirtmek için **GridColumn** sınıfının **IgnoreCase** özelliğini kullanabilirsiniz. Bir sütun üzerinde StartWith kriterlerini içeren RowFilter'ın kullanılıp kullanılmayacağını belirtmek için **GridColumn** sınıfının **IsStartWithCriteria** adında bir özelliği de kullanabilirsiniz; özellik varsayılan olarak false olarak ayarlanmıştır.

{{% /alert %}} 
## **Veri Filtreleme**
Bu örnekte Hem Otomatik Filtreleme hem de Özel Veri Filtreleme özelliklerini uyguluyoruz. GridDesktop'ta bazı veri listesini dolduruyoruz, Otomatik Filtreleme özelliğini etkinleştiriyoruz ve ardından bazı kriterlere göre filtrelenmiş satırları arıyoruz.
### **Otomatik Filtreleme**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Özel Veri Filtresi**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
