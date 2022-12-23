---
title: Aspose.Cells.GridDesktop Olaylarıyla Çalışma
type: docs
weight: 30
url: /tr/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

Olaylar, bir kontrolde veya sınıfta bir değişiklik meydana geldiğinde bildirim göndermek için kullanılır. Aspose.Cells.GridDesktop, denetimde belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılan çeşitli olaylara sahiptir. Bu konu, Aspose.Cells.GridDesktop denetimi tarafından desteklenen tüm olaylara bir giriş sağlar ve bu olayların nasıl işlenebileceğini açıklar.

{{% /alert %}} 
## **Giriş**
Aspose.Cells.GridDesktop kontrolü, belirli olaylar tetiklendiğinde işlemlerin gerçekleştirilmesi için daha fazla kontrol sağlayan birkaç olayı destekler. Aspose.Cells.GridDesktop denetimi tarafından desteklenen olayların tam listesi aşağıdadır.

{{% alert color="primary" %}} 

Bu liste, Control sınıfından Aspose.Cells.GridDesktop tarafından devralınan olayları içermez.

{{% /alert %}} 

|**Olaylar**|**Açıklama**|
|:- |:- |
|Hesaplamadan Önce|Çalışma kitabında formülü hesaplamadan önce oluşur.|
|DosyaYüklemeden Önce|Çalışma kitabı dosyadan yüklenmeden önce gerçekleşir.|
|Sütun BaşlığıTıklama|Sütun başlığı tıklandığında gerçekleşir.|
|Sütun BaşlığıDoubleClick|Sütun başlığına çift tıklandığında gerçekleşir.|
|Hücre Verileri Değiştirildi|Bir Grid hücresinin içindeki veri veya değer değiştirildiğinde gerçekleşir. Bu olay, bir hücrenin değeri, bir GridCell'in Value özelliği veya SetCellValue yöntemi kullanılarak programlı olarak değiştirilirse de tetiklenebilir.|
|HücreDüğmesiTıklama|Hücre düğmesine tıklandığında gerçekleşir.|
|Hücre Kontrol EdildiDeğiştirildi|Hücre onay kutusunun Checked özelliği değiştirildiğinde gerçekleşir.|
|CellSelectedIndexChanged|Hücre açılan kutusunun SelectedIndex özelliği değiştirildiğinde gerçekleşir.|
|Hücre Tıklaması|Bir Izgara hücresine tıklandığında gerçekleşir.|
|HücreDoubleClick|Bir Grid hücresi çift tıklandığında gerçekleşir.|
|Hücre Tuşuna Basıldı|Bir hücre odağa sahipken bir tuşa basıldığında gerçekleşir. CellKeyPressed olayı için bir olay işleyici oluşturmak istiyorsanız, GridDesktop kontrolünün key olayını işlemesini engellemek için CellKeyEventArgs bağımsız değişkeninin Handled özelliğini true olarak ayarlayın.|
|Sütun Ekleme Sonrası|Bir sütun eklendiğinde gerçekleşir. Aspose.Cells.GridDesktop.WorksheetEventArgs bağımsız değişkeninin Index özelliğini kullanarak sütun dizinini alabilirsiniz.|
|Satır Ekledikten Sonra|Bir satır eklendiğinde gerçekleşir. Aspose.Cells.GridDesktop.WorksheetEventArgs bağımsız değişkeninin Index özelliğini kullanarak satır dizinini alabilirsiniz.|
|BaşarısızYükDosyası|Çalışma kitabı yüklenemediğinde oluşur.|
|BitirHesapla|Çalışma kitabında formülü hesapladıktan sonra oluşur.|
|BitirYükDosyası|Çalışma kitabı yüklendiğinde gerçekleşir.|
|OdaklanmışHücreDeğiştirildi|Bir hücrenin odağı değiştiğinde gerçekleşir.|
|RowHeaderClick|Satır başlığı tıklandığında gerçekleşir.|
|RowHeaderDoubleClick|Satır başlığına çift tıklandığında gerçekleşir.|
|RowColumnHiddenChanged|Satır veya sütun gizli durumu değiştirildiğinde gerçekleşir.|
|SelectedSheetIndexChanged|Kullanıcı yeni bir çalışma sayfası seçtiğinde, yani seçilen sayfa bir çalışma sayfasından diğerine değiştiğinde gerçekleşir. GridDesktop denetiminin ActiveSheetIndex özelliği değişirse, bu olay programlı olarak da tetiklenebilir.|
## **Izgara Olaylarını Yönetme**
Belirli bir olay tetiklendiğinde belirli bir işlemi gerçekleştirmek için bir olay işleyici oluşturun. Bir olay işleyici, belirli bir olay tetiklendiğinde belirli bir görevi gerçekleştirir. Aşağıda, Visual Studio.NET kullanılarak basit bir Grid olayını işlemek için bir olay işleyicisi ayarlanmıştır.

**Adım 1: Aspose.Cells.GridDesktop Control Olayını Seçme**

1. Visual Studio'da Aspose.Cells.GridDesktop denetimini seçin ve denetimini açın.**Özellikler** diyalog
1.  Tıkla**Olaylar** sekme.
1.  Bir etkinlik seçin. (bu örnek için,**Hücre Tıklaması** olay seçilir).

**2. Adım: Olay İşleyici Oluşturma**

1.  Seçilen bir olayı çift tıklatın.**Özellikler** diyalog
1. Olay çift tıklandığında, Visual Studio.NET tarafından bir olay işleyicisi oluşturulur. Aşağıda, GridControl Denetimi için bir olayın oluşturulduğunu gösteren, tasarımcı tarafından oluşturulmuş kod yer almaktadır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 Şimdi olay işleyici içinde istenen işlemi gerçekleştirmek için kod ekleyin. Bu örnek için, bildirimler için bir mesaj kutusu görüntüleyen bir kod satırı ekledik.
Visual Studio'nun GridDesktop denetiminin CellClick olayına eklediği olay işleyicisine bir göz atın. Aşağıdaki kod gibi bir şey görünecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**3. Adım: Uygulamayı Çalıştırma**

1. Uygulamayı oluşturun ve çalıştırın.
1. Bir ızgara hücresi tıklandığında, "Cell Tıklandı" mesajını içeren bir mesaj kutusu görünür.
