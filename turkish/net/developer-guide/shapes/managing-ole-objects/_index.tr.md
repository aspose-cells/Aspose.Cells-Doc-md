---
title: OLE Nesnelerini Yönetme
type: docs
weight: 50
url: /tr/net/managing-ole-objects/
---
## **giriiş**

OLE (Object Linking and Embedding), Microsoft'in bir bileşik belge teknolojisi çerçevesidir. Kısaca, bir bileşik belge, her türlü görsel ve bilgi nesnesini içerebilen bir ekran masaüstü gibi bir şeydir: metin, takvimler, animasyonlar, ses, hareketli video, 3B, sürekli güncellenen haberler, kontroller vb. Her masaüstü nesnesi, bir kullanıcıyla etkileşime girebilen ve ayrıca masaüstündeki diğer nesnelerle iletişim kurabilen bağımsız bir program varlığıdır.

 OLE (Object Linking and Embedding) birçok farklı program tarafından desteklenir ve bir programda oluşturulan içeriğin başka bir programda kullanılabilir olmasını sağlamak için kullanılır. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Ne tür içerik ekleyebileceğinizi görmek için tıklayın**Nesne** üzerinde**Sokmak** Menü. Yalnızca bilgisayarda yüklü olan ve OLE nesnelerini destekleyen programlar görüntülenir.**Nesne türü** kutu.

### **OLE Nesnelerini Çalışma Sayfasına Ekleme**

Aspose.Cells, çalışma sayfalarına OLE nesneleri eklemeyi, ayıklamayı ve değiştirmeyi destekler. Bu nedenle Aspose.Cells,[**OleNesne Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) toplama listesine yeni bir OLE Nesnesi eklemek için kullanılan sınıf. Başka bir sınıf,[**Ole nesnesi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Görüntü Verileri**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)özelliği, bayt dizisi türündeki görüntü (simge) verilerini belirtir. Görüntü, çalışma sayfasında OLE Nesnesini göstermek için görüntülenecektir.
-  bu[**Nesne Verileri**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)özelliği, nesne verilerini bir bayt dizisi biçiminde belirtir. OLE Object ikonuna çift tıkladığınızda bu veriler ilgili programda gösterilecektir.

Aşağıdaki örnek, bir OLE Nesnesinin/Nesnelerinin bir çalışma sayfasına nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Çalışma Kitabındaki OLE Nesnelerini Çıkarma**

Aşağıdaki örnek, bir Çalışma Kitabında OLE Nesnelerinin nasıl ayıklanacağını gösterir. Örnek, mevcut bir XLS dosyasından farklı OLE nesneleri alır ve OLE nesnesinin dosya formatı türüne göre farklı dosyaları (DOC, XLS, PPT, PDF vb.) kaydeder.

Kodu çalıştırdıktan sonra, ilgili OLE Nesneleri biçim türlerine göre farklı dosyaları kaydedebiliriz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Katıştırılmış MOL Dosyasını Çıkarma**

Aspose.Cells, MOL (atomlar ve bağlar hakkında bilgi içeren moleküler veri dosyası) gibi alışılmadık türdeki nesnelerin çıkarılmasını destekler. Aşağıdaki kod parçacığı, gömülü MOL dosyasının çıkarılmasını ve bunu kullanarak diske kaydetmeyi gösterir.[örnek excel dosyası](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **ileri konular**
- [Bağlantılı Ole Nesnesinin Görüntü Etiketine Erişin ve Değiştirin](/cells/tr/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cells kullanarak Microsoft Excel aracılığıyla OLE nesnesini otomatik olarak yenile](/cells/tr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [OLE Nesnelerini Çalışma Kitabından Çıkarın](/cells/tr/net/extract-ole-objects-from-workbook/)
- [Katıştırılmış OLE Nesnesinin Sınıf Tanımlayıcısını Alın veya Ayarlayın](/cells/tr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [WAV dosyasını Ole Nesnesi olarak ekleme](/cells/tr/net/inserting-a-wav-file-as-an-ole-object/)

