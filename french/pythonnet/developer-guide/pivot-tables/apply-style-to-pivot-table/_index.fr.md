---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via .NET
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via .NET
description: Apprenez à appliquer des styles prédéfinis et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for Python via .NET, couvrant les autoformats XLS hérités, les styles nommés modernes d'Excel 2007+, les styles personnalisés de tableau croisé dynamique, et le raccourci FormatAll.
keywords: Aspose.Cells Python via .NET style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l'application à la fois des autoformats hérités de tableau croisé dynamique (destinés aux fichiers `.xls`) et des styles nommés ou personnalisés modernes de tableau croisé dynamique (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré en `.xlsx`, et dans ce cas c'est l'API de style moderne qui s'applique plutôt que l'API héritée.
- `PivotTable.pivot_table_style_type` sélectionne l'un des styles nommés prédéfinis (thèmes clairs et foncés, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `PivotTable.pivot_table_style_name` sélectionne un style personnalisé que vous définissez vous-même via `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Les styles personnalisés sont nécessaires dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que proposent les préréglages.
De plus, `PivotTable.format_all(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, supplantant tout ce qui a été défini via l'une ou l'autre des API de nom de style ci-dessus. Cela est utile lorsqu'une apparence uniforme est requise indépendamment du thème sous-jacent.

## **Appliquer un autoformat prédéfini XLS hérité**
`PivotTable.auto_format_type` accepte une valeur issue de l'énumération `aspose.cells.pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `REPORT_1` à `REPORT_10`, `CLASSIC`, et `TABLE_1` à `TABLE_10`.
L'exemple suivant charge un nouveau classeur, renseigne les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.REPORT_5`, puis enregistre le résultat en `.xls`.

{{% alert color="primary" %}}
**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour des **tableaux croisés dynamiques à une seule dimension** comportant uniquement des champs de ligne et des valeurs — ils n'intègrent aucune mise en forme pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), qui sont conçus pour la mise en page bidimensionnelle utilisée par Excel moderne.
{{% /alert %}}

```python
import aspose.cells as ac
# Scénario 1 : Appliquer un format automatique prédéfini XLS hérité
# API utilisée : PivotTable.AutoFormatType
# Format de fichier cible : .xls (hérité)
# Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Créer un nouveau classeur
workbook = ac.Workbook()
# Obtenir la première feuille de calcul
sheet = workbook.worksheets[0]
# Remplir les données sources avec une ligne d'en-tête (Fruit, Année, Montant)
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
# Assigner les champs : Fruit -> Lignes, Montant -> Données
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Appliquer le format automatique prédéfini XLS hérité "Report5"
# Remarque : Cette propriété n'a de sens que lors de l'enregistrement en .xls.
# Lorsqu'il est enregistré en .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
# et utilise ce que PivotTableStyleType / PivotTableStyleName spécifie.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5
# Enregistrer le classeur au format .xls hérité
workbook.save("output.xls")
```

## **Appliquer un style de tableau croisé dynamique prédéfini nommé moderne**

## **Définir et appliquer un style personnalisé de tableau croisé dynamique**
Les préréglages intégrés ne peuvent pas être modifiés. Chaque fois que vous devez modifier les couleurs, les bordures ou les polices, vous devez définir un style personnalisé de tableau croisé dynamique. Le flux de travail comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `table_styles` du classeur via `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WHOLE_TABLE` ou `GRAND_TOTAL_ROW`) via `table_style.table_style_elements.add(TableStyleElementType)`, puis affectez un `Style` à chaque élément via `table_style_element.set_element_style(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `PivotTable.pivot_table_style_name` sur le nom du style. N'utilisez pas `pivot_table_style_type` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}
`pivot_table_style_name` et `pivot_table_style_type` ne sont pas interchangeables. Utilisez `pivot_table_style_type` pour les préréglages intégrés, et `pivot_table_style_name` pour les styles personnalisés que vous avez définis via `add_pivot_table_style`. Définir les deux est sans danger, mais seul celui qui correspond à la source prévue est rendu.
{{% /alert %}}

Les valeurs `TableStyleElementType` disponibles incluent `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` et `PAGE_FIELD_VALUES`.
L'exemple suivant définit un style personnalisé de tableau croisé dynamique avec une fine bordure noire sur `WHOLE_TABLE` et une police rouge en gras sur `GRAND_TOTAL_ROW`, puis l'applique via `pivot_table_style_name` et enregistre en `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Remplir les données source : ligne d'en-tête + 9 lignes de données (A1:C10)
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
`PivotTable.format_all(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui avait été précédemment défini via `pivot_table_style_type` ou `pivot_table_style_name` est supplanté.

{{% alert color="primary" %}}
`format_all` supplante à la fois `pivot_table_style_type` et `pivot_table_style_name`. Utilisez-le uniquement lorsqu'une apparence uniforme, indépendante du thème, est requise sur l'ensemble du tableau croisé dynamique.
{{% /alert %}}

L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras, et de fines bordures noires sur tous les côtés, puis l'applique avec `format_all` et enregistre en `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Scénario 4 : Appliquer un seul Style à chaque cellule du tableau croisé dynamique en utilisant FormatAll
# API utilisée : PivotTable.FormatAll(Style)
# Format cible : .xlsx
# Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de style de tableau croisé dynamique
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Remplir les données source : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
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
# Affecter les champs du tableau croisé : Fruit -> zone Lignes, Year -> zone Colonnes, Amount -> zone Données
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Construire un Style qui sera forcé sur chaque cellule du tableau croisé dynamique
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
| `.xls` (hérité) | `PivotTable.auto_format_type` | Valeurs issues de `aspose.cells.pivot.PivotTableAutoFormatType` (par exemple `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoré lors de l'enregistrement aux formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.pivot_table_style_type` | Valeurs issues de `aspose.cells.PivotTableStyleType` (thèmes clairs/foncés, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurer via `table_style_element.set_element_style(...)`. |
| Tout format (substitution uniforme) | `PivotTable.format_all(Style)` | Raccourci qui supplante tout autre paramètre de style sur l'ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez en `.xlsx` et utilisez `pivot_table_style_type` pour les thèmes intégrés, ou `pivot_table_style_name` pour les thèmes personnalisés.

{{< app/cells/assistant language="python-net" >}}