---
title: Obtenir la validation appliquée sur une cellule avec Golang via C++
linktitle: Obtenir la validation appliquée sur une cellule
type: docs
weight: 200
url: /fr/go-cpp/get-validation-applied-on-a-cell/
description: Cet article montre comment appliquer une validation sur une cellule avec Golang via C++.
keywords: appliquer la validation de cellule dans excel avec c++, appliquer une validation sur une cellule dans excel avec c++, appliquer validation dans excel avec c++, validation de cellule dans excel avec c++, c++ appliquer la validation de cellule dans excel, c++ appliquer la validation sur une cellule dans excel, validation de cellule c++ dans excel, validation de cellule c++
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour obtenir la validation appliquée à une cellule. Aspose.Cells fournit la méthode [**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/) à cet effet. S'il n'y a aucune validation appliquée sur la cellule, elle renvoie null.

De même, vous pouvez utiliser la méthode [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

## Code C++ pour obtenir la validation appliquée à une cellule

Le code ci-dessous vous montre comment obtenir la validation appliquée à une cellule.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## Articles Connexes

- [Validation des données](/cells/fr/cpp/data-validation/)
