---
title: Conserver le préfixe de guillemets simples de la valeur ou de la plage Cell
type: docs
weight: 1900
url: /fr/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Scénarios d'utilisation possibles**

Lorsque vous mettez une valeur dans la cellule qui comporte une apostrophe ou un guillemet simple, Microsoft Excel la masque, mais lorsque vous sélectionnez la cellule, elle affiche l'apostrophe ou le guillemet simple dans une barre de formule, comme indiqué dans la capture d'écran suivante.

![tâche : image_autre_texte](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells masque également l'apostrophe principale ou le guillemet simple comme Microsoft Excel mais il définit le[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) comme**vrai** pour cette cellule. Si vous définissez un style de cellule vide, alors[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) devient**faux** de nouveau. Afin de faire face à ce problème, le Aspose.Cells fournit[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) propriété, lorsqu'elle est définie**faux**, ensuite[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)n'est pas du tout mis à jour et son ancienne valeur est conservée. Cela signifie que si l'ancienne valeur de[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)la propriété était**vrai**, elle restera vraie et si l'ancienne valeur était fausse, elle restera fausse.

## **Conserver le préfixe de guillemets simples de la valeur ou de la plage Cell**

L'exemple de code suivant explique l'utilisation de[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)propriété telle que décrite précédemment. Veuillez lire les commentaires à l'intérieur du code et voir la sortie de la console du code ci-dessous pour plus d'aide.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Sortie console**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
