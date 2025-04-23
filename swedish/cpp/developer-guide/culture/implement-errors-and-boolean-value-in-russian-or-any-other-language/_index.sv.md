---
title: Implementera fel och booleanvärden på ryska eller annat språk med C++
linktitle: Implementera Fel och Boolean Värde
type: docs
weight: 40
url: /sv/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Lär dig hur du implementerar fel och booleanvärden på ryska eller annat språk med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Om du använder Microsoft Excel på rysk lokalitet eller språk eller något annat, kommer den att visa fel och booleanvärden enligt den lokalen eller språket. Du kan åstadkomma liknande beteende med Aspose.Cells genom att använda [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) egenskapen. Du måste åsidosätta följande metoder i [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Implementera fel och booleska värden på ryska eller något annat språk**

Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Kontrollera den [Exempel Excel-filen](73990159.xlsx) som används i denna kod och dess [Utdata-PDF](73990160.pdf). Skärmbilden visar skillnaden mellan Exempel Excel-filen och Utdata-PDF för referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exempelkod**

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
