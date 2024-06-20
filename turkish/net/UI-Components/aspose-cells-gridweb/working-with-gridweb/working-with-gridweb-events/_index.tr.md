---
title: GridWeb Olayları İle Çalışmak
type: docs
weight: 70
url: /tr/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb, olaylar, olay
description: Bu makale, GridWeb de çeşitli olaylarla çalışmayı nasıl tanıttığınızı içeriyor.
---

{{% alert color="primary" %}} 

Tüm programcılar olayları ve amaçlarını bilmelidir. Olaylar, bir kontrol veya sınıfta meydana gelebilecek değişikliklerin bildirimlerini göndermek için kullanılır. Aspose.Cells.GridWeb'in belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılabilecek çeşitli olayları vardır.

Bu konu, Aspose.Cells.GridWeb kontrolü tarafından desteklenen tüm olaylara giriş yapar ve bu olayları nasıl ele alacağınıza dair bazı detaylar içerir.

{{% /alert %}} 
## **Olaylarla Çalışma**
### **Olaylara Giriş**
Aspose.Cells.GridWeb kontrolü, kontrolde belirli olaylar tetiklendiğinde belirli işlemleri gerçekleştirmek için daha fazla kontrol sağlayan birkaç olayı destekler. Aspose.Cells.GridWeb kontrolü tarafından desteklenen olayların tam listesi aşağıda bulunabilir.

{{% alert color="primary" %}} 

Bu liste Aspose.Cells.GridWeb'in Control sınıfından devralınan olayları içermez.

{{% /alert %}} 

|**Olaylar** |**Açıklama** |
| :- | :- |
|CellCommand |Hücrenin komut bağlantısına tıklandığında oluşur. Bu olay tetiklendiğinde, parametre e.Argument komutun adını sağlar. |
|CellDoubleClick |Hücre çift tıklandığında oluşur. |
|CellError |Hücrenin girdi değerinde bir hata varsa oluşur. |
|ColumnDeleted |Kullanıcı bir sütunu istemci tarafı menüsünü kullanarak bir çalışma sayfasından sildiğinde oluşur. |
|ColumnDeleting |Kullanıcı bir sütunu istemci tarafı menüsü kullanarak bir çalışma sayfasından silmeye çalıştığında oluşur. |
|ColumnDoubleClick |Sütun başlığı çift tıklandığında oluşur. |
|ColumnInserted |Kullanıcı tarafından bir sütun client-side menüsü kullanılarak çalışma sayfasına eklenildiğinde meydana gelir. |
|CustomCommand |Kullanıcı özel bir komut düğmesine tıkladığında meydana gelir. |
|LoadCustomData |Kontrolün EnableSession özelliği false olarak ayarlandığında ve çalışma sayfası verilerini yüklemesi gerektiğinde meydana gelir. Bu olayı oturumsuz modda işleyebilirsiniz, çalışma sayfası verilerini bir dosyadan veya veritabanından yüklemek için. |
|PageIndexChanged |Kontrolün sayfa dizini değiştirildiğinde meydana gelir. |
|RowDeleted |Kullanıcı tarafından bir satır client-side menüsü kullanılarak çalışma sayfasından silindiğinde meydana gelir. |
|RowDeleting |Kullanıcı bir satırı client-side menüsü kullanarak çalışma sayfasından silmeye çalıştığında meydana gelir. |
|RowDoubleClick |Satır başlığı çift tıklandığında meydana gelir. |
|RowInserted |Kullanıcı bir satır client-side menüsü kullanarak çalışma sayfasına eklediğinde meydana gelir. |
|SaveCommand |**Kaydet** düğmesine tıklandığında meydana gelir. |
|SheetDataUpdated |Kontrol gönderilen verileri yüklediğinde ve çalışma sayfası verilerini güncellediğinde meydana gelir. |
|SheetTabClick |Sayfa sekmesine tıklandığında meydana gelir. |
|SubmitCommand |**Gönder** düğmesine tıklandığında meydana gelir. |
|UndoCommand |**Geri Al** düğmesine tıklandığında meydana gelir. |
|AjaxCallFinished |Kontrolün AJAX güncellemesi tamamlandığında meydana gelir. (EnableAJAX true olarak ayarlanmalıdır). |
|CellModifiedOnAjax |AJAX çağrısında hücre değiştirildiğinde meydana gelir. |
|OnAfterColumnFilter |Bir sütuna uygulandıktan sonra filtrelenmişse meydana gelir. |
|OnBeforeColumnFilter |Bir sütuna filtre uygulanmadan önce meydana gelir. |
## **Grid Olaylarını İşleme**
Belirli bir olay tetiklendiğinde belirli bir işlemi gerçekleştirmek için bir olay işleyici oluşturmamız gerekiyor. Bir olay işleyicisi, belirli bir olay tetiklendiğinde istenen görevi gerçekleştirir. Aşağıdaki adımlar, Visual Studio kullanarak basit bir grid olayını nasıl işleyeceğinizi göstermektedir.
### **Adım 1: Aspose.Cells.GridWeb Kontrolünün Bir Olayını Seçme**
1. Aspose.Cells.GridWeb kontrolünü seçin ve sağ taraftaki Özellikler iletişim kutusunu açın.
1. **Olaylar Sekmesi** düğmesine tıklayın.
1. Bir olay seçin.
   Bu örnekte, SaveCommand olayı seçilmiştir.
### **Adım 2: Olay İşleyicisi Oluşturma**
1. Özellikler iletişim kutusunda bir olaya çift tıklayın. 

   Seçilen bir olaya çift tıklayın 

![todo:image_alt_text](working-with-gridweb-events_1.png)




Olay çift tıklandığında, Visual Studio tarafından otomatik olarak bir olay işleyicisi oluşturulur. 

Visual Studio tarafından oluşturulan bir olay işleyicisi 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Bir işlem gerçekleştirmek üzere kod ekleyin olay işleyicisine.

Burada, **Kaydet** düğmesine tıklandığında ızgara içeriğini bir Excel dosyasına kaydeden tek bir kod satırı eklenmiştir.

Daha fazla bilgi için, imleci kodların üzerine getirin, ardından Visual Studio'nun GridWeb'in SaveCommand olayına bir olay işleyici eklemek için yeterince akıllı olduğunu fark edeceksiniz.
### **Adım 3: Uygulamanızı Çalıştırma**
1. Uygulamayı oluşturun ve çalıştırın.
1. **Kaydet** düğmesine tıklayın.

Izgara içeriği bir Excel dosyasına kaydedilir. 

**Uygulama çalışma modunda** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
