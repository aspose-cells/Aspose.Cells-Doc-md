---
title: Gelişmiş Koşullu Biçimlendirmeyi C++ ile Uygula
linktitle: Gelişmiş Koşullu Biçimlendirme Uygulama
description: C++ kullanarak Aspose.Cells kütüphanesi ile gelişmiş koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, Gelişmiş Koşullu Biçimlendirme, C++, Koşullu, Biçimlendirme
type: docs
weight: 70
url: /tr/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 ve sonraki sürümler (2010/2013/2016) koşullu biçimlendirme için bazı gelişmiş özellikler sunar. Örneğin hücre gölendirme, sınırlar, renkli simgeler, oklar, bayraklar ve yazı tipi biçimlendirme uygulamanıza olanak tanır, bu oldukça sofistike hale gelmiştir.

{{% /alert %}}

## **Microsoft Excel Dosyalarına Gelişmiş Koşullu Biçimlendirme Uygulama**
Koşullu biçimlendirme şunları yapabilir:

- Basit bir çubuk grafiğini hücrelere gömerek altta yatan sayıları grafiksel olarak vurgulamak için gölgeli veri çubukları ekleyebilir.
- Hücreleri otomatik olarak renk skalalarına göre gölgelendirir, bu, aralıktaki diğer hücrelerdeki değerlere bağlı olarak en düşük değeri kırmızıdan en yüksek değeri yeşile hareket ettirir.
- Renk skalaları gibi simge setlerini renk skalaları gibi kullanır, ancak hücreleri gölgelendirmek yerine oklar ve trafik ışıkları gibi küçük simgeler ekler.

Aspose.Cells, Microsoft Excel 2007 ve sonraki sürümlerin sağladığı koşullu biçimlendirmeleri XLSX formatında çalışma zamanında tamamen destekler. Bu örnek, farklı özelliklere sahip simge setleri, veri çubukları, renk skalaları, zaman periyotları, en üst/en alt ve diğer kurallara yönelik gelişmiş koşullu biçimlendirme türleri için bir egzersiz göstermektedir.

### **Microsoft Excel'in Renk Skalası Koşullu Biçimlendirme Kullanıldığında Seçtiği Rengi Hesapla**
Aspose.Cells, bir şablon dosyasında Renk Skalası koşullu biçimlendirme kullanıldığında seçilen rengi hesaplamanıza olanak tanır. Aşağıdaki örnek kodu kullanarak Microsoft Excel tarafından seçilen rengi nasıl hesaplayacağınızı öğrenin.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
