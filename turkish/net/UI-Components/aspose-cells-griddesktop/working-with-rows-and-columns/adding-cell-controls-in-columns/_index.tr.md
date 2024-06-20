---
title: Kolonlara Hücre Kontrolleri Ekleme
type: docs
weight: 90
url: /tr/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: Bu makale, GridDesktop ta sütunda kontrol ekleme nedenine tanıtır.
---

{{% alert color="primary" %}} 

Daha sonraki tartışmalarımızda, çalışma sayfasında hücre kontrolleri eklemek ve yönetmek hakkında konuştuk. Ancak, bu yaklaşımları kullanarak, tek tek tek hücrelere hücre kontrolleri ekleyebiliriz. Bir veya daha fazla sütunun tüm hücrelerine hücre kontrolleri eklemek isteyen biri ne olacak? Bu durumlarda, geliştiricilerin çabalarını azaltmak için Aspose.Cells.GridDesktop, sütun bazında hücre kontrolleri eklemenin özelliğini sağlar. Bu, geliştiricilerin sadece istenen bir sütunu seçebileceklerini ve herhangi bir hücre kontrolünü belirtebileceklerini anlamına gelir. Belirtilen hücre kontrolü belirtilen sütunun tüm hücrelerine eklenir. Bu özelliği nasıl kullanabileceğimizi görelim.

{{% /alert %}} 
## **Giriş**
Şu anda, Aspose.Cells.GridDesktop, aşağıdakileri içeren üç tür hücre denetimi eklemeyi desteklemektedir:

- **Düğme**
- **Onay Kutusu**
- **Kombo Kutusu**

Bu kontrollerin hepsi, **CellControl** soyut sınıfından türetilmiştir.

**ÖNEMLİ:** Tüm sütunun değil de tek bir hücreye hücre kontrolleri eklemek istiyorsanız, [Tablolarda Hücre Kontrolleri Ekleme](/cells/tr/net/adding-cell-controls-in-worksheets/) bölümüne başvurabilirsiniz.
### **Düğme Ekleme**
Aspose.Cells.GridDesktop kullanarak bir sütuna düğmeler eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Çalışsayfası**'nın herhangi belirtilen **Sütunu**'na **Düğme** ekleyin

**NOT:** **Düğme** eklerken, düğmenin genişliği, yüksekliği ve yazısı belirtilebilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


Yukarıdaki kod parçası, belirtilen sütunun tüm hücrelerine düğmeler ekler. Belirli bir sütun hücresi seçildiğinde, bir düğme görünür hale gelir. Düğmelerin olay işlemleri hakkında daha fazla bilgi için lütfen [Düğme Kontrolünün Olay İşlemi](/cells/tr/net/adding-cell-controls-in-worksheets/#event-handling-of-button) bölümüne bakın
### **CheckBox Ekleme**
Aspose.Cells.GridDesktop kullanarak bir sütuna onay kutuları eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Çalışsayfası**'nın herhangi belirtilen **Sütunu**'na **Onay Kutusu** ekleyin

**NOT:** **CheckBox** eklerken, kutunun durumunu da belirleyebiliriz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


Yukarıdaki kod parçacığı, belirtilen sütunun tüm hücrelerine onay kutuları ekler. Onay kutularının olay işleme hakkında daha fazla bilgi için [CheckBox Kontrolünün Olay İşleme Bölümüne](/cells/tr/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox) başvurun.
### **ComboBox Ekleme**
Aspose.Cells.GridDesktop kullanarak bir sütuna combobox eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **ComboBox** için ekleyeceğiniz öğelerin (veya değerlerin) bir dizisini oluşturun
- **Çalışsayfa**'nın belirtilen **Sütunu**na **ComboBox** (öğeler veya değerler içeren) ekleyin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


Yukarıdaki kod parçacığı, belirtilen sütunun tüm hücrelerine combobox ekler. Belirli bir sütunun herhangi bir hücresi seçildiğinde, bir combobox görünür hale gelir. Comboboxların olay işleme hakkında daha fazla bilgi için [ComboBox Kontrolünün Olay İşleme Bölümüne](/cells/tr/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox) başvurun.
