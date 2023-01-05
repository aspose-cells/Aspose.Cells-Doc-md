---
title: Tablo Oluşturma
type: docs
weight: 40
url: /tr/java/creating-a-list-object/
---
{{% alert color="primary" %}}

E-tabloların avantajlarından biri, telefon listeleri, görev listeleri, işlem listeleri, varlıklar veya yükümlülükler gibi farklı türde listeler oluşturmanıza izin vermesidir. Birkaç kullanıcı, çeşitli listeleri kullanmak, oluşturmak ve sürdürmek için birlikte çalışabilir.

Aspose.Cells, Liste oluşturmayı ve yönetmeyi destekler.

{{% /alert %}}

## **Bir tablonun avantajları**

Bir veri listesini gerçek bir Liste Nesnesine dönüştürdüğünüzde pek çok avantaj vardır:

- Yeni satırlar ve sütunlar otomatik olarak dahil edilir.
- SUM, AVERAGE, COUNT, vb. görüntülemek için listenizin en altına bir toplam satırı kolayca eklenebilir.
- Sağa eklenen sütunlar otomatik olarak List nesnesine eklenir.
- Satır ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste, yanlışlıkla satır ve sütun silinmesine karşı korumalıdır.

## **Microsoft Excel kullanarak tablo oluşturma**

**Liste nesnesi oluşturmak için veri aralığı seçme** 

![yapılacaklar:resim_alternatif_metin](creating-a-list-object_1.png)

Bu, Liste Oluştur iletişim kutusunu görüntüler.

**Liste Oluştur iletişim kutusu** 

![yapılacaklar:resim_alternatif_metin](creating-a-list-object_2.png)

 List nesnesini uygulama ve Toplam Satırı belirtme (Select**Veri** , o zamanlar**Liste** , bunu takiben**Toplam Satır**).

**Liste nesnesi oluşturma** 

![yapılacaklar:resim_alternatif_metin](creating-a-list-object_3.png)

## **Kullanarak tablo oluşturma Aspose.Cells API**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Oluşturmak için[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) bir çalışma sayfasında, kullanın[**Nesneleri Listele**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) Worksheet sınıfının toplama özelliği. Her biri[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) aslında bir nesnedir[**Nesne Koleksiyonunu Listele**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)ayrıca bir List nesnesi eklemek ve liste için bir hücre aralığı belirtmek için add yöntemini sağlayan sınıf.

Liste nesnesi, belirtilen hücre aralığına göre çalışma sayfasında Aspose.Cells tarafından oluşturulur.[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Listeyi kontrol etmek için sınıf.

 Aşağıda verilen örnekte, aynısını oluşturduk[**Nesne Listesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz gibi Aspose.Cells API kullanarak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
