---
title: Vérifier que la valeur de la cellule satisfait aux règles de validation des données avec Golang via C++
linktitle: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Apprenez comment vérifier si la valeur d une cellule satisfait les règles de validation des données via l API Aspose.Cells for C++.
keywords: Obtenir la valeur de validation de la cellule, obtenir la valeur de validation de la cellule, vérifier si une valeur satisfait aux règles de validation des données appliquées à la cellule
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale précise que seuls des nombres compris entre 10 et 20 peuvent être saisis. Si un utilisateur entre un autre nombre, Excel affiche un message d'erreur et lui demande d'entrer un nombre dans la plage correcte. Si vous copiez et collez un nombre, disons 3, dans la cellule, Excel ne lance pas de vérification de validation ni n'affiche de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule de manière programmée. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 

## **Introduction**
Aspose.Cells fournit la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) pour valider les valeurs des cellules par programmation. Si la valeur dans une cellule ne satisfait pas à la règle de validation de données appliquée à cette cellule, elle renvoie **False**, sinon **True**.

Le code d'exemple suivant illustre le fonctionnement de la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/). Tout d'abord, il entre la valeur 3 dans C1. Parce que cela ne satisfait pas la règle de validation des données, la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) renvoie **False**. Ensuite, il entre la valeur 15 dans C1. Parce que cette valeur satisfait la règle de validation des données, la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) renvoie **True**. De même, elle renvoie **False** pour la valeur 30.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Sortie**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
