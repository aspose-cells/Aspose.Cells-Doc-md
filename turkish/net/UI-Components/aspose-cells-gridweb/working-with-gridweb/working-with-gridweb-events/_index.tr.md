---
title: GridWeb Events ile Çalışma
type: docs
weight: 70
url: /tr/net/working-with-gridweb-events/
---
{{% alert color="primary" %}} 

Tüm programcılar olaylara ve amaçlarına aşina olmalıdır. Olaylar, bir kontrolde veya sınıfta meydana gelebilecek değişikliklerin bildirimlerini göndermek için kullanılır. Aspose.Cells.GridWeb, kontrolde belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılabilecek birkaç olaya sahiptir.

Bu konu, Aspose.Cells.GridWeb denetimi tarafından desteklenen tüm olaylara bir giriş ve bu olayların nasıl ele alınacağına ilişkin bazı ayrıntılar sağlar.

{{% /alert %}} 
## **Izgara Olaylarıyla Çalışma**
### **Izgara Olaylarına Giriş**
Aspose.Cells.GridWeb kontrolü, kontrolde belirli olaylar tetiklendiğinde işlemlerin gerçekleştirilmesi için daha fazla kontrol sağlayan birkaç olayı destekler. Aspose.Cells.GridWeb denetimi tarafından desteklenen olayların tam listesi aşağıda bulunabilir.

{{% alert color="primary" %}} 

Bu liste, Control sınıfından Aspose.Cells.GridWeb tarafından devralınan olayları içermez.

{{% /alert %}} 

|**Olaylar** |**Tanım** |
|:- |:- |
| Hücre Komutu| Bir hücrenin komut köprüsü tıklandığında gerçekleşir. Bu olay başlatıldığında, e.Argument parametresi komutun adını sağlar.|
| HücreDoubleClick| Hücre çift tıklandığında gerçekleşir.|
| hücre hatası| Bir hücrenin giriş değerinde bir hata olduğunda gerçekleşir.|
| SütunSilindi|Kullanıcı, istemci yan menüsünü kullanarak bir çalışma sayfasından bir sütunu sildiğinde gerçekleşir.|
| Sütun Silme| Bir kullanıcı, istemci yan menüsünü kullanarak bir çalışma sayfasından bir sütunu silmeye çalıştığında gerçekleşir.|
| SütunDoubleClick| Sütun başlığına çift tıklandığında gerçekleşir.|
| Sütun Eklendi| Kullanıcı, istemci yan menüsünü kullanarak çalışma sayfasına bir sütun eklediğinde gerçekleşir.|
| Özel Komut| Bir kullanıcı özel bir komut düğmesini tıklattığında gerçekleşir.|
| Özel Verileri Yükle| Denetimin EnableSession özelliği false olarak ayarlandığında ve çalışma sayfası verilerini yüklemesi gerektiğinde gerçekleşir. Çalışma sayfası verilerini bir dosyadan veya veritabanından yüklemek için bu olayı oturumsuz modda işleyebilirsiniz.|
| Sayfa DiziniDeğişti| Denetimin sayfa sayfası dizini değiştirildiğinde gerçekleşir.|
| SatırSilindi| Kullanıcı, istemci yan menüsünü kullanarak bir çalışma sayfasından bir satırı sildiğinde gerçekleşir.|
| Satır Silme| Bir kullanıcı, istemci yan menüsünü kullanarak bir çalışma sayfasından bir satırı silmeye çalıştığında gerçekleşir.|
| SatırDoubleClick|Satır başlığına çift tıklandığında gerçekleşir.|
| Satır Eklendi| Bir kullanıcı, istemci yan menüsünü kullanarak çalışma sayfasına bir satır eklediğinde gerçekleşir.|
| Komutu Kaydet| Ne zaman oluşur**Kaydetmek** butonu tıklanır.|
| SheetDataGüncellendi| Denetim deftere nakledilen verileri yüklediğinde ve çalışma sayfası verilerini güncelleştirdiğinde gerçekleşir.|
| SheetSekmeClick| Bir sayfa sekmesi tıklandığında gerçekleşir.|
| Komut Gönder| Ne zaman oluşur**Göndermek** butonu tıklanır.|
| Komutu Geri Al| Ne zaman oluşur**Geri alma** butonu tıklanır.|
| AjaxCallBitti| Kontrolün AJAX güncellemesi bittiğinde tetiklenir. (EnableAJAX, true olarak ayarlanmalıdır).|
| CellModifiedOnAjax| AJAX çağrısında hücre değiştirildiğinde tetiklenir.|
| OnAfterColumnFilter| Filtre bir sütuna uygulandıktan sonra tetiklenir.|
| OnBeforeColumnFilter| Filtre bir sütuna uygulanmadan önce tetiklenir.|
## **Izgara Olaylarını Yönetme**
Belirli bir olayı tetikleme konusunda belirli bir işlem gerçekleştirmek için bir olay işleyici oluşturmamız gerekir. Bir olay işleyici, belirli bir olay tetiklendiğinde istenen görevi gerçekleştirir. Aşağıda gösterilen adımlar, Visual Studio kullanılarak basit bir ızgara olayının nasıl işleneceğini gösterir.
### **Adım 1: Aspose.Cells.GridWeb Control Olayını Seçme**
1. Aspose.Cells.GridWeb kontrolünü seçin ve sağ taraftaki Özellikler iletişim kutusunu açın.
1.  Tıkla**Etkinlikler Sekmesi** buton.
1. Bir etkinlik seçin.
 Bu örnek için, SaveCommand olayı seçilmiştir.
### **2. Adım: Olay İşleyici Oluşturma**
1.  Özellikler iletişim kutusunda bir olayı çift tıklayın.

   **Seçilen bir olaya çift tıklama** 

![yapılacaklar:resim_alternatif_Metin](working-with-gridweb-events_1.png)




 Olay çift tıklandığında, Visual Studio tarafından otomatik olarak bir olay işleyicisi oluşturulur.

**Visual Studio tarafından oluşturulan bir olay işleyicisi** 

![yapılacaklar:resim_alternatif_Metin](working-with-gridweb-events_2.png)




1. Olay işleyici içinde bazı eylemler gerçekleştirmek için kod ekleyin.

 Burada, ızgara içeriğini bir Excel dosyasına kaydeden tek bir kod satırı**Kaydetmek** butonu tıklandığında eklendi.

Daha fazla bilgi almak için, bazı kodları görmek üzere imleci yukarıya hareket ettirin, ardından Visual Studio'nun GridWeb'in SaveCommand olayına bir olay işleyicisi eklemek için yeterince akıllı olduğunu göreceksiniz.
### **3. Adım: Uygulamanızı Çalıştırma**
1. Uygulamayı oluşturun ve çalıştırın.
1.  Tıklamak**Kaydetmek**.

 Izgara içeriği bir Excel dosyasına kaydedilir.

**Çalışma modunda uygulama** 

![yapılacaklar:resim_alternatif_Metin](working-with-gridweb-events_3.png)
