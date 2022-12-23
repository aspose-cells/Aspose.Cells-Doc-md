---
title: Microsoft Excel dosyalarının tablolarını oluşturun ve yönetin.
linktitle: Tablolar
type: docs
weight: 150
url: /tr/net/create-and-format-table/
description: Aspose.Cells kitaplığını kullanarak Excel dosyalarının tablosunu ekleyin, yeniden boyutlandırın, düzenleyin, silin, biçimlendirin.
---
## **Tablo Oluştur**

E-tabloların avantajlarından biri, telefon listeleri, görev listeleri, işlem listeleri, varlıklar veya yükümlülükler gibi farklı türde listeler oluşturmanıza izin vermesidir. Birkaç kullanıcı, çeşitli listeleri kullanmak, oluşturmak ve sürdürmek için birlikte çalışabilir.

Aspose.Cells, Liste oluşturmayı ve yönetmeyi destekler.

### **Liste Nesnesinin Avantajları**

Bir veri listesini gerçek bir Liste Nesnesine dönüştürdüğünüzde pek çok avantaj vardır.

- Yeni satırlar ve sütunlar otomatik olarak dahil edilir.
- SUM, AVERAGE, COUNT, vb. görüntülemek için listenizin en altına bir toplam satırı kolayca eklenebilir.
- Sağa eklenen sütunlar otomatik olarak List nesnesine eklenir.
- Satır ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste, yanlışlıkla satır ve sütun silinmesine karşı korumalıdır.

### **Microsoft Excel kullanarak Liste Nesnesi Oluşturma**

- Liste nesnesi oluşturmak için veri aralığı seçme
- Bu, Liste Oluştur iletişim kutusunu görüntüler.
-  Veriler için Liste nesnesini uygulayın ve toplam satırı belirtin (Seçin**Veri** , o zamanlar**Liste** , bunu takiben**Toplam Satır**).

### **Aspose.Cells API'i kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Oluşturmak için[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) bir çalışma sayfasında,[**Nesneleri Listele**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) toplama özelliği[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. Her biri[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) aslında bir nesnedir[**Nesne Koleksiyonunu Listele**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) ayrıca sağlayan sınıf,[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)Liste nesnesi ekleme ve liste için bir hücre aralığı belirtme yöntemi.

Liste nesnesi, belirtilen hücre aralığına göre Aspose.Cells tarafından oluşturulur. Nitelikleri kullanın (örneğin,[**Toplamları Göster**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**Sütunları Listele**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) , vb.)[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Listeyi kontrol etmek için sınıf.

 Aşağıda verilen örnekte, aynısını oluşturduk[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz gibi Aspose.Cells API kullanarak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Tablo Biçimlendirme**

Bir grup ilgili veriyi yönetmek ve analiz etmek için, bir hücre aralığını bir liste nesnesine (Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Tablo, diğer satır ve sütunlardaki verilerden bağımsız olarak yönetilen ilgili verileri içeren bir dizi satır ve sütundur. Varsayılan olarak, liste nesnesi verilerinizi hızlı bir şekilde filtreleyebilmeniz veya sıralayabilmeniz için tablodaki her sütunun başlık satırında filtreleme etkindir. Her bir toplam satırı hücresi için toplama işlevlerinin açılır listesini sağlayan liste nesnesine, bir toplam satırı (sayısal verilerle çalışmak için kullanışlı toplama işlevleri seçimi sağlayan bir listedeki özel bir satır) ekleyebilirsiniz. Aspose.Cells, listeler (veya tablolar) oluşturmak ve yönetmek için seçenekler sunar.

### **Liste Nesnesini Biçimlendirme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Oluşturmak için[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) bir çalışma sayfasında, kullanın[**Nesneleri Listele**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) toplama özelliği[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. Her biri[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) aslında bir nesnedir[**Nesne Koleksiyonunu Listele**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) ayrıca sağlayan sınıf,[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) List nesnesi ekleme ve kapsaması gereken hücre aralığını belirleme yöntemi. Belirtilen hücre aralığına göre, bir[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)çalışma sayfasında Aspose.Cells tarafından oluşturulur. Nitelikleri kullanın (örneğin,[**Tablo Stili Türü**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) )[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)tabloyu gereksinimlerinize göre biçimlendirmek için sınıf.

 Aşağıdaki örnek, bir çalışma sayfasına örnek veriler ekler,[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ve varsayılan stilleri ona uygulayın.[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)stiller Microsoft Excel 2007/2010 tarafından desteklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **ileri konular**
- [Tabloyu ODS'e Dönüştür](/cells/tr/net/convert-table-to-ods/)
- [Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun](/cells/tr/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma](/cells/tr/net/read-and-write-table-with-query-table-data-source/)
- [Çalışma Sayfasında Tablo veya Liste Nesnesinin Yorumunu Ayarlama](/cells/tr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablolar ve Aralıklar](/cells/tr/net/tables-and-ranges/)

