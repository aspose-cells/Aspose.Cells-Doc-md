---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells pour .NET
linktitle: Appliquer des styles aux tableaux croisés dynamiques
description: Apprenez à appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for Python via .NET, couvrant les autoformats XLS hérités, les styles nommés modernes Excel 2007+, les styles de tableau croisé dynamique personnalisés et le raccourci FormatAll.
keywords: Aspose.Cells Python via .NET style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'application des autoformats hérités pour les tableaux croisés dynamiques (destinés aux fichiers `.xls`) ainsi que des styles nommés modernes ou personnalisés pour les tableaux croisés dynamiques (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API à appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.

{{% /alert %}}

## **Introduction**

Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré au format `.xlsx`, et dans ce cas l'API de style moderne s'applique plutôt que celle héritée.

Pour la sortie au format `.xls` hérité, utilisez la propriété `PivotTable.auto_format_type` conjointement avec l'énumération `aspose.cells.pivot.PivotTableAutoFormatType`. Cette API correspond au sélecteur d'autoformat que la version classique d'Excel proposait pour les tableaux croisés dynamiques.

Pour les sorties modernes `.xlsx`, `.xlsm` et `.xlsb`, deux variantes d'API de style sont disponibles :

- `PivotTable.pivot_table_style_type` sélectionne l'un des styles nommés intégrés (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `PivotTable.pivot_table_style_name` sélectionne un style personnalisé que vous définissez vous-même via `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Les styles personnalisés sont nécessaires lorsque vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que les préréglages offrent.

De plus, `PivotTable.format_all(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, écrasant tout ce qui a été défini via l'une des API de nom de style ci-dessus. Cela est utile lorsqu'une apparence uniforme est requise indépendamment du thème sous-jacent.

## **Appliquer un autoformat prédéfini XLS hérité**

`PivotTable.auto_format_type` accepte une valeur de l'énumération `aspose.cells.pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `REPORT_1` à `REPORT_10`, `CLASSIC`, et `TABLE_1` à `TABLE_10`.

{{% alert color="primary" %}}

`auto_format_type` n'est pris en compte que lorsque le classeur est enregistré au format `.xls`. Lorsque le même classeur est enregistré au format `.xlsx`, `.xlsm` ou `.xlsb`, Excel ignore cette propriété et se rabat sur les paramètres `pivot_table_style_type` et `pivot_table_style_name`.

{{% /alert %}}

L'exemple suivant charge un nouveau classeur, remplit les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.REPORT_5` et enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}

**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour des **tableaux croisés dynamiques à une dimension** avec uniquement des champs de ligne et des valeurs — ils n'ont pas de style intégré pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du Scénario 2 ci-dessous, qui sont conçus pour la disposition bidimensionnelle qu'utilise Excel moderne.

{{% /alert %}}

```python
import aspose.cells as ac

# Scénario 1 : Appliquer un autoformat prédéfini XLS existant
# API utilisée : PivotTable.AutoFormatType
# Format de fichier cible : .xls (ancien)
# Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Créer un nouveau classeur
workbook = ac.Workbook()

# Obtenir la première feuille de calcul
sheet = workbook.worksheets[0]

# Remplir les données source avec une ligne d'en-tête (Fruit, Year, Amount)
# et 9 lignes de données couvrant raisin, myrtille, kiwi, cerise sur 2020 et 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# Ajouter un tableau croisé dynamique à la cellule de destination E3, nommé "Pivot1", en utilisant la plage source A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Affecter les champs : Fruit -> Lignes, Year -> Colonnes, Amount -> Données
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Appliquer l'autoformat prédéfini XLS existant "Report5"
# Remarque : Cette propriété n'a de sens que lors de l'enregistrement au format .xls.
# Lors de l'enregistrement au format .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
# et utilise ce que spécifient PivotTableStyleType / PivotTableStyleName.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Enregistrer le classeur au format .xls existant
workbook.save("output.xls")
```

## **Appliquer un style de tableau croisé dynamique prédéfini nommé moderne**

`PivotTable.pivot_table_style_type` accepte une valeur de l'énumération `aspose.cells.PivotTableStyleType`. L'énumération couvre les thèmes clairs `PIVOT_TABLE_STYLE_LIGHT_1` à `PIVOT_TABLE_STYLE_LIGHT_28` et les thèmes sombres `PIVOT_TABLE_STYLE_DARK_1` à `PIVOT_TABLE_STYLE_DARK_28`. Les styles ajoutés dans Excel 2017 (la deuxième vague de thèmes clairs et sombres) sont accessibles via la même énumération.

Il s'agit de l'API recommandée pour tout format de fichier moderne. Contrairement à l'autoformat hérité, le style sélectionné ici est rendu fidèlement par Excel et survit aux aller-retours avec d'autres outils Office.

L'exemple suivant utilise les mêmes données Fruit/Année/Montant, crée un tableau croisé dynamique identique, applique `PIVOT_TABLE_STYLE_DARK_1` et enregistre le classeur au format `.xlsx`.

