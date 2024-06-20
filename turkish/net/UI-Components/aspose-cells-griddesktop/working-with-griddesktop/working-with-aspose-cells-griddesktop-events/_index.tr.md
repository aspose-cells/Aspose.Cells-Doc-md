---
title: Aspose.Cells.GridDesktop Olayları İle Çalışma
type: docs
weight: 30
url: /tr/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, olay, olaylar
description: Bu makale, GridDesktop taki olayları nasıl kullanacağınızı tanıtıyor.
---

{{% alert color="primary" %}} 

Olaylar, bir kontrolün veya sınıfın bir değişiklik meydana geldiğinde bildirim göndermek için kullanılır. Aspose.Cells.GridDesktop'ın, denetimde belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılan birkaç olayı bulunmaktadır. Bu konu, Aspose.Cells.GridDesktop kontrolü tarafından desteklenen tüm olaylara bir giriş sağlar ve bu olayların nasıl ele alınacağını açıklar.

{{% /alert %}} 
## **Giriş**
Aspose.Cells.GridDesktop kontrolü, belirli olayların tetiklendiğinde işlemlerin gerçekleştirilmesi için daha fazla kontrol sağlayan birkaç olayı destekler. Aşağıda Aspose.Cells.GridDesktop kontrolü tarafından desteklenen olayların tam listesi bulunmaktadır.

{{% alert color="primary" %}} 

Bu liste, Aspose.Cells.GridDesktop tarafından Control sınıfından devralınan olayları içermez.

{{% /alert %}} 

|**Olaylar**|**Açıklama**|
| :- | :- |
|BeforeCalculate| Çalışma kitabında formülün hesaplanmadan önce oluşur.|
|BeforeLoadFile| Dosyadan çalışma kitabı yüklendiğinde oluşur.|
|ColumnHeaderClick|Sütun başlığı tıklandığında oluşur.|
|ColumnHeaderDoubleClick|Sütun başlığı çift tıklandığında oluşur.|
|CellDataChanged|Grid hücresi içindeki veri veya değer değiştiğinde oluşur. Bu olay, ayrıca bir hücrenin değeri, GridCell'in Value özelliğini veya SetCellValue yöntemini kullanarak programlı şekilde değiştirildiğinde tetiklenebilir.|
|CellButtonClick|Hücre düğmesi tıklandığında oluşur.|
|CellCheckedChanged|Hücre onay kutusunun Kontrol edilme durumu değiştiğinde oluşur.|
|CellSelectedIndexChanged|Hücre combo kutusunun SeçilenEndeks özelliği değiştiğinde oluşur.|
|CellClick|Grid hücresi tıklandığında oluşur.|
|CellDoubleClick|Izgara hücresi çift tıklandığında oluşur.|
|CellKeyPressed|Hücre odaklıyken bir tuşa basıldığında oluşur. Bir CellKeyPressed olayı için olay işleyici oluşturmak istiyorsanız, önlemek için CellKeyEventArgs argümanının Handled özelliğini true olarak ayarlayın.
|AfterInsertColumns|Bir sütun eklendiğinde oluşur. Aspose.Cells.GridDesktop.WorksheetEventArgs argümanının Index özelliğini kullanarak sütun endeksini alabilirsiniz.|
|AfterInsertRows|Bir satır eklendiğinde oluşur. Aspose.Cells.GridDesktop.WorksheetEventArgs argümanının Index özelliğini kullanarak satır endeksini alabilirsiniz.|
|FailLoadFile|Çalışma kitabı yüklenemediğinde oluşur.|
|FinishCalculate|Çalışma kitabında formül hesaplandıktan sonra oluşur.|
|FinishLoadFile|Çalışma kitabı yüklendiğinde oluşur.|
|FocusedCellChanged|Hücrenin odaklanması her değiştiğinde oluşur.|
|RowHeaderClick|Satır başlığı tıklandığında oluşur.|
|RowHeaderDoubleClick|Satır başlığı çift tıklandığında oluşur.|
|RowColumnHiddenChanged|Satır veya sütun gizlilik durumu değiştiğinde oluşur.|
|SelectedSheetIndexChanged|Kullanıcı yeni bir çalışma sayfasını seçtiğinde oluşur. Bu olay, ayrıca GridDesktop kontrolünün ActiveSheetIndex özelliği değiştiğinde programlı olarak da tetiklenebilir.
## **Grid Olaylarını İşleme**
Belirli bir olay tetiklendiğinde belirli bir işlem gerçekleştirmek için bir olay işleyici oluşturun. Bir olay işleyicisi, belirli bir olay tetiklendiğinde belirli bir görevi gerçekleştirir. Aşağıda, Visual Studio.NET'i kullanarak basit bir Grid olayını işlemek için bir olay işleyicisi kurulmuştur.

**Adım 1: Aspose.Cells.GridDesktop Kontrolünün Olayını Seçme**

1. Visual Studio'da Aspose.Cells.GridDesktop kontrolünü seçin ve **Özellikler** iletişim kutusunu açın.
1. **Olaylar** sekmesine tıklayın.
1. Bir olay seçin. (bu örnekte, **CellClick** olayı seçilmiştir).

**Adım 2: Bir Olay İşleyici Oluşturma**

1. Seçilen etkinliğin **Özellikler** iletişim kutusunda iki kez tıklayın.
1. Etkinlik çift tıklandığında Visual Studio.NET tarafından bir olay işleyici oluşturulur. Aşağıdaki tasarımcı tarafından oluşturulan kod bir olayın GridControl Kontrolü için oluşturulduğunu göstermektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Şimdi, olay işleyicisi içinde istenen işlemi gerçekleştirmek için kod ekleyin. Bu örnekte, bildirimler için bir ileti kutusu görüntüleyen bir kod satırı ekledik. 
Visual Studio'nun GridDesktop kontrolünün CellClick olayına eklediği olay işleyicisine bakın. Aşağıdaki gibi görünecek.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Adım 3: Uygulamayı Çalıştırma**

1. Uygulamayı oluşturun ve çalıştırın.
1. Bir hücreye tıklandığında, 'Hücre Tıklandı' ileti kutusu görünür.
