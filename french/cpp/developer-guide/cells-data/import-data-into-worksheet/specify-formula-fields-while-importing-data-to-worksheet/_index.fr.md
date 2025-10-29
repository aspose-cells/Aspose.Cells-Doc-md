---
title: Spécifier les champs de formule lors de l importation de données dans une feuille de calcul avec C++
linktitle: Spécifiez les champs de formule lors de l importation de données dans la feuille de calcul
type: docs
weight: 300
url: /fr/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Apprenez comment spécifier des champs de formule lors de l importation de données dans une feuille via l API Aspose.Cells for C++.
keywords: Spécifiez les champs de formule lors de l importation de données dans la feuille de calcul, Définissez les champs de formule lors de l ajout de données dans la feuille de calcul
---

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier les champs de formule lors de l'importation de données dans votre feuille de calcul en utilisant le [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/). Cette propriété prend le tableau booléen où la valeur **true** signifie que le champ est un champ de formule. Par exemple, si le troisième champ est un champ de formule, alors la troisième valeur dans le tableau sera **true**.

## **Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul**

Veuillez consulter le code d'exemple suivant qui explique comment spécifier le champ de formule lors de l'importation de données dans une feuille de calcul. Veuillez consulter le fichier Excel de sortie généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Code d'exemple**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

static U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

class DataItems {
public:
    int Number1;
    int Number2;
    U16String Formula1;
    U16String Formula2;

    DataItems() : Number1(0), Number2(0) {}
};

void Run() {
    vector<DataItems> dis;

    DataItems di;
    di.Number1 = 2002;
    di.Number2 = 3502;
    di.Formula1 = u"=SUM(A2,B2)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2003;
    di.Number2 = 3503;
    di.Formula1 = u"=SUM(A3,B3)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2004;
    di.Number2 = 3504;
    di.Formula1 = u"=SUM(A4,B4)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2005;
    di.Number2 = 3505;
    di.Formula1 = u"=SUM(A5,B5)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    for (size_t i = 0; i < dis.size(); ++i) {
        const DataItems& item = dis[i];
        int row = static_cast<int>(i);
        ws.GetCells().Get(row, 0).PutValue(item.Number1);
        ws.GetCells().Get(row, 1).PutValue(item.Number2);
        ws.GetCells().Get(row, 2).SetFormula(item.Formula1);
        ws.GetCells().Get(row, 3).SetFormula(item.Formula2);
    }

    wb.CalculateFormula();
    ws.AutoFitColumns();
    wb.Save(outputDir + u"outputSpecifyFormulaFieldsWhileImportingDataToWorksheet.xlsx");

    cout << "SpecifyFormulaFieldsWhileImportingDataToWorksheet executed successfully." << endl;
}

int main() {
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
