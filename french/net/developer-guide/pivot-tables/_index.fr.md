---
title: Insérer un tableau croisé dynamique
linktitle: Tableaux croisés dynamiques
type: docs
weight: 160
url: /fr/net/pivot-tables/
description: Créer et formater des tableaux croisés dynamiques de fichiers de feuilles de calcul Excel.
keywords: Créer un Tableau Croisé Dynamique, Insérer un Tableau Croisé Dynamique, Formater un Tableau Croisé Dynamique.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Créer un tableau croisé dynamique**

Il est possible d'utiliser Aspose.Cells pour ajouter des tableaux croisés dynamiques aux feuilles de calcul par programmation.

### **Modèle d'objet de tableau croisé dynamique**

Aspose.Cells fournit un ensemble spécial de classes dans l'espace de noms [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) qui sont utilisées pour créer et contrôler les tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir les objets [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), les éléments constitutifs d'un tableau croisé dynamique. Les objets sont :

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) représente un champ dans un [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) dans le [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) représente un PivotTable dans une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) représente une collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) sur une feuille de calcul.

### **Création d'un tableau croisé dynamique simple avec Aspose.Cells**

1. Ajoutez des données à une feuille de calcul en utilisant la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) de l'objet [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Ces données seront utilisées comme source de données du tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) de la collection [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), qui est encapsulée dans l'objet Worksheet.
3. Accédez au nouvel objet [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) de la collection [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) en passant l'index de l'objet PivotTable.
4. Utilisez l'un des objets [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après l'exécution du code d'exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Lors de l'attribution d'une plage de cellules en tant que source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
