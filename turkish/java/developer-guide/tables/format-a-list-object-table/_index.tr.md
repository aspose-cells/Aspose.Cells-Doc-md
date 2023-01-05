---
title: Liste Nesnesini Biçimlendirme - Tablo
type: docs
weight: 50
url: /tr/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

Bir grup ilgili veriyi yönetmek ve analiz etmek için, bir hücre aralığını bir liste nesnesine (Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Tablo, diğer satır ve sütunlardaki verilerden bağımsız olarak yönetilen ilgili verileri içeren bir dizi satır ve sütundur. Varsayılan olarak, liste nesnesi verilerinizi hızlı bir şekilde filtreleyebilmeniz veya sıralayabilmeniz için tablodaki her sütunun başlık satırında filtreleme etkindir. Her bir toplam satırı hücresi için toplama işlevlerinin açılır listesini sağlayan liste nesnesine, bir toplam satırı (sayısal verilerle çalışmak için kullanışlı toplama işlevleri seçimi sağlayan bir listedeki özel bir satır) ekleyebilirsiniz. Aspose.Cells, listeler (veya tablolar) oluşturmak ve yönetmek için seçenekler sunar.

{{% /alert %}}

## **Liste Nesnesini Biçimlendirme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Oluşturmak için[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) bir çalışma sayfasında, kullanın[**Nesneleri Listele**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) toplama özelliği[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. Her biri[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) aslında bir nesnedir[**Nesne Koleksiyonunu Listele**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)Ayrıca bir List nesnesi eklemek ve içermesi gereken hücre aralığını belirtmek için add yöntemini sağlayan sınıf. Belirtilen hücre aralığına göre, bir[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) çalışma sayfasında Aspose.Cells tarafından oluşturulur. Nitelikleri kullanın (örneğin,[**Tablo Stili Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) )[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)tabloyu gereksinimlerinize göre biçimlendirmek için sınıf.

 Aşağıdaki örnek, bir çalışma sayfasına örnek veriler ekler,[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ve ona varsayılan stiller uygular.[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)stiller Microsoft Excel 2007/2010 tarafından desteklenir.

Kod çalıştırıldığında aşağıdaki çıktı üretilir.

**Çalışma sayfasında biçimlendirilmiş bir tablo oluşturulur** 

![yapılacaklar:resim_alternatif_metin](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
