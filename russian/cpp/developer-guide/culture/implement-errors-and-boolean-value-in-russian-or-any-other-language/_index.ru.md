---
title: Реализовать ошибки и булевы значения на русском или другом языке с помощью C++
linktitle: Реализовать ошибки и булевы значения
type: docs
weight: 40
url: /ru/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Узнайте, как реализовать ошибки и булевы значения на русском или другом языке с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Если вы используете Microsoft Excel на русском языке или другом языке/локали, ошибки и булевы значения будут отображаться согласно выбранной локали или языку. Это можно реализовать с помощью Aspose.Cells, используя свойство [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Для этого необходимо переопределить методы класса [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Реализация ошибок и логических значений на русском или на любом другом языке**

Приведенный ниже образец кода иллюстрирует, как реализовать ошибки и логические значения на русском или на любом другом языке. Пожалуйста, проверьте [используемый образец файл Excel](73990159.xlsx) в этом коде и его [выходной PDF](73990160.pdf). На скриншоте показано различие между образцом файла Excel и выходным PDF для справки.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Образец кода**

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
