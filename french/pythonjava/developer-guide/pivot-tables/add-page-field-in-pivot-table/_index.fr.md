---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Ajouter des champs de filtre
description: Apprenez à ajouter et configurer des champs de filtre dans les tableaux croisés dynamiques à l'aide d'Aspose.Cells for Python via Java, y compris l'ajout de champs de filtre, le filtrage à sélection unique et le filtrage à sélection multiple.
keywords: Aspose.Cells, Python, Java, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/python-java/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API de haut niveau pratique ou via la collection de bas niveau `page_fields`, et vous pouvez piloter le filtre en mode sélection unique, le réinitialiser pour afficher chaque élément de page, ou basculer le champ vers la sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de page à la fois via l'interface à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**

Un champ de filtre est un champ de tableau croisé dynamique qui contrôle *quel sous-ensemble* des données sources le corps du tableau croisé dynamique affiche. Les utilisateurs finaux le voient comme une liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et la sélection de l'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page sont résumés. Un champ de tableau croisé dynamique devient un champ de filtre lorsqu'il est enregistré en tant que `PivotFieldType.PAGE` plutôt que `PivotFieldType.ROW`, `PivotFieldType.COLUMN` ou `PivotFieldType.DATA`.

Un champ de filtre peut fonctionner selon deux comportements. Dans le comportement par défaut de **sélection unique**, un seul élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique résume exactement un sous-ensemble. Dans le comportement de **sélection multiple**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique résume l'union de chaque élément de page coché. Le même champ source peut être basculé d'avant en arrière entre ces comportements en activant une seule propriété.

Aspose.Cells for Python via Java expose deux manières équivalentes d'enregistrer un champ de filtre. L'API de haut niveau est `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `PivotTable.page_fields.add(PivotField)`, qui est utilisée lorsque vous détenez déjà une référence `PivotField` et souhaitez ajouter la même instance de champ à la zone de filtre. Les deux API finissent par alimenter la même collection `page_fields`, et le reste de cet article montre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de filtre**

Il existe deux manières d'enregistrer un champ de tableau croisé dynamique dans la zone de filtre. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne de caractères et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et est pratique lorsque le même objet de champ doit être réutilisé dans plusieurs zones de tableau croisé dynamique. Les deux appels placent le champ dans `PivotTable.page_fields`, après quoi il apparaît comme la liste déroulante de page en haut du tableau croisé dynamique rendu.

### Ajout d'un champ de filtre avec add_field_to_area

L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique à la cellule E3 avec `Fruit` sur la zone de lignes, `Amount` sur la zone de données et `Year` sur la zone de filtre, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Créer un nouveau classeur
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Configurer la ligne d'en-tête
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Remplir 9 lignes de données d'exemple : Fruit, Année, Montant
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Ajouter un tableau croisé dynamique ancré à la cellule E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Ajouter des champs à leurs zones : Fruit comme Ligne, Montant comme Données, Année comme Page
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Actualiser et calculer les données du tableau croisé dynamique
pivotTable.calculateData()

# Enregistrer le classeur
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Ajout d'un champ de filtre avec page_fields.add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la passer directement à `PivotTable.page_fields.add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final dans la zone de filtre est remplacé par l'appel d'API de bas niveau.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
#   Scénario 1a (données Fruit/Année/Montant, tableau croisé à E3, Fruit→Ligne,
#   Montant→Données). Ci-dessous, nous obtenons le PivotField Année de la
#   collection BaseFields et le passons à PageFields.Add — l'
#   alternative de bas niveau à AddFieldToArea. Le résultat est
#   fonctionnellement identique au Scénario 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# En-têtes
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Données d'exemple (9 lignes)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Ajouter un tableau croisé dynamique à E3 couvrant A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> Ligne, Montant -> Données (Année ira à Page ci-dessous)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Approche de bas niveau : récupérer le PivotField Année existant depuis BaseFields
# et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Actualiser pour que le nouveau champ de page soit reflété dans le classeur enregistré
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Filtrage à sélection unique (affichage d'un élément de page)**

Dans le comportement par défaut de sélection unique, le champ de filtre est rendu sous forme de liste déroulante unique et l'entier `PivotField.current_page_item` sélectionne quel élément de page pilote le corps du tableau croisé dynamique. L'assignation d'un index spécifique sélectionne cet élément unique ; l'assignation de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) réinitialise le filtre de sorte que chaque élément de page soit résumé simultanément. La sélection unique est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments

