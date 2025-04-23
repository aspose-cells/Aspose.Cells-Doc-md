---
title: C++ ile Sayıyı Para Birimi Olarak Biçimlendirme Nasıl Yapılır
linktitle: Sayı Biçimlendirme Nasıl Yapılır, Para Birimi Olarak Formatlama
type: docs
weight: 10
url: /tr/cpp/format-number-to-currency/
description: Bu makale, Aspose.Cells for C++ API sini kullanarak sayıları para birimi biçiminde nasıl biçimlendireceğinizi anlatacaktır.
keywords: sayı biçimini para birimi olarak ayarla, hücre sayı ayarları, sayıyı para birimine biçimlendir, para birimi ayarları, para birimi biçimi.
---

## **Olası Kullanım Senaryoları**
Excel’de sayıları para birimine biçimlendirmek, özellikle finansal verilerle çalışırken, birkaç nedenle önemlidir. İşte para birimi biçimlendirmesinin avantajları:

1. **Finansal Değerleri Açıklar**: bir sayıyı para birimi olarak biçimlendirmek, değerinin para ile ilişkili olduğunu gösterir. Örneğin, 1000 yerine, $1,000 açıkça bu değerin para tutarını temsil ettiğini gösterir.
1. **Para Birimi Sembollerini İçerir**: uluslararası veya çoklu para birimleriyle uğraşırken, sayıları uygun para birimi sembolü (örneğin $, €, £) ile biçimlendirmek, kullanılan para birimini netleştirir ve çok uluslu finansal raporlarda veya işlemlerde karışıklığı azaltır.
1. **Profesyonel Sunumu Artırır**: iyi biçimlendirilmiş para birimi değerleri düzgün ve profesyonel görünür, bu özellikle raporlar, sunumlar ve iş belgeleri için önemlidir. $10,000.00, sade 10000'e göre daha güvenilir ve düzenlidir.
1. **Okunabilirliği Artırır**: para birimi biçimlendirmesi, binlik ayırıcı olarak virgüller ve ondalık basamaklar ekler, bu da büyük sayıların daha kolay okunmasını sağlar. Örneğin, 1000000, $1,000,000.00 olur, bu da gözle okunabilirliği artırır ve anlamayı kolaylaştırır.
1. **Tutarlılığı Sağlar**: tutarlı para birimi biçimlendirmesi uygulayarak, bir veri kümesindeki tüm para değerlerinin aynı biçimde görüntülenmesini sağlarsınız. Bu tutarlılık finansal doğruluk ve profesyonel iletişim açısından önemlidir, özellikle birçok sayıya sahip büyük elektronik tablolar için.
1. **Hassasiyeti Gösterir**: para birimi biçimlendirmesi genellikle iki ondalık basamağı içerir, bu da kesin mali tutarları görmeyi kolaylaştırır. Örneğin, $100.50, $100.00'dan açıkça farklıdır, bu da hassasiyetin önemli olduğu finansal raporlarda gereklidir.
1. **Finansal Hesaplamaları Basitleştirir**: toplamların toplanması veya maliyetlerin ortalamasının alınması gibi finansal hesaplamalarda, para birimi biçimlendirmesi Excel ve kullanıcıların verilerin mali terimler olduğunu anlamasına yardımcı olur. Formüllerde ve fonksiyonlarda uygun biçimlendirmeyi uygular, böylece sonuçların tutarlılığı sağlanır.
1. **Yanlış Yorumlamayı Azaltır**: para birimi biçimlendirmesi olmadan, sayılar genel sayısal değerler olarak yanlış yorumlanabilir, yani toplam fiyat ve anlamda karışıklık yaşanabilir. Örneğin, 500, nesne veya birim sayımı olarak karıştırılabilirken, $500.00 açıkça bir finansal tutarı gösterir.
1. **Muhasebe Özellikleriyle Uyumlu Çalışır**: para birimi biçimlendirmesi, Bilanço veya nakit akış raporları gibi muhasebe fonksiyonlarıyla uyum sağlar. Paranın ana odak noktası olduğu finansal tablolarda kullanımı kolaylaştırır.
<br>
Özetle, numaraları para birimi olarak biçimlendirmek, parasal değerleri diğer sayı türlerinden ayırmaya yardımcı olur, açıklığı artırır ve verilerin yorumlanmasını kolaylaştırır, özellikle finansal bağlamlarda.

## **Excel'de Sayı Nasıl Para Birimi Olarak Biçimlendirilir**
Excel'de sayıları para birimi olarak biçimlendirmek için şu adımları izleyin:

### **Para Birimi Biçim Seçeneğinin Kullanılması**
1. Para birimi olarak biçimlendirmek istediğiniz hücreleri seçin.
1. Şeritteki Giriş sekmesine gidin.
1. Sayı grubunda, sayı biçimi kutusunun yanındaki aşağı açılır oka tıklayın (varsayılan olarak "Genel" görüntülenebilir).
<br>
<img src="1.png" width=60% />
1. Listeden Para Birimi seçeneğini seçin.

### **Hücreleri Biçimlendir Diyalog Kutusunu Kullanarak**
1. Biçimlendirmek istediğiniz hücreleri seçin.
1. Seçili hücrelere sağ tıklayın ve Biçimlendir seçeneğini seçin, böylece Hücreleri Biçimlendir iletişim kutusu açılır.
1. Sayı sekmesinde, sol taraftaki listeden Para Birimi seçin.
<br>
<img src="2.png" width=60% />
1. Aşağıdaki ayarları özelleştirebilirsiniz: Ondalık basamaklar, Sembol, Negatif sayılar.
1. Tamam düğmesine tıklayarak biçimlendirmeyi uygulayın.

## **Aspose.Cells'de Sayı Nasıl Para Birimi Olarak Biçimlendirilir**

Aspose.Cells for C++ kitaplığı kullanarak Excel dosyalarıyla çalışırken sayıları para birimi formatına dönüştürmek için hücrelere programatik olarak para birimi biçimi uygulayabilirsiniz. İşte Aspose.Cells ile C++ kullanarak nasıl yapılacağı:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the currency format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value to the cell
    a1.PutValue(1234.56);

    // Create a style object to apply the currency format
    Style a1Style = a1.GetStyle();
    // "7" is the currency format in Excel
    a1Style.SetNumber(7);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(3456.78);

    // Create a style object to apply the currency format
    Style a2Style = a2.GetStyle();
    // Custom format for dollar currency
    a2Style.SetCustom(u"$#,##0.00");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"CurrencyFormatted.xlsx");

    std::cout << "Workbook saved successfully with currency formatting!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
