---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET
description: Apprenez à appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for .NET, notamment les formats automatiques XLS hérités, les styles nommés modernes d'Excel 2007 et versions ultérieures, les styles personnalisés de tableaux croisés dynamiques et le raccourci FormatAll.
keywords: Aspose.Cells .NET style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l'application des formats automatiques hérités de tableaux croisés dynamiques (destinés aux fichiers `.xls`) ainsi que des styles modernes de tableaux croisés dynamiques, nommés ou personnalisés (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format depuis lequel il a été chargé. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré au format `.xlsx` ; dans ce cas, l'API de style moderne s'applique, et non l'API héritée.
- `PivotTable.PivotTableStyleType` sélectionne l'un des styles nommés intégrés (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `PivotTable.PivotTableStyleName` sélectionne un style personnalisé que vous définissez via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Les styles personnalisés sont nécessaires chaque fois que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà des possibilités offertes par les préréglages.
De plus, `PivotTable.FormatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, en supplantant tout style défini via l'une ou l'autre des API de nom de style ci-dessus. Cette méthode est utile lorsque vous avez besoin d'une apparence uniforme, quel que soit le thème sous-jacent.

## **Appliquer un format automatique prédéfini hérité pour XLS**
`PivotTable.AutoFormatType` accepte une valeur issue de l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic` et `Table1` à `Table10`.
L'exemple suivant charge un classeur vierge, renseigne les données d'exemple Fruit/Year/Amount, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.Report5`, puis enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}
**Pourquoi pas de champs de colonne ?** Les formats automatiques de type Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus pour Excel classique pour les **tableaux croisés dynamiques à une seule dimension**, comportant uniquement des champs de ligne et des valeurs — ils ne comportent aucune mise en forme intégrée pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` décrits dans [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), qui sont conçus pour la disposition bidimensionnelle utilisée par les versions modernes d'Excel.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scénario 1 : Appliquer un format automatique prédéfini XLS existant
// API utilisée : PivotTable.AutoFormatType
// Format de fichier cible : .xls (ancien)
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-cells/Aspose-Cells-for-.NET
// Créer un nouveau classeur
Workbook workbook = new Workbook();
// Obtenir la première feuille de calcul
Worksheet sheet = workbook.Worksheets[0];
// Remplir les données sources avec une ligne d'en-tête (Fruit, Year, Amount)
// et 9 lignes de données couvrant grape, blueberry, kiwi et cherry sur 2020 et 2021
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
// Ajouter un tableau croisé dynamique à la cellule E3, nommé "Pivot1", en utilisant la plage source A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// Attribuer les champs : Fruit -> Lignes, Amount -> Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Appliquer le format automatique prédéfini XLS existant "Report5"
// Remarque : cette propriété n'a de sens que lors de l'enregistrement au format .xls.
// Lors de l'enregistrement aux formats .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
// et utilise ce que spécifient PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// Enregistrer le classeur au format .xls existant
workbook.Save("output.xls");
```

## **Appliquer un style de tableau croisé dynamique moderne, intégré et nommé**

`PivotTable.PivotTableStyleType` sélectionne l’un des styles nommés intégrés qu’Excel 2007 a introduits pour les tableaux croisés dynamiques. L’énumération `PivotTableStyleType` expose trois familles de thèmes : la famille claire allant de `PivotTableStyleLight1` à `PivotTableStyleLight28`, la famille moyenne allant de `PivotTableStyleMedium1` à `PivotTableStyleMedium28` et la famille sombre allant de `PivotTableStyleDark1` à `PivotTableStyleDark28`. Elle définit également `None` et `Custom`. Les membres portant les numéros les plus élevés de chaque famille sont les styles ajoutés dans Excel 2017.
Ces préréglages sont en lecture seule. Dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que fournit un préréglage, vous devez plutôt définir un style de tableau croisé dynamique personnalisé, comme indiqué dans [Scénario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Pourquoi les préréglages modernes et non les formats automatiques de la série de rapports ?** Les valeurs `Report1` à `Report10` et `Table1` à `Table10` de `PivotTableAutoFormatType` sont antérieures aux champs de colonne des tableaux croisés dynamiques, elles ne comportent donc aucun style pour les en-têtes de champs de colonne et Excel affiche ces en-têtes sans mise en forme. Les préréglages `PivotTableStyleType` ont été conçus pour la disposition à deux dimensions utilisée par Excel moderne et appliquent le même style aux en-têtes de champs de ligne et de colonne.
{{% /alert %}}

Ce scénario réutilise le jeu de données Fruit/Year/Amount du Scénario 1, ajoute `Year` à la zone des colonnes à côté du champ de ligne `Fruit` via `PivotFieldType.Column`, applique le préréglage au thème sombre `PivotTableStyleDark1` avec `PivotTable.PivotTableStyleType`, puis enregistre le résultat au format `.xlsx` — le format pour lequel `PivotTableStyleType` est pertinent.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scénario 2 : appliquer à l’aide de PivotTableStyleType un style prédéfini moderne nommé pour Excel 2007+.
// Format de fichier cible : .xlsx. L’énumération PivotTableStyleType se trouve dans l’espace de noms Aspose.Cells
// (pas dans Aspose.Cells.Pivot) -- c’est pourquoi nous n’avons besoin d’aucune directive using supplémentaire.
// Référence GitHub : https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Ligne d’en-tête : Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 9 lignes de données contenant Fruit / Year / Amount
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
// Ajouter un tableau croisé dynamique à E3, nommé "Pivot1", avec A1:C10 comme source
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Attribuer les champs du tableau croisé dynamique : Fruit -> zone de lignes (Row), Year -> zone de colonnes (Column), Amount -> zone de données (Data)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Appliquer un style moderne de tableau croisé dynamique, prédéfini et nommé pour Excel 2007+.
// PivotTableStyleType est l’API correcte pour les fichiers .xlsx / .xlsm / .xlsb ; AutoFormatType
// est ignoré par Excel pour ces formats. PivotTableStyleDark1 appartient à la famille
// des thèmes sombres (PivotTableStyleDark1..PivotTableStyleDark28), et la même énumération expose également les
// thèmes clair/sombre plus récents d’Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;
// Enregistrer au format .xlsx moderne -- c’est le format pour lequel PivotTableStyleType est pris en compte.
workbook.Save("output.xlsx");
```
## **Définir et appliquer un style de tableau croisé dynamique personnalisé**
Les préréglages intégrés ne peuvent pas être modifiés. Lorsque vous souhaitez modifier les couleurs, les bordures ou les polices, vous devez définir un style de tableau croisé dynamique personnalisé. Le processus comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Cette méthode renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) via `TableStyle.TableStyleElements.Add(TableStyleElementType)`, puis attribuez un objet `Style` à chaque élément via `TableStyleElement.SetElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en affectant le nom du style à la propriété `PivotTable.PivotTableStyleName`. N'utilisez pas `PivotTableStyleType` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}
`PivotTableStyleName` et `PivotTableStyleType` ne sont pas interchangeables. Utilisez `PivotTableStyleType` pour les préréglages intégrés et `PivotTableStyleName` pour les styles personnalisés que vous avez définis via `AddPivotTableStyle`. Le fait de définir les deux propriétés n'a aucune incidence, mais seule celle qui correspond à la source du style est prise en compte lors du rendu.
Les valeurs disponibles de `TableStyleElementType` comprennent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.
L'exemple suivant définit un style de tableau croisé dynamique personnalisé avec une fine bordure noire sur l'élément `WholeTable` et une police rouge en gras sur l'élément `GrandTotalRow`, puis applique ce style via `PivotTableStyleName` et enregistre le classeur au format `.xlsx`.
{{% /alert %}}

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
// Ajouter un tableau croisé dynamique à partir de A1:C10, ancré en E3, nommé "Pivot1"
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

## **Appliquer un seul style à chaque cellule d'un tableau croisé dynamique avec FormatAll**
`PivotTable.FormatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de ligne et de colonne ainsi que les totaux. Tout style défini précédemment via `PivotTableStyleType` ou `PivotTableStyleName` est supplanté.

