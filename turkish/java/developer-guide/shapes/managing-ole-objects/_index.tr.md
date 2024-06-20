---
title: OLE Nesneleri Yönetme
type: docs
weight: 30
url: /tr/java/managing-ole-objects/
---

## **Giriş**

OLE (Object Linking and Embedding), Microsoft'un bileşik bir belge teknolojisi için çerçevesidir. Kısaca, bileşik bir belge türü her türlü görsel ve bilgi nesnesini içerebilen bir masaüstü görüntüsü gibidir: metin, takvimler, animasyonlar, ses, hareketli video, 3D, sürekli güncellenen haberler, kontroller vb. Her masaüstü nesnesi, bir kullanıcıyla etkileşime girebilir ve aynı zamanda masaüstünde bulunan diğer nesnelerle iletişim kurabilir.

OLE (Object Linking and Embedding), birçok farklı programa destek sağlar ve bir programda oluşturulan içeriğin başka bir programa kullanılmasını sağlar. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Ekleyebileceğiniz içerik türlerini görmek için **Ekle** menüsünde **Nesne**'ye tıklayın. Bilgisayara yüklü olan ve OLE nesneleri destekleyen yalnızca programlar **Nesne türü** kutusunda görünür.

## **Bir Çalışma Sayfasına OLE Nesneleri Ekleme**

Aspose.Cells, çalışma sayfalarındaki OLE nesnelerini eklemeyi, çıkarmayı ve manipüle etmeyi destekler. Bu nedenle, Aspose.Cells'in [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection) sınıfını kullanarak koleksiyon listesine yeni bir OLE Nesnesi eklemek için kullanılır. Başka bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), bir OLE Nesnesini temsil eder. Bu sınıfın bazı önemli üyeleri vardır:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData), bayt dizisi türünde resmi (ikon) verisini belirtir. Resim, çalışma sayfasındaki OLE Nesnesini göstermek için kullanılacaktır.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData), bir bayt dizisi şeklinde nesne verisini belirtir. Bu veri, OLE Nesnesi simgesine çift tıkladığınızda ilgili programda gösterilecektir.

Aşağıdaki örnek, bir OLE Nesnesini çalışma sayfasına nasıl ekleyeceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Çalışsayan Elemanlar'ın Çalışsayan Elemanları Çıkarma**

Aşağıdaki örnek, bir çalışma kitabından çalışsayan elemanları çıkarmayı göstermektedir. Örnek, mevcut bir XLS dosyasından farklı çalışsayan elemanlar alır ve farklı dosyalar (DOC, XLS, PPT, PDF vb.) çalışsayan elemanın dosya biçim türüne dayalı olarak kaydeder.

İşte şablon XLS dosyasının ekran görüntüsü, ilk çalışma sayfasına gömülü farklı OLE Nesnelerine sahiptir.

**Şablon dosya dört OLE nesnesini içerir** 

![todo:image_alt_text](managing-ole-objects_1.png)

Kodu çalıştırdıktan sonra, ilgili OLE Nesneler biçim türlerine göre farklı dosyaları kaydedebiliriz. Oluşturulan bazı dosyaların ekran görüntüleri aşağıda verilmiştir.

**Çıkarılan XLS dosyası** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Çıkarılan PPT dosyası** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Gömülü MOL Dosyasının Çıkarılması**

Aspose.Cells, MOL (Atomlar ve bağlar hakkında bilgi içeren moleküler veri dosyası) gibi yaygın olmayan tipteki nesneleri çıkarmayı destekler. Aşağıdaki kod parçacığı, gömülü MOL dosyasını çıkarmayı ve onu diske kaydetmeyi göstermektedir [örnek excel dosyasını kullanarak](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Gelişmiş Konular**
- [Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme](/cells/tr/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Microsoft Excel kullanarak Aspose.Cells ile Çalışmayan Elemanı Otomatik Yenileme](/cells/tr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Çalışma Kitabından Çalışmayan Elemanları Çıkarma](/cells/tr/java/extract-ole-objects-from-workbook/)
- [Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla](/cells/tr/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
