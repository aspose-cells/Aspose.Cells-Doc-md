---
title: Liste Nesnesi Oluşturma
type: docs
weight: 20
url: /tr/python-java/creating-a-list-object/
---
Çalışma sayfalarının kullanımı, örneğin farklı türde listelerle çalışmayı kolaylaştırır. telefon listeleri, görev listeleri. vb. Aspose.Cells, liste oluşturmayı ve yönetmeyi destekler.

## **Liste Nesnesinin Avantajları**

Bir veri listesini gerçek bir Liste Nesnesine dönüştürdüğünüzde pek çok avantaj vardır:

- Yeni satırlar ve sütunlar otomatik olarak dahil edilir.
- SUM, AVERAGE, COUNT, vb. görüntülemek için listenizin en altına bir toplam satırı kolayca eklenebilir.
- Sağa eklenen sütunlar otomatik olarak List nesnesine eklenir.
- Satır ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste, yanlışlıkla satır ve sütun silinmesine karşı korumalıdır.

## **Microsoft Excel kullanarak Liste Nesnesi Oluşturma**

**Liste nesnesi oluşturmak için veri aralığı seçme** 

![yapılacaklar:resim_alternatif_Metin](picture1.png)

Bu, Liste Oluştur iletişim kutusunu görüntüler.

**Liste Oluştur iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](picture2.png)

List nesnesini uygulama ve Toplam Satırı belirtme (Select**Veri**, sonra**Liste**, bunu takiben**Toplam Satır**).

**Liste nesnesi oluşturma** 

![yapılacaklar:resim_alternatif_Metin](picture3.png)

## **Aspose.Cells API kullanarak Liste Nesnesi Oluşturma**

Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Oluşturmak için[**Nesne Listesi**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)bir çalışma sayfasında, kullanın[**Nesneleri Listele**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)toplama özelliği[**Çalışma kağıdı**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)sınıf. Her biri[**Nesne Listesi**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)aslında bir nesnedir[**Nesne Koleksiyonunu Listele**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)ayrıca sağlayan sınıf,[**Ekle**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) List nesnesi ekleme ve liste için bir hücre aralığı belirtme yöntemi.

Liste nesnesi, belirtilen hücre aralığına göre çalışma sayfasında Aspose.Cells tarafından oluşturulur.[**Nesne Listesi**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)Listeyi kontrol etmek için sınıf.

Aşağıda verilen örnekte, aynısını oluşturduk[**Nesne Listesi**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)Yukarıdaki bölümde Aspose.Cells Excel kullanarak oluşturduğumuz gibi Aspose.Cells for Python via Java API kullanarak.

## Kaynak kodu

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
