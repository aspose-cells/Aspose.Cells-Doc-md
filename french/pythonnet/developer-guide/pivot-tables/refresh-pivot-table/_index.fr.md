---
title: Actualiser les tableaux croisés dynamiques et les caches de tableaux croisés dynamiques dans Aspose.Cells for Python via .NET
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Python via .NET à l'aide de l'API d'actualisation des tableaux croisés dynamiques de la version 26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les tableaux croisés dynamiques
keywords: Aspose.Cells, Python via .NET, tableau croisé dynamique, actualiser, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir de **Aspose.Cells for Python via .NET v26.7**, la méthode héritée `PivotTable.refresh_data()` est marquée comme obsolète et doit être remplacée par les API plus efficaces et conscientes du cache décrites dans cet article.
{{% /alert %}}

## Introduction
L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données source d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour chaque situation.
La chaîne de données à quatre couches est :
1. **Source de données** — les plages de la feuille de calcul d'origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont rassemblées et agrégées.
3. **Tableau croisé dynamique** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cellules** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` rend ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`PivotCache.source_type` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la version 26.7, `PivotCache.refresh()` ne prend en charge que les types de sources **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans les plages de la feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées via l'API de cache.
{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :
- **`PivotTable.calculate_data()`** — recalcule l'affichage d'un `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources provenant de cellules de la feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Démarrage rapide
Si vous avez uniquement besoin du code le plus court possible qui actualise chaque tableau croisé dynamique dans le classeur, un seul appel suffit :

```python
import aspose.cells as ac
# Créer un nouveau classeur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits sur 2020 et 2021)
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
# Modifier plusieurs valeurs de Montant dans les données sources pour simuler des changements
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# Actualiser tous les tableaux croisés dynamiques / caches de tableaux croisés dynamiques dans le classeur
workbook.refresh_all()
# Enregistrer le classeur
workbook.save("output.xlsx")
```

Tout le reste de cet article explique quand choisir une API plus restreinte à la place.

## Imports requis
Tous les exemples Python de cet article commencent par les trois instructions d'importation suivantes car les types de tableaux croisés dynamiques se trouvent dans l'espace de noms `aspose.cells.pivot` :
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Actualiser tous les tableaux croisés dynamiques dans le classeur
Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique dans le classeur reflète les dernières données sources, l'API la plus simple et la plus complète est `Workbook.refresh_all()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` à partir de sa source, puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes du document où la performance n'est pas un problème.
L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `refresh_all()` pour tout mettre à jour en un seul appel.

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

## Actualiser tous les tableaux croisés dynamiques sur une seule feuille de calcul
Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul sont connus pour être non liés et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.refresh_pivot_tables()`, qui est limité à une seule instance de `Worksheet`.

## Actualiser un seul tableau croisé dynamique
Lorsque vous souhaitez un contrôle fin sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres de vue/disposition du tableau croisé dynamique lui-même.

### Les données sources ont changé — Utilisez `PivotCache.refresh()`
Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivot_table.pivot_cache.refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Seule la vue/disposition a changé — Utilisez `calculate_data()`
Si les données sources n'ont *pas* changé mais que seuls les paramètres de vue ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été activé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu a besoin d'être recalculé. Dans ce cas, `pivot_table.calculate_data()` est le bon choix.
L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `calculate_data()` pour le restituer à partir du cache existant.
Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lots, ou pour diagnostiquer l'impact d'un cache partagé — utilisez `PivotCache.get_pivot_tables()`. Cette méthode renvoie la collection de chaque `PivotTable` qui dépend du cache donné.

## Migration depuis le `PivotTable.refresh_data()` obsolète
Avant Aspose.Cells for Python via .NET v26.7, la façon standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.refresh_data()` sur chaque tableau croisé dynamique individuellement. À partir de la version 26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API conscientes du cache décrites ci-dessus.
Il y a deux raisons pour lesquelles l'approche `refresh_data()` par tableau est problématique dans les classeurs du monde réel :
- Elle récupère les données à partir de la source *à chaque* appel, même lorsque la source n'a pas changé.
Les remplacements recommandés sont :
L'exemple suivant illustre le nouveau modèle efficace pour les classeurs contenant plusieurs tableaux croisés dynamiques partageant un seul cache.

## Quelle API d'actualisation dois-je utiliser ?
Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.
| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.refresh_all()` | Un seul appel ; couvre tous les caches et tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques sur une seule feuille | `Worksheet.refresh_pivot_tables()` | Limité à une seule feuille de calcul. |
| Les données sources ont changé pour un cache | `pivot_table.pivot_cache.refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/disposition ont changé | `pivot_table.calculate_data()` | Évite un aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivot_cache.get_pivot_tables()` | À utiliser pour énumérer avant une actualisation en masse. |
En pratique, préférez les API basées sur le cache par rapport à l'obsolète `refresh_data()` par tableau. Elles sont conscientes des caches partagés, évitent les récupérations redondantes de données, et vous permettent de choisir la plus petite portée qui satisfait votre besoin d'actualisation.

## Pièges courants
- **Oublier d'actualiser avant d'enregistrer.** Un tableau croisé dynamique n'écrit ses valeurs rendues dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules sources, appelez `PivotCache.Refresh()` (ou `Workbook.RefreshAll()`) avant `Workbook.save()`, sinon le fichier enregistré contiendra toujours les anciennes valeurs agrégées.
- **Appeler l'obsolète `RefreshData()` par tableau.** Dans la version 26.7, `PivotTable.RefreshData()` est marquée comme obsolète et récupère la source à chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela signifie N récupérations de source redondantes. Remplacez par un seul `PivotCache.Refresh()` suivi de `CalculateData()` par tableau.
- **Actualiser alors que seule la disposition a changé.** Si vous n'avez modifié que la vue d'un tableau croisé dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données sources, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour restituer à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d'une connexion externe (base de données, cube OLAP, etc.), `PivotCache.Refresh()` ne peut pas l'actualiser dans la version 26.7 — elle ne prend actuellement en charge que les types de sources `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False
# CalculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

{{< app/cells/assistant language="python-net" >}}