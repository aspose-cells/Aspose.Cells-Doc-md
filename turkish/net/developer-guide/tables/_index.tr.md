---
title: Microsoft Excel dosyalarının tablolarını oluşturun ve yönetin.
linktitle: Tablolar
type: docs
weight: 150
url: /tr/net/create-and-format-table/
description: Aspose.Cells kütüphanesi kullanarak Excel dosyalarının tablosunu ekle, yeniden boyutlandır, düzenle, sil ve biçimlendirin.
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

- Liste nesnesi oluşturmak için veri aralığını seçme
- Bu, Liste Oluştur iletişim kutusunu görüntüler.
- Veri için Liste nesnesini uygulama ve toplam satırı belirtme (Seç **Veri**, ardından **Liste**, sonra **Toplam Satır**).

### **Aspose.Cells API'si Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasında bir [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) oluşturmak için, [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) sınıfının koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) sınıfının bir nesnesidir ve daha fazla List nesnesi eklemek ve belirtilen hücre aralığı için [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) yöntemini sağlayan [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) sınıfının bir nesnesidir.

Belirtilen hücre aralığına göre, Aspose.Cells tarafından Liste nesnesi oluşturulur. Liste yönetmek için [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) sınıfının özniteliklerini (örneğin, [**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns), vb.) kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz gibi, Aspose.Cells API'sini kullanarak aynı [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)'yi oluşturduk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Tabloyu Biçimlendir**

İlgili veri grubunu yönetmek ve analiz etmek için, hücre aralığını bir liste nesnesine (aynı zamanda bir Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Bir tablo, ilişkili verileri içeren bir dizi satır ve sütun, diğer satır ve sütunlardaki veriden bağımsız olarak yönetilir. Varsayılan olarak, tablodaki her sütunun başlık satırında filtreleme etkinleştirilir, böylece listeniz nesnesi verilerinizi hızlı bir şekilde filtreleyebilir veya sıralayabilir. Listeniz nesnesine (sayısal verilerle çalışmak için faydalı olan bir listede özel bir satır) toplam satır ekleyebilirsiniz. Bu toplam satırın her hücresi için bir toplama işlevlerinin açılır menüsünü sağlayan özel bir satır. Aspose.Cells, listelerin (veya tabloların) oluşturulması ve yönetilmesi için seçenekler sunar.

### **Liste Nesnesini Biçimlendirme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasında bir [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) oluşturmak için, [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) sınıfının koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) sınıfının bir nesnesidir ve istenen hücre aralığını belirlemek amacıyla [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) yöntemini sağlayan [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) sınıfından bir nesnedir. Belirtilen hücre aralığına göre, Aspose.Cells tarafından bir [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) oluşturulur. [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) sınıfının özniteliklerini (örneğin, [**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)) kullanarak tablonuzu biçimlendirebilirsiniz.

Aşağıdaki örnek, bir çalışma sayfasına örnek veri ekler, bir [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ekler ve ona varsayılan stilleri uygular. Microsoft Excel 2007/2010 tarafından desteklenen [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) stilleri bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Gelişmiş Konular**
- [Tabloyu ODS'ye Dönüştür](/cells/tr/net/convert-table-to-ods/)
- [Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve List Obje Bulma](/cells/tr/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma](/cells/tr/net/read-and-write-table-with-query-table-data-source/)
- [Çalışma Sayfası içinde Masa veya Liste Nesnesi Yorumunu Ayarlayın](/cells/tr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablolar ve Aralıklar](/cells/tr/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
