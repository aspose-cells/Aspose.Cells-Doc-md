---
title: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 1900
url: /fr/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Scénarios d'utilisation possibles**

Lorsque vous placez une valeur à l'intérieur de la cellule qui comporte une apostrophe ou un guillemet simple en tête, Microsoft Excel la cache, mais lorsque vous sélectionnez la cellule, elle affiche l'apostrophe ou le guillemet simple en tête dans une barre de formule comme indiqué dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells masque également l'apostrophe initiale ou l'apostrophe unique comme Microsoft Excel mais définit le [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) comme **vrai** pour cette cellule. Si vous définissez un style vide pour la cellule, alors [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) redeviendra **faux**. Pour résoudre ce problème, Aspose.Cells fournit la propriété [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix), lorsqu'elle est définie sur **faux**, alors [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) n'est pas du tout mis à jour et sa vieille valeur est préservée. Cela signifie que si l'ancienne valeur de la propriété [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) était **vraie**, elle restera vraie et si l'ancienne valeur était fausse, elle restera fausse.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

L'exemple de code suivant explique l'utilisation de la propriété [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) comme décrit précédemment. Veuillez lire les commentaires à l'intérieur du code et consultez la sortie de la console du code ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
