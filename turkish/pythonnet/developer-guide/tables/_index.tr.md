---
title: Microsoft Excel dosyalarının tablolarını oluşturun ve yönetin.
linktitle: Tablolar
type: docs
weight: 150
url: /tr/python-net/create-and-format-table/
description: Aspose.Cells kütüphanesi kullanarak Excel dosyalarının tablosunu ekle, yeniden boyutlandır, düzenle, sil ve biçimlendirin.
---

## **Tablo Oluştur**

Hesap tablolarının avantajlarından biri, telefon listeleri, görev listeleri, işlemler, varlıklar veya borçlar gibi farklı tiplerde listeler oluşturmanıza olanak tanımalarıdır. Çeşitli kullanıcılar birden fazla listeyi kullanmak, oluşturmak ve yönetmek için birlikte çalışabilir.

Aspose.Cells for Python via .NET listeler oluşturmayı ve yönetmeyi destekler.

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

### **Aspose.Cells for Python via .NET API kullanarak**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir koleksiyon içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasında bir [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) oluşturmak için, [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) sınıfının koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject), aslında [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) sınıfının bir nesnesidir ve daha fazla List nesnesi eklemek ve belirtilen hücre aralığı için [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) yöntemini sağlayan [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) sınıfının bir nesnesidir.

Belirtilen hücre aralığına göre, List nesnesi Aspose.Cells for Python via .NET tarafından oluşturulur. List'i kontrol etmek için [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) sınıfının özelliklerini (örneğin, [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals), [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns) vb.) kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuzla aynı [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)’yi Aspose.Cells for Python via .NET API kullanarak oluşturduk.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **Tabloyu Biçimlendir**

İlişkili veri grubunu yönetmek ve analiz etmek için, hücre aralığını liste nesnesine (diğer adıyla Excel tablosu) dönüştürmek mümkündür. Bir tablo, diğer satır ve sütun verilerinden bağımsız olarak yönetilen ilişkili verilere sahip bir dizi satır ve sütundur. Varsayılan olarak, tablodaki her sütun başlık satırında filtreleme etkinleştirilmiştir, böylece listenin veri üzerinde hızlıca filtreleme veya sıralama yapabilirsiniz. Liste nesline toplam satır ekleyebilirsiniz (toplam fonksiyonları içeren özel bir satır), bu satırda toplam fonksiyonlarının açılır listeyi sağlar. Aspose.Cells for Python via .NET, listeler (veya tablolar) oluşturmak ve yönetmek için seçenekler sunar.

### **Liste Nesnesini Biçimlendirme**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyon içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasında bir [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) oluşturmak için, [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) sınıfının koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection) sınıfının bir nesnesidir ve istenen hücre aralığını belirlemek amacıyla [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) yöntemini sağlayan [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection) sınıfından bir nesnedir. Belirtilen hücre aralığına göre, Aspose.Cells tarafından bir [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) oluşturulur. [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) sınıfının özniteliklerini (örneğin, [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) kullanarak tablonuzu biçimlendirebilirsiniz.

Aşağıdaki örnek, bir çalışma sayfasına örnek veri ekler, bir [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) ekler ve ona varsayılan stilleri uygular. Microsoft Excel 2007/2010 tarafından desteklenen [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) stilleri bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **Gelişmiş Konular**
- [Tabloyu ODS'ye Dönüştür](/cells/tr/python-net/convert-table-to-ods/)
- [Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve List Obje Bulma](/cells/tr/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma](/cells/tr/python-net/read-and-write-table-with-query-table-data-source/)
- [Çalışma Sayfası içinde Masa veya Liste Nesnesi Yorumunu Ayarlayın](/cells/tr/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablolar ve Aralıklar](/cells/tr/python-net/tables-and-ranges/)


{{< app/cells/assistant language="python-net" >}}
