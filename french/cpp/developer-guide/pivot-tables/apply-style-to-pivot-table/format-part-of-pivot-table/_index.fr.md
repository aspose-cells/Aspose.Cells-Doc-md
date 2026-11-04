---
title: Formater une partie d'un tableau croisé dynamique
description: Formatez une partie d'un tableau croisé dynamique dans Aspose.Cells for C++ en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.Format, les formats étant stockés dans PivotTable.GetPivotFormats et conservés lorsque le tableau croisé dynamique est actualisé.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /fr/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.FormatAll` applique un seul style à l'ensemble du tableau croisé dynamique et est expliqué sur la page parente. Il ne fait pas de distinction entre les libellés, les valeurs, les totaux ou des régions particulières du rapport.
En pratique, seule une partie d'un tableau croisé dynamique doit généralement se démarquer. Les cibles courantes comprennent les libellés appartenant à un champ de ligne, les cellules de valeurs générées par un champ, la ligne du total général, ou un rectangle arbitraire comme les deux premières lignes d'éléments.
Appliquer un style directement aux cellules de la feuille de calcul d'un tableau croisé dynamique n'est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les libellés d'un champ ou les valeurs de données, et il est résolu à nouveau lorsque le tableau croisé dynamique est recalculé, actualisé ou étendu. En revanche, un style écrit directement sur une cellule appartient à la position de cette cellule et n'est pas suivi par le modèle pivot.
Aspose.Cells expose la famille complète de surcharges de `PivotTable.Format` afin que les deux types de mise en forme soient disponibles :
- `Format(const PivotArea&, const Style&)` lie un style à une région sémantique construite avec `PivotArea.Select` ou `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` lie un style à un rectangle de la feuille de calcul à l'intérieur du tableau croisé dynamique.
- `Format(int32_t row, int32_t column, const Style&)` cible une seule cellule.
- `FormatAll(const Style&)` met en forme l'ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l'approche recommandée lorsqu'une mise en évidence doit suivre un champ ou une région du rapport.
1. Créez un `PivotArea` avec `PivotArea pivotArea(pivotTable);`. L'objet décrit une région sémantique appartenant à ce tableau croisé dynamique spécifique.
2. Sélectionnez un champ par sa position indexée à zéro sur un axe donné avec `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType::DataAndLabel` sélectionne à la fois les libellés et les données du champ.
   - `PivotTableSelectionType::LabelOnly` sélectionne uniquement les libellés du champ.
   - `PivotTableSelectionType::DataOnly` sélectionne uniquement les cellules de données du champ.
3. Sélectionnez un champ par son nom avec `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. Lorsque un champ de ligne est sélectionné par son nom, la région se résout aux cellules de valeur produites par les éléments de ce champ.
4. Créez un `Style` avec `Workbook.CreateStyle()`, configurez sa police, sa couleur de premier plan et son motif de remplissage uni, puis transmettez le style à `PivotTable.Format(pivotArea, style)`.
5. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.GetPivotFormats()`.
6. Les formats ancrés aux champs sont appliqués lorsque les données du pivot sont calculées. Par conséquent, appelez `PivotTable.CalculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.
L'exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux libellés de ligne `Fruit` avec `PivotArea.Select` et `PivotTableSelectionType::LabelOnly`, applique un style aux cellules de valeur générées par ce même champ de ligne avec `PivotArea.SelectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.Format(const CellArea&, const Style&)` lorsque la région d'intérêt est un simple rectangle de la feuille de calcul plutôt qu'une région pivot sémantique.
Un `CellArea` est décrit par les champs publics `StartRow`, `StartColumn`, `EndRow` et `EndColumn`. Les valeurs sont des coordonnées de feuille de calcul indexées à zéro, et les coordonnées de fin identifient la dernière ligne et la dernière colonne incluses dans le rectangle, ainsi la zone couvre les cellules de la position de départ jusqu'à la position de fin incluses.
Contrairement à un format ancré à un champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `CalculateData()` n'est pas nécessaire pour que le style apparaisse.
Un rectangle `CellArea` peut contenir à la fois des cellules de libellés et des cellules de valeurs. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.
L'exemple suivant met en forme le rectangle `E4:F5` du tableau croisé dynamique avec un style italique et bleu clair, puis enregistre le classeur sans aucun recalcul supplémentaire.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Comment les zones Pivot et les zones CellArea sont associées**
Excel stocke la mise en forme du tableau croisé dynamique sous forme d'enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu'une demande de mise en forme est traduite en zones pivot lorsqu'elle est enregistrée.
La relation entre le `CellArea` fourni par l'utilisateur et les zones pivot stockées en interne est de type plusieurs-à-plusieurs dans les deux sens.
- Un `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules de libellés et des cellules de valeurs, il est décomposé en règles distinctes pour les libellés et les données, car le modèle pivot traite la mise en forme des libellés et des données séparément.
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu'une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C'est pourquoi `PivotArea.GetCellAreas()` renvoie un `Vector<CellArea>` au lieu d'un seul rectangle.
Chaque opération de mise en forme effectuée via `PivotTable.Format` est enregistrée dans `PivotTable.GetPivotFormats()`. Chaque entrée `PivotTableFormat` expose le `PivotArea` associé et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu'un `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.
Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `GetOnlyLabel()` et `GetOnlyData()`. L'exemple ci‑dessus met en forme un seul rectangle couvrant à la fois les libellés et les valeurs, inspecte `PivotTable.GetPivotFormats()`, et affiche les coordonnées `CellArea` que chaque zone pivot stockée résout à.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Parce que les formats sont stockés en tant que zones pivot plutôt qu'en tant que styles de cellules ordinaires, ils survivent aux recalculs et aux actualisations. Lorsque le tableau croisé dynamique est actualisé avec `PivotTable.RefreshData`, recalculé avec `CalculateData`, ou enregistré puis rechargé, chaque zone pivot stockée se résout à nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez un `PivotArea` construit avec `Select` ou `SelectField` lorsqu'une mise en évidence doit rester attachée à un champ ou à une région sémantique lors des actualisations, et utilisez un `CellArea` lorsque le formatage d'un rectangle fixe dans la disposition actuelle du tableau croisé dynamique suffit. La surcharge de cellule unique `Format(int32_t row, int32_t column, const Style&)` cible une cellule individuelle. Utilisez `FormatAll`, expliqué sur la page parente, lorsque l'ensemble du tableau croisé dynamique doit être restylé en une fois.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/)
- [Ajouter des champs de ligne et de colonne au tableau croisé dynamique](/cells/fr/cpp/pivot-table-add-row-and-column-fields/)
- [Gérer les champs de valeur dans le tableau croisé dynamique](/cells/fr/cpp/manage-value-fields/)
- [Actualiser le tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}