---
title: Actualiser les Tableaux Croisés Dynamiques et les caches de tableaux croisés dynamiques dans Aspose.Cells for Python via Java
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Python via Java en utilisant l'API d'actualisation des tableaux croisés v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les Tableaux Croisés Dynamiques
keywords: Aspose.Cells, Python via Java, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données de tableau croisé dynamique à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for Python via Java v26.7**, la méthode héritée `PivotTable.refreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, conscientes du cache, décrites dans cet article.
{{% /alert %}}

## Introduction
L'actualisation d'un tableau croisé dynamique n'est que rarement une opération ponctuelle. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données sources d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation dans chaque situation.
La chaîne de données à quatre niveaux est :
1. **Source de données** — les plages de feuilles de calcul d'origine, la requête de base de données, ou la plage de consolidation où vivent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, colonne, valeur et filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cells** — la collection `Cells` de la feuille de calcul dans laquelle le `PivotTable` rend ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. À partir de la v26.7, `PivotCache.refresh()` ne prend en charge que les types de source **`SHEET`** et **`CONSOLIDATION`** — c'est-à-dire les données qui vivent dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API du cache.
{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :
- **`PivotTable.calculateData()`** — recalcule l'affichage d'un `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources de cellules de feuille de calcul, donc le type de source est `SHEET` et les opérations d'actualisation se comportent comme décrit.

## Démarrage rapide
Si vous avez seulement besoin du code le plus court possible qui actualise chaque tableau croisé dynamique dans le classeur, un seul appel suffit :

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
# Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits sur 2020 et 2021)
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
# Affecter les champs du tableau croisé dynamique : Fruit aux Lignes, Année aux Colonnes, Montant aux Données
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Modifier plusieurs valeurs de Montant dans les données source pour simuler des changements
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Actualiser tous les tableaux croisés dynamiques / caches de tableaux croisés dynamiques dans le classeur
workbook.refreshAll()
# Enregistrer le classeur
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Tout le reste de cet article explique quand choisir une API plus restreinte à la place.

## Importations requises
Tous les exemples Python de cet article reposent sur les importations suivantes car les types de tableau croisé dynamique vivent dans l'espace de noms `aspose.cells.pivot` :
- `import jpype`
- `import aspose.cells as cells`
Le module `jpype` est utilisé pour démarrer la JVM, tandis que `aspose.cells` expose les types de classeur/feuille de calcul/cellule/tableau croisé dynamique utilisés tout au long de cet article.

## Actualiser tous les Tableaux Croisés Dynamiques dans le classeur
Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflète les dernières données sources, l'API la plus simple et la plus complète est `Workbook.refreshAll()`. Un seul appel parcourt le classeur entier — actualisant chaque `PivotCache` à partir de sa source puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes de documents où la performance n'est pas une préoccupation.
L'exemple suivant crée un classeur avec une plage source Fruits/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `refreshAll()` pour tout mettre à jour en un seul appel.

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

## Actualiser tous les Tableaux Croisés Dynamiques sur une seule feuille de calcul
Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui vivent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques d'autres feuilles de calcul sont connus pour être sans rapport et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.refreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

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
# Ajouter un tableau croisé dynamique nommé "Pivot1" placé dans la cellule de destination E3, à partir de la plage A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Affecter les champs : Fruit à Ligne, Année à Colonne, Montant à Données
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Modifier une propriété d'affichage/disposition — il s'agit d'une modification purement visuelle,
# elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# CalculateData() réaffiche l'affichage de CE tableau croisé dynamique (données + style) à partir des
# données déjà contenues dans le PivotCache. Comme les données source n'ont pas changé,
# aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
# dans les cellules de la feuille de calcul.
pivotTable.calculateData()
# Enregistrer le classeur sur le disque
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Actualiser un seul Tableau Croisé Dynamique
Lorsque vous souhaitez un contrôle fin sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres de vue/disposition du tableau croisé dynamique lui-même.

### Données sources modifiées — Utilisez `PivotCache.refresh()`
Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivotTable.getPivotCache().refresh()`. Cet appel relit les données sources dans le cache puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Seule la vue/la disposition a été modifiée — Utilisez `calculateData()`
Si les données sources n'ont *pas* changé mais que seuls les paramètres de vue ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une zone différente, ou un paramètre d'actualisation à l'ouverture a été basculé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu a besoin d'être recalculé. Dans ce cas, `pivotTable.calculateData()` est le bon choix.
L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `calculateData()` pour le rendre à nouveau à partir du cache existant.
Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact d'un cache partagé — utilisez `PivotCache.getPivotTables()`. Cette méthode renvoie la collection de chaque `PivotTable` qui dépend du cache donné.

## Migration depuis l'obsolète `PivotTable.refreshData()`
Avant Aspose.Cells for Python via Java v26.7, la méthode standard pour actualiser un tableau croisé dynamique consistait à appeler `PivotTable.refreshData()` sur chaque tableau croisé dynamique individuellement. À partir de la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API conscientes du cache décrites ci-dessus.
Il y a deux raisons pour lesquelles l'approche `refreshData()` par tableau est problématique dans les classeurs réels :
- Elle récupère les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
Les remplacements recommandés sont :
L'exemple suivant démontre le nouveau modèle efficace pour les classeurs contenant plusieurs tableaux croisés dynamiques partageant un seul cache.

## Quelle API d'actualisation dois-je utiliser ?
Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.
| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.refreshAll()` | Un seul appel ; couvre tous les caches et tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.refreshPivotTables()` | Limité à une feuille de calcul. |
| Données sources modifiées pour un cache | `pivotTable.getPivotCache().refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/disposition ont changé | `pivotTable.calculateData()` | Évite un aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivotCache.getPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |
En pratique, préférez les API basées sur le cache par rapport à l'obsolète `refreshData()` par tableau. Elles sont conscientes des caches partagés, elles évitent les récupérations de source redondantes, et elles vous permettent de choisir le plus petit niveau qui satisfait votre besoin d'actualisation.

## Pièges courants
- **Oublier d'actualiser avant de sauvegarder.** Un tableau croisé dynamique n'écrit ses valeurs rendues dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules sources, appelez `PivotCache.Refresh()` (ou `Workbook.RefreshAll()`) avant `Workbook.save()`, sinon le fichier sauvegardé contiendra toujours les anciennes valeurs agrégées.
- **Appeler l'obsolète `RefreshData()` par tableau.** Dans la v26.7, `PivotTable.RefreshData()` est marquée comme obsolète et récupère la source pour chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela signifie N récupérations de source redondantes. Remplacez par un seul `PivotCache.Refresh()` suivi de `CalculateData()` par tableau.
- **Actualiser lorsque seule la disposition a changé.** Si vous n'avez modifié que la vue d'un tableau croisé dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données sources, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour rendre à nouveau à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d'une connexion externe (base de données, cube OLAP, etc.), `PivotCache.Refresh()` ne peut pas l'actualiser dans la v26.7 — elle ne prend actuellement en charge que les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}