---
title: Refreshing Pivot Tables in Aspose.Cells for Python via .NET
linktitle: Refreshing Pivot Tables
description: Learn how to refresh pivot tables in Aspose.Cells for Python via .NET using the v26.7+ pivot-refresh API. This article covers RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData, and GetPivotTables with practical code examples.
keywords: Aspose.Cells, Python via .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données de tableaux croisés dynamiques à quatre portées différentes — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir de **Aspose.Cells for Python via .NET v26.7**, la méthode héritée `PivotTable.refresh_data()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, prenant en charge le cache, décrites dans cet article.

{{% /alert %}}

## Introduction

L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui connecte vos données sources d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour toute situation.

La chaîne de données à quatre niveaux est :

1. **Source de données** — les plages de feuilles de calcul d'origine, la requête de base de données ou la plage de consolidation où résident les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cellules** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` rend ses valeurs calculées et ses styles.

Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques dans un classeur font référence à la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise chaque `PivotTable` dépendant en une seule fois.

{{% alert color="primary" %}}

`PivotCache.source_type` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. À partir de v26.7, `PivotCache.refresh()` prend uniquement en charge les types de sources **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui résident dans les plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API de cache.

{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :

- **`PivotCache.refresh()`** — recharge la source vers le cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.calculate_data()`** — recalcule l'affichage d'un `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.

Tous les scénarios de cet article utilisent des données sources de cellules de feuille de calcul, le type de source est donc `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Imports requis

Tous les exemples Python de cet article commencent par les trois instructions d'importation suivantes, car les types de tableaux croisés dynamiques se trouvent dans l'espace de noms `aspose.cells.pivot` :

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Actualiser tous les tableaux croisés dynamiques du classeur

Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflète les dernières données sources, l'API la plus simple et la plus complète est `Workbook.refresh_all()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` depuis sa source, puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales de documents complets où la performance n'est pas un souci.

L'exemple suivant crée un classeur avec une plage source Fruit/Year/Amount, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `refresh_all()` pour tout mettre à jour en un seul appel.

```python
import aspose.cells as ac

# Créer un nouveau classeur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données sur les fruits pour 2020 et 2021)
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

# Affecter les champs du tableau croisé dynamique : Fruit aux Lignes, Année aux Colonnes, Montant aux Données
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modifier plusieurs valeurs de Montant dans les données source pour simuler des changements
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Actualiser tous les tableaux croisés dynamiques / caches de tableau croisé dynamique dans le classeur
workbook.refresh_all()

# Enregistrer le classeur
workbook.save("output.xlsx")
```

## Actualiser tous les tableaux croisés dynamiques d'une seule feuille de calcul

Parfois, vous avez uniquement besoin d'actualiser les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul ne sont pas liés et ne doivent pas être touchés. Dans ce cas, Aspose.Cells fournit `Worksheet.refresh_pivot_tables()`, qui est limité à une seule instance de `Worksheet`.

C'est plus sélectif que `Workbook.refresh_all()` : seuls les tableaux croisés dynamiques de la feuille de calcul ciblée sont actualisés, laissant intacts les tableaux croisés dynamiques des autres feuilles de calcul.

L'exemple suivant remplit les mêmes données sources Fruit/Year/Amount, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs sources, puis actualise uniquement les tableaux croisés dynamiques de cette feuille de calcul.

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

Lorsque vous souhaitez un contrôle précis sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre les deux dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres d'affichage/de mise en page du tableau croisé dynamique lui-même.

### Les données sources ont changé — Utilisez `PivotCache.refresh()`

Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivot_table.pivot_cache.refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

{{% alert color="primary" %}}

Parce que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel de `PivotCache.refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un seul cache les actualise tous les deux.

{{% /alert %}}

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs sources, puis actualise via une seule référence de cache.

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

# Assigner les champs pour Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Ajouter un SECOND tableau croisé dynamique "Pivot2" ancré à E15 en utilisant la MÊME plage source A1:C9
# Pivot1 et Pivot2 partagent un seul PivotCache car la plage source est identique.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Assigner les mêmes champs pour Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modifier plusieurs valeurs de cellules Montant dans les données source pour simuler un changement de données
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Rafraîchir le PivotCache partagé.
# Parce que Pivot1 et Pivot2 partagent le même PivotCache, cet unique appel
# rafraîchit LES DEUX tableaux croisés dynamiques (données + style) à partir de la source mise à jour.
pivotTable1.pivot_cache.refresh()

# Enregistrer le classeur
workbook.save("output.xlsx")
```

### Seuls l'affichage/la mise en page ont changé — Utilisez `calculate_data()`

Si les données sources n'ont *pas* changé mais que seuls les paramètres d'affichage ou de mise en page du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été basculé), il n'est pas nécessaire de retourner à la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu nécessite un recalcul. Dans ce cas, `pivot_table.calculate_data()` est le bon choix.

Cela évite la récupération de source inutile et est nettement plus rapide lorsque de nombreux tableaux croisés dynamiques partagent le même cache.

L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `calculate_data()` pour le restituer à partir du cache existant.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Écrire la ligne d'en-tête Fruit / Année / Montant
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

# Ajouter un tableau croisé dynamique nommé "Pivot1" placé à la cellule de destination E3, avec comme source A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Affecter les champs : Fruit à Ligne, Année à Colonne, Montant à Données
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Modifier une propriété d'affichage/de mise en page — il s'agit d'une modification de présentation uniquement,
# elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() restitue l'affichage de CE tableau croisé dynamique (données + style) à partir des
# données déjà conservées dans le PivotCache. Comme les données source n'ont pas changé,
# aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
# dans les cellules de la feuille de calcul.
pivot_table.calculate_data()

# Enregistrer le classeur sur le disque
workbook.save("output.xlsx")
```

## Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.get_pivot_tables()`. Cette méthode renvoie la collection de chaque `PivotTable` qui dépend du cache donné.

C'est également le moyen le plus direct de confirmer que deux tableaux croisés dynamiques partagent bien la même instance de `PivotCache` : vous pouvez comparer les références de cache, ou simplement itérer la collection renvoyée par `get_pivot_tables()` et observer quels tableaux croisés dynamiques y apparaissent.

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.


## Migration depuis la méthode obsolète `PivotTable.refresh_data()`

Avant Aspose.Cells for Python via .NET v26.7, la façon standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.refresh_data()` sur chaque tableau croisé dynamique individuellement. À partir de v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API basées sur le cache décrites ci-dessus.

Il y a deux raisons pour lesquelles l'approche `refresh_data()` par table est problématique dans les classeurs du monde réel :

- Elle récupère à nouveau les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
- Chaque appel actualise l'ensemble du cache partagé. Lorsque de nombreux tableaux croisés dynamiques partagent un cache, l'appel répété de `refresh_data()` par tableau croisé dynamique provoque la récupération répétée du même cache encore et encore, ce qui est très lent.

Les remplacements recommandés sont :

- **Actualiser TOUS les tableaux croisés dynamiques du classeur** → utilisez `workbook.refresh_all();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivot_table.pivot_cache.refresh();` pour un cache. Parce que le cache est partagé, cet appel unique met à jour chaque tableau croisé dynamique construit au-dessus de ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seuls l'affichage/la mise en page du tableau croisé ont changé** → utilisez `pivot_table.calculate_data();` pour restituer à partir du cache existant sans aucun aller-retour vers la source.

L'exemple suivant illustre le nouveau modèle efficace pour les classeurs comportant plusieurs tableaux croisés dynamiques partageant un seul cache.

```python
import aspose.cells as ac

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Construire les données source : Fruit / Année / Montant (en-tête + 9 lignes) ---
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
# Pivot1 et Pivot2 partagent UN SEUL PivotCache sous-jacent.
# C'est exactement le scénario où l'approche héritée par table RefreshData()
# devient inefficace : rafraîchir une table ré-extrait l'intégralité du cache
# partagé, donc rafraîchir N tables effectue la même extraction coûteuse N fois.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Modifier plusieurs valeurs de Montant dans les données source ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- Modèle OBSOLÈTE (avant la 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # ré-extrait depuis la source, rafraîchit tout le cache
# pivot_table2.refresh_data();  # ré-extrait À NOUVEAU — le cache est déjà à jour !
# Chaque appel reconstruit le cache partagé, donc N tables = N extractions redondantes.

# --- NOUVEAU modèle v26.7+ : rafraîchir le cache UNE SEULE FOIS, puis ré-afficher au besoin ---
# Un seul appel à PivotCache.Refresh() récupère les valeurs modifiées dans le cache
# partagé ET recalcule l'affichage de CHAQUE tableau croisé dynamique qui le référence.
# Comme Pivot1 et Pivot2 partagent un seul PivotCache, cet appel unique met à jour
# les deux tables — aucun second aller-retour vers la source n'est nécessaire.
pivot_table1.pivot_cache.refresh()

# CalculateData() ne ré-affiche que la vue d'un tableau croisé dynamique (données + style)
# à partir des données déjà détenues dans le cache — il ne touche PAS à la source.
# Nous l'appelons sur Pivot2 ici uniquement pour démontrer l'API : après le rafraîchissement
# du cache une seule fois, toute table dépendante peut être ré-affichée sans
# revenir à la source. Utilisez CalculateData() seul lorsque seuls les paramètres
# d'affichage/mise en page du tableau croisé ont changé et que le cache est à jour.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Quelle API d'actualisation dois-je utiliser ?

Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune.

| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.refresh_all()` | Un seul appel ; couvre tous les caches et tous les tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.refresh_pivot_tables()` | Limité à une feuille de calcul. |
| Données sources modifiées pour un cache | `pivot_table.pivot_cache.refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres d'affichage/de mise en page ont changé | `pivot_table.calculate_data()` | Évite les allers-retours inutiles vers la source. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivot_cache.get_pivot_tables()` | À utiliser pour énumérer avant une actualisation en masse. |

En pratique, préférez les API basées sur le cache à la méthode obsolète `refresh_data()` par table. Elles sont conscientes des caches partagés, évitent les récupérations redondantes depuis la source et vous permettent de choisir le plus petit périmètre qui satisfait votre besoin d'actualisation.{{< app/cells/assistant language="python" >}}
