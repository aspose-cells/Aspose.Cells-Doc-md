---
title: Actualiser les tableaux croisés dynamiques dans Aspose.Cells for Python via Java
linktitle: Actualiser les tableaux croisés dynamiques dans Aspose.Cells for Python via Java
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Python via Java à l'aide de l'API d'actualisation des tableaux croisés dynamiques v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code concrets.
keywords: Aspose.Cells, Python via Java, tableau croisé dynamique, actualiser, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for Python via Java v26.7**, la méthode héritée `PivotTable.refreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces et conscientes du cache décrites dans cet article.

{{% /alert %}}

## **Introduction**

Actualiser un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données sources originales aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation dans toutes les situations.

La chaîne de données à quatre couches est :

1. **Source de données** — les plages de la feuille de calcul d'origine, la requête de base de données ou la plage de consolidation où résident les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont collectées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cells** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` restitue ses valeurs calculées et ses styles.

Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques dans un classeur font référence à la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise d'un seul coup chaque `PivotTable` dépendant.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.refresh()` ne prend en charge que les types de sources **`SHEET`** et **`CONSOLIDATION`** — c'est-à-dire les données qui se trouvent dans les plages de la feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API de cache.

{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :

- **`PivotCache.refresh()`** — recharge la source → cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.calculateData()`** — recalcule l'affichage d'un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.

Tous les scénarios de cet article utilisent des données sources provenant de cellules de la feuille de calcul, donc le type de source est `SHEET` et les opérations d'actualisation se comportent comme décrit.

## **Imports requis**

Tous les exemples Python de cet article reposent sur les importations suivantes, car les types de tableaux croisés dynamiques se trouvent dans l'espace de noms `aspose.cells.pivot` :

- `import jpype`
- `import aspose.cells as cells`

Le module `jpype` est utilisé pour amorcer la JVM, tandis que `aspose.cells` expose les types classeur/feuille de calcul/cellule/pivot utilisés tout au long de cet article.

## **Actualiser tous les tableaux croisés dynamiques dans le classeur**

Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflètent les dernières données sources, l'API la plus simple et la plus complète est `Workbook.refreshAll()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` à partir de sa source, puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes de documents où la performance n'est pas un souci.

L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `refreshAll()` pour tout mettre à jour en un seul appel.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Créer un nouveau classeur
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits couvrant 2020 et 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)

# Ajouter un tableau croisé dynamique : plage source "A1:C9", cellule de destination "E3", nom "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assigner les champs du tableau croisé dynamique : Fruit aux Lignes, Year aux Colonnes, Amount aux Données
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modifier plusieurs valeurs Amount dans les données source pour simuler des changements
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Actualiser chaque tableau croisé dynamique / cache de tableau croisé dynamique dans le classeur
workbook.refreshAll()

# Enregistrer le classeur
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Actualiser tous les tableaux croisés dynamiques sur une seule feuille de calcul**

Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul sont connus pour être sans rapport et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.refreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

Ceci est plus sélectif que `Workbook.refreshAll()` : seuls les tableaux croisés dynamiques de la feuille de calcul ciblée sont actualisés, laissant intacts les tableaux croisés dynamiques présents sur d'autres feuilles de calcul.

L'exemple suivant remplit les mêmes données sources Fruit/Année/Montant, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs sources, puis actualise uniquement les tableaux croisés dynamiques de cette feuille de calcul.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)

pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)

worksheet.refreshPivotTables()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Actualiser un seul tableau croisé dynamique**

Lorsque vous souhaitez un contrôle fin sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres de vue/disposition du tableau croisé dynamique lui-même.

### **Données sources modifiées — Utilisez `PivotCache.refresh()`**

Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivotTable.getPivotCache().refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

{{% alert color="primary" %}}

Parce que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel à `PivotCache.refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un cache actualise les deux.

{{% /alert %}}

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs sources, puis actualise via une seule référence de cache.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Écrire la ligne d'en-tête : Fruit / Année / Montant
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Écrire environ 9 lignes de données (raisin / myrtille / kiwi / cerise pour 2020-2021)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# Ajouter le premier tableau croisé dynamique "Pivot1" ancré à la cellule E3, plage source A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Assigner les champs pour Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Ajouter un DEUXIÈME tableau croisé dynamique "Pivot2" ancré à E15 en utilisant la MÊME plage source A1:C9
# Pivot1 et Pivot2 partagent un seul PivotCache car la plage source est identique.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Assigner les mêmes champs pour Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Modifier plusieurs valeurs de cellules Montant dans les données source pour simuler un changement de données
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Actualiser le PivotCache partagé.
# Parce que Pivot1 et Pivot2 partagent le même PivotCache, cet appel unique
# actualise LES DEUX tableaux croisés dynamiques (données + style) à partir de la source mise à jour.
pivotTable1.getPivotCache().refresh()

# Enregistrer le classeur
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### **Seule la vue/disposition a changé — Utilisez `calculateData()`**

Si les données sources n'ont *pas* changé, mais que seuls les paramètres de vue ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été basculé), il n'y a pas besoin de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu nécessite un recalcul. Dans ce cas, `pivotTable.calculateData()` est le bon choix.

Cela évite la récupération source inutile et est nettement plus rapide lorsque de nombreux tableaux croisés dynamiques partagent le même cache.

L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `calculateData()` pour le restituer à partir du cache existant.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Écrire la ligne d'en-tête Fruit / Année / Montant
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Écrire 8 lignes de données (lignes 2-9, correspondant à la plage source A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)

# Ajouter un tableau croisé dynamique nommé "Pivot1" placé à la cellule de destination E3, avec comme source A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assigner les champs : Fruit à Ligne, Year à Colonne, Amount à Données
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modifier une propriété d'affichage/de mise en page — il s'agit d'une modification de présentation uniquement,
# elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() réaffiche l'affichage de CE tableau croisé dynamique (données + style) à partir des
# données déjà conservées dans le PivotCache. Comme les données source n'ont pas changé,
# aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
# dans les cellules de la feuille de calcul.
pivotTable.calculateData()

# Enregistrer le classeur sur le disque
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache**

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lots, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.getPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.

C'est également le moyen le plus direct de confirmer que deux tableaux croisés dynamiques partagent bien la même instance de `PivotCache` : vous pouvez comparer les références de cache, ou simplement itérer sur la collection renvoyée par `getPivotTables()` et observer quels tableaux croisés dynamiques y apparaissent.

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.


## **Migrer depuis l'obsolète `PivotTable.refreshData()`**

Avant Aspose.Cells for Python via Java v26.7, la manière standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.refreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API conscientes du cache décrites ci-dessus.

Il y a deux raisons pour lesquelles l'approche par table `refreshData()` est problématique dans les classeurs réels :

- Elle récupère les données depuis la source *chaque* fois qu'elle est appelée, même lorsque la source n'a pas changé.
- Chaque appel actualise tout le cache partagé. Lorsque de nombreux tableaux croisés dynamiques partagent un cache, l'appel répété de `refreshData()` par tableau croisé dynamique entraîne une récupération répétée du même cache, ce qui est très lent.

Les remplacements recommandés sont :

- **Actualiser TOUS les tableaux croisés dynamiques dans le classeur** → utilisez `workbook.refreshAll();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivotTable.getPivotCache().refresh();` pour un cache. Parce que le cache est partagé, cet appel unique met à jour chaque tableau croisé dynamique construit au-dessus de ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seule la vue/disposition du pivot a changé** → utilisez `pivotTable.calculateData();` pour restituer à partir du cache existant sans aucun aller-retour vers la source.

L'exemple suivant démontre le nouveau motif efficace pour les classeurs comportant plusieurs tableaux croisés dynamiques partageant un seul cache.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Construire les données sources : Fruit / Année / Montant (en-tête + 9 lignes) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Ajouter le premier tableau croisé dynamique (Pivot1) à la cellule de destination E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Ajouter le SECOND tableau croisé dynamique (Pivot2) sur la MÊME plage source ---
# Pivot1 et Pivot2 partagent UN SEUL PivotCache sous-jacent.
# C'est exactement le scénario où l'approche héritée RefreshData() par table
# devient inefficace : actualiser une table relance toute la récupération
# du cache partagé, donc actualiser N tables effectue la même récupération coûteuse N fois.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Modifier plusieurs valeurs de Montant dans les données sources ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- Modèle OBSOLÈTE (avant 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // récupère depuis la source, actualise tout le cache
# pivotTable2.RefreshData();  // récupère À NOUVEAU — le cache est déjà frais !
# Chaque appel reconstruit le cache partagé, donc N tables = N récupérations redondantes.

# --- NOUVEAU modèle v26.7+ : actualiser le cache UNE SEULE FOIS, puis re-rendre si nécessaire ---
# Un seul appel à PivotCache.Refresh() récupère les valeurs modifiées dans le cache partagé
# ET recalcule l'affichage de CHAQUE tableau croisé qui le référence.
# Comme Pivot1 et Pivot2 partagent un PivotCache, cet unique appel met à jour
# les deux tables — aucune seconde aller-retour vers la source n'est nécessaire.
pivotTable1.getPivotCache().refresh()

# CalculateData() ne fait que re-rendre l'affichage d'un tableau croisé (données + style)
# à partir des données déjà détenues dans le cache — il ne touche PAS à la source.
# Nous l'appelons sur Pivot2 ici uniquement pour démontrer l'API : après que le cache
# a été actualisé une fois, toute table dépendante peut être re-rendue sans
# revenir à la source. Utilisez CalculateData() seul lorsque seuls les paramètres
# d'affichage/de mise en page du tableau croisé ont changé et que le cache est à jour.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Quelle API d'actualisation dois-je utiliser ?**

Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.

| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.refreshAll()` | Un seul appel ; couvre tous les caches et toutes les tables. |
| Actualiser uniquement les tableaux croisés dynamiques sur une seule feuille | `Worksheet.refreshPivotTables()` | Limitée à une seule feuille de calcul. |
| Données sources modifiées pour un cache | `pivotTable.getPivotCache().refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/disposition ont changé | `pivotTable.calculateData()` | Évite l'aller-retour source inutile. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivotCache.getPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |

En pratique, privilégiez les API basées sur le cache à l'approche obsolète `refreshData()` par table. Elles sont conscientes des caches partagés, elles évitent les récupérations sources redondantes et elles vous permettent de choisir la portée la plus petite qui satisfait votre besoin d'actualisation.{{< app/cells/assistant language="python" >}}
