---
title: Vérifiez que la valeur Cell satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Découvrez comment vérifier que la valeur Cell satisfait aux règles de validation des données via le Aspose.Cells for .NET API.
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale précise que seuls les nombres compris entre 10 et 20 peuvent être saisis. Si un utilisateur saisit un numéro différent. Microsoft Excel affiche un message d'erreur et les invite à saisir un nombre dans la plage correcte. Si vous copiez et collez un nombre, par exemple 3, dans la cellule, Excel n'exécute pas de contrôle de validation et n'affiche pas de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait aux règles de validation des données appliquées à la cellule par programme. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 
##  **Introduction**
 Aspose.Cells fournit le[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)méthode pour valider les valeurs des cellules par programme. Si la valeur d'une cellule ne satisfait pas à la règle de validation des données appliquée à cette cellule, elle renvoie *False**, sinon *True**.

 L'exemple de code suivant illustre comment le[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) la méthode fonctionne. Tout d’abord, il entre la valeur 3 dans C1. Parce que cela ne satisfait pas à la règle de validation des données, le[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) la méthode renvoie**FAUX**. Ensuite, il entre la valeur 15 dans C1. Étant donné que cette valeur satisfait à la règle de validation des données, la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) renvoie **True**. De même, il renvoie **False** pour la valeur 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **Sortir**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
