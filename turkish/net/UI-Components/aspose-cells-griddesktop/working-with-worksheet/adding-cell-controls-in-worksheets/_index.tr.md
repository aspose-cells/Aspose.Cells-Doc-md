---
title: Çalışma Sayfalarına Cell Kontrolleri Ekleme
type: docs
weight: 120
url: /tr/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 Cell kontrolleri aslında çalışma sayfalarına eklenebilen kontrollerdir. biz onlara diyoruz**Cell Kontroller** çünkü bu kontroller hücrelerde görüntülenir. Bu konuda, bu hücre kontrollerinin olaylarını ekleme ve işleme hakkında tartışacağız.

{{% /alert %}} 
## **giriiş**
Şu anda Aspose.Cells.GridDesktop, aşağıdakileri içeren üç tür hücre denetimi eklemeyi destekler:

- **Buton**
- **Onay Kutusu**
- **Açılan kutu**

Bu kontrollerin tümü soyut bir sınıftan türetilmiştir,**Hücre Kontrolü**. Her çalışma sayfası bir koleksiyon içerir**Kontroller**Bu kullanılarak yeni hücre kontrolleri eklenebilir ve mevcut olanlara erişilebilir.**Kontroller**kolayca toplayın.

**ÖNEMLİ:**Tek tek eklemek yerine bir sütunun tüm hücrelerine hücre kontrolleri eklemek istiyorsanız, o zaman başvurabilirsiniz.[Cell Kontrollerini Sütunlarda Yönetme.](/cells/tr/net/adding-cell-controls-in-worksheets/)
### **Ekleme Düğmesi**
Aspose.Cells.GridDesktop kullanarak çalışma sayfasına düğme eklemek için lütfen aşağıdaki adımları izleyin:

- Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
- İstediğiniz herhangi birine erişin**Çalışma kağıdı**
- Ekle**Buton**için**Kontroller**koleksiyonu**Çalışma kağıdı**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


eklerken**Buton**, hücrenin konumunu (nerede görüntüleneceğini), genişliğini ve yüksekliğini ve düğmenin başlığını belirtebiliriz.
#### **Düğmenin Olay İşleme**
ekleme hakkında konuştuk**Buton**kontrol etmek**Çalışma kağıdı**ancak kullanamıyorsak, çalışma sayfasında bir düğme olmasının avantajı nedir? Bu nedenle, düğmenin olay işleme ihtiyacı burada ortaya çıkıyor.

işlemek için**Tıklamak**olayı**Buton**kontrol, Aspose.Cells.GridDesktop sağlar**HücreDüğmesiTıklama**geliştiriciler tarafından ihtiyaçlarına göre uygulanması gereken olay. Örneğin, aşağıda gösterildiği gibi, düğmeye tıklandığında bir mesaj görüntüledik:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Düğme Denetimi için Arka Plan Görüntüsü Belirtme**
Aşağıdaki kodda gösterildiği gibi etiketi/metni ile düğme kontrolü için arka plan resmini/resmini ayarlayabiliriz:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**ÖNEMLİ:**Hücre kontrollerinin tüm olayları bir**CellControlEventArgs**hücre kontrolünü içeren (olayı tetiklenen) hücrenin satır ve sütun numaralarını sağlayan bağımsız değişken.
### **Onay Kutusu Ekleme**
Aspose.Cells.GridDesktop kullanarak çalışma sayfasına bir onay kutusu eklemek için lütfen aşağıdaki adımları izleyin:

- Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
- İstediğiniz herhangi birine erişin**Çalışma kağıdı**
- Ekle**Onay Kutusu**için**Kontroller**koleksiyonu**Çalışma kağıdı**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


eklerken**Onay Kutusu**, hücrenin konumunu (nerede görüntüleneceğini) ve onay kutusunun durumunu belirtebiliriz.
#### **CheckBox Olay İşleme**
Aspose.Cells.GridDesktop sağlar**Hücre Kontrol EdildiDeğiştirildi**olduğunda tetiklenen olay**Kontrol**onay kutusunun durumu değiştirilir. Geliştiriciler bu olayı gereksinimlerine göre işleyebilir. Örneğin, göstermek için az önce bir mesaj görüntüledik.**Kontrol**aşağıdaki koddaki onay kutusunun durumu:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **ComboBox ekleme**
Aspose.Cells.GridDesktop kullanarak çalışma sayfasına açılan kutu eklemek için lütfen aşağıdaki adımları izleyin:

- Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
- İstediğiniz herhangi birine erişin**Çalışma kağıdı**
- Eklenecek bir dizi öğe (veya değer) oluşturun**Açılan kutu**
- Ekle**Açılan kutu**için**Kontroller**koleksiyonu**Çalışma kağıdı**hücrenin konumunu (birleşik kutunun görüntüleneceği yer) ve açılan kutu tıklandığında görüntülenecek öğeleri/değerleri belirterek



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **ComboBox Olay İşleme**
Aspose.Cells.GridDesktop sağlar**CellSelectedIndexChanged**olduğunda tetiklenen olay**Seçilmiş Dizin**açılan kutunun şekli değişti. Geliştiriciler bu olayı kendi isteklerine göre halledebilirler. Örneğin, göstermek için az önce bir mesaj görüntüledik.**Seçilen öğe**açılan kutunun:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
