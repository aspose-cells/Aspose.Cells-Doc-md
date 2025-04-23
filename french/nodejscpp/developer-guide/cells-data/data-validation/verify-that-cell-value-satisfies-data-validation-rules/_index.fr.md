---
title: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Apprenez comment vérifier si la valeur d une cellule satisfait les règles de validation de données via l API Aspose.Cells for Node.js via C++.
keywords: Obtenez la valeur de validation de cellule Node.js via C++, Obtenez la valeur de validation de cellule Node.js via C++, Vérifiez si une valeur satisfait les règles de validation de données appliquées à la cellule Node.js via C++
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale précise que seuls des nombres compris entre 10 et 20 peuvent être saisis. Si un utilisateur entre un autre nombre, Excel affiche un message d'erreur et lui demande d'entrer un nombre dans la plage correcte. Si vous copiez et collez un nombre, disons 3, dans la cellule, Excel ne lance pas de vérification de validation ni n'affiche de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule de manière programmée. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 
## **Introduction**
Aspose.Cells for Node.js via C++ fournit la méthode [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) pour valider les valeurs des cellules de manière programmatique. Si la valeur d'une cellule ne satisfait pas à la règle de validation des données appliquée à cette cellule, elle renvoie **false**, sinon **true**.

Le code d'exemple suivant illustre le fonctionnement de la méthode [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--). Tout d'abord, il saisit la valeur 3 dans C1. Comme cela ne satisfait pas à la règle de validation des données, la méthode [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) renvoie **false**. Ensuite, il saisit la valeur 15 dans C1. Comme cette valeur satisfait à la règle de validation, la méthode [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) renvoie **true**. De même, elle renvoie **false** pour la valeur 30.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Sortie**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
