---
title: Tablo Oluştur ve Biçimlendir
type: docs
weight: 10
url: /tr/cpp/create-and-format-table/
---

## **Tablo Oluştur**
Hesap tablolarının avantajlarından biri, telefon listeleri, görev listeleri, işlemler, varlıklar veya borçlar gibi farklı tiplerde listeler oluşturmanıza olanak tanımalarıdır. Çeşitli kullanıcılar birden fazla listeyi kullanmak, oluşturmak ve yönetmek için birlikte çalışabilir.

Aspose.Cells, listeler oluşturmayı ve yönetmeyi destekler.
### **Liste Nesnesi Avantajları**
Veri listesini gerçek bir Liste Nesnesine dönüştürdüğünüzde birkaç avantaj bulunmaktadır

- Yeni satır ve sütunlar otomatik olarak dahil edilir.
- Listenizin altından toplam satırı SUM, AVERAGE, COUNT vb. göstermek için kolayca ekleyebilirsiniz.
- Sağa eklenen sütunlar otomatik olarak List nesnesine dahil edilir.
- Satırlar ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste kazara satır ve sütun silme işlemlerine karşı korunur.
### **Microsoft Excel Kullanarak Bir Liste Nesnesi Oluşturma**

|**Liste öğesi oluşturmak için veri aralığı seçme**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Bu, Liste Oluştur iletişim kutusunu görüntüler.

|**Liste Oluştur iletişim kutusu**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Veri ve özel satır (Seçin **Veri**, sonra **Liste**, ardından **Toplam Satır**) belirterek Liste öğesini uygulamak.

|**Liste öğesi oluşturma**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Aspose.Cells API'si Kullanımı**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfıyla temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için geniş bir yöntem yelpazesi sunar. Bir [ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) oluşturmak için bir çalışma sayfasında, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) koleksiyon yöntemini kullanın. Her `[ListObject]` aslında, [ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) sınıfının bir nesnesidir ve ayrıca bir `[ListObject]` nesnesi eklemek için [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) yöntemini sağlar ve listenin hücre aralığını belirtir.

Belirtilen hücre aralığına göre, Aspose.Cells tarafından `[ListObject]` nesnesi oluşturulur. Liste öğesinin denetimini sağlamak için `[ListObject]` sınıfının özelliklerini (örneğin [SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) ve [GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/) vb.) kullanın.

Aşağıdaki örnekte, Microsoft Excel'de oluşturduğumuz `[ListObject]`'i Aspose.Cells API'sını kullanarak aynısını oluşturduk.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **Tabloyu Biçimlendir**
İlgili veri grubunu yönetmek ve analiz etmek için hücre aralığını bir liste öğesine dönüştürmek mümkün olup (ayrıca bir Excel tablosu olarak bilinir). Bir tablo, diğer satır ve sütunlardaki verilerden bağımsız olarak yönetilen ilgili verileri içeren sütunların ve satırların bir dizisidir. Varsayılan olarak, tablodaki her sütunun başlık satırında filtreleme etkinleştirilmiştir, böylece listenizin verilerini hızlı bir şekilde filtreleyebilir veya sıralayabilirsiniz. Liste öğesine sayısal verilerle çalışırken kullanışlı olan bir seçim sağlayan özel bir satır olan toplam satırı ekleyebilirsiniz. Aspose.Cells, listelerin (veya tabloların) oluşturulması ve yönetilmesi için seçenekler sunar.
### **Liste Nesnesini Biçimlendirme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfıyla temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfalarını yönetmek için geniş bir yöntem yelpazesi sunar. Bir *ListObject* oluşturmak için `ListObjectCollection` kullanın. Her `[ListObject]` aslında, `ListObjectCollection` sınıfının bir nesnesidir ve ayrıca bir [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) yöntemiyle bir `[ListObject]` nesnesi ekleyebilir ve kapsaması gereken hücre aralığını belirleyebilirsiniz. Belirtilen hücre aralığına göre, Aspose.Cells tarafından bir *ListObject* oluşturulur. `[ListObject]` sınıfının özellikleri (örneğin [SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) kullanarak tabloyu isteğinize göre biçimlendirin.

Aşağıdaki örnek, çalışma sayfasına örnek veri ekler, bir `[ListObject]` ekler ve ona varsayılan stiller uygular. `[ListObject]` stillleri, Microsoft Excel 2007/2010 tarafından desteklenir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
