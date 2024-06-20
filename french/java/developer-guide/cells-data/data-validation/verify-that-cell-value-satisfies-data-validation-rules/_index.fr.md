---
title: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 90
url: /fr/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules de la feuille de calcul. Par exemple, une validation décimale peut être appliquée pour restreindre les nombres entre 10 et 20. Si un autre nombre en dehors de cette plage spécifiée est saisi, Microsoft Excel affiche un message d'erreur et invite l'utilisateur à ressaisir un nombre de la plage correcte. Si l'utilisateur copie-colle un nombre, disons 3, dans la cellule, Excel ne lance pas la vérification de la validation ou n'affiche pas de message d'erreur.

{{% /alert %}}

## Vérifier si la valeur de la cellule satisfait les règles de validation des données

Parfois, il est nécessaire de vérifier dynamiquement si une valeur donnée satisfait les règles de validation des données appliquées à la cellule. À cette fin, les API Aspose.Cells fournissent la méthode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Si la valeur dans une cellule ne satisfait pas la règle de validation des données appliquée à cette cellule, elle renvoie **False**, sinon **True**.

Le fichier Microsoft Excel d'exemple suivant est utilisé avec le code d'exemple ci-dessous pour tester la méthode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Comme vous pouvez le voir dans la capture d'écran, les cellules **C1** ont une **validation de données décimales** appliquée et n'accepteront que des valeurs **entre 10 et 20**. Chaque fois que la valeur de la cellule est entre 10 et 20, la méthode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) renverra **True**, sinon elle renverra **False**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

Le code d'exemple suivant illustre le fonctionnement de la méthode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Tout d'abord, il entre la valeur 3 dans C1. Comme cela ne satisfait pas la règle de validation des données, la méthode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) renvoie **False**. Ensuite, il entre la valeur 15 dans C1. Comme cette valeur satisfait la règle de validation des données, la méthode [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) renvoie **True**. De même, elle renvoie **False** pour la valeur 30.

## Code Java pour vérifier si une valeur de cellule satisfait les règles de validation des données

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Sortie console générée par le code d'exemple

Voici la sortie console générée lorsque le code d'exemple est exécuté avec le fichier Excel d'exemple montré ci-dessus.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
