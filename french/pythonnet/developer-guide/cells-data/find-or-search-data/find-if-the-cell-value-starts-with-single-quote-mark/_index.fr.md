---
title: Trouvez si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 270
url: /fr/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Apprenez à savoir si la valeur de la cellule commence par un guillemet simple grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Rechercher la valeur de la cellule qui commence par un guillemet simple en Python, Rechercher la valeur de la cellule qui commence par un guillemet simple en Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fournit maintenant la propriété [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) pour savoir si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de distinguer entre des chaînes telles que sample et 'sample etc.

{{% /alert %}}

Le code d'exemple suivant explique que les chaînes comme échantillon et 'échantillon ne peuvent pas être différenciées avec la propriété [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/). Nous devons donc utiliser la propriété [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) pour les distinguer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
