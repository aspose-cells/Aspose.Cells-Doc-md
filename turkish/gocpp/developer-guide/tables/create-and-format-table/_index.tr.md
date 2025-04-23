---
title: Tablo Oluştur ve Biçimlendir
type: docs
weight: 10
url: /tr/go-cpp/create-and-format-table/
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

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonu içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için geniş bir yöntem yelpazesi sağlar. Bir çalışma sayfasında [ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) oluşturmak için, [GetListObjects](https://reference.aspose.com/cells/go-cpp/worksheet/getlistobjects/) koleksiyon metodunu kullanın. Her `[ListObject]`, aslında [ListObjectCollection](https://reference.aspose.com/cells/go-cpp/listobjectcollection/) sınıfının bir nesnesidir ve bu da [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add_int_int_int_int_bool/) yöntemini sağlar ve liste için hücreler aralığını belirler.

Belirtilen hücre aralığına göre, `[ListObject]` nesnesi Aspose.Cells tarafından oluşturulur. Listeyi kontrol etmek için `[ListObject]` sınıfının özniteliklerini (örneğin [SetShowTotals](https://reference.aspose.com/cells/go-cpp/listobject/setshowtotals/) ve [GetListColumns](https://reference.aspose.com/cells/go-cpp/listobject/getlistcolumns/) vb.) kullanın.

Aşağıdaki örnekte, Microsoft Excel'de oluşturduğumuz `[ListObject]`'i Aspose.Cells API'sını kullanarak aynısını oluşturduk.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingListObjects.go" >}}

## **Tabloyu Biçimlendir**

İlgili veri grubunu yönetmek ve analiz etmek için hücre aralığını bir liste öğesine dönüştürmek mümkün olup (ayrıca bir Excel tablosu olarak bilinir). Bir tablo, diğer satır ve sütunlardaki verilerden bağımsız olarak yönetilen ilgili verileri içeren sütunların ve satırların bir dizisidir. Varsayılan olarak, tablodaki her sütunun başlık satırında filtreleme etkinleştirilmiştir, böylece listenizin verilerini hızlı bir şekilde filtreleyebilir veya sıralayabilirsiniz. Liste öğesine sayısal verilerle çalışırken kullanışlı olan bir seçim sağlayan özel bir satır olan toplam satırı ekleyebilirsiniz. Aspose.Cells, listelerin (veya tabloların) oluşturulması ve yönetilmesi için seçenekler sunar.

### **Liste Nesnesini Biçimlendirme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonu içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, çalışma sayfalarını yönetmek için geniş bir yöntem yelpazesi sağlar. Bir sayfa içinde *ListObject* oluşturmak için `ListObjectCollection` kullanın. Her `[ListObject]`, aslında `ListObjectCollection` sınıfının bir nesnesidir ve `[Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add/)` metodunu kullanarak bir `[ListObject]` nesnesi ekler ve içermesi gereken hücre aralığını belirtir. Belirtilen hücre aralığına göre, Aspose.Cells tarafından çalışma sayfasında bir *ListObject* oluşturulur. Tabloyu biçimlendirmek için `[ListObject]` sınıfının özniteliklerini (örneğin, [SetTableStyleType](https://reference.aspose.com/cells/go-cpp/listobject/settablestyletype/)) kullanın.

Aşağıdaki örnek, çalışma sayfasına örnek veri ekler, bir `[ListObject]` ekler ve ona varsayılan stiller uygular. `[ListObject]` stillleri, Microsoft Excel 2007/2010 tarafından desteklenir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatTable.go" >}}
