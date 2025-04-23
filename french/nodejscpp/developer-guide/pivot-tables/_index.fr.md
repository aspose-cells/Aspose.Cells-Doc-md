---
title: Insérer un tableau croisé dynamique
linktitle: Tableaux croisés dynamiques
type: docs
weight: 160
url: /fr/nodejs-cpp/create-pivot-table/
description: Créer et formater des tableaux croisés dynamiques de fichiers de feuilles de calcul Excel.
---

## **Créer un tableau croisé dynamique**

 Il est possible d’utiliser Aspose.Cells for Node.js via C++ pour ajouter des tableaux croisés dynamiques aux feuilles de calcul de manière programmatique.

### **Modèle d'objet de tableau croisé dynamique**

 Aspose.Cells for Node.js via C++ fournit un ensemble spécial de classes utilisées pour créer et contrôler les tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir des objets [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), qui sont les blocs de construction d’un tableau croisé dynamique. Les objets sont:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) représente un champ dans un [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) dans le [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) représente un PivotTable dans une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) représente une collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) sur une feuille de calcul.

### **Création d'un tableau croisé dynamique simple avec Aspose.Cells**

1. Ajoutez des données à une feuille de calcul en utilisant la méthode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) de l'objet [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).
   Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) de la collection [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), qui est encapsulée dans l'objet FeuilleDeCalcul.
1. Accédez au nouvel objet [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) de la collection [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) en passant l'indice de PivotTable.
1. Utilisez l'un des objets [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après l'exécution du code d'exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

Lors de l'attribution d'une plage de cellules en tant que source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.

{{% /alert %}}
