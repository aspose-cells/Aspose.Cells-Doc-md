---
title: Personnaliser les paramètres de mondialisation pour le tableau croisé dynamique avec C++
linktitle: Personnaliser les paramètres de globalisation pour la table croisée dynamique
type: docs
weight: 50
url: /fr/cpp/customize-globalization-settings-for-pivot-table/
description: Apprenez comment personnaliser les paramètres de mondialisation du tableau croisé dynamique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

 Parfois, vous souhaitez personnaliser le texte *Total Pivot, Sous-total, Total général, Tous les éléments, plusieurs éléments, Étiquettes de colonne, Étiquettes de ligne, Valeurs vides* selon vos besoins. Aspose.Cells for C++ vous permet de personnaliser les paramètres de mondialisation du tableau croisé dynamique pour gérer de tels scénarios. Vous pouvez également utiliser cette fonctionnalité pour changer les étiquettes dans d'autres langues comme l'arabe, l'hindi, le polonais, etc.

## **Personnaliser les paramètres de globalisation pour le tableau croisé dynamique**

Le code d'exemple ci-dessous explique comment personnaliser les paramètres de mondialisation pour le tableau croisé dynamique en C++. Il crée une classe *CustomPivotTableGlobalizationSettings* dérivée de la classe de base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.settings/pivotglobalizationsettings/) et surcharge toutes les méthodes nécessaires. Ces méthodes renvoient du texte personnalisé pour divers éléments du tableau croisé dynamique. Le code assigne ensuite cette mise en œuvre à la propriété [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). L'exemple charge un [fichier Excel source](40468488.xlsx), actualise les données du tableau croisé dynamique, et l'enregistre sous forme de [PDF de sortie](40468487.pdf). La capture d'écran ci-dessous montre des étiquettes personnalisées dans la sortie.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomPivotTableGlobalizationSettings : public PivotGlobalizationSettings {
public:
    virtual U16String GetTextOfTotal() override {
        std::cout << "---------GetPivotTotalName-------------" << std::endl;
        return u"AsposeGetPivotTotalName";
    }

    virtual U16String GetTextOfGrandTotal() override {
        std::cout << "---------GetPivotGrandTotalName-------------" << std::endl;
        return u"AsposeGetPivotGrandTotalName";
    }

    virtual U16String GetTextOfMultipleItems() override {
        std::cout << "---------GetMultipleItemsName-------------" << std::endl;
        return u"AsposeGetMultipleItemsName";
    }

    virtual U16String GetTextOfAll() override {
        std::cout << "---------GetAllName-------------" << std::endl;
        return u"AsposeGetAllName";
    }

    virtual U16String GetTextOfColumnLabels() override {
        std::cout << "---------GetColumnLabelsOfPivotTable-------------" << std::endl;
        return u"AsposeGetColumnLabelsOfPivotTable";
    }

    virtual U16String GetTextOfRowLabels() override {
        std::cout << "---------GetRowLabelsNameOfPivotTable-------------" << std::endl;
        return u"AsposeGetRowLabelsNameOfPivotTable";
    }

    virtual U16String GetTextOfEmptyData() override {
        std::cout << "---------GetEmptyDataName-------------" << std::endl;
        return u"(blank)AsposeGetEmptyDataName";
    }

    virtual U16String GetTextOfSubTotal(PivotFieldSubtotalType subTotalType) override {
        std::cout << "---------GetSubTotalName-------------" << std::endl;

        switch(subTotalType) {
            case PivotFieldSubtotalType::Sum:
                return u"AsposeSum";
            case PivotFieldSubtotalType::Count:
                return u"AsposeCount";
            case PivotFieldSubtotalType::Average:
                return u"AsposeAverage";
            case PivotFieldSubtotalType::Max:
                return u"AsposeMax";
            case PivotFieldSubtotalType::Min:
                return u"AsposeMin";
            case PivotFieldSubtotalType::Product:
                return u"AsposeProduct";
            case PivotFieldSubtotalType::CountNums:
                return u"AsposeCount";
            case PivotFieldSubtotalType::Stdev:
                return u"AsposeStdDev";
            case PivotFieldSubtotalType::Stdevp:
                return u"AsposeStdDevp";
            case PivotFieldSubtotalType::Var:
                return u"AsposeVar";
            case PivotFieldSubtotalType::Varp:
                return u"AsposeVarp";
            default:
                return u"AsposeSubTotalName";
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb(srcDir + u"samplePivotTableGlobalizationSettings.xlsx");

    CustomPivotTableGlobalizationSettings customSettings;
    wb.GetSettings().GetGlobalizationSettings()->SetPivotSettings(&customSettings);

    wb.GetWorksheets().Get(0).SetIsVisible(false);

    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);

    pt.SetRefreshDataFlag(true);
    pt.RefreshData();
    pt.CalculateData();
    pt.SetRefreshDataFlag(false);

    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);

    wb.Save(outDir + u"outputPivotTableGlobalizationSettings.pdf", options);

    std::cout << "Pivot table globalization settings applied successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