```python
import aspose.cells as ac

# Scénario 2 : Appliquer un style prédéfini nommé moderne d'Excel 2007+ en utilisant PivotTableStyleType.
# Format de fichier cible : .xlsx. L'énumération PivotTableStyleType se trouve dans l'espace de noms Aspose.Cells
# (pas dans Aspose.Cells.Pivot) — c'est pourquoi nous n'avons pas besoin d'un using supplémentaire pour cela.
# Référence GitHub : https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Ligne d'en-tête : Fruit / Année / Montant
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 lignes de données de Fruit / Année / Montant
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# Ajouter un tableau croisé dynamique en E3 nommé "Pivot1", provenant de A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assigner les champs du tableau croisé dynamique : Fruit -> Zone de ligne, Année -> Zone de colonne, Montant -> Zone de données
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Appliquer un style de tableau croisé dynamique prédéfini nommé moderne d'Excel 2007+.
# PivotTableStyleType est l'API correcte pour les fichiers .xlsx / .xlsm / .xlsb ; AutoFormatType
# est ignoré par Excel pour ces formats. PivotTableStyleDark1 appartient à la famille
# des thèmes sombres (PivotTableStyleDark1..PivotTableStyleDark28), et la même énumération expose également les
# thèmes plus récents d'Excel 2017 clairs/sombres (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Enregistrer en tant que .xlsx moderne — c'est le format pour lequel PivotTableStyleType est significatif.
workbook.save("output.xlsx")
```

## **Définir et appliquer un style de tableau croisé dynamique personnalisé**

Les préréglages intégrés ne peuvent pas être modifiés. Chaque fois que vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style de tableau croisé dynamique personnalisé. Le flux de travail comporte trois étapes :

1. Ajoutez un style personnalisé à la collection `table_styles` du classeur via `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WHOLE_TABLE` ou `GRAND_TOTAL_ROW`) via `table_style.table_style_elements.add(TableStyleElementType)`, puis affectez un `Style` à chaque élément via `table_style_element.set_element_style(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `PivotTable.pivot_table_style_name` sur le nom du style. N'utilisez pas `pivot_table_style_type` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}

`pivot_table_style_name` et `pivot_table_style_type` ne sont pas interchangeables. Utilisez `pivot_table_style_type` pour les préréglages intégrés, et `pivot_table_style_name` pour les styles personnalisés que vous avez définis via `add_pivot_table_style`. Définir les deux est sans danger, mais seul celui correspondant à la source prévue est rendu.

{{% /alert %}}

Les valeurs `TableStyleElementType` disponibles incluent `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` et `PAGE_FIELD_VALUES`.

L'exemple suivant définit un style de tableau croisé dynamique personnalisé avec une bordure noire fine sur `WHOLE_TABLE` et une police rouge en gras sur `GRAND_TOTAL_ROW`, puis l'applique via `pivot_table_style_name` et enregistre au format `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Remplir les données sources : ligne d'en-tête + 9 lignes de données (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# Ajouter un tableau croisé dynamique à partir de A1:C10, ancré à E3, nommé "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Étape 1 : enregistrer un nouveau style de tableau croisé dynamique personnalisé et capturer son index
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge en gras
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est pour les préréglages intégrés)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **Appliquer un seul style à chaque cellule du tableau croisé dynamique avec FormatAll**

`PivotTable.format_all(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui a été précédemment défini via `pivot_table_style_type` ou `pivot_table_style_name` est écrasé.

{{% alert color="primary" %}}

`format_all` écrase à la fois `pivot_table_style_type` et `pivot_table_style_name`. Utilisez-le uniquement lorsqu'une apparence uniforme, indépendante du thème, est requise sur l'ensemble du tableau croisé dynamique.

{{% /alert %}}

L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras et des bordures noires fines sur tous les côtés, puis l'applique avec `format_all` et enregistre au format `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Scénario 4 : Appliquer un seul Style à chaque cellule de tableau croisé dynamique en utilisant FormatAll
# API utilisée : PivotTable.FormatAll(Style)
# Format cible : .xlsx
# Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de mise en forme de tableau croisé dynamique

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Remplir les données sources : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3, nom "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assigner les champs du tableau croisé dynamique : Fruit -> zone Lignes, Year -> zone Colonnes, Amount -> zone Données
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Construire un Style qui sera appliqué de force sur chaque cellule du tableau croisé dynamique
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# Appliquer FormatAll : force ce style unique sur chaque cellule du tableau croisé dynamique,
# écrasant tout PivotTableStyleType / PivotTableStyleName précédemment défini
pivot_table.format_all(style)

# Enregistrer le classeur au format moderne .xlsx
workbook.save("output.xlsx")
```

## **Quelle API de style dois-je utiliser ?**

Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.

| Format de fichier cible | API à utiliser | Notes |
|---|---|---|
| `.xls` (hérité) | `PivotTable.auto_format_type` | Valeurs de `aspose.cells.pivot.PivotTableAutoFormatType` (par ex. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoré lors de l'enregistrement dans des formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.pivot_table_style_type` | Valeurs de `aspose.cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez via `table_style_element.set_element_style(...)`. |
| Tout format (substitution uniforme) | `PivotTable.format_all(Style)` | Raccourci qui écrase tous les autres paramètres de style sur l'ensemble du tableau croisé dynamique. |

En cas de doute, enregistrez au format `.xlsx` et utilisez `pivot_table_style_type` pour les thèmes intégrés, ou `pivot_table_style_name` pour les thèmes personnalisés.

{{< app/cells/assistant language="python-net" >}}