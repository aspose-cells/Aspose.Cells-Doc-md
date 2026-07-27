---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Ajouter des champs de filtre
description: Apprenez à ajouter et configurer des champs de filtre dans des tableaux croisés dynamiques à l'aide d'Aspose.Cells for Python via .NET, y compris l'ajout de champs de filtre, le filtrage en sélection unique et le filtrage en sélection multiple.
keywords: Aspose.Cells, Python via .NET, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/python-net/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API de haut niveau pratique ou via la collection `page_fields` de bas niveau, et vous pouvez piloter le filtre en mode sélection unique, l'effacer pour afficher chaque élément de page, ou basculer le champ en sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de page à la fois via l'interface à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**

Un champ de filtre est un champ croisé dynamique qui contrôle *quel sous-ensemble* des données source le corps du tableau croisé dynamique affiche. Les utilisateurs finaux le voient comme une liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et sélectionner l'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page sont synthétisés. Un champ croisé dynamique devient un champ de filtre lorsqu'il est enregistré en tant que `PivotFieldType.PAGE` plutôt que `PivotFieldType.ROW`, `PivotFieldType.COLUMN` ou `PivotFieldType.DATA`.

Un champ de filtre peut fonctionner selon deux comportements. Dans le comportement par défaut en **sélection unique**, un seul élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique synthétise exactement un sous-ensemble. Dans le comportement en **sélection multiple**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique synthétise l'union de chaque élément de page coché. Le même champ source peut être déplacé d'avant en arrière entre ces comportements en activant ou désactivant une seule propriété.

Aspose.Cells for Python via .NET expose deux façons équivalentes d'enregistrer un champ de filtre. L'API de haut niveau est `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `PivotTable.page_fields.add(PivotField)`, qui est utilisée lorsque vous détenez déjà une référence `PivotField` et souhaitez ajouter la même instance de champ à la zone de filtre. Les deux API finissent par remplir la même collection `page_fields`, et le reste de cet article montre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de filtre**

Il existe deux manières d'enregistrer un champ croisé dynamique dans la zone de filtre. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et est pratique lorsque le même objet champ doit être réutilisé dans plusieurs zones du tableau croisé dynamique. Les deux appels placent le champ dans `PivotTable.page_fields`, après quoi il apparaît comme la liste déroulante de page en haut du tableau croisé dynamique rendu.

### Ajout d'un champ de filtre avec add_field_to_area

L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone de ligne, `Amount` dans la zone de données et `Year` dans la zone de filtre, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import aspose.cells as ac

# Créer un nouveau classeur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Configurer la ligne d'en-tête
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Remplir 9 lignes de données d'exemple : Fruit, Year, Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Ajouter un tableau croisé dynamique ancré à la cellule E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Ajouter des champs à leurs zones : Fruit comme Ligne, Amount comme Données, Year comme champ de Page
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Actualiser et calculer les données du tableau croisé dynamique
pivot_table.calculate_data()

# Enregistrer le classeur
workbook.save("pageFieldSample.xlsx")
```

### Ajout d'un champ de filtre avec page_fields.add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la passer directement à `PivotTable.page_fields.add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final dans la zone de filtre est remplacé par l'appel d'API de bas niveau.

```python
import aspose.cells as ac

# — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
#   le scénario 1a (données Fruit/Année/Montant, pivot à E3, Fruit→Ligne,
#   Montant→Données). Ci-dessous, nous obtenons le PivotField Année à partir
#   de la collection BaseFields et le passons à PageFields.Add — l'alternative
#   de bas niveau à AddFieldToArea. Le résultat est fonctionnellement
#   identique au scénario 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# En-têtes
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Données d'exemple (9 lignes)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# Ajoute le tableau croisé dynamique à E3 couvrant A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit -> Ligne, Montant -> Données (Année ira dans Page ci-dessous)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Approche de bas niveau : récupère le PivotField Année existant depuis BaseFields
# et l'enregistre dans la zone Page via PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Actualise pour que le nouveau champ de page soit reflété dans le classeur enregistré
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Filtrage en sélection unique (affichage d'un seul élément de page)**

Dans le comportement par défaut en sélection unique, le champ de filtre s'affiche sous forme de liste déroulante unique et l'entier `PivotField.current_page_item` sélectionne l'élément de page qui pilote le corps du tableau croisé dynamique. L'affectation d'un index spécifique sélectionne cet élément unique ; l'affectation de la sentinelle spéciale `0x7FFD` (32765 en décimal) efface le filtre afin que chaque élément de page soit synthétisé en une seule fois. La sélection unique est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments

Définir `current_page_item` sur la valeur magique `0x7FFD` équivaut à effacer le filtre : le corps du tableau croisé dynamique synthétise chaque élément de page comme si aucun filtre n'était appliqué.

```python
import aspose.cells as ac

