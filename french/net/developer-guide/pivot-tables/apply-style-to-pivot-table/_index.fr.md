---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells pour .NET
linktitle: Appliquer des styles aux tableaux croisés dynamiques
description: Apprenez à appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for .NET, en couvrant les anciens autoformats XLS, les styles nommés modernes d'Excel 2007+, les styles personnalisés de tableau croisé dynamique et le raccourci FormatAll.
keywords: Aspose.Cells .NET style tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'application à la fois des anciens autoformats de tableau croisé dynamique (destinés aux fichiers `.xls`) et des styles modernes nommés ou personnalisés de tableau croisé dynamique (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API à appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.

{{% /alert %}}

## **Introduction**

Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré au format `.xlsx`, et dans ce cas, c'est l'API de style moderne qui s'applique plutôt que l'ancienne.

Pour la sortie au format `.xls` hérité, utilisez la propriété `PivotTable.AutoFormatType` conjointement avec l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Cette API correspond au sélecteur d'autoformat qu'Excel classique proposait pour les tableaux croisés dynamiques.

Pour la sortie aux formats modernes `.xlsx`, `.xlsm` et `.xlsb`, deux variantes d'API de style sont disponibles :

- `PivotTable.PivotTableStyleType` sélectionne l'un des styles nommés intégrés (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `PivotTable.PivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Les styles personnalisés sont requis dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que proposent les préréglages.

De plus, `PivotTable.FormatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, en supplantant tout ce qui a été défini via l'une ou l'autre des API de nom de style ci-dessus. Cela est utile lorsqu'une apparence uniforme est requise, indépendamment du thème sous-jacent.

## **Application d'un autoformat prédéfini XLS hérité**

`PivotTable.AutoFormatType` accepte une valeur issue de l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic` et `Table1` à `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` n'est pris en compte que lorsque le classeur est enregistré au format `.xls`. Lorsque le même classeur est enregistré au format `.xlsx`, `.xlsm` ou `.xlsb`, Excel ignore cette propriété et se rabat sur les paramètres `PivotTableStyleType` et `PivotTableStyleName`.

{{% /alert %}}

L'exemple suivant charge un nouveau classeur, renseigne les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.Report5` et enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}

**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour des **tableaux croisés dynamiques à une dimension** avec uniquement des champs de ligne et des valeurs — ils n'ont pas de style intégré pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du Scénario 2 ci-dessous, qui sont conçus pour la disposition bidimensionnelle qu'utilise Excel moderne.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scénario 1 : Appliquer un format automatique prédéfini XLS hérité
// API utilisée : PivotTable.AutoFormatType
// Format de fichier cible : .xls (hérit)
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Créer un nouveau classeur
Workbook workbook = new Workbook();

// Obtenir la première feuille de calcul
Worksheet sheet = workbook.Worksheets[0];

// Remplir les données sources avec une ligne d'en-tête (Fruit, Année, Montant)
// et 9 lignes de données couvrant raisin, myrtille, kiwi, cerise pour 2020 et 2021
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

