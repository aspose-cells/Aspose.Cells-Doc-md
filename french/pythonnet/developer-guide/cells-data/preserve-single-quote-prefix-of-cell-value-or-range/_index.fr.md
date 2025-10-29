---
title: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 310
url: /fr/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Apprenez comment préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage en Python, Masquer l apostrophe ou le guillemet simple initial en Python, Afficher l apostrophe ou le guillemet simple initial en Python
---

## **Scénarios d'utilisation possibles**

Lorsque vous placez une valeur à l'intérieur de la cellule qui comporte une apostrophe ou un guillemet simple en tête, Microsoft Excel la cache, mais lorsque vous sélectionnez la cellule, elle affiche l'apostrophe ou le guillemet simple en tête dans une barre de formule comme indiqué dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NET fait également disparaître l'apostrophe ou le guillemet simple en tête comme le fait Microsoft Excel, mais il définit [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) comme **true** pour cette cellule. Si vous définissez un style vide pour la cellule, alors [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) redevient **false**. Afin de traiter cet problème, Aspose.Cells for Python via .NET fournit la propriété [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix), lorsqu'elle est définie comme **false**, alors [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) n'est pas du tout mis à jour et sa vieille valeur est conservée. Cela signifie que si l'ancienne valeur de la propriété [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) était **true**, elle restera **true** et si l'ancienne valeur était **false**, elle restera **false**.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) comme décrit précédemment. Veuillez lire les commentaires dans le code et voir la sortie de la console du code ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
