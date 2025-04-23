---
title: Obtenir la validation appliquée sur une cellule
type: docs
weight: 80
url: /fr/java/get-validation-applied-on-a-cell/
description: Cet article montre comment appliquer une validation à une cellule avec Java
keywords: appliquer une validation de cellule dans Excel avec Java, appliquer une validation sur une cellule dans Excel avec Java, appliquer une validation dans Excel avec Java, validation de cellule dans Excel avec Java, Java appliquer une validation de cellule dans Excel, Java appliquer une validation sur une cellule dans Excel, Java validation de cellule dans Excel, Java validation de cellule
---

{{% alert color="primary" %}}

Vous pouvez utiliser l'API Aspose.Cells pour obtenir la validation appliquée à n'importe quelle cellule. Aspose.Cells fournit la méthode [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) à cette fin. S'il n'y a aucune validation sur la cellule, elle renvoie null. De même, vous pouvez utiliser la méthode [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell-int-int-) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

La capture d'écran suivante montre le fichier Microsoft Excel d'exemple utilisé dans le code d'exemple ci-dessous. La cellule **C1** a une **validation décimale** appliquée et ne peut prendre que des valeurs **entre 10 et 20**.

**Une cellule avec validation**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

Le code d'exemple ci-dessous obtient la validation appliquée à C1 et lit ses différentes propriétés.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Voici la sortie sur la console du code d'exemple exécuté avec le fichier d'exemple montré dans la capture d'écran ci-dessus.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Articles Connexes

- [Validation des données](/cells/fr/java/data-validation/)
{{< app/cells/assistant language="java" >}}
