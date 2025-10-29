---
title: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
type: docs
weight: 240
url: /fr/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Apprenez comment obtenir la valeur de chaîne de la cellule avec ou sans mise en forme via l’API Aspose.Cells for Node.js via C++.
keywords: Obtenez la valeur de la chaîne de la cellule avec ou sans mise en forme Node.js via C++, Récupérez la valeur de la chaîne de la cellule avec ou sans mise en forme Node.js via C++, Obtenez la valeur de la chaîne de la cellule avec ou sans mise en forme Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells fournit une méthode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) qui peut être utilisée pour obtenir la valeur de chaîne de la cellule avec ou sans mise en forme. Supposons que vous ayez une cellule avec la valeur 0.012345 et que vous l’ayez formatée pour n’afficher que deux décimales. Elle sera alors affichée comme 0.01 dans Excel. Vous pouvez récupérer les valeurs sous forme de 0.01 et de 0.012345 en utilisant la méthode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Elle prend l’énumération [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) en paramètre, qui possède les valeurs suivantes :

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Le code d’exemple suivant explique l’utilisation de la méthode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
