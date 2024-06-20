---
title: Çalışma Sayfalarında Hücre Denetimleri Eklemek
type: docs
weight: 120
url: /tr/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: Bu makale, GridDesktop içinde çalışma sayfasına denetim eklemenin nasıl yapıldığını tanıtır.
---

{{% alert color="primary" %}} 

Hücre denetimleri aslında çalışma sayfalarına eklenebilecek denetimlerdir. Onları **Hücre Denetimleri** olarak adlandırıyoruz çünkü bu denetimler hücrelerde görüntülenir. Bu konuda bu hücre denetimlerini eklemek ve olaylarını ele almak üzerinde konuşacağız.

{{% /alert %}} 
## **Giriş**
Şu anda, Aspose.Cells.GridDesktop, aşağıdakileri içeren üç tür hücre denetimi eklemeyi desteklemektedir:

- **Düğme**
- **Onay Kutusu**
- **Kombo Kutusu**

Tüm bu denetimler, **HücreDenetim** soyut sınıfından türetilmiştir. Her çalışma sayfası, **Denetimler** adlı bir koleksiyon içerir. Yeni hücre denetimleri eklenip mevcut olanlara bu **Denetimler** koleksiyonunu kullanarak kolayca erişilebilir.

**ÖNEMLİ:** Bir sütunun tüm hücrelerine tek tek eklemek yerine yönetmeniz gerekiyorsa [Sütunlarda Hücre Denetimlerini Yönetme.](/cells/tr/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/) bağlantısına bakabilirsiniz.
### **Düğme Ekleme**
Aspose.Cells.GridDesktop kullanarak çalışma sayfasına düğme eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop denetimini ekleyin
- Herhangi bir istenen **Elektronik Tablo**'na erişin
- **Denetimler** koleksiyonuna **Düğme** ekleyin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


**Düğme** eklerken, hücrenin konumunu (nerede görüntüleneceği), genişliği ve yüksekliği ve düğmenin açıklamasını belirleyebiliriz.
#### **Düğmenin Olaylarını Ele Alma**
**Düğme** denetimini **Çalışma Sayfası**'na eklemeyi tartıştık ancak sadece bir düğmeye sahip olmanın avantajı nedir, eğer kullanamıyorsak. İşte burada, düğmenin olaylarını ele almanın gerekliliği ortaya çıkar.

**Düğme** denetiminin **Tıklama** olayını ele almak için, Aspose.Cells.GridDesktop, **CellButtonClick** olayını geliştiricilere ihtiyaçlarına göre uygulamaları için sağlar. Örneğin, aşağıdaki gibi düğmeye tıklandığında bir mesajı sadece görüntüledik.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Düğme Denetimi İçin Arka Plan Resmi Belirtme**
Düğme denetiminin arkaplan resmini resmini/ görüntüsünü aşağıdaki kodda gösterildiği şekilde etiket/metin ile birlikte belirleyebiliriz:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**ÖNEMLİ:** Hücre denetimlerinin tüm olayları, tetiklenen hücre denetimini içeren **CellControlEventArgs** argümanını içerir (veya sağlar);
### **CheckBox Ekleme**
Aspose.Cells.GridDesktop kullanarak elektronik tabloya bir onay kutusu eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop denetimini ekleyin
- Herhangi bir istenen **Elektronik Tablo**'na erişin
- **CheckBox**'ı **Elektronik Tablo**'nun **Denetimler** koleksiyonuna ekleyin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


**CheckBox** eklerken, kutunun konumunu (nerede görüntüleneceğini) ve onay kutusunun durumunu belirtebiliriz.
#### **CheckBox Olay İşleme**
Aspose.Cells.GridDesktop, onay kutusunun **İşaretlendi**ği durumun değiştiğinde tetiklenen **CellCheckedChanged** olayını sağlar. Geliştiriciler bu olaya kendi gereksinimlerine göre işleyebilir. Örneğin, aşağıdaki kodda onay kutusunun İşaretlendi durumunu göstermek için sadece bir iletiyi gösterdik:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **ComboBox Ekleme**
Aspose.Cells.GridDesktop kullanarak elektronik tabloya bir açılır kutu eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop denetimini ekleyin
- Herhangi bir istenen **Elektronik Tablo**'na erişin
- **ComboBox**'ın tıklanacağında görüntülenecek hücrenin konumunu (açılır kutunun görüntüleneceği konum) ve öğeler/değerler dizisini oluşturun
- **ComboBox**'ı **Elektronik Tablo**'nun **Denetimler** koleksiyonuna konumunu (açılır kutunun görüntüleneceği hücrenin konumu) ve combobox tıklanıldığında görüntülenecek öğeler/değerler dizisini belirterek ekleyin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **ComboBox Olay İşleme**
Aspose.Cells.GridDesktop, açılır kutunun **Seçilen İndeks**i değiştiğinde tetiklenen **CellSelectedIndexChanged** olayını sağlar. Geliştiriciler bu olayı isteklerine göre işleyebilirler. Örneğin, aşağıdaki kodda sadece açılır kutunun **Seçili Öğe** sini göstermek için bir iletiyi gösterdik:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
