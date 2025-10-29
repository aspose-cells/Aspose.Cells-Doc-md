---
title: Obtenir la validation appliquée sur une cellule
type: docs
weight: 200
url: /fr/nodejs-cpp/get-validation-applied-on-a-cell/
description: Cet article explique comment appliquer une validation sur une cellule avec Node.js via C++.
keywords: appliquer la validation de cellule dans excel avec Node.js via C++, appliquer une validation sur une cellule dans excel avec Node.js via C++, appliquer une validation dans excel avec Node.js via C++, validation de cellule dans excel avec Node.js via C++, Node.js via C++ appliquer la validation de cellule dans excel, Node.js via C++ appliquer une validation sur une cellule dans excel, Node.js via C++ validation de cellule dans excel
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour Node.js pour obtenir la validation appliquée à une cellule. Aspose.Cells fournit la méthode [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) à cet effet. S'il n'y a pas de validation appliquée à la cellule, elle retourne null.

De même, vous pouvez utiliser la méthode [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

## Code Node.js pour obtenir la validation appliquée à une cellule

Le code ci-dessous vous montre comment obtenir la validation appliquée à une cellule.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## Articles Connexes

- [Validation des données](/cells/fr/nodejs-cpp/data-validation/)
{{< app/cells/assistant language="nodejs-cpp" >}}
