---
title: Implementieren Sie Fehler und Boolesche Werte in Russisch oder jeder anderen Sprache mit C++
linktitle: Implementieren Sie Fehler und boolesche Werte
type: docs
weight: 40
url: /de/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Lernen Sie, wie Sie Fehler und boolesche Werte in Russisch oder jeder anderen Sprache mit Aspose.Cells und C++ implementieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Microsoft Excel in russischer Sprache, Locale oder einer beliebigen anderen Sprache verwenden, werden Fehler und boolesche Werte entsprechend dieser Sprache angezeigt. Sie können ein ähnliches Verhalten mit Aspose.Cells erreichen, indem Sie die [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/)-Eigenschaft verwenden. Sie müssen die folgenden Methoden der [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)-Klasse überschreiben.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren**

Der folgende Beispielcode veranschaulicht, wie Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementiert werden. Bitte überprüfen Sie die in diesem Code verwendete [Beispiel Excel-Datei](73990159.xlsx) und deren [Ausgabe-PDF](73990160.pdf). Der Screenshot zeigt den Unterschied zwischen der Beispiel-Excel-Datei und der Ausgabe-PDF zur Referenz.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Beispielcode**

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
