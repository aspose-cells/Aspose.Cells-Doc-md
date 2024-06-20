---
title: Obtenir la valeur de chaîne de la cellule avec une stratégie de format
type: docs
weight: 240
url: /fr/python-net/get-cell-string-value-with-format-strategy/
description: Apprenez à obtenir la valeur de chaîne de la cellule avec et sans formatage grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, obtenir la valeur de chaîne de la cellule en Python avec et sans formatage, récupérer la valeur de chaîne de la cellule en Python avec et sans formatage, obtenir la valeur de chaîne de la cellule en Python avec et sans formatage
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fournit une méthode [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) qui peut être utilisée pour obtenir la valeur de chaîne de la cellule avec ou sans formatage. Supposons que vous ayez une cellule avec la valeur 0,012345 et que vous l'ayez formatée pour n'afficher que deux décimales. Elle s'affichera alors comme 0,01 dans Excel. Vous pouvez récupérer les valeurs de chaîne à la fois comme 0,01 et comme 0,012345 en utilisant la méthode [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/). Elle prend comme paramètre une énumération [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) qui a les valeurs suivantes

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la méthode [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
