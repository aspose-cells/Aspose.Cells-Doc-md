---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET
description: Apprenez à appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for .NET, couvrant les autoformats XLS hérités, les styles nommés modernes d'Excel 2007+, les styles de tableau croisé dynamique personnalisés et le raccourci FormatAll.
keywords: Aspose.Cells .NET style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l'application à la fois des autoformats hérités de tableau croisé dynamique (destinés aux fichiers `.xls`) et des styles nommés modernes ou personnalisés de tableau croisé dynamique (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé depuis un fichier `.xls` peut être réenregistré au format `.xlsx` ; dans ce cas, l'API de style moderne s'applique plutôt que l'API héritée.
- `PivotTable.PivotTableStyleType` sélectionne l'un des styles nommés intégrés (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces présélections sont en lecture seule.
- `PivotTable.PivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Les styles personnalisés sont requis lorsque vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que les présélections offrent.
De plus, `PivotTable.FormatAll(Style)` est un raccourci qui applique un objet `Style` unique à chaque cellule du tableau croisé dynamique et remplace tout ce qui a été défini via l'une des API de nom de style ci-dessus. Cela est utile lorsqu'une apparence uniforme est requise quel que soit le thème sous-jacent.

## **Appliquer un autoformat prédéfini XLS hérité**
`PivotTable.AutoFormatType` accepte une valeur de l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic`, et `Table1` à `Table10`.
L'exemple suivant charge un nouveau classeur, remplit les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.Report5` et enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}
**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour les **tableaux croisés dynamiques à une seule dimension** contenant uniquement des champs de ligne et des valeurs — ils n'ont pas de mise en forme intégrée pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les présélections modernes `PivotTableStyleType` du [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), qui sont conçues pour la disposition bidimensionnelle utilisée par les versions modernes d'Excel.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scénario 1 : Appliquer un autoformat prédéfini XLS hérité
// API utilisée : PivotTable.AutoFormatType
// Format de fichier cible : .xls (hérité)
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Créer un nouveau classeur
Workbook workbook = new Workbook();
// Obtenir la première feuille de calcul
Worksheet sheet = workbook.Worksheets[0];
// Remplir les données sources avec une ligne d'en-tête (Fruit, Année, Montant)
// et 9 lignes de données couvrant raisin, myrtille, kiwi, cerise sur 2020 et 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");
sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);
sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);
sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);
sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);
sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);
sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);
sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);
sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);
sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);
// Ajouter un tableau croisé dynamique à la cellule de destination E3, nommé "Pivot1", en utilisant la plage source A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// Assigner les champs : Fruit -> Lignes, Montant -> Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Appliquer l'autoformat prédéfini XLS hérité "Report5"
// Note : Cette propriété n'a de sens que lors de l'enregistrement en .xls.
// Lors de l'enregistrement en .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
// et utilise ce que spécifient PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// Enregistrer le classeur au format .xls hérité
workbook.Save("output.xls");
```

## **Appliquer un style de tableau croisé dynamique prédéfini nommé moderne**

## **Définir et appliquer un style de tableau croisé dynamique personnalisé**
Les présélections intégrées ne peuvent pas être modifiées. Lorsque vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style de tableau croisé dynamique personnalisé. Le flux de travail comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) via `TableStyle.TableStyleElements.Add(TableStyleElementType)`, puis attribuez un `Style` à chaque élément via `TableStyleElement.SetElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `PivotTable.PivotTableStyleName` sur le nom du style. N'utilisez pas `PivotTableStyleType` ici, car cette propriété sélectionne les présélections intégrées.

{{% alert color="primary" %}}
`PivotTableStyleName` et `PivotTableStyleType` ne sont pas interchangeables. Utilisez `PivotTableStyleType` pour les présélections intégrées, et `PivotTableStyleName` pour les styles personnalisés que vous avez définis via `AddPivotTableStyle`. Définir les deux est sans danger, mais seul celui qui correspond à la source prévue est rendu.
{{% /alert %}}

Les valeurs `TableStyleElementType` disponibles incluent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.
L'exemple suivant définit un style de tableau croisé dynamique personnalisé avec une fine bordure noire sur `WholeTable` et une police rouge en gras sur `GrandTotalRow`, puis l'applique via `PivotTableStyleName` et enregistre au format `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Remplir les données sources : ligne d'en-tête + 9 lignes de données (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);
// Ajouter un tableau croisé dynamique à partir de A1:C10, ancré à E3, nommé "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Étape 1 : enregistrer un nouveau style de tableau croisé dynamique personnalisé et capturer son index
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);
// Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge en gras
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est pour les préréglages intégrés)
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **Appliquer un seul style à chaque cellule de tableau croisé dynamique avec FormatAll**
`PivotTable.FormatAll(Style)` est un raccourci qui applique un objet `Style` unique à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui a été précédemment défini via `PivotTableStyleType` ou `PivotTableStyleName` est remplacé.

{{% alert color="primary" %}}
`FormatAll` remplace à la fois `PivotTableStyleType` et `PivotTableStyleName`. Utilisez-le uniquement lorsqu'une apparence uniforme, indépendante du thème, est requise pour l'ensemble du tableau croisé dynamique.
{{% /alert %}}

L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras et de fines bordures noires sur tous les côtés, puis l'applique avec `FormatAll` et enregistre au format `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scénario 4 : Appliquer un seul Style à chaque cellule de tableau croisé dynamique en utilisant FormatAll
// API utilisée : PivotTable.FormatAll(Style)
// Format cible : .xlsx
// Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de style de tableau croisé dynamique
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Remplir les données source : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);
// Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3, nom "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Assigner les champs du tableau croisé dynamique : Fruit -> zone Ligne, Year -> zone Colonne, Amount -> zone Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Construire un Style qui sera appliqué de force à chaque cellule du tableau croisé dynamique
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;
// Appliquer FormatAll : force ce style unique sur chaque cellule du tableau croisé dynamique,
// écrasant tout PivotTableStyleType / PivotTableStyleName précédemment défini
pivotTable.FormatAll(style);
// Enregistrer le classeur dans le format moderne .xlsx
workbook.Save("output.xlsx");
```

## **Quelle API de style dois-je utiliser ?**
Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.
| Format de fichier cible | API à utiliser | Notes |
|---|---|---|
| `.xls` (hérité) | `PivotTable.AutoFormatType` | Valeurs de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoré lors de l'enregistrement aux formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.PivotTableStyleType` | Valeurs de `Aspose.Cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | À utiliser lorsque les présélections intégrées ne suffisent pas. Configurer via `TableStyleElement.SetElementStyle(...)`. |
| Tout format (remplacement uniforme) | `PivotTable.FormatAll(Style)` | Raccourci qui remplace tous les autres paramètres de style sur l'ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez au format `.xlsx` et utilisez `PivotTableStyleType` pour les thèmes intégrés, ou `PivotTableStyleName` pour les thèmes personnalisés.

## Articles connexes
- [Add Pivot Table Row and Column Fields in Aspose.Cells for .NET](/cells/fr/net/pivot-table-add-row-and-column-fields/)
- [Manage Pivot Table Value Fields in Aspose.Cells for .NET](/cells/fr/net/manage-value-fields/)
- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/fr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}