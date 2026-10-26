---
title: Créer un tableau croisé dynamique
linktitle: Créer un tableau croisé dynamique
description: Créez et formatez des tableaux croisés dynamiques avec Aspose.Cells for C++.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Formater un tableau croisé dynamique.
type: docs
weight: 160
url: /fr/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un grand bloc de données brutes présentées ligne par ligne en une matrice compacte, sans aucune formule. Vous décidez quelles colonnes deviennent des étiquettes de ligne, lesquelles deviennent des étiquettes de colonne et lesquelles sont agrégées comme valeurs — le tableau croisé dynamique assure le regroupement et les calculs :
- **Résumer** — total des ventes par produit, par région ou par trimestre, au lieu de longues chaînes de formules.
- **Comparer** — les catégories sur les lignes et les périodes sur les colonnes transforment une liste plate en rapport croisé où les tendances sont visibles d’un coup d’œil.
- **Explorer les détails** — double-cliquez sur n’importe quelle valeur de synthèse pour examiner les lignes de données source sous-jacentes.
- **Actualiser** — lorsque les données source changent, une actualisation recalcule l’ensemble du rapport.
Les scénarios typiques sont les tableaux de bord des ventes, les ventilations des dépenses et l’analyse des stocks — toute question de la forme « comment ces chiffres se répartissent-ils par catégorie et par période ? ». Dans Aspose.Cells for C++, un tableau croisé dynamique est créé à l’aide de la méthode [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) d’une feuille de calcul. Une fois le tableau croisé dynamique créé, vous pouvez travailler avec lui à l’aide de la classe [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/).

## **Créer un tableau croisé dynamique**
L’exemple de code suivant montre comment créer un tableau croisé dynamique et à travailler avec celui-ci. Veuillez consulter le [fichier Excel de sortie](23167010.xlsx) généré à l’aide de ce code et la capture d’écran ci-dessous montrant ce fichier dans Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **Exemple de code**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Créer un nouveau classeur et obtenir la première feuille de calcul
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Écrire les données source : ventes par sport et par trimestre
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // Ajouter un tableau croisé dynamique à la cellule de destination E3, à partir de A1:C8
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Enregistrer le classeur
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}