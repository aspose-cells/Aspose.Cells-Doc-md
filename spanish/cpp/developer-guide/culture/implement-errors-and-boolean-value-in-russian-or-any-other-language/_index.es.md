---
title: Implementar errores y valores booleanos en ruso o en cualquier otro idioma con C++
linktitle: Implementar errores y valores booleanos
type: docs
weight: 40
url: /es/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aprende cómo implementar errores y valores booleanos en ruso o en cualquier otro idioma usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Si usas Microsoft Excel en ruso u otro idioma, mostrará errores y valores booleanos según ese idioma. Puedes lograr un comportamiento similar usando Aspose.Cells con la propiedad [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Tendrás que sobrescribir los siguientes métodos de la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Implementar Errores y Valor Booleano en Ruso u Otro Idioma**

El siguiente código de ejemplo ilustra cómo implementar Errores y Valor Booleano en Ruso u Otro Idioma. Por favor revise el [archivo de Excel de muestra](73990159.xlsx) usado en este código y su [PDF de salida](73990160.pdf). La captura de pantalla muestra la diferencia entre el archivo de Excel de muestra y el PDF de salida para referencia.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Código de muestra**

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
