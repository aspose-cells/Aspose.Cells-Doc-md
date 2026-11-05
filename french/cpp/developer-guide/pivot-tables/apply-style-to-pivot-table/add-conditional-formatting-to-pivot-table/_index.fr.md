---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for C++ - ancrer une règle à la région de données avec ApplyTo et une portée PivotConditionFormatScopeType, ou définir la cible avec AddCellArea et PivotAreas, puis attacher les règles et les styles via FormatConditions.AddCondition.
keywords: Aspose.Cells for C++, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /fr/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques - une région `PivotArea` ou `CellArea` est peinte une fois et conserve son style quelles que soient les valeurs. La mise en forme conditionnelle est le pendant basé sur des règles - mettre en évidence chaque montant supérieur à 200, ombrer les cinquante pour cent du milieu, ou signaler les éléments les moins bien classés - et la mise en évidence suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou actualisé.  
Dans Aspose.Cells, la mise en forme conditionnelle des tableaux croisés dynamiques se trouve dans la collection `pivotTable.GetConditionalFormats()`. Chaque entrée est un `PivotConditionalFormat` qui répond à deux questions de manière indépendante :
- **Où la règle s’applique‑t‑elle ?** La région cible est définie soit via `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, qui reflète le sélecteur de portée de l’interface utilisateur Excel, soit via `AddCellArea(CellArea)` et la collection `GetPivotAreas()`, qui nomment explicitement la région.
- **Quelle est la condition de la règle ?** Une ou plusieurs conditions sont ajoutées via `GetFormatConditions()` avec `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, et chaque condition possède son propre `Style`.

{{% alert color="primary" %}}
Ne pas appeler `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ou `FormatConditionCollection.AddArea(CellArea)` sur l’objet `GetFormatConditions()` d’un format conditionnel de tableau croisé dynamique. Ces deux surcharges sont héritées de l’API de mise en forme conditionnelle ordinaire des feuilles de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques - la zone de cellule n’est jamais convertie en zone de tableau croisé dynamique, de sorte que la requête est ignorée silencieusement. Définissez toujours la région sur le `PivotConditionalFormat` lui‑même (`ApplyTo`, `AddCellArea` ou `GetPivotAreas()`) et ajoutez la règle avec l’une des surcharges `AddCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l’interface Excel)**
La première méthode place la règle comme le fait l’interface utilisateur Excel. Une cellule du tableau croisé dynamique est nommée par ses coordonnées de feuille de calcul basées sur zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu’où la règle doit s’étendre à partir de cette cellule :
- `PivotConditionFormatScopeType::Data` - toutes les cellules de valeur que le tableau croisé dynamique produit, y compris les totaux généraux.
- `PivotConditionFormatScopeType::Field` - les cellules de valeur qui appartiennent au champ que la cellule identifie, à l’exclusion des totaux généraux. La cellule doit être une cellule de champ comme une étiquette de champ ligne ; passer une cellule de valeur provoque une exception.
- `PivotConditionFormatScopeType::Selection` - uniquement les cellules de valeur à l’intersection que la cellule sélectionne, généralement une seule cellule de valeur.
L’exemple ci‑dessous crée un tableau croisé dynamique des ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `Data`, et met en évidence chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Pomme 220, Banane 330, Cerise 200, et le total général 750, la règle colore F4, F5 et F7 - la région résolue est toute la colonne de données F4:F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Ancrer la même règle à l’étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `Field` résout à F4:F6 à la place - la même colonne de données sans la ligne de total général - car la portée décrit maintenant le champ `Fruit` plutôt que toute la zone des valeurs. La portée `Selection` ancrée à F4 se résout uniquement à F4.

## **Définir la région manuellement**
La deuxième méthode ignore le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec AddCellArea**
`AddCellArea(CellArea)` enregistre le rectangle donné comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul basées sur zéro, et la région correspond exactement au rectangle fourni - aucune expansion vers la colonne de données et aucune logique de total général. Utilisez‑le lorsque les cellules d’intérêt forment un rectangle fixe connu du présent agencement du tableau croisé dynamique.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Une région pivot sémantique avec PivotAreas**
`GetPivotAreas()` fournit le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `Select` ou `SelectField`, et ajoutez‑le avec `GetPivotAreas().AddPivotArea(PivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est actualisé et que la mise en page change. La surcharge `GetPivotAreas().Add(PivotArea)` compile encore mais est marquée obsolète - privilégiez `AddPivotArea`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `pivotTable.GetConditionalFormats().Add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier dans l’exemple ci‑dessous montre la même règle avec son type, son opérateur et sa formule intacts, et `GetCellAreas()` indique les mêmes régions. Les entrées qui n’ont jamais reçu de condition sont supprimées lors de l’enregistrement du classeur, de la même manière qu’Excel supprime une mise en forme conditionnelle dépourvue de règle.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articles associés**
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/)
- [Mettre en forme une partie d’un tableau croisé dynamique](/cells/fr/cpp/format-part-of-pivot-table/)
- [Top 10 Afficher ou filtrer dans le tableau croisé dynamique](/cells/fr/cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}