{{% alert color="primary" %}}
`FormatAll` supplant les propriétés `PivotTableStyleType` et `PivotTableStyleName`. Utilisez cette méthode uniquement lorsqu'une apparence uniforme et indépendante du thème est nécessaire sur l'ensemble du tableau croisé dynamique.
L'exemple suivant crée un objet `Style` avec un remplissage jaune uni, une police bleu foncé en gras et de fines bordures noires sur tous les côtés, puis l'applique à l'aide de `FormatAll` et enregistre le classeur au format `.xlsx`.
{{% /alert %}}

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scénario 4 : appliquer un seul Style à chaque cellule du tableau croisé dynamique à l’aide de FormatAll
// API utilisée : PivotTable.FormatAll(Style)
// Format cible : .xlsx
// Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de mise en forme de tableaux croisés dynamiques
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Remplir les données source : ligne d’en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
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
// Affecter les champs du tableau croisé dynamique : Fruit -> zone Ligne, Year -> zone Colonne, Amount -> zone Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Créer un Style qui sera imposé à chaque cellule du tableau croisé dynamique
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
// Appliquer FormatAll : impose ce style unique à chaque cellule du tableau croisé dynamique,
// en remplaçant tout PivotTableStyleType / PivotTableStyleName défini précédemment
pivotTable.FormatAll(style);
// Enregistrer le classeur au format .xlsx moderne
workbook.Save("output.xlsx");
```

## **Quelle API de style devez-vous utiliser ?**
Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez le classeur. Utilisez le tableau ci-dessous comme référence rapide.
| Format de fichier cible | API à utiliser | Notes |
|---|---|---|
| `.xls` (hérité) | `PivotTable.AutoFormatType` | Valeurs de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par exemple, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). La propriété est ignorée lors de l'enregistrement dans des formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.PivotTableStyleType` | Valeurs de `Aspose.Cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les styles ajoutés dans Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez le style via `TableStyleElement.SetElementStyle(...)`. |
| Tous les formats (substitution uniforme) | `PivotTable.FormatAll(Style)` | Raccourci qui supplantе tous les autres paramètres de style sur l'ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez le classeur au format `.xlsx` et utilisez `PivotTableStyleType` pour les thèmes intégrés, ou `PivotTableStyleName` pour les thèmes personnalisés.

## Articles connexes
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/pivot-table-add-row-and-column-fields/)
- [Gérer les champs de valeur des tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/manage-value-fields/)
- [Actualiser les tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}