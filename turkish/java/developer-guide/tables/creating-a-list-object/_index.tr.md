---
title: Tablo Oluşturma
type: docs
weight: 40
url: /tr/java/creating-a-list-object/
---

{{% alert color="primary" %}}

Hesap tablolarının avantajlarından biri, telefon listeleri, görev listeleri, işlemler, varlıklar veya borçlar gibi farklı tiplerde listeler oluşturmanıza olanak tanımalarıdır. Çeşitli kullanıcılar birden fazla listeyi kullanmak, oluşturmak ve yönetmek için birlikte çalışabilir.

Aspose.Cells, listeler oluşturmayı ve yönetmeyi destekler.

{{% /alert %}}

## **Bir tablonun avantajları**

Bir veri listesini gerçek bir Liste Objesine dönüştürdüğünüzde birkaç avantaj vardır:

- Yeni satır ve sütunlar otomatik olarak dahil edilir.
- Listenizin altından toplam satırı SUM, AVERAGE, COUNT vb. göstermek için kolayca ekleyebilirsiniz.
- Sağa eklenen sütunlar otomatik olarak List nesnesine dahil edilir.
- Satırlar ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste kazara satır ve sütun silme işlemlerine karşı korunur.

## **Microsoft Excel kullanarak bir tablo oluşturma**

**Liste nesnesi oluşturmak için veri aralığını seçme** 

![todo:image_alt_text](creating-a-list-object_1.png)

Bu, Liste Oluştur iletişim kutusunu görüntüler.

**Liste Oluştur iletişim kutusu** 

![todo:image_alt_text](creating-a-list-object_2.png)

Liste nesnesini uygulama ve Toplam Satır belirtme (Önce **Veri**, sonra **Liste**, ardından **Toplam Satır** seçeneğini belirleyin).

**Liste Nesnesi Oluşturma** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Aspose.Cells API kullanarak bir tablo oluşturma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) koleksiyonu içerir.

Bir çalışma sayfası {0} sınıfı tarafından temsil edilir. {1} sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bir çalışma sayfasında bir {2} oluşturmak için, Worksheet sınıfının {3} koleksiyon özelliğini kullanın. Her {4}, aslında, {5} sınıfının bir nesnesidir ve listenin oluşturulması ve listeye ait hücre aralığının belirtilmesi için {6} yöntemini sağlar.

Belirtilen hücre aralığına göre Aspose.Cells tarafından çalışma sayfasında bir Liste nesnesi oluşturulur. Listeyi, [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) sınıfının öznitelikleri (örneğin, ShowTotals, ListColumns vb.) kullanarak kontrol etmek için kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz gibi, Aspose.Cells API'sini kullanarak aynı [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)'yi oluşturduk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
{{< app/cells/assistant language="java" >}}