Définir `current_page_item` sur la valeur magique `0x7FFD` équivaut à effacer le filtre : le corps du tableau croisé dynamique résume chaque élément de page comme si aucun filtre n'était appliqué.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Créer un nouveau classeur
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Remplir les données Fruit/Année/Montant
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Créer un tableau croisé dynamique à E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Configurer les champs du tableau croisé dynamique : Fruit→Ligne, Amount→Données, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.calculateData()

# Effacer le filtre de page afin que chaque élément du champ de page soit visible.
# 0x7FFD (décimal 32765) est la valeur sentinelle spéciale qui signifie "tous les éléments" —
# équivalent à sélectionner "(Tous)" dans le menu déroulant du champ de page d'Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Affichage d'un élément spécifique

Définir `current_page_item` sur un index réel sélectionne uniquement cet élément de page. L'index est la position de l'élément dans la liste triée des éléments du champ de filtre, donc par exemple `1` sélectionne le deuxième élément après le tri.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Créer le classeur
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Ajouter des données d'exemple (Fruit/Année/Montant)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Ajouter un tableau croisé dynamique à E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Ajouter des champs : Fruit→Ligne, Montant→Données, Année→Page
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Opérations spécifiques au champ de page
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = deuxième élément dans l'ordre trié (par ex. "2021")

# Actualiser et calculer le tableau croisé dynamique
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Filtrage à sélection multiple**

Le filtrage à sélection multiple transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner simultanément plusieurs éléments de page. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.is_multiple_item_selection_allowed` doit être défini sur `True` avant que l'interface de sélection multiple ne prenne effet. Une fois activée, `PivotItem.is_hidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, de sorte que vous pouvez soit afficher tous les éléments, soit autoriser uniquement certains éléments spécifiques.

Le code ci-dessous active la sélection multiple sur le même champ de filtre Year construit dans le scénario 1a, puis montre deux modèles : la partie A révèle chaque élément de page en laissant `is_hidden` défini sur `False` pour chaque entrée, tandis que la partie B n'autorise que les valeurs sources que vous choisissez et masque tout le reste via un bloc `switch (pivot_items[i].get_string_value())`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
#   Scénario 1a (données Fruit/Année/Montant, pivot à E3, Fruit→Ligne,
#   Montant→Données, Année→Page via AddFieldToArea).
#   Ci-dessous, nous appliquons un filtrage multi-sélection sur le champ de page.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Données d'exemple : Fruit | Année | Montant
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Activer la multi-sélection sur le champ de page
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Partie B — sélectionner uniquement des éléments spécifiques par valeur source
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Remarque :** Lorsque vous utilisez le filtrage à sélection multiple via `PivotItem.is_hidden`, **au moins un `PivotItem` doit rester visible** (`is_hidden == False`). Si tous les éléments sont masqués, Excel plante à l'ouverture du fichier ou rend un tableau croisé dynamique vide. Vérifiez toujours que votre liste autorisée de sélection multiple inclut au moins un élément de vos données sources.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (le plus courant) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | Haut niveau, une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous avez déjà un objet `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | À utiliser lorsque l'objet de champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de page (mode par défaut) | `PivotField.current_page_item` | définir sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / effacer le filtre | `PivotField.current_page_item` | définir sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface de sélection multiple dans Excel | `PivotField.is_multiple_item_selection_allowed` | définir sur `True` | Requis avant que tout appel à `is_hidden` ne prenne effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.is_hidden` | définir par élément | Au moins un élément doit rester visible (`is_hidden == False`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage à sélection multiple. Si chaque `PivotItem` dans un champ de filtre à sélection multiple est masqué, Excel plante à l'ouverture ou rend un tableau croisé dynamique vide. Construisez votre liste autorisée à partir de vos données sources afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur chaque machine.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}
