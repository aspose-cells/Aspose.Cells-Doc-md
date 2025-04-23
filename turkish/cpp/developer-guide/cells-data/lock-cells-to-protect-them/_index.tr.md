---
title: C++ ile Hücreleri Kilitleyerek Koruma Nasıl Sağlanır
linktitle: Hücreleri Kilitleyerek Korumak için Nasıl Yapılır
type: docs
weight: 130
url: /tr/cpp/how-to-lock-cells-to-protect-them/
description: Bu makale, Aspose.Cells kütüphanesini kullanarak hücreleri kilitleme ve koruma konusunda kod örnekleri sağlar.
keywords: C++ kullanarak Hücreleri Kilitleme, Hücreleri Koruma Amaçlı Kilitleme, C++ kullanarak Hücreleri Kilitleme, C++ ta Hücreleri Kilitleme.
---

## **Olası Kullanım Senaryoları**
Hücreleri korumak için kilitlemek, Microsoft Excel veya Google Sheets gibi elektronik tablo uygulamalarında sık kullanılan önemli bir uygulamadır çünkü birçok önemli nedeni vardır:

1. Kazara Değişiklikleri Önleme: Hücreleri kilitlemek, kullanıcıların önemli veri veya formülleri kazara değiştirmesini önleyebilir. Bu, karmaşık tablolarda istenmeyen değişikliklerin ciddi hatalara yol açabileceği durumlarda özellikle faydalıdır.

1. Veri Bütünlüğünü Sağlama: Hücreleri kilitleyerek, kritik verilerin tutarlığını ve doğruluğunu koruyabilirsiniz. Bu, finansal belgeler, raporlar ve veri bütünlüğünün önemli olduğu diğer belgeler için çok önemlidir.

1. Kontrollü Erişim: İşbirliği ortamlarında, hücreleri kilitlemek, belirli alanlara kimlerin erişebileceğini kontrol etmenize olanak sağlar. Örneğin, yalnızca belirli ekip üyelerinin belirli hücreleri düzenlemesine izin verirken, diğer bütün sayfayı koruyabilirsiniz.

1. Formülleri Korumak: Formüller hesaplamalar ve veri analizi için genellikle kritiktir. Formülleri içeren hücreleri kilitlemek, bu formüllerin kazara değiştirilmesini veya silinmesini engeller; bu, bütün sayfa üzerindeki fonksiyonelliği bozabilir.

1. İş Kurallarını Zorunlu Kılmak: Bazı durumlarda, belirli iş kuralları veya mevzuatlar, verilerin değiştirilmesinin engellenmesini gerektirebilir. Hücreleri kilitlemek, bu gereksinimlere uyumu sağlar.

1. Kullanıcıları Yönlendirme: Hücreleri kilitleyerek ve hangi hücrelerin düzenlenebileceğine dair net talimatlar sağlayarak kullanıcıların tabloyla etkileşimde nasıl bulunacaklarını yönlendirebilirsiniz, bu da karışıklığı ve hataları azaltır.

## **Excel'de Hücreleri Kilitleyerek Nasıl Korumak Yapılır**
İşte Microsoft Excel'de hücreleri kilitlemenin yolu:

1. Kilitlemek İstediğiniz Hücreleri Seçin: Kilitlemek istediğiniz hücreleri seçin. Bütün sayfayı kilitlemek istiyorsanız, bu adımı atlayabilirsiniz.
1. Hücreleri Biçimlendirme Diyaloğunu Açın: Seçilen hücrelere sağ tıklayın ve "Hücreleri Biçimlendir" seçeneğini seçin veya Ctrl+1 tuşlarına basın.
<br>
<img src="1.png" width=60% />
1. Hücreleri Kilitleyin: Hücreleri biçimlendirme diyaloğunda, "Koruma" sekmesine gidin. "Kilitle" kutusunu işaretleyin. "Tamam" düğmesine tıklayın.
1. Sayfayı Koruyun: Şerit üzerindeki "Gözden Geçir" sekmesine gidin. "Sayfayı Koru" seçeneğine tıklayın. Bir şifre belirleyin (isteğe bağlı) ve izin vermek istediğiniz işlemleri seçin (ör. kilitli hücreleri seçme, hücreleri biçimlendirme vb.). "Tamam" düğmesine tıklayın.
<br>
<img src="2.png" width=60% />

## **C++ Kullanarak Hücreleri Nasıl Kilitlersiniz ve Korursunuz**

Aspose.Cells, Excel dosyalarıyla programlı olarak çalışmak için güçlü bir kütüphanedir. Aspose.Cells kullanarak hücreleri kilitlemek için şu adımları izlemeniz gerekir: [örnek dosyayı yükle](sample.xlsx), önce tüm hücreleri kilidini açın (varsayılan olarak tüm hücreler kilitlidir ancak, çalışma sayfası korunan değilse, bu kilitler etkili değildir), sonra korumak istediğiniz belirli hücreleri kilitleyin ve sonunda çalışma sayfasını koruyarak kilitleri uygularsınız.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unlock all cells first
    Style unlockStyle = workbook.CreateStyle();
    unlockStyle.SetIsLocked(false);

    StyleFlag styleFlag;
    styleFlag.SetLocked(true);
    sheet.GetCells().ApplyStyle(unlockStyle, styleFlag);

    // Lock specific cells (e.g., A1 and B2)
    Style lockStyle = workbook.CreateStyle();
    lockStyle.SetIsLocked(true);

    sheet.GetCells().Get(u"A1").SetStyle(lockStyle);
    sheet.GetCells().Get(u"B2").SetStyle(lockStyle);

    // Protect the worksheet to enforce the locking
    sheet.Protect(ProtectionType::All);

    // Save the modified workbook
    workbook.Save(u"output_locked.xlsx");

    std::cout << "Worksheet protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sonuç Çıktısı**
Bu kod, sadece belirtilen hücrelerin (örneğin A1 ve B2) kilitlendiğinden emin olur ve bu ayarların uygulanması için sayfa korumasını sağlar. Sayfanın diğer tüm hücreleri kilitsiz ve düzenlenebilir kalır.

<br>
<img src="3.png" width=60% />

