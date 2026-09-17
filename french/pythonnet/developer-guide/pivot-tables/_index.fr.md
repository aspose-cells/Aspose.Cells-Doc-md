---
title: Insérer un tableau croisé dynamique
description: Créer et Formater un Tableau Croisé Dynamique avec Aspose.Cells pour Python via .NET.
linktitle: Tableaux croisés dynamiques
url: /fr/python-net/create-pivot-table/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: Créer un Tableau Croisé Dynamique, Insérer un Tableau Croisé Dynamique, Formater un Tableau Croisé Dynamique.
---

## **Créer un tableau croisé dynamique**
Il est possible d'utiliser Aspose.Cells pour Python via .NET pour ajouter des tableaux croisés dynamiques aux feuilles de calcul de manière programmée.

### **Modèle d'objet de tableau croisé dynamique**
Aspose.Cells pour Python via .NET fournit un ensemble spécial de classes dans l'espace de noms [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) qui sont utilisées pour créer et contrôler des tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir des objets [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), les éléments constitutifs d'un tableau croisé dynamique. Les objets sont :
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) représente un champ dans un [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) dans le [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) représente un PivotTable dans une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) représente une collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) sur une feuille de calcul.

### **Création d'un tableau croisé dynamique simple avec Aspose.Cells**
1. Ajoutez des données à une feuille de calcul en utilisant la méthode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) de l'objet [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) de la collection [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), qui est encapsulée dans l'objet FeuilleDeCalcul.
1. Accédez au nouvel objet [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) de la collection [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) en passant l'indice de PivotTable.
1. Utilisez l'un des objets [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) (expliqués ci-dessus) pour gérer le tableau croisé dynamique.
Après l'exécution du code d'exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
Lors de l'attribution d'une plage de cellules en tant que source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.
{{% /alert %}}

## **Sujets avancés**

{{< app/cells/assistant language="python-net" >}}