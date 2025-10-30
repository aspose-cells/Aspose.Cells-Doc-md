---
title: Ruhlar ve Boolean Değerleri Rusça veya Diğer Dillerde Uygulama
linktitle: Hatalar ve Boolean Değerleri Uygula
type: docs
weight: 40
url: /tr/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aspose.Cells kullanarak Rusça veya diğer dillerde hatalar ve boolean değerleri nasıl uygulayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

 Eğer Microsoft Excel'i Rusya Bölgede veya Dilinde veya başka herhangi bir bölge veya dilde kullanıyorsanız, Hatalar ve Boolean değerler buna göre görüntülenir. Benzer bir davranışa, [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) özelliğini kullanarak Aspose.Cells ile ulaşabilirsiniz. [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfının aşağıdaki metodlarını geçersiz kılmanız gerekir.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Rusça veya Başka Bir Dilde Hataları ve Boolean Değerleri Uygulayın**

Aşağıdaki örnek kod, Rusça veya başka bir dilde Hataları ve Boolean Değerleri nasıl uygulayacağınızı göstermektedir. Bu kodda kullanılan bu [Örnek Excel Dosyasını](73990159.xlsx) ve [Çıktı PDF](73990160.pdf) dosyasını kontrol edin. Ekran görüntüsü, Örnek Excel Dosyası ile Çıktı PDF arasındaki farkı göstermektedir.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class RussianGlobalization : public GlobalizationSettings
{
public:
    virtual U16String GetErrorValueString(const U16String& err) override
    {
        if (err == u"#NAME?")
        {
            return u"#RussianName-имя?";
        }
        return u"RussianError-ошибка";
    }

    virtual U16String GetBooleanValueString(bool bv) override
    {
        return bv ? u"RussianTrue-правда" : u"RussianFalse-ложный";
    }
};

class ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        Workbook wb(u"sampleRussianGlobalization.xlsx");

        auto russianGlobalization = std::make_shared<RussianGlobalization>();
        wb.GetSettings().SetGlobalizationSettings(russianGlobalization.get());

        wb.CalculateFormula();

        wb.Save(u"outputRussianGlobalization.pdf");

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage::Run();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
