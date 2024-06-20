---
title: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Découvrez comment vérifier si la valeur de la cellule satisfait aux règles de validation des données via l API Aspose.Cells for .NET.
keywords: Obtenir la valeur de validation de la cellule, obtenir la valeur de validation de la cellule, vérifier si une valeur satisfait aux règles de validation des données appliquées à la cellule
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale spécifie que seuls les nombres entre 10 et 20 peuvent être saisis. Si un utilisateur entre un nombre différent, Microsoft Excel affiche un message d'erreur et l'invite à saisir un nombre dans la plage correcte. Si vous copiez-collez un nombre, par exemple 3, dans la cellule, Excel ne vérifie pas la validation ni n'affiche de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule de manière programmée. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 
## **Introduction**
Aspose.Cells fournit la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) pour valider les valeurs des cellules de manière programmatique. Si la valeur dans une cellule ne satisfait pas la règle de validation des données appliquée à cette cellule, elle renvoie **Faux**, sinon **Vrai**.

L'exemple de code suivant illustre le fonctionnement de la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue). Tout d'abord, il entre la valeur 3 dans C1. Comme cela ne satisfait pas la règle de validation des données, la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) renvoie **Faux**. Ensuite, il entre la valeur 15 dans C1. Comme cette valeur satisfait la règle de validation des données, la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) renvoie **Vrai**. De même, elle renvoie **Faux** pour la valeur 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Sortie**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
