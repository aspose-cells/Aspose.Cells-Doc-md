---
title: Aspose.Cells ile Varsayılan Hesaplama Motorunu Geliştirmek için Özel Hesaplama Motoru Uygula c++ ile
linktitle: Özel Hesaplama Motoru Uygula
description: Bu makale, Aspose.Cells kütüphanesini kullanarak özel bir hesaplama motoru uygulayarak varsayılan hesaplama motorunu nasıl genişletebileceğinizi anlatır. Var olan bir Excel dosyasını yükleyerek veya yeni bir dosya oluşturarak, Aspose.Cells tarafından sağlanan metodları kullanarak bir özel hesaplama motoru uygulayabilir ve sonuçları alabilirsiniz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, Özel Hesaplama Motoru, varsayılan hesaplama motorunu genişletir, C++
type: docs
weight: 80
url: /tr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells'in neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoru bulunmaktadır. Bununla birlikte, varsayılan hesaplama motorunu genişletmenize olanak tanır ve size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Bu, bir [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) arayüzünü uygular ve içinde bir [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) yöntemi bulunmaktadır. Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde **TODAY** işlevini yakalar ve sistem tarihine bir gün ekler. Dolayısıyla, mevcut tarih 27/07/2023 ise, özel motor, TODAY() işlemini 28/07/2023 olarak hesaplar.

### **Programlama Örneği**

```c++
#include <iostream>
#include <cwctype>
#include "Aspose.Cells.h"
#include <chrono>

using namespace Aspose::Cells;

class CustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        U16String funcName = data.GetFunctionName();
        std::u16string upperName;
        for (int i = 0; i < funcName.GetLength(); ++i)
        {
            upperName.push_back(std::towupper(funcName[i]));
        }
		if (upperName == u"TODAY")
		{
			auto now = std::chrono::system_clock::now();
			std::time_t now_time = std::chrono::system_clock::to_time_t(now);
			std::tm local_tm;

#ifdef _WIN32
			localtime_s(&local_tm, &now_time);
#else
			localtime_r(&now_time, &local_tm);
#endif

            Date today{ local_tm.tm_year + 1900, local_tm.tm_mon + 1, local_tm.tm_mday };
			data.SetCalculatedValue(Date{ today.year, today.month, today.day + 1 });
		}
    }

    bool GetProcessBuiltInFunctions() override { return true; }
};

class ImplementCustomCalculationEngine
{
public:
    static void Run()
    {
        Workbook workbook;
        Worksheet sheet = workbook.GetWorksheets().Get(0);
        Cell a1 = sheet.GetCells().Get(u"A1");
        Style style = a1.GetStyle();
        style.SetNumber(14);
        a1.SetStyle(style);
        a1.SetFormula(u"=TODAY()");
        workbook.CalculateFormula();
        std::cout << "The value of A1 with default calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        CustomEngine engine;
        CalculationOptions opts;
        opts.SetCustomEngine(&engine);
        workbook.CalculateFormula(opts);
        std::cout << "The value of A1 with custom calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }
};

int main()
{
    Aspose::Cells::Startup();
    ImplementCustomCalculationEngine::Run();
    Aspose::Cells::Cleanup();
    return 0;
}

```

### **Sonuç**

Lütfen yukarıdaki örnek kodun konsol çıktısını kontrol edin, özel motor ile A1'in değeri (tarih saati) motor olmadan sonuçtan bir gün sonraki olmalıdır.

### **İlgili Makale**

{{% alert color="primary" %}}

[Özel fonksiyonun worksheet'e yazmadan doğrudan hesaplanması](/cells/tr/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
