---
title: Obtenez la validation appliquée sur un Cell
type: docs
weight: 80
url: /fr/java/get-validation-applied-on-a-cell/
description: Cet article montre comment appliquer la validation sur un Cell avec Java
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Vous pouvez utiliser Aspose.Cells API pour obtenir la validation appliquée à n'importe quelle cellule. Aspose.Cells fournit le[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) méthode à cet effet. S'il n'y a pas de validation sur la cellule, elle renvoie null. De même, vous pouvez utiliser le[**Feuille de calcul.getValidations().getValidationInCell(ligne int, colonne int)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

 L'instantané suivant montre l'exemple de fichier Excel Microsoft utilisé dans l'exemple de code ci-dessous. Cell**C1** a**validation décimale** appliqué et ne peut prendre que des valeurs**entre 10 et 20**.

**Une cellule avec validation**

![tâche : image_autre_texte](get-validation-applied-on-a-cell_1.png)

L'exemple de code ci-dessous obtient la validation appliquée à C1 et lit ses différentes propriétés.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Voici la sortie de la console à partir de l'exemple de code exécuté avec l'exemple de fichier présenté dans l'instantané ci-dessus.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Articles Liés

- [La validation des données](/cells/fr/java/data-validation/)
