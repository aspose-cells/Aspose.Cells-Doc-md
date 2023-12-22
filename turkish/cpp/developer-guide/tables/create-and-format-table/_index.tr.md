---
title: Tablo Oluşturma ve Biçimlendirme
type: docs
weight: 10
url: /tr/cpp/create-and-format-table/
---
##  **Tablo Oluştur**
Elektronik tabloların avantajlarından biri, telefon listeleri, görev listeleri, işlem listeleri, varlıklar veya yükümlülükler gibi farklı türde listeler oluşturmanıza olanak sağlamasıdır. Çeşitli listeleri kullanmak, oluşturmak ve sürdürmek için birkaç kullanıcı birlikte çalışabilir.

Aspose.Cells, Listelerin oluşturulmasını ve yönetilmesini destekler.
###  **Liste Nesnesinin Avantajları**
Bir veri listesini gerçek bir Liste Nesnesine dönüştürmenin pek çok avantajı vardır.

- Yeni satırlar ve sütunlar otomatik olarak eklenir.
- SUM, ORTALAMA, COUNT vb. öğeleri görüntülemek için listenizin alt kısmındaki toplam satırı kolayca eklenebilir.
- Sağa eklenen sütunlar otomatik olarak List nesnesine dahil edilir.
- Satır ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilecektir.
- Liste yanlışlıkla satır ve sütun silinmesine karşı korunur.
###  **Microsoft Excel'i kullanarak Liste Nesnesi Oluşturma**

|**Liste nesnesini oluşturmak için veri aralığını seçme**|
| :- |
|![yapılacak şey:image_alt_text](jHcNq4o.png)|
Bu, Liste Oluştur iletişim kutusunu görüntüler.

|**Liste Oluştur iletişim kutusu**|
| :- |
|![yapılacak şey:image_alt_text](kJmukRF.png)|
Veriler için Liste nesnesini uygulama ve toplam satırı belirtme (*Veri**'yi, ardından *Liste**'yi ve ardından *Toplam Satır**'ı seçin).

|**Liste nesnesi oluşturma**|
| :- |
|![yapılacak şey:image_alt_text](ECSGVdR.png)|
###  **Aspose.Cells API'i kullanma**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class, bir çalışma sayfasını yönetmek için çok çeşitli yöntemler sağlar. Bir oluşturmak için[ListeObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) bir çalışma sayfasında şunu kullanın:[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) toplama yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf. Her `[ListObject]` aslında bir nesnedir.[ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) ayrıca aşağıdakileri sağlayan sınıf[Eklemek](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)`[ListObject]` nesnesi ekleme ve liste için bir hücre aralığı belirleme yöntemi.

 Belirtilen hücre aralığına göre `[ListObject]` nesnesi Aspose.Cells tarafından oluşturulur. Nitelikleri kullanın (örneğin[Toplamları GösterGöster](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) Ve[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)Listeyi kontrol etmek için `[ListObject]` sınıfının.

Aşağıda verilen örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuzun aynısını Aspose.Cells API kullanarak oluşturduk.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Tabloyu Biçimlendirme**
Bir grup ilgili veriyi yönetmek ve analiz etmek için, bir hücre aralığını bir liste nesnesine (Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Tablo, diğer satır ve sütunlardaki verilerden bağımsız olarak yönetilen ilgili verileri içeren bir dizi satır ve sütundan oluşur. Liste nesnesi verilerinizi hızlı bir şekilde filtreleyebilmeniz veya sıralayabilmeniz için, varsayılan olarak tablodaki her sütunun başlık satırında filtreleme etkindir. Her bir toplamlar satır hücresi için toplama işlevlerinin açılır listesini sağlayan liste nesnesine bir toplam satırı (sayısal verilerle çalışmak için yararlı toplama işlevleri seçimini sağlayan bir listedeki özel bir satır) ekleyebilirsiniz. Aspose.Cells, liste (veya tablo) oluşturma ve yönetme seçenekleri sunar.
###  **Liste Nesnesini Biçimlendirme**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Oluşturmak için*ListeObject*bir çalışma sayfasında `ListObjectCollection`'i kullanın. Her `[ListObject]` aslında `ListObjectCollection` sınıfının bir nesnesidir;[Eklemek](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)`[ListObject]` nesnesi ekleme yöntemini seçin ve bu nesnenin kapsaması gereken hücre aralığını belirtin. Belirtilen hücre aralığına göre*ListeObject* çalışma sayfasında Aspose.Cells tarafından oluşturulmuştur. Nitelikleri kullanın (örneğin,[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)Tabloyu gereksinimlerinize göre biçimlendirmek için `[ListObject]` sınıfının ) öğesini kullanın.

Aşağıdaki örnek, bir çalışma sayfasına örnek veriler ekler, bir `[ListObject]` ekler ve buna varsayılan stiller uygular. `[ListObject]` stilleri Microsoft Excel 2007/2010 tarafından desteklenir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
