---
title: Conserver le préfixe de quote simple de la valeur ou de la plage de cellules avec Golang via C++
linktitle: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 310
url: /fr/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Apprenez comment préserver le préfixe de guillemet simple du contenu ou de la plage via l’API Aspose.Cells for C++.
keywords: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage, Masquer le guillemet apostrophe ou le marqueur de guillemet simple en tête, Afficher le guillemet apostrophe ou le marqueur de guillemet simple en tête
---

## **Scénarios d'utilisation possibles**

Lorsque vous insérez une valeur dans la cellule qui commence par un apostrophe ou une marque de guillemet simple, alors Microsoft Excel la masque, mais lorsque vous sélectionnez la cellule, il affiche l’apostrophe ou le guillemet simple dans la barre de formule comme illustré dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells masque également l’apostrophe ou le guillemet simple comme Microsoft Excel, mais il définit [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) comme **true** pour cette cellule. Si vous définissez un style vide pour la cellule, alors [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) redevient **false**. Pour gérer ce problème, Aspose.Cells fournit la propriété [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/). Lorsqu’elle est réglée sur **false**, [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) n’est pas du tout mis à jour et sa valeur ancienne est conservée. Cela signifie que si la valeur ancienne de la propriété [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) était **true**, elle restera **true**, et si elle était **false**, elle restera **false**.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

Le code d’exemple ci-dessous explique l’utilisation de la propriété [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) comme décrit précédemment. Veuillez lire les commentaires dans le code et voir la sortie console ci-dessous pour plus d’aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
