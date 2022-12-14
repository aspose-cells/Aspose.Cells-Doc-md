---
title: OLE Nesnelerini Yönetme
type: docs
weight: 30
url: /tr/java/managing-ole-objects/
---
## **giriiş**

OLE (Object Linking and Embedding), Microsoft'in bir bileşik belge teknolojisi çerçevesidir. Kısaca, bir bileşik belge, her türlü görsel ve bilgi nesnesini içerebilen bir ekran masaüstü gibi bir şeydir: metin, takvimler, animasyonlar, ses, hareketli video, 3B, sürekli güncellenen haberler, kontroller vb. Her masaüstü nesnesi, bir kullanıcıyla etkileşime girebilen ve ayrıca masaüstündeki diğer nesnelerle iletişim kurabilen bağımsız bir program varlığıdır.

 OLE (Object Linking and Embedding) birçok farklı program tarafından desteklenir ve bir programda oluşturulan içeriğin başka bir programda kullanılabilir olmasını sağlamak için kullanılır. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Ne tür içerik ekleyebileceğinizi görmek için tıklayın**Nesne** üzerinde**Sokmak** Menü. Yalnızca bilgisayarda yüklü olan ve OLE nesnelerini destekleyen programlar görüntülenir.**Nesne türü** kutu.

## **OLE Nesnelerini Çalışma Sayfasına Ekleme**

Aspose.Cells, çalışma sayfalarına OLE nesneleri eklemeyi, ayıklamayı ve değiştirmeyi destekler. Bu nedenle Aspose.Cells,[**OleNesne Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)toplama listesine yeni bir OLE Nesnesi eklemek için kullanılan sınıf. Başka bir sınıf,[**Ole nesnesi**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri vardır:

- [**Görüntü Verileri**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)bayt dizisi türündeki görüntü (simge) verilerini belirtir. Görüntü, çalışma sayfasında OLE Nesnesini göstermek için görüntülenecektir.
- [**Nesne Verileri**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)nesne verilerini bir bayt dizisi biçiminde belirtir. OLE Object ikonuna çift tıkladığınızda bu veriler ilgili programda gösterilecektir.

Aşağıdaki örnek, bir OLE Nesnesinin çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Çalışma Kitabındaki OLE Nesnelerini Çıkarma**

Aşağıdaki örnek, bir Çalışma Kitabında OLE Nesnelerinin nasıl ayıklanacağını gösterir. Örnek, mevcut bir XLS dosyasından farklı OLE nesneleri alır ve OLE nesnesinin dosya formatı türüne göre farklı dosyaları (DOC, XLS, PPT, PDF vb.) kaydeder.

İşte şablon XLS dosyasının ekran görüntüsü, ilk çalışma sayfasına katıştırılmış farklı OLE Nesneleri var.

**Şablon dosyası dört OLE nesnesi içerir** 

![yapılacaklar:resim_alternatif_Metin](managing-ole-objects_1.png)

Kodu çalıştırdıktan sonra, ilgili OLE Nesneleri biçim türlerine göre farklı dosyaları kaydedebiliriz. Oluşturulan dosyalardan bazıları için ekran görüntüleri aşağıdadır.

**Ayıklanan XLS dosyası** 

![yapılacaklar:resim_alternatif_Metin](managing-ole-objects_2.png)

**Çıkarılan PPT dosyası** 

![yapılacaklar:resim_alternatif_Metin](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Katıştırılmış MOL Dosyasını Çıkarma**

Aspose.Cells, MOL (atomlar ve bağlar hakkında bilgi içeren moleküler veri dosyası) gibi alışılmadık türdeki nesnelerin çıkarılmasını destekler. Aşağıdaki kod parçacığı, gömülü MOL dosyasının çıkarılmasını ve bunu kullanarak diske kaydetmeyi gösterir.[örnek excel dosyası](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **ileri konular**
- [Bağlantılı Ole Nesnesinin Görüntü Etiketine Erişin ve Değiştirin](/cells/tr/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cells kullanarak Microsoft Excel aracılığıyla OLE nesnesini otomatik olarak yenile](/cells/tr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [OLE Nesnelerini Çalışma Kitabından Çıkarın](/cells/tr/java/extract-ole-objects-from-workbook/)
- [Katıştırılmış OLE Nesnesinin Sınıf Tanımlayıcısını Alın veya Ayarlayın](/cells/tr/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
