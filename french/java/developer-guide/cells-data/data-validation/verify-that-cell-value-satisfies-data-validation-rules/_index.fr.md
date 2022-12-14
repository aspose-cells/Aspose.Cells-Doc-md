---
title: Vérifiez que la valeur Cell satisfait aux règles de validation des données
type: docs
weight: 90
url: /fr/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules de la feuille de calcul. Par exemple, une validation décimale peut être appliquée pour limiter les nombres entre 10 et 20. Si un autre nombre hors de cette plage spécifiée est entré, le Microsoft Excel affiche un message d'erreur et invite l'utilisateur à ressaisir un nombre de la plage correcte. Si l'utilisateur copie colle un nombre, disons 3, dans la cellule, Excel n'exécute pas le contrôle de validation ou n'affiche pas de message d'erreur.

{{% /alert %}}

## Vérifiez que la valeur Cell satisfait aux règles de validation des données

Parfois, il est nécessaire de vérifier dynamiquement si une valeur donnée satisfait les règles de validation des données appliquées à la cellule. A cet effet, les API Aspose.Cells fournissent les[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) méthode. Si la valeur d'une cellule ne satisfait pas la règle de validation des données appliquée à cette cellule, elle renvoie**Faux** , autre**Vrai**.

L'exemple de fichier Excel Microsoft suivant est utilisé avec l'exemple de code ci-dessous pour tester le[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) méthode. Comme vous pouvez le voir dans l'instantané, les cellules**C1** a**validation des données décimales** appliqué et n'acceptera que les valeurs**entre 10 et 20** . Chaque fois que la valeur de la cellule est comprise entre 10 et 20,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) la méthode renverra**Vrai** , sinon, il reviendra**Faux**.

![tâche : image_autre_texte](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 L'exemple de code suivant illustre comment le[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) méthode fonctionne. Tout d'abord, il entre la valeur 3 dans C1. Comme cela ne satisfait pas la règle de validation des données, le[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) la méthode renvoie**Faux** . Ensuite, il entre la valeur 15 dans C1. Étant donné que cette valeur satisfait la règle de validation des données, le[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) la méthode renvoie**Vrai** . De même, il revient**Faux** pour la valeur 30.

## Code Java pour vérifier si une valeur Cell satisfait aux règles de validation des données

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Sortie de la console générée par l'exemple de code

Voici la sortie de la console générée lorsque l'exemple de code est exécuté avec l'exemple de fichier Excel illustré ci-dessus.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
