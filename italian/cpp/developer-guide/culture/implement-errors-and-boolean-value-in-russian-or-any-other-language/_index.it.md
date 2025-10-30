---
title: Implementa errori e valori booleani in Russo o qualsiasi altra lingua con C++
linktitle: Implementa Errori e Valori Booleani
type: docs
weight: 40
url: /it/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Impara come implementare errori e valori booleani in Russo o qualsiasi altra lingua usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Se usi Microsoft Excel in locale o lingua russa o in qualsiasi altra lingua o locale, sarà visualizzato errori e valori booleani in base a quel locale o lingua. Puoi ottenere un comportamento simile utilizzando Aspose.Cells usando la proprietà [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Dovrai sovrascrivere i seguenti metodi della classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Implementare gli errori e il valore booleano in russo o in qualsiasi altra lingua**

Il seguente codice di esempio illustra come implementare gli errori e il valore booleano in russo o in qualsiasi altra lingua. Controlla il [File Excel di esempio](73990159.xlsx) utilizzato in questo codice e il suo [PDF di output](73990160.pdf). Lo screenshot mostra la differenza tra il file Excel di esempio e il PDF di output a titolo di riferimento.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Codice di Esempio**

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
