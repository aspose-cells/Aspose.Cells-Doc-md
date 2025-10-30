---
title: Cell.Calculate metodunun hesaplama Süresini C++ ile azaltın
linktitle: Cell.Calculate hesaplama Süresini azaltın
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de hücre hesaplama yöntemlerinin hesaplama süresini azaltmayı nasıl kullanacağımızı tanıtıyor. Mevcut bir Excel dosyası yükleyerek veya yeni bir tane oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanabilir ve hücre hesaplama yöntemini optimize edip performansını iyileştirebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, Hücre hesaplama yöntemleri, optimizasyon, performans, hesaplama süresinin azaltılması
type: docs
weight: 100
url: /tr/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Olası Kullanım Senaryoları**

Normalde, kullanıcıların [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metodunu bir kez çağırıp, ardından bireysel hücrelerin hesaplanan değerlerini almalarını öneririz. Ancak bazen kullanıcılar, tüm çalışma kitabını değil, sadece tek bir hücreyi hesaplamak isterler. Aspose.Cells, bu amaçla [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) özelliğini sağlar, bu özelliği **false** olarak ayarlayabilirsiniz ve bu, bireysel hücrelerin hesaplama süresini önemli ölçüde azaltır. Çünkü recursive özelliği **true** ise, tüm bağımlı hücreler her çağrıda yeniden hesaplanır. Ancak recursive **false** ise, bağımlı hücreler sadece bir kez hesaplanır ve sonraki çağrılarda tekrar hesaplanmaz.

## **Hücre.Calculate() Yönteminin Hesaplama Zamanını Azaltma**

Aşağıdaki örnek kod, [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) özelliğinin kullanımını gösterir. Lütfen bu kodu verilen [örnek Excel dosyası](5113710.xlsx) ile çalıştırın ve konsol çıktısını kontrol edin. Recursive özelliğini **false** olarak ayarlamanın hesaplama süresini önemli ölçüde azalttığını göreceksiniz. Ayrıca, bu özelliğin daha iyi anlaşılması için açıklamaları okuyun.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

void TestCalcTimeRecursive(bool isRecursive) {
    Workbook* workbook = new Workbook();
    CalculationOptions options;
    options.SetRecursive(isRecursive);

    auto start = std::chrono::high_resolution_clock::now();
    workbook->CalculateFormula(&options);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;

    delete workbook;
}

int main() {
    Aspose::Cells::Startup();

    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

void TestCalcTimeRecursive(bool rec) {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(0);
    CalculationOptions opts;
    opts.SetRecursive(rec);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++) {
        ws.GetCells().Get(u"A1").Calculate(opts);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    long estimatedTime = duration.count() / 1000;
    std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Konsol Çıktısı**

Yukarıdaki örnek kodun komut satırı çıktısı, [örnek Excel dosyası](5113710.xlsx) kullanılarak bizim makinemizde çalıştırıldığında elde edilmiştir. Lütfen, çıkış değerleriniz farklı olabilir, ancak recursive özelliği **false** olarak ayarladıktan sonra geçen zaman her zaman **true** ayarından daha az olacaktır.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
