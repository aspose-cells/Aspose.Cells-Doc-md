---
title: Tableaux croisés dynamiques
linktitle: Tableaux croisés dynamiques
description: Créez et formatez des tableaux croisés dynamiques avec Aspose.Cells for Python via Java.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Formater un tableau croisé dynamique.
type: docs
weight: 160
url: /fr/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un grand volume de données brutes présentées ligne par ligne en une matrice compacte, sans la moindre formule. Vous choisissez les colonnes qui deviennent des étiquettes de ligne, celles qui deviennent des étiquettes de colonne et celles qui sont agrégées comme valeurs — le tableau croisé dynamique assure le regroupement et les calculs :
- **Synthétiser** — calculer le total des ventes par produit, par région ou par trimestre, au lieu d’utiliser de longues chaînes de formules.
- **Comparer** — les catégories placées sur les lignes et les périodes placées sur les colonnes transforment une liste plate en rapport croisé dans lequel les tendances sont visibles immédiatement.
- **Explorer le détail** — double-cliquez sur n’importe quelle valeur de synthèse pour examiner les lignes de données sources sous-jacentes.
- **Actualiser** — lorsque les données sources changent, une seule actualisation recalcule l’ensemble du rapport.
Les scénarios typiques sont les tableaux de bord des ventes, la répartition des dépenses et l’analyse des stocks — toute question du type « comment ces chiffres se répartissent-ils par catégorie et par période ? ». Aspose.Cells for Python via Java construit les mêmes tableaux croisés dynamiques de manière programmatique, afin que les classeurs générés par votre application contiennent des rapports prêts à l’emploi, et non uniquement des données brutes.

### **Modèle d’objet du tableau croisé dynamique**
Aspose.Cells fournit un ensemble de classes qui permettent de créer et de contrôler des tableaux croisés dynamiques. Les éléments constitutifs sont :
- `PivotField` représente un champ dans un objet `PivotTable`.
- `PivotFieldCollection` représente la collection de tous les objets `PivotField` contenus dans l’objet `PivotTable`.
- `PivotTable` représente un tableau croisé dynamique situé sur une feuille de calcul.
- `PivotTableCollection` représente la collection de tous les objets `PivotTable` d’une feuille de calcul.

### **Création d’un tableau croisé dynamique simple avec Aspose.Cells**
La création d’un tableau croisé dynamique se fait en trois étapes : écrire les données sources dans les cellules de la feuille de calcul, ajouter le tableau croisé dynamique à l’emplacement de destination, puis placer les champs du tableau dans les zones de ligne, de colonne et de données.
1. Ajoutez des données à une feuille de calcul à l’aide de la méthode `putValue` de la cellule. Ces données serviront de source de données au tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode `add` de la collection `PivotTables` : `add(sourceData, row, column)`. `sourceData` correspond à la plage source (par exemple, "A1:C8") ; `row` et `column` sont les coordonnées indexées à partir de zéro de la cellule de destination située dans l’angle supérieur gauche du tableau croisé dynamique (la cellule E3 correspond à la ligne 2 et à la colonne 4). La méthode renvoie directement le nouvel objet `PivotTable`.
3. Placez les champs à l’aide de la méthode `addFieldToArea` de l’objet `PivotTable` : placez un nom de champ dans la zone de ligne (`PivotFieldType.ROW`), dans la zone de colonne (`PivotFieldType.COLUMN`) ou dans la zone de données (`PivotFieldType.DATA`).
4. Enregistrez le classeur — le tableau croisé dynamique est écrit dans le fichier enregistré.
Après l’exécution de l’exemple de code, un tableau croisé dynamique est ajouté à la feuille de calcul.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Créer un nouveau classeur et obtenir la première feuille de calcul
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Écrire les données source : ventes par sport et trimestre
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# Ajouter un tableau croisé dynamique à la cellule de destination E3, à partir de A1:C8
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Enregistrer le classeur
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Lorsqu’une plage de cellules est utilisée comme source de données, elle doit s’étendre du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide, mais "C3:A1" ne l’est pas.
{{% /alert %}}

## Articles associés
- [Ajouter des champs de filtre à un tableau croisé dynamique avec Aspose.Cells for Python via Java](/cells/fr/python-java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques avec Aspose.Cells for Python via Java](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/python-java/change-page-field-layout/)
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Gérer les champs de valeurs des tableaux croisés dynamiques avec Aspose.Cells for Python via Java](/cells/fr/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}