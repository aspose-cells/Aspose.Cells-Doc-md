---
title: Bir Liste Objesi Oluşturma
type: docs
weight: 20
url: /tr/python-java/creating-a-list-object/
---

Çeşitli türde listelerle çalışmayı kolaylaştırmak için çalışsayfalarının kullanımı kolaydır, örneğin telefon listeleri, görev listeleri vb. Aspose.Cells, listeler oluşturmayı ve yönetmeyi destekler.

## **Liste Nesnesi Avantajları**

Bir veri listesini gerçek bir Liste Objesine dönüştürdüğünüzde birkaç avantaj vardır:

- Yeni satır ve sütunlar otomatik olarak dahil edilir.
- Listenizin altından toplam satırı SUM, AVERAGE, COUNT vb. göstermek için kolayca ekleyebilirsiniz.
- Sağa eklenen sütunlar otomatik olarak List nesnesine dahil edilir.
- Satırlar ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste kazara satır ve sütun silme işlemlerine karşı korunur.

## **Microsoft Excel Kullanarak Bir Liste Nesnesi Oluşturma**

**Liste nesnesi oluşturmak için veri aralığını seçme** 

![todo:image_alt_text](picture1.png)

Bu, Liste Oluştur iletişim kutusunu görüntüler.

**Liste Oluştur iletişim kutusu** 

![todo:image_alt_text](picture2.png)

Liste nesnesi uygulama ve Toplam Satır belirtme (Seçim **Veri**, ardından **Liste**, devamında **Toplam Satır**).

**Liste Nesnesi Oluşturma** 

![todo:image_alt_text](picture3.png)

## **Aspose.Cells API kullanarak bir Liste Objesi oluşturma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) koleksiyonu içerir.

Çalışsayfa, [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) sınıfı, bir çalışsayfayı yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışsayfada [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) oluşturmak için, [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects) sınıfının [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) aslında [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection) sınıfının bir nesnesidir ve ayrıca [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) yöntemini sağlar, bu yöntemle Liste Objesi eklenip liste için hücre aralığı belirtilebilir.

Belirtilen hücre aralığına göre, Aspose.Cells tarafından çalışsayfada Liste Objesi oluşturulur. [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) sınıfının özellikleri (örneğin, Toplamları Göster, Liste Sütunları vb.) ile listeyi kontrol etmek için kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz aynı [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)'yi Aspose.Cells for Python via Java API kullanarak nasıl oluşturduğumuzu göstermekteyiz.

## Kaynak Kod

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
