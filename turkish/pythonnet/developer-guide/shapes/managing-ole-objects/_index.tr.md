---
title: OLE Nesneleri Yönetme
type: docs
weight: 50
url: /tr/python-net/managing-ole-objects/
---

## **Giriş**

OLE (Object Linking and Embedding), Microsoft'un bileşik bir belge teknolojisi için çerçevesidir. Kısaca, bileşik bir belge türü her türlü görsel ve bilgi nesnesini içerebilen bir masaüstü görüntüsü gibidir: metin, takvimler, animasyonlar, ses, hareketli video, 3D, sürekli güncellenen haberler, kontroller vb. Her masaüstü nesnesi, bir kullanıcıyla etkileşime girebilir ve aynı zamanda masaüstünde bulunan diğer nesnelerle iletişim kurabilir.

OLE (Object Linking and Embedding), birçok farklı programa destek sağlar ve bir programda oluşturulan içeriğin başka bir programa kullanılmasını sağlar. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Ekleyebileceğiniz içerik türlerini görmek için **Ekle** menüsünde **Nesne**'ye tıklayın. Bilgisayara yüklü olan ve OLE nesneleri destekleyen yalnızca programlar **Nesne türü** kutusunda görünür.

### **Çalışsayan Elemanları Çalışsayan Eleman (OLE) Nesnesi Ekleme**

Aspose.Cells for Python via .NET, OLE nesnelerini çalışma sayfalarına ekleme, çıkarma ve manipüle etme desteği sağlar. Bu nedenle, Aspose.Cells for Python via .NET'de, koleksiyon listesine yeni bir OLE nesnesi eklemek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection) sınıfı bulunur. Diğer bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), bir OLE nesnesini temsil eder. Bazı önemli üyeleri şunlardır:

- [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) özelliği, ikon olarak gösterilecek görüntü (ikon) verisini bayt dizisi türünde belirtir. Görüntü, çalışsayan elemanı çalışsayan eleman levhasında göstermek için kullanılacaktır.
- [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) özelliği, bayt dizisi biçimindeki nesne verisini belirtir. Bu veri, çalışsayan eleman simgesine çift tıkladığınızda ilgili programda gösterilecektir.

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Çalışsayan Elemanlar'ın Çalışsayan Elemanları Çıkarma**

Aşağıdaki örnek, bir çalışma kitabından çalışsayan elemanları çıkarmayı göstermektedir. Örnek, mevcut bir XLS dosyasından farklı çalışsayan elemanlar alır ve farklı dosyalar (DOC, XLS, PPT, PDF vb.) çalışsayan elemanın dosya biçim türüne dayalı olarak kaydeder.

Kodu çalıştırdıktan sonra, ilgili Çalışsayan Elemanın biçim türlerine dayalı olarak farklı dosyaları kaydedebiliriz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Gömülü MOL Dosyasının Çıkarılması**

Aspose.Cells for Python via .NET, MOL gibi sıradışı türdeki nesneleri çıkarma desteği sağlar (atomlar ve bağlar hakkında bilgi içeren Moleküler veri dosyası). Aşağıdaki kod parçacığı, gömülü MOL dosyasını çıkarmayı ve bu [örnek Excel dosyasını](94896196.xlsx) kullanarak diske kaydetmeyi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Gelişmiş Konular**
- [Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme](/cells/tr/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [OLE nesnesini otomatik yenile](/cells/tr/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Çalışma Kitabından Çalışmayan Elemanları Çıkarma](/cells/tr/python-net/extract-ole-objects-from-workbook/)
- [Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla](/cells/tr/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Ole Nesnesi Olarak Bir WAV Dosyası Eklemek](/cells/tr/python-net/inserting-a-wav-file-as-an-ole-object/)

