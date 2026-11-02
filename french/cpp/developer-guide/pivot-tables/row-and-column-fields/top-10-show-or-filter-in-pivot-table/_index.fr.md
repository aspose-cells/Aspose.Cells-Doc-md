---
title: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
linktitle: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux classés ou les moins bien classés d'un champ de tableau croisé dynamique à l'aide d'Aspose.Cells for C++. Cet article présente la méthode Top10AutoShow pour Excel 97-2003, la lecture des options avec GetTop10AutoShowSettings et le filtre Top 10 pour Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, C++, tableau croisé dynamique, 10 premiers éléments, affichage automatique, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /fr/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique qui répertorie tous les éléments d'un champ de ligne peut être difficile à lire lorsque le champ comporte des dizaines de membres. Un rapport « 10 premiers » ne conserve que les éléments les mieux ou les moins bien classés, ce qui correspond exactement aux besoins des rapports de classement — « 5 premiers produits par chiffre d'affaires » ou « 3 dernières régions par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cette fin, qui correspondent à deux générations de Microsoft Excel.
- **Excel 97-2003 – Affichage automatique** — la méthode `PivotField.Top10AutoShow()`. Il s'agit du paramètre classique « Afficher les N éléments les mieux ou les moins bien classés », stocké directement sur le champ de tableau croisé dynamique. Il fonctionne dans toutes les versions d'Excel, qu'elles soient anciennes ou récentes, car il fait partie du format d'origine des tableaux croisés dynamiques.
- **Excel 2007-365 – Filtre des 10 premiers éléments** — la méthode `PivotField.FilterTop10()`. Il s'agit du filtre moderne de valeurs Top 10, accessible dans le menu du champ sous « Filtres de valeurs ». Il est stocké sous forme d'objet `PivotFilter` associé au champ et permet un classement selon le nombre d'éléments ou selon un pourcentage.

## **Affichage des 10 premiers éléments dans Excel 97-2003 (Top10AutoShow)**
L'affichage automatique classique se configure par un appel unique à `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)` :
- `isAutoShow` — active ou désactive le paramètre d'affichage automatique sur le champ.
- `isTop` — `true` conserve les éléments les mieux classés (« Haut »), `false` conserve les éléments les moins bien classés (« Bas »).
- `count` — le nombre d'éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `rankBy` — l'indice, à partir de zéro, du **champ de données** dont les valeurs servent à classer les éléments. Passez -1 pour classer les éléments selon le champ lui-même.
Le classement peut reposer sur un champ de valeurs ou sur le champ lui-même. Deux variantes sont présentées ci-dessous.

### **Classer selon un champ de valeurs**
Classez les éléments du champ de ligne en fonction d'un champ de valeurs ordinaire, tel que « Somme des ventes ». L'exemple suivant construit un tableau croisé dynamique contenant un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports dont les ventes sont les plus élevées. `rankBy` vaut 0, car « Somme des ventes » est le champ de données situé à l'indice 0.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Afficher les 2 principaux éléments classés par « Somme des ventes » (index 0 du champ de données)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Classer selon le champ lui-même**
Un champ peut également être classé par lui-même — transmettez -1 comme valeur de `rankBy`. Aucun champ de données supplémentaire n'est requis pour cette variante ; le champ doit seulement figurer dans la zone des lignes ou des colonnes. L'exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lorsque ce paramètre est enregistré, l'attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 correspond à la valeur par défaut du format ; `GetTop10AutoShowSettings().GetRankBy()` renvoie -1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Afficher les 3 derniers éléments classés par le champ lui-même (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Lire les options actuelles (GetTop10AutoShowSettings)**
La méthode `PivotField.GetTop10AutoShowSettings()` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options d'affichage automatique actuellement stockées sur le champ. Utilisez-la pour examiner les éléments qu'affichera un classeur existant ou un tableau croisé dynamique que vous venez de configurer, y compris lorsque le classeur est chargé à partir d'un fichier.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Les quatre membres correspondent aux attributs classiques d'affichage automatique écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), de sorte que les valeurs renvoyées sont celles que toutes les versions d'Excel prennent en compte.

## **Note**

{{% alert color="primary" %}}
- Les propriétés directes de `PivotField` (`IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` et `GetAutoShowField`) sont dépréciées. Utilisez plutôt l'objet `PivotFieldTop10AutoShowSettings` : `IsAutoShow` devient `GetTop10AutoShowSettings().IsAutoShow()`, `IsAscendShow` devient `GetTop10AutoShowSettings().IsTop()`, `GetAutoShowCount` devient `GetTop10AutoShowSettings().GetAutoShowCount()` et `GetAutoShowField` devient `GetTop10AutoShowSettings().GetRankBy()`. La méthode `Top10AutoShow()` elle-même est le mécanisme pris en charge pour modifier les paramètres.
- `Top10AutoShow` fonctionne avec les champs de ligne et de colonne. Un champ placé uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre des 10 premiers éléments (FilterTop10)**
Les versions récentes d'Excel permettent d'appliquer un filtre Top 10 à partir du menu du champ (Filtres de valeurs, 10 premiers éléments...). Aspose.Cells l'implémente au moyen de la méthode `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — l'indice, à partir de zéro, du champ de données dont les valeurs agrégées servent à classer les éléments.
- `type` — la signification de `itemCount`. `PivotFilterType::Count` conserve un nombre fixe d'éléments (option « Éléments » de la boîte de dialogue). `PivotFilterType::Percent` conserve un pourcentage des éléments ; `itemCount` correspond alors directement au pourcentage : la valeur 30 conserve les 30 % d'éléments les mieux classés. `PivotFilterType::Sum` classe les éléments en fonction du cumul des valeurs.
- `isTop` — `true` pour l'option « Haut », `false` pour l'option « Bas ».
- `itemCount` — le N dans « N premiers » ou « N derniers » ; son unité dépend de `type`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Filtre Top 10 — conserver les 2 premiers éléments selon « Sum of Sales » (index 0 du champ de données)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // Pour utiliser plutôt un filtre basé sur un pourcentage, conserver les 30 % premiers éléments :
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` et `FilterTop10` sont deux fonctionnalités distinctes. L'affichage automatique écrit sur le champ de tableau croisé dynamique l'ensemble des attributs classiques associés à `autoShow`. Cette fonctionnalité est prise en charge par toutes les versions d'Excel, depuis Excel 97. `FilterTop10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu'un classeur est ouvert dans une version antérieure d'Excel, un tableau croisé dynamique qui utilise le filtre moderne affiche tous les éléments. Pour les documents devant être ouverts et réenregistrés par des outils hérités, préférez `Top10AutoShow` ; pour les classeurs modernes, préférez `FilterTop10`, car cette fonctionnalité peut être combinée avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles connexes**
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/cpp/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/cpp/pivot-table-add-row-and-column-fields/)
- [Regrouper les champs d'un tableau croisé dynamique](/cells/fr/cpp/group-pivot-fields-in-the-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/)
- [Ajouter un champ de page à un tableau croisé dynamique](/cells/fr/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}