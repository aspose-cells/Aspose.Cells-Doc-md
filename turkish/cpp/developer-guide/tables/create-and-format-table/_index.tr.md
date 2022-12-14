---
title: Tablo Oluşturma ve Biçimlendirme
type: docs
weight: 10
url: /tr/cpp/create-and-format-table/
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

|**Liste nesnesi oluşturmak için veri aralığı seçme**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](jHcNq4o.png)|
Bu, Liste Oluştur iletişim kutusunu görüntüler.

|**Liste Oluştur iletişim kutusu**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](kJmukRF.png)|
 Veriler için List nesnesini uygulamak ve toplam satırı belirtmek (Select**Veri** , sonra**Liste** , bunu takiben**Toplam Satır**).

|**Liste nesnesi oluşturma**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](ECSGVdR.png)|
### **Aspose.Cells API'i kullanma**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli yöntemler sağlar. oluşturmak için[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) bir çalışma sayfasında,[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) toplama yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. Her `[IListObject]` aslında bir nesnedir.[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) ayrıca sağlayan sınıf,[Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)`[IListObject]` nesnesi ekleme ve liste için bir hücre aralığı belirtme yöntemi.

 Belirtilen hücre aralığına göre, `[IListObject]` nesnesi Aspose.Cells tarafından oluşturulur. Nitelikleri kullanın (örneğin[Toplamları Göster](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) ve[Sütunları Listele](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)vb.) listeyi kontrol etmek için `[IListObject]` sınıfından.

Aşağıda verilen örnekte yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz `[IListObject]`'in aynısını Aspose.Cells API kullanarak oluşturduk.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Tablo Biçimlendirme**
Bir grup ilgili veriyi yönetmek ve analiz etmek için, bir hücre aralığını bir liste nesnesine (Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Tablo, diğer satır ve sütunlardaki verilerden bağımsız olarak yönetilen ilgili verileri içeren bir dizi satır ve sütundur. Varsayılan olarak, liste nesnesi verilerinizi hızlı bir şekilde filtreleyebilmeniz veya sıralayabilmeniz için tablodaki her sütunun başlık satırında filtreleme etkindir. Her bir toplam satırı hücresi için toplama işlevlerinin açılır listesini sağlayan liste nesnesine, bir toplam satırı (sayısal verilerle çalışmak için yararlı toplama işlevleri seçimi sağlayan bir listedeki özel bir satır) ekleyebilirsiniz. Aspose.Cells, listeler (veya tablolar) oluşturmak ve yönetmek için seçenekler sunar.
### **Liste Nesnesini Biçimlendirme**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Oluşturmak için*Nesne Listesi*bir çalışma sayfasında `IListObjectCollection` kullanın. Her `[IListObject]` aslında `IListObjectCollection` sınıfının bir nesnesidir ve bu da[Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)`[IListObject]` nesnesi ekleme yöntemi ve kapsaması gereken hücre aralığını belirtin. Belirtilen hücre aralığına göre, bir*Nesne Listesi* çalışma sayfasında Aspose.Cells tarafından oluşturulur. Nitelikleri kullanın (örneğin,[Tablo Stili Türü](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) tabloyu gereksinimlerinize göre biçimlendirmek için `[IListObject]` sınıfından.

Aşağıdaki örnek, bir çalışma sayfasına örnek veriler ekler, bir `[IListObject]` ekler ve buna varsayılan stiller uygular. `[IListObject]` stilleri, Microsoft Excel 2007/2010 tarafından desteklenir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
