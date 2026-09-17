---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for C++
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for C++
description: Découvrez comment appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for C++, notamment les mises en forme automatique XLS héritées, les styles nommés modernes d’Excel 2007+, les styles de tableau croisé dynamique personnalisés et le raccourci FormatAll.
keywords: Aspose.Cells C++ style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l’application des mises en forme automatique héritées des tableaux croisés dynamiques, destinées aux fichiers `.xls`, ainsi que des styles modernes nommés ou personnalisés de tableaux croisés dynamiques, destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`. L’API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous lisez. Un classeur chargé à partir d’un fichier `.xls` peut être enregistré de nouveau au format `.xlsx` ; dans ce cas, l’API de styles modernes s’applique plutôt que l’API héritée.
- `PivotTable.PivotTableStyleType` sélectionne l’un des styles intégrés nommés, avec des thèmes clairs et sombres, notamment les styles ajoutés dans Excel 2017. Ces préréglages sont en lecture seule.
- `PivotTable.PivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même au moyen de `Worksheets.TableStyles.AddPivotTableStyle(...)`. Les styles personnalisés sont nécessaires chaque fois que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que proposent les préréglages.
En outre, `PivotTable.FormatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, remplaçant ainsi tous les paramètres définis au moyen de l’une ou l’autre des API de nom de style ci-dessus. Cela est utile lorsqu’une apparence uniforme est requise, indépendamment du thème sous-jacent.

## **Appliquer une mise en forme automatique XLS héritée**
`PivotTable.AutoFormatType` accepte une valeur de l’énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic` et `Table1` à `Table10`.
L’exemple suivant charge un nouveau classeur, renseigne les données d’exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.Report5`, puis enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}
**Pourquoi aucun champ de colonne n’est-il défini ?** Les mises en forme automatique des séries `Report1` à `Report10` et `Table1` à `Table10` ont été conçues dans l’Excel classique pour les **tableaux croisés dynamiques à une dimension** avec uniquement des champs de ligne et des valeurs ; elles ne disposent d’aucune mise en forme intégrée pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique doit comporter des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du [scénario 2](#apply-a-modern-named-preset-pivot-table-style), conçus pour la disposition bidimensionnelle utilisée par les versions modernes d’Excel.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Créer un nouveau classeur
    Workbook workbook;
    // Obtenir la première feuille de calcul
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Remplir les données sources avec la ligne d'en-tête (Fruit, Année, Montant)
    // et 9 lignes de données couvrant raisin, myrtille, kiwi, cerise sur 2020 et 2021
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");
    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);
    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);
    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);
    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);
    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);
    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);
    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);
    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);
    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);
    // Ajouter un tableau croisé dynamique à la cellule de destination E3, nommé "Pivot1", en utilisant la plage source A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);
    // Assigner les champs : Fruit -> Lignes, Montant -> Données
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Appliquer le format automatique prédéfini XLS hérité "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);
    // Enregistrer le classeur au format .xls hérité
    workbook.Save(u"output.xls");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Appliquer un style nommé moderne préréglé à un tableau croisé dynamique**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);
    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);
    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);
    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);
    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);
    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Définir et appliquer un style de tableau croisé dynamique personnalisé**
Les préréglages intégrés ne peuvent pas être modifiés. Chaque fois que vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style de tableau croisé dynamique personnalisé. La procédure comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur au moyen de `Worksheets.TableStyles.AddPivotTableStyle(string name)`. Cette opération renvoie l’index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments, tels que `WholeTable` ou `GrandTotalRow`, au moyen de `TableStyle.TableStyleElements.Add(TableStyleElementType)`, puis affectez un `Style` à chaque élément au moyen de `TableStyleElement.SetElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en affectant le nom du style à `PivotTable.PivotTableStyleName`. N’utilisez pas `PivotTableStyleType` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}
`PivotTableStyleName` et `PivotTableStyleType` ne sont pas interchangeables. Utilisez `PivotTableStyleType` pour les préréglages intégrés et `PivotTableStyleName` pour les styles personnalisés que vous avez définis au moyen de `AddPivotTableStyle`. La définition simultanée des deux propriétés est sans effet secondaire, mais seule celle qui correspond à la source prévue est rendue.
{{% /alert %}}

Les valeurs `TableStyleElementType` disponibles comprennent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.
L’exemple suivant définit un style de tableau croisé dynamique personnalisé avec une bordure noire fine sur `WholeTable` et une police rouge en gras sur `GrandTotalRow`, puis applique ce style au moyen de `PivotTableStyleName` et enregistre le classeur au format `.xlsx`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Remplir les données source : ligne d'en-tête + 9 lignes de données (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);
    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);
    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);
    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);
    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);
    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);
    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);
    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);
    // Ajouter un tableau croisé dynamique sourcé depuis A1:C10, ancré à E3, nommé "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Étape 1 : enregistrer un nouveau style de tableau croisé dynamique personnalisé et capturer son index
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);
    // Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);
    // Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge en gras
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);
    // Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est pour les préréglages intégrés)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Appliquer un style à chaque cellule du tableau croisé dynamique avec FormatAll**
`PivotTable.FormatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de ligne et de colonne ainsi que les totaux. Tous les paramètres définis précédemment au moyen de `PivotTableStyleType` ou de `PivotTableStyleName` sont remplacés.

{{% alert color="primary" %}}
`FormatAll` remplace à la fois `PivotTableStyleType` et `PivotTableStyleName`. Utilisez-le uniquement lorsqu’une apparence uniforme et indépendante du thème est requise pour l’ensemble du tableau croisé dynamique.
{{% /alert %}}

L’exemple suivant crée un `Style` avec un remplissage jaune uni, une police bleu foncé en gras et des bordures noires fines sur tous les côtés, puis l’applique avec `FormatAll` et enregistre le classeur au format `.xlsx`.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Ligne d'en-tête
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Lignes de données
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);
    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);
    // Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3, nom "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Assigner les champs du tableau croisé dynamique
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Construire un style qui sera appliqué à chaque cellule du tableau croisé dynamique
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    // Appliquer FormatAll
    pivotTable.FormatAll(style);
    // Enregistrer le classeur
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Quelle API de style utiliser ?**
Le choix de l’API de style dépend du format de fichier dans lequel vous enregistrez le classeur. Utilisez le tableau ci-dessous comme guide de référence rapide.
| Format de fichier cible | API à utiliser | Remarques |
|---|---|---|
| `.xls` (hérité) | `PivotTable.AutoFormatType` | Valeurs de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Cette propriété est ignorée lors de l’enregistrement dans des formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.PivotTableStyleType` | Valeurs de `Aspose.Cells.PivotTableStyleType` (thèmes clairs et sombres, notamment les styles ajoutés dans Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez le style au moyen de `TableStyleElement.SetElementStyle(...)`. |
| Tous les formats (remplacement uniforme) | `PivotTable.FormatAll(Style)` | Raccourci qui remplace tous les autres paramètres de style dans l’ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez le classeur au format `.xlsx` et utilisez `PivotTableStyleType` pour les thèmes intégrés, ou `PivotTableStyleName` pour les thèmes personnalisés.

{{< app/cells/assistant language="cpp" >}}