---
title: Cell Kontrollerini Sütunlara Ekleme
type: docs
weight: 90
url: /tr/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Daha sonraki tartışmalarımızda, çalışma sayfasına hücre kontrolleri ekleme ve yönetme hakkında tartıştık. Ancak, bu yaklaşımları kullanarak, tek tek hücrelere hücre kontrolleri ekleyebiliriz. Birisi bir veya daha fazla sütunun tüm hücrelerine hücre kontrolleri eklemek isterse ne olur? Bu gibi durumlarda, geliştiricilerin çabalarını azaltmak için Aspose.Cells.GridDesktop, sütun bazında hücre kontrolleri ekleme özelliği sağlar. Bu, geliştiricilerin yalnızca istenen bir sütunu seçebileceği ve herhangi bir hücre kontrolünü belirtebileceği anlamına gelir. Belirtilen hücre denetimi, belirtilen sütunun tüm hücrelerine eklenecektir. Bu özelliği nasıl kullanabileceğimize bakalım.

{{% /alert %}} 
## **giriiş**
Şu anda Aspose.Cells.GridDesktop, aşağıdakileri içeren üç tür hücre denetimi eklemeyi destekler:

- **Buton**
- **Onay Kutusu**
- **Açılan kutu**

 Bu kontrollerin tümü soyut bir sınıftan türetilmiştir,**Hücre Kontrolü**.

**ÖNEMLİ:** Tüm sütun yerine tek bir hücreye hücre kontrolleri eklemek istiyorsanız, o zaman başvurabilirsiniz.[Çalışma Sayfalarına Cell Kontrolleri Ekleme.](/cells/tr/net/adding-cell-controls-in-worksheets/)
### **Ekleme Düğmesi**
Aspose.Cells.GridDesktop kullanarak bir sütuna düğme eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Ekle**Buton** belirtilen herhangi birine**Kolon** arasında**Çalışma kağıdı**

**NOT:** eklerken**Buton**, butonun genişliğini, yüksekliğini ve başlığını belirtebiliriz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 Yukarıdaki kod parçacığı, belirtilen sütunun tüm hücrelerine düğmeler ekler. Belirli bir sütunun herhangi bir hücresi seçildiğinde, bir düğme görünür hale gelir. Düğmelerin olay işlemesi hakkında daha fazla bilgi için lütfen şuraya bakın:[Düğme Denetiminin Olay İşleme.](/cells/tr/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Onay Kutusu Ekleme**
Aspose.Cells.GridDesktop kullanarak bir sütuna onay kutuları eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Ekle**Onay Kutusu** belirtilen herhangi birine**Kolon** arasında**Çalışma kağıdı**

**NOT:** eklerken**Onay Kutusu**, onay kutusunun durumunu da belirtebiliriz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 Yukarıdaki kod parçacığı, belirtilen sütunun tüm hücrelerine onay kutuları ekler. Onay kutularının olay işlemesi hakkında daha fazla bilgi için lütfen şuraya bakın:[CheckBox Denetiminin Olay İşleme.](/cells/tr/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **ComboBox ekleme**
Aspose.Cells.GridDesktop kullanarak bir sütuna açılan kutu eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Eklenecek bir dizi öğe (veya değer) oluşturun**Açılan kutu**
-  Ekle**Açılan kutu** (öğeleri veya değerleri içeren) belirtilen herhangi bir**Kolon** arasında**Çalışma kağıdı**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 Yukarıdaki kod parçacığı, belirtilen sütunun tüm hücrelerine açılan kutular ekler. Belirli bir sütunun herhangi bir hücresi seçildiğinde, bir açılan kutu görünür hale gelir. Birleşik giriş kutularının olay işlemesi hakkında daha fazla bilgi için lütfen bkz.[Bir ComboBox Denetiminin Olay İşleme.](/cells/tr/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
