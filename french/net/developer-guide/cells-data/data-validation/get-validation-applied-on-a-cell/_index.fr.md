---
title: Obtenir la validation appliquée sur une cellule
type: docs
weight: 200
url: /fr/net/get-validation-applied-on-a-cell/
description: Cet article montre comment appliquer une validation sur une cellule avec C#
keywords: Appliquer une validation de cellule dans Excel avec C#, appliquer une validation sur une cellule dans Excel avec C#, appliquer une validation dans Excel avec C#, validation de cellule dans Excel avec C#, C# appliquer une validation de cellule dans Excel, C# appliquer une validation sur une cellule dans Excel, C# validation de cellule dans Excel, C# validation de cellule
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour obtenir la validation appliquée à une cellule. Aspose.Cells fournit la méthode [**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) à cet effet. S'il n'y a aucune validation appliquée sur la cellule, elle renvoie null.

De même, vous pouvez utiliser la méthode [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

## Code C# pour obtenir la validation appliquée sur une cellule

L'exemple de code ci-dessous vous montre comment obtenir la validation appliquée sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## Articles Connexes

- [Validation des données](/cells/fr/net/data-validation/)
{{< app/cells/assistant language="csharp" >}}
