---
title: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Python via .NET
linktitle: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Python via .NET
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Python via .NET à l'aide de l'API d'actualisation des tableaux croisés dynamiques v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, Python via .NET, tableau croisé dynamique, actualiser, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for Aspose.Cells for Python via .NET v26.7**, la méthode héritée `PivotTable.refresh_data()` est marquée comme obsolète et doit être remplacée par les API plus efficaces et conscientes du cache décrites dans cet article.

{{% /alert %}}

## Introduction

L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui connecte vos données sources originales aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour toute situation.

La chaîne de données à quatre niveaux est :

1. **Source de données** — les plages de feuilles de calcul originales, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est ici que toutes les données sont collectées et agrégées.
3. **Tableau croisé dynamique** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cellules** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` rend ses valeurs calculées et ses styles.

Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques dans un classeur référencent la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise chaque `PivotTable` dépendant en une seule fois.

{{% alert color="primary" %}}

`PivotCache.source_type` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.refresh()` ne prend en charge que les types de source **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API du cache.

{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :

- **`PivotCache.refresh()`** — recharge source → cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.calculate_data()`** — recalcule l'affichage d'un seul `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.

Tous les scénarios de cet article utilisent des données sources de cellules de feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Importations requises

Tous les exemples Python de cet article commencent par les trois instructions d'importation suivantes car les types de tableaux croisés dynamiques se trouvent dans le namespace `aspose.cells.pivot` :

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Actualiser tous les tableaux croisés dynamiques dans le classeur

Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique dans le classeur reflète les dernières données sources, l'API la plus simple et la plus complète est `Workbook.refresh_all()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` depuis sa source puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales de documents complets où la performance n'est pas un souci.

L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `refresh_all()` pour tout mettre à jour en un seul appel.

```python
import aspose.cells as ac

# Créer un nouveau classeur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits pour 2020 et 2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# Ajouter un tableau croisé dynamique : plage source "A1:C9", cellule de destination "E3", nom "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Affecter les champs du tableau croisé dynamique : Fruit aux Lignes, Year aux Colonnes, Amount aux Données
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modifier plusieurs valeurs de Amount dans les données sources pour simuler des changements
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Actualiser tous les tableaux croisés dynamiques / le cache du tableau croisé dynamique dans le classeur
workbook.refresh_all()

# Enregistrer le classeur
workbook.save("output.xlsx")
```

## Actualiser tous les tableaux croisés dynamiques sur une seule feuille de calcul

Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul sont connus pour être sans rapport et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.refresh_pivot_tables()`, qui est limité à une seule instance de `Worksheet`.

Ceci est plus sélectif que `Workbook.refresh_all()` : seuls les tableaux croisés dynamiques sur la feuille de calcul ciblée sont actualisés, laissant intacts les tableaux croisés dynamiques sur d'autres feuilles de calcul.

L'exemple suivant remplit les mêmes données sources Fruit/Année/Montant, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs sources, puis actualise uniquement les tableaux croisés dynamiques sur cette feuille de calcul.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```

## Actualiser un seul tableau croisé dynamique

Lorsque vous souhaitez un contrôle granulaire sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres de vue/mise en page du tableau croisé dynamique lui-même.

### Données sources modifiées — Utilisez `PivotCache.refresh()`

Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivot_table.pivot_cache.refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

{{% alert color="primary" %}}

Étant donné que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel de `PivotCache.refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un cache actualise les deux.

{{% /alert %}}

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs sources, puis actualise via une référence de cache.

```python
import aspose.cells as ac

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Écrire la ligne d'en-tête : Fruit / Année / Montant
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Écrire environ 9 lignes de données (raisin / myrtille / kiwi / cerise sur 2020-2021)
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

# Ajouter le premier tableau croisé dynamique "Pivot1" ancré à la cellule E3, plage source A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Attribuer les champs pour Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Ajouter un SECOND tableau croisé dynamique "Pivot2" ancré à E15 en utilisant la MÊME plage source A1:C9
# Pivot1 et Pivot2 partagent un seul PivotCache car la plage source est identique.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Attribuer les mêmes champs pour Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modifier plusieurs valeurs de cellules Montant dans les données source pour simuler un changement de données
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Actualiser le PivotCache partagé.
# Parce que Pivot1 et Pivot2 partagent le même PivotCache, cet unique appel
# actualise LES DEUX tableaux croisés dynamiques (données + style) à partir de la source mise à jour.
pivotTable1.pivot_cache.refresh()

# Enregistrer le classeur
workbook.save("output.xlsx")
```

### Seule la vue/mise en page a changé — Utilisez `calculate_data()`

Si les données sources n'ont *pas* changé mais que seuls les paramètres de vue ou de mise en page du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une zone différente, ou un paramètre d'actualisation à l'ouverture a été basculé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu nécessite un recalcul. Dans ce cas, `pivot_table.calculate_data()` est le bon choix.

Cela évite la récupération inutile des données sources et est significativement plus rapide lorsque de nombreux tableaux croisés dynamiques partagent le même cache.

L'exemple suivant modifie une propriété non-source du tableau croisé dynamique, puis appelle `calculate_data()` pour le rendre à nouveau depuis le cache existant.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Écrire la ligne d'en-tête Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Écrire 8 lignes de données (lignes 2-9, correspondant à la plage source A1:C9)
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
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# Ajouter un tableau croisé dynamique nommé "Pivot1" placé dans la cellule de destination E3, avec comme source la plage A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assigner les champs : Fruit à Ligne, Year à Colonne, Amount à Données
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Modifier une propriété d'affichage/de mise en page — il s'agit d'une modification de présentation uniquement,
# donc elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() restitue l'affichage de CE tableau croisé dynamique (données + style) à partir des
# données déjà détenues dans le PivotCache. Comme les données source n'ont pas changé,
# aucun aller-retour vers la source n'est effectué — seules les valeurs en cache sont recalculées
# dans les cellules de la feuille de calcul.
pivot_table.calculate_data()

# Enregistrer le classeur sur le disque
workbook.save("output.xlsx")
```

## Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.get_pivot_tables()`. Cette méthode renvoie la collection de chaque `PivotTable` qui dépend du cache donné.

C'est aussi le moyen le plus direct de confirmer que deux tableaux croisés dynamiques partagent bien la même instance de `PivotCache` : vous pouvez comparer les références du cache, ou simplement itérer la collection renvoyée par `get_pivot_tables()` et observer quels tableaux croisés dynamiques y apparaissent.

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

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

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Migration depuis l'obsolète `PivotTable.refresh_data()`

Avant Aspose.Cells for Aspose.Cells for Python via .NET v26.7, la manière standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.refresh_data()` sur chaque tableau croisé dynamique individuellement. Depuis la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API conscientes du cache décrites ci-dessus.

Il y a deux raisons pour lesquelles l'approche par table `refresh_data()` est problématique dans les classeurs du monde réel :

- Elle récupère les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
- Chaque appel actualise l'intégralité du cache partagé. Lorsque de nombreux tableaux croisés dynamiques partagent un cache, appeler à plusieurs reprises `refresh_data()` par tableau croisé dynamique entraîne la re-récupération du même cache encore et encore, ce qui est très lent.

Les remplacements recommandés sont :

- **Actualiser TOUS les tableaux croisés dynamiques dans le classeur** → utilisez `workbook.refresh_all();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivot_table.pivot_cache.refresh();` pour un cache. Étant donné que le cache est partagé, cet appel unique met à jour chaque tableau croisé dynamique construit au-dessus de ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seule la vue/mise en page du tableau croisé dynamique a changé** → utilisez `pivot_table.calculate_data();` pour rendre à nouveau depuis le cache existant sans aucun aller-retour vers la source.

L'exemple suivant démontre le nouveau modèle efficace pour les classeurs avec plusieurs tableaux croisés dynamiques partageant un seul cache.

```python
import aspose.cells as ac

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Construire les données sources : Fruit / Année / Montant (en-tête + 9 lignes) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Ajouter le premier tableau croisé dynamique (Pivot1) à la cellule de destination E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Ajouter le SECOND tableau croisé dynamique (Pivot2) sur la MÊME plage source ---
# Pivot1 et Pivot2 partagent UN seul PivotCache sous-jacent.
# C'est exactement le scénario où l'approche héritée RefreshData() par tableau
# devient inefficace : rafraîchir un tableau récupère à nouveau l'intégralité
# du cache partagé, donc rafraîchir N tableaux effectue la même opération coûteuse N fois.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Modifier plusieurs valeurs Montant dans les données sources ---
sheet.cells["C2"].put_value(5000)   # Raisin 2020
sheet.cells["C5"].put_value(7500)   # Cerise 2020
sheet.cells["C9"].put_value(9500)   # Cerise 2021

# --- Modèle OBSOLÈTE (avant 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # récupère à nouveau depuis la source, rafraîchit tout le cache
# pivot_table2.refresh_data();  # récupère À NOUVEAU — le cache est déjà à jour !
# Chaque appel reconstruit le cache partagé, donc N tableaux = N récupérations redondantes.

# --- NOUVEAU modèle v26.7+ : rafraîchir le cache UNE SEULE FOIS, puis rafraîchir l'affichage si nécessaire ---
# Un appel à PivotCache.Refresh() récupère les valeurs modifiées dans le cache partagé
# ET recalcule l'affichage de CHAQUE tableau croisé dynamique qui y fait référence.
# Puisque Pivot1 et Pivot2 partagent un seul PivotCache, cet unique appel met à jour
# les deux tableaux — aucune seconde récupération depuis la source n'est nécessaire.
pivot_table1.pivot_cache.refresh()

# CalculateData() ne rafraîchit que l'affichage d'un tableau croisé dynamique (données + style)
# à partir des données déjà contenues dans le cache — il ne touche PAS à la source.
# Nous l'appelons sur Pivot2 ici uniquement pour démontrer l'API : après le cache
# avoir été rafraîchi une fois, tout tableau dépendant peut être ré-affiché sans
# revenir à la source. Utilisez CalculateData() seul lorsque seuls les
# paramètres d'affichage/mise en page du tableau croisé dynamique ont changé et que le cache est à jour.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Quelle API d'actualisation dois-je utiliser ?

Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune.

| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.refresh_all()` | Un seul appel ; couvre tous les caches et tables. |
| Actualiser uniquement les tableaux croisés dynamiques sur une seule feuille | `Worksheet.refresh_pivot_tables()` | Limité à une seule feuille de calcul. |
| Données sources modifiées pour un cache | `pivot_table.pivot_cache.refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/mise en page ont changé | `pivot_table.calculate_data()` | Évite l'aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivot_cache.get_pivot_tables()` | Utilisez pour énumérer avant l'actualisation en masse. |

En pratique, préférez les API basées sur le cache par rapport à l'obsolète `refresh_data()` par table. Elles sont conscientes des caches partagés, évitent les récupérations redondantes depuis la source, et vous permettent de choisir la plus petite portée qui satisfait votre besoin d'actualisation.

{{< app/cells/assistant language="python" >}}