# Créer un nouveau classeur
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Remplir les données Fruit/Année/Montant
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# Créer un tableau croisé dynamique à E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Configurer les champs du tableau croisé dynamique : Fruit→Ligne, Montant→Données, Année→Page
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# Effacer le filtre de page pour que chaque élément du champ de page soit visible.
# 0x7FFD (décimal 32765) est la valeur sentinelle spéciale qui signifie "tous les éléments" —
# équivalent à sélectionner "(Tous)" dans le menu déroulant du champ de page d'Excel.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Affichage d'un élément spécifique

Définir `current_page_item` sur un index réel sélectionne uniquement cet élément de page. L'index est la position de l'élément dans la liste triée des éléments du champ de filtre, donc par exemple `1` sélectionne le deuxième élément après le tri.

```python
import aspose.cells as ac

# Créer un classeur
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Ajouter des données d'exemple (Fruit/Année/Montant)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Ajouter un tableau croisé dynamique à E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Ajouter des champs : Fruit→Ligne, Montant→Données, Année→Page
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Opérations spécifiques au champ de page
pivot_table.page_fields[0].current_page_item = 1  # 1 = deuxième élément dans l'ordre trié (par ex. "2021")

# Actualiser et calculer le tableau croisé dynamique
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Filtrage en sélection multiple**

Le filtrage en sélection multiple transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner plusieurs éléments de page simultanément. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.is_multiple_item_selection_allowed` doit être défini sur `True` avant que l'interface de sélection multiple ne prenne effet. Une fois activée, `PivotItem.is_hidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, ce qui vous permet soit d'afficher chaque élément, soit de n'autoriser que des éléments spécifiques.

Le code ci-dessous active la sélection multiple sur le même champ de filtre Year construit dans le scénario 1a, puis montre deux schémas : la partie A révèle chaque élément de page en laissant `is_hidden` défini sur `False` pour chaque entrée, tandis que la partie B n'autorise que les valeurs source que vous choisissez et masque tout le reste via un bloc `if` / `elif` qui teste `pivot_items[i].get_string_value()`.

```python
import aspose.cells as ac

# — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
#   Scénario 1a (données Fruit/Année/Montant, pivot en E3, Fruit→Ligne,
#   Montant→Données, Année→Page via AddFieldToArea).
#   Ci-dessous, nous appliquons un filtrage multi-sélection sur le champ de page.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Données d'exemple : Fruit | Année | Montant
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Activer la multi-sélection sur le champ de page
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Partie B — sélectionner uniquement des éléments spécifiques par valeur source
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Remarque :** Lors de l'utilisation du filtrage en sélection multiple via `PivotItem.is_hidden`, **au moins un `PivotItem` doit rester visible** (`is_hidden == False`). Si chaque élément est masqué, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste d'autorisation en sélection multiple inclut au moins un élément de vos données source.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans avoir à lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (cas le plus courant) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | Haut niveau, une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous avez déjà un objet `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | Utilisez lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de page (mode par défaut) | `PivotField.current_page_item` | définir sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / effacer le filtre | `PivotField.current_page_item` | définir sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface de sélection multiple dans Excel | `PivotField.is_multiple_item_selection_allowed` | définir sur `True` | Requis avant que les appels à `is_hidden` ne prennent effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.is_hidden` | définir par élément | Au moins un élément doit rester visible (`is_hidden == False`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage en sélection multiple. Si chaque `PivotItem` d'un champ de filtre à sélection multiple est masqué, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste d'autorisation à partir de vos données source afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur toutes les machines.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}
