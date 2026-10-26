---
title: Insérer un tableau croisé dynamique
linktitle: Insérer un tableau croisé dynamique
description: Créez et mettez en forme des tableaux croisés dynamiques avec Aspose.Cells for Python via .NET.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Mettre en forme un tableau croisé dynamique.
type: docs
weight: 160
url: /fr/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un grand volume de données brutes présentées ligne par ligne en une matrice compacte, sans la moindre formule. Vous décidez quelles colonnes deviennent des étiquettes de ligne, lesquelles deviennent des étiquettes de colonne et lesquelles sont utilisées comme valeurs agrégées — le tableau croisé dynamique assure le regroupement et les calculs :
- **Résumer** — le total des ventes par produit, par région ou par trimestre, au lieu de longues chaînes de formules.
- **Comparer** — les catégories en lignes et les périodes en colonnes transforment une liste plate en rapport croisé où les tendances apparaissent d’un coup d’œil.
- **Explorer le détail** — double-cliquez sur une valeur de synthèse pour examiner les lignes de données source qui la sous-tendent.
- **Actualiser** — lorsque les données source changent, une seule actualisation recalcule l’ensemble du rapport.
Les scénarios typiques sont les tableaux de bord des ventes, la répartition des dépenses et l’analyse des stocks — toute question du type « comment ces chiffres se répartissent-ils par catégorie et par période ? ». Aspose.Cells for Python via .NET permet de créer de manière programmatique les mêmes tableaux croisés dynamiques, afin que les classeurs générés par votre application contiennent des rapports prêts à l’emploi plutôt que uniquement les données brutes.

### **Modèle d’objet du tableau croisé dynamique**
Aspose.Cells for Python via .NET fournit un ensemble de classes dédiées dans le namespace [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) qui permettent de créer et de contrôler les tableaux croisés dynamiques. Ces classes servent à créer et à configurer des objets [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), qui constituent la base d’un tableau croisé dynamique. Les objets sont :
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) représente un champ dans un objet [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) du [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) représente un objet PivotTable dans une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) représente une collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) dans une feuille de calcul.

### **Création d’un tableau croisé dynamique simple avec Aspose.Cells**
La création d’un tableau croisé dynamique comprend les étapes suivantes : écrire les données source dans les cellules de la feuille de calcul, ajouter le tableau croisé dynamique à l’emplacement de destination et placer les champs dans les zones de lignes, de colonnes et de données.
1. Ajoutez des données à une feuille de calcul à l’aide de la méthode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) de l’objet [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Ces données constitueront la source de données du tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) de la collection [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) : `add(source_data, row, column)`. `source_data` est la plage source (par exemple, `"A1:C8"`) ; `row` et `column` sont les coordonnées basées sur zéro de la cellule de destination située dans l’angle supérieur gauche du tableau croisé dynamique (la cellule E3 correspond à la ligne 2 et à la colonne 4). La méthode renvoie directement le nouvel objet [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
3. Placez les champs du tableau croisé dynamique à l’aide de la méthode `add_field_to_area` de l’objet [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) : un nom de champ est ajouté à la zone des lignes (`PivotFieldType.ROW`), à la zone des colonnes (`PivotFieldType.COLUMN`) ou à la zone des données (`PivotFieldType.DATA`).
4. Enregistrez le classeur — le tableau croisé dynamique est inscrit dans le fichier enregistré.
Après l’exécution de l’exemple de code, un tableau croisé dynamique est ajouté à la feuille de calcul.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Créer un nouveau classeur et obtenir la première feuille de calcul
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Écrire les données source : ventes par sport et trimestre
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# Ajouter un tableau croisé dynamique à la cellule de destination E3, à partir de A1:C8
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Enregistrer le classeur
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Lorsqu’une plage de cellules est définie comme source de données, elle doit s’étendre du coin supérieur gauche au coin inférieur droit. Par exemple, `"A1:C3"` est valide, mais `"C3:A1"` ne l’est pas.
{{% /alert %}}

## Articles associés
- [Ajouter des champs de filtre à un tableau croisé dynamique avec Aspose.Cells for Python via .NET](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques avec Aspose.Cells for Python via .NET](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/python-net/change-page-field-layout/)
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Gérer les champs de valeur d’un tableau croisé dynamique avec Aspose.Cells for Python via .NET](/cells/fr/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}