---
title: Özel Fonksiyonun Doğrudan Hesaplanması, Worksheet e Yazmadan C++ ile
linktitle: Özel Fonksiyonun Doğrudan Hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de özel fonksiyonları çalışma tablosuna yazmadan doğrudan nasıl hesaplacağınızı tanıtıyor. Mevcut bir Excel dosyası yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanabilir ve özel fonksiyonu hesaplayabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, özel fonksiyonlar, doğrudan hesaplamalar, yazma ihtiyacı yok, çalışma tabloları
type: docs
weight: 90
url: /tr/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Worksheet'e Yazmadan Özel Fonksiyonun Doğrudan Hesaplanması**

Bu konu, özel fonksiyonlarınızı öncelikle çalışma sayfasına yazmadan doğrudan nasıl hesaplayabileceğinizi açıklar. Lütfen bu amaçla [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) metodunu kullanın.

Lütfen aşağıdaki örnek kodu inceleyin, bu metodun kullanımını gösterir. MyCompany::CustomFunction() adında bir özel fonksiyon kullandık ve değeri "Aspose.Cells." olarak hesapladık. Bu değer otomatik olarak hesaplama motoru tarafından hücre A1'in değeri olan "Welcome to " ile birleştirilir ve nihai hesaplanan değer "Welcome to Aspose.Cells." olur. Koddaki gibi, özel fonksiyonumuzu herhangi bir worksheet'e yazmadık ve tamamen kendi özel mantığımızla hesaplandı.

### **Programlama Örneği**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ICustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Check the formula name and calculate it yourself
        if (data.GetFunctionName() == u"MyCompany.CustomFunction")
        {
            // This is our calculated value
            data.SetCalculatedValue(Aspose::Cells::Object(u"Aspose.Cells."));
        }
    }
};

class ImplementDirectCalculationOfCustomFunction
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        // Create a workbook
        Workbook wb;

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Add some text in cell A1
        ws.GetCells().Get(u"A1").PutValue(u"Welcome to ");

        // Create a calculation options with custom engine
        CalculationOptions opts;
        opts.SetCustomEngine(new ICustomEngine());

        // This line shows how you can call your own custom function without
        // a need to write it in any worksheet cell
        // After the execution of this line, it will return
        // Welcome to Aspose.Cells.
        Aspose::Cells::Object ret = ws.CalculateFormula(u"=A1 & MyCompany.CustomFunction()", opts);

        // Print the calculated value on Console
        std::cout << "Calculated Value: " << ret.ToString().ToUtf8() << std::endl;

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementDirectCalculationOfCustomFunction::Run();
    return 0;
}
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **İlgili Makale**

{{% alert color="primary" %}}

[Özel Hesaplama Motoru Uygula ve Aspose.Cells'in Varsayılan Hesaplama Motorunu Geliştir](/cells/tr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
