---
title: Implémenter erreurs et valeurs booléennes en russe ou dans toute autre langue avec C++
linktitle: Implémenter erreurs et valeurs booléennes
type: docs
weight: 40
url: /fr/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Apprenez comment implémenter des erreurs et des valeurs booléennes en russe ou dans toute autre langue en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Si vous utilisez Microsoft Excel en localisation ou langue russe ou dans toute autre localisation ou langue, il affichera des erreurs et des valeurs booléennes en fonction de cette localisation ou langue. Vous pouvez obtenir un comportement similaire en utilisant Aspose.Cells avec la propriété [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Vous devrez remplacer les méthodes suivantes de la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **Mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue**

Le code d'exemple suivant illustre comment mettre en œuvre des erreurs et des valeurs booléennes en russe ou dans une autre langue. Veuillez consulter le [Fichier Excel exemple](73990159.xlsx) utilisé dans ce code et son [Fichier PDF de sortie](73990160.pdf). La capture d'écran montre la différence entre le fichier Excel exemple et le fichier PDF de sortie pour référence.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Code d'exemple**

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
