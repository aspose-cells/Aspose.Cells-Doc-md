---
title: OLE Nesneleri Yönetme
type: docs
weight: 50
url: /tr/net/managing-ole-objects/
---

## **Giriş**

OLE (Object Linking and Embedding), Microsoft'un bileşik bir belge teknolojisi için çerçevesidir. Kısaca, bileşik bir belge türü her türlü görsel ve bilgi nesnesini içerebilen bir masaüstü görüntüsü gibidir: metin, takvimler, animasyonlar, ses, hareketli video, 3D, sürekli güncellenen haberler, kontroller vb. Her masaüstü nesnesi, bir kullanıcıyla etkileşime girebilir ve aynı zamanda masaüstünde bulunan diğer nesnelerle iletişim kurabilir.

OLE (Object Linking and Embedding), birçok farklı programa destek sağlar ve bir programda oluşturulan içeriğin başka bir programa kullanılmasını sağlar. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Ekleyebileceğiniz içerik türlerini görmek için **Ekle** menüsünde **Nesne**'ye tıklayın. Bilgisayara yüklü olan ve OLE nesneleri destekleyen yalnızca programlar **Nesne türü** kutusunda görünür.

### **Çalışsayan Elemanları Çalışsayan Eleman (OLE) Nesnesi Ekleme**

Aspose.Cells, çalışsayan elemanları çalışsayan eleman koleksiyon listesine eklemek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) sınıfını destekler, çünkü Aspose.Cells'in bir [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject) nesnesi bulunmaktadır. [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), bir çalışsayan elemanı temsil eder. Bazı önemli üyelere sahiptir:

- [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) özelliği, ikon olarak gösterilecek görüntü (ikon) verisini bayt dizisi türünde belirtir. Görüntü, çalışsayan elemanı çalışsayan eleman levhasında göstermek için kullanılacaktır.
- [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) özelliği, bayt dizisi biçimindeki nesne verisini belirtir. Bu veri, çalışsayan eleman simgesine çift tıkladığınızda ilgili programda gösterilecektir.

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Çalışsayan Elemanlar'ın Çalışsayan Elemanları Çıkarma**

Aşağıdaki örnek, bir çalışma kitabından çalışsayan elemanları çıkarmayı göstermektedir. Örnek, mevcut bir XLS dosyasından farklı çalışsayan elemanlar alır ve farklı dosyalar (DOC, XLS, PPT, PDF vb.) çalışsayan elemanın dosya biçim türüne dayalı olarak kaydeder.

Kodu çalıştırdıktan sonra, ilgili Çalışsayan Elemanın biçim türlerine dayalı olarak farklı dosyaları kaydedebiliriz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Gömülü MOL Dosyasının Çıkarılması**

Aspose.Cells, MOL(Moleküler veri dosyası atomlar ve bağlar hakkında bilgi içeren) gibi nadir türdeki nesneleri çıkarmayı destekler. Aşağıdaki kod parçacığı, gömülü MOL dosyasının çıkarılmasını ve bunun diskte [örnek excel dosyası](94896196.xlsx)'ını kullanarak kaydedilmesini göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Gelişmiş Konular**
- [Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme](/cells/tr/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Microsoft Excel kullanarak Aspose.Cells ile Çalışmayan Elemanı Otomatik Yenileme](/cells/tr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Çalışma Kitabından Çalışmayan Elemanları Çıkarma](/cells/tr/net/extract-ole-objects-from-workbook/)
- [Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla](/cells/tr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Ole Nesnesi Olarak Bir WAV Dosyası Eklemek](/cells/tr/net/inserting-a-wav-file-as-an-ole-object/)

{{< app/cells/assistant language="csharp" >}}
