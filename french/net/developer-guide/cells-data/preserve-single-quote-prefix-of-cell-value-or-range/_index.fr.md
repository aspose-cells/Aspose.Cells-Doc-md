---
title: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 310
url: /fr/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Apprenez à préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage via l API Aspose.Cells for .NET.
keywords: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage, Masquer le guillemet apostrophe ou le marqueur de guillemet simple en tête, Afficher le guillemet apostrophe ou le marqueur de guillemet simple en tête
---

## **Scénarios d'utilisation possibles**

Lorsque vous placez une valeur à l'intérieur de la cellule qui comporte une apostrophe ou un guillemet simple en tête, Microsoft Excel la cache, mais lorsque vous sélectionnez la cellule, elle affiche l'apostrophe ou le guillemet simple en tête dans une barre de formule comme indiqué dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells masque également l'apostrophe en tête comme Microsoft Excel mais il définit [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) comme **true pour cette cellule. Si vous définissez un style vide de la cellule, alors [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) redevient **false. Pour résoudre ce problème, Aspose.Cells fournit une propriété [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix), lorsqu'elle est définie sur **false, alors [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) n'est plus mis à jour du tout et sa vieille valeur est conservée. Cela signifie que si l'ancienne valeur de la propriété [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) était **true, elle restera **true et si l'ancienne valeur était **false, elle restera **false.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) comme décrit précédemment. Veuillez lire les commentaires dans le code et voir la sortie de la console du code ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
