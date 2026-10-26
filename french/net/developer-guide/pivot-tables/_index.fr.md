---
title: Insérer un tableau croisé dynamique
linktitle: Insérer un tableau croisé dynamique
description: Créez et formatez des tableaux croisés dynamiques dans des fichiers de feuille de calcul Excel.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Formater un tableau croisé dynamique.
type: docs
weight: 160
url: /fr/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un volume important de données brutes présentées ligne par ligne en une matrice compacte, sans la moindre formule. Vous choisissez les colonnes qui deviennent des étiquettes de ligne, celles qui deviennent des étiquettes de colonne et celles dont les valeurs sont agrégées — le tableau croisé dynamique effectue le regroupement et les calculs :
- **Résumer** — le total des ventes par produit, par région ou par trimestre, au lieu de longues chaînes de formules.
- **Comparer** — les catégories sur les lignes et les périodes sur les colonnes transforment une liste plate en rapport croisé où les tendances sont visibles immédiatement.
- **Analyser en détail** — double-cliquez sur n’importe quelle valeur de synthèse pour examiner les lignes de données source qui la composent.
- **Actualiser** — lorsque les données source changent, une seule actualisation recalcule l’ensemble du rapport.
Les cas d’utilisation typiques sont les tableaux de bord des ventes, les ventilations de dépenses et l’analyse des stocks — toute question du type « comment ces chiffres se répartissent-ils par catégorie et par période ? ». Aspose.Cells for .NET permet de créer par programme les mêmes tableaux croisés dynamiques, de sorte que les classeurs générés par votre application peuvent contenir des rapports prêts à l’emploi et non uniquement des données brutes.

### **Modèle d’objet du tableau croisé dynamique**
Aspose.Cells fournit, dans l’espace de noms [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot), un ensemble de classes permettant de créer et de contrôler les tableaux croisés dynamiques. Ces classes servent à créer et à configurer des objets [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), qui sont les éléments constitutifs d’un tableau croisé dynamique. Les objets sont :
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) représente un champ d’un objet [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) d’un objet [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) représente un tableau croisé dynamique sur une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) représente une collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) d’une feuille de calcul.

### **Créer un tableau croisé dynamique simple avec Aspose.Cells**
La création d’un tableau croisé dynamique repose sur trois étapes : écrire les données source dans les cellules de la feuille de calcul, ajouter le tableau croisé dynamique à l’emplacement de destination et placer les champs dans les zones de lignes, de colonnes et de données.
1. Ajoutez des données à une feuille de calcul à l’aide de la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) de l’objet [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Ces données seront utilisées comme source de données du tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) de la collection [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) : `Add(sourceData, row, column)`. `sourceData` est la plage source (par exemple, "A1:C8") ; `row` et `column` sont les indices de ligne et de colonne de la cellule de destination, avec une indexation commençant à zéro. Cette cellule est située dans l’angle supérieur gauche du tableau croisé dynamique (la cellule E3 correspond à la ligne 2 et à la colonne 4). La méthode renvoie directement le nouvel objet [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
3. Placez les champs à l’aide de la méthode `AddFieldToArea` de l’objet [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) : spécifiez le nom du champ à placer dans la zone des lignes (`PivotFieldType.Row`), des colonnes (`PivotFieldType.Column`) ou des données (`PivotFieldType.Data`).
4. Enregistrez le classeur — le tableau croisé dynamique figure dans le fichier enregistré.
Après l’exécution de l’exemple de code, un tableau croisé dynamique est ajouté à la feuille de calcul.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Créer un nouveau classeur et obtenir la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Écrire les données source : ventes par sport et trimestre
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// Ajouter un tableau croisé dynamique à la cellule de destination E3, à partir de A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Enregistrer le classeur
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Pour attribuer une plage de cellules comme source de données, celle-ci doit s’étendre du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide, mais "C3:A1" ne l’est pas.
{{% /alert %}}

## Articles associés
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/net/filter-by-label-or-value-of-pivot-table/)
- [Gérer les champs de valeurs des tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}