// Assigner les champs : Fruit -> Lignes, Année -> Colonnes, Montant -> Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Appliquer le format automatique prédéfini XLS hérité "Report5"
// Remarque : Cette propriété n'est significative que lors de l'enregistrement en .xls.
// Lors de l'enregistrement en .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
// et utilise ce que spécifie PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Enregistrer le classeur au format .xls hérité
workbook.Save("output.xls");
```

## **Application d'un style prédéfini nommé moderne de tableau croisé dynamique**

`PivotTable.PivotTableStyleType` accepte une valeur issue de l'énumération `Aspose.Cells.PivotTableStyleType`. L'énumération couvre les thèmes clairs `PivotTableStyleLight1` à `PivotTableStyleLight28` et les thèmes sombres `PivotTableStyleDark1` à `PivotTableStyleDark28`. Les styles ajoutés dans Excel 2017 (la deuxième vague de thèmes clairs et sombres) sont accessibles via la même énumération.

C'est l'API recommandée pour tout format de fichier moderne. Contrairement à l'autoformat hérité, le style sélectionné ici est rendu fidèlement par Excel et survit aux aller-retours via d'autres outils Office.

L'exemple suivant utilise les mêmes données Fruit/Année/Montant, crée un tableau croisé dynamique identique, applique `PivotTableStyleDark1` et enregistre le classeur au format `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scénario 2 : Appliquer un style prédéfini nommé moderne d'Excel 2007+ en utilisant PivotTableStyleType.
// Format de fichier cible : .xlsx. L'énumération PivotTableStyleType se trouve dans l'espace de noms Aspose.Cells
// (pas dans Aspose.Cells.Pivot) — c'est pourquoi nous n'avons pas besoin d'un using supplémentaire pour cela.
// Référence GitHub : https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Ligne d'en-tête : Fruit / Année / Montant
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 lignes de données de Fruit / Année / Montant
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// Ajouter un tableau croisé dynamique à E3 nommé "Pivot1", provenant de A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Assigner les champs du tableau croisé dynamique : Fruit -> zone de ligne, Année -> zone de colonne, Montant -> zone de données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Appliquer un style de tableau croisé dynamique prédéfini nommé moderne d'Excel 2007+.
// PivotTableStyleType est l'API correcte pour les fichiers .xlsx / .xlsm / .xlsb ; AutoFormatType
// est ignoré par Excel pour ces formats. PivotTableStyleDark1 appartient à la famille
// des thèmes sombres (PivotTableStyleDark1..PivotTableStyleDark28), et la même énumération expose également les
// thèmes plus récents d'Excel 2017 clair/sombre (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Enregistrer en tant que .xlsx moderne — c'est le format pour lequel PivotTableStyleType a du sens.
workbook.Save("output.xlsx");
```

## **Définition et application d'un style personnalisé de tableau croisé dynamique**

Les préréglages intégrés ne peuvent pas être modifiés. Dès que vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style personnalisé de tableau croisé dynamique. Le flux de travail comporte trois étapes :

1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) via `TableStyle.TableStyleElements.Add(TableStyleElementType)`, puis attribuez un `Style` à chaque élément via `TableStyleElement.SetElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `PivotTable.PivotTableStyleName` sur le nom du style. N'utilisez pas `PivotTableStyleType` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}

`PivotTableStyleName` et `PivotTableStyleType` ne sont pas interchangeables. Utilisez `PivotTableStyleType` pour les préréglages intégrés, et `PivotTableStyleName` pour les styles personnalisés que vous avez définis via `AddPivotTableStyle`. Définir les deux est sans incidence, mais seul celui qui correspond à la source prévue est rendu.

{{% /alert %}}

Les valeurs `TableStyleElementType` disponibles incluent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.

L'exemple suivant définit un style personnalisé de tableau croisé dynamique avec une bordure noire fine sur `WholeTable` et une police rouge en gras sur `GrandTotalRow`, puis l'applique via `PivotTableStyleName` et enregistre au format `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Remplir les données source : ligne d'en-tête + 9 lignes de données (A1:C10)
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

// Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est destiné aux préréglages intégrés)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **Application d'un style unique à chaque cellule du tableau croisé dynamique avec FormatAll**

`PivotTable.FormatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui a été défini précédemment via `PivotTableStyleType` ou `PivotTableStyleName` est supplanté.

{{% alert color="primary" %}}

`FormatAll` supplante à la fois `PivotTableStyleType` et `PivotTableStyleName`. Utilisez-le uniquement lorsqu'une apparence uniforme, indépendante du thème, est requise sur l'ensemble du tableau croisé dynamique.

{{% /alert %}}

L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras et des bordures noires fines sur tous les côtés, puis l'applique avec `FormatAll` et enregistre au format `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scénario 4 : Appliquer un seul Style à chaque cellule de tableau croisé dynamique en utilisant FormatAll
// API utilisée : PivotTable.FormatAll(Style)
// Format cible : .xlsx
// Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de mise en forme de tableaux croisés dynamiques

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Remplir les données sources : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
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

// Assigner les champs du tableau croisé : Fruit -> zone de ligne, Year -> zone de colonne, Amount -> zone de données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Construire un Style qui sera appliqué de force sur chaque cellule du tableau croisé dynamique
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

// Enregistrer le classeur au format moderne .xlsx
workbook.Save("output.xlsx");
```

## **Quelle API de style dois-je utiliser ?**

Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.

| Format de fichier cible | API à utiliser | Notes |
|---|---|---|
| `.xls` (hérité) | `PivotTable.AutoFormatType` | Valeurs issues de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorée lors de l'enregistrement aux formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.PivotTableStyleType` | Valeurs issues de `Aspose.Cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez via `TableStyleElement.SetElementStyle(...)`. |
| Tout format (substitution uniforme) | `PivotTable.FormatAll(Style)` | Raccourci qui supplante tout autre paramètre de style sur l'ensemble du tableau croisé dynamique. |

En cas de doute, enregistrez au format `.xlsx` et utilisez `PivotTableStyleType` pour les thèmes intégrés, ou `PivotTableStyleName` pour les thèmes personnalisés.

{{< app/cells/assistant language="csharp" >}}