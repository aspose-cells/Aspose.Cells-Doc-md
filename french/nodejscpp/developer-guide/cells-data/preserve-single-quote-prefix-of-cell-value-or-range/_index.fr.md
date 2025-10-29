---
title: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 310
url: /fr/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Apprenez comment préserver le préfixe de guillemet simple du contenu ou de la plage de cellules grâce à l API Aspose.Cells for Node.js via C++.
keywords: Préserver le préfixe de guillemet simple du contenu ou de la plage Node.js via C++, masquer l apostrophe ou le guillemet simple en tête Node.js via C++, afficher l apostrophe ou le guillemet simple en tête Node.js via C++
---

## **Scénarios d'utilisation possibles**

Lorsque vous placez une valeur à l'intérieur de la cellule qui comporte une apostrophe ou un guillemet simple en tête, Microsoft Excel la cache, mais lorsque vous sélectionnez la cellule, elle affiche l'apostrophe ou le guillemet simple en tête dans une barre de formule comme indiqué dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ masque également l'apostrophe ou le guillemet simple en tête comme Microsoft Excel, mais il définit [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) comme **vrai** pour cette cellule. Si vous appliquez un style vide à la cellule, alors [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) redevient **faux**. Pour gérer ce problème, Aspose.Cells for Node.js via C++ offre la méthode [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-), lorsque son état est **faux**, alors [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) n’est pas mis à jour du tout et sa valeur ancienne est conservée. Cela signifie que si la valeur ancienne de [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) était **vraie**, elle restera **vraie**, et si la valeur ancienne était **fausse**, elle restera **fausse**.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

Le code d'exemple suivant explique l'utilisation de la méthode [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) comme décrit précédemment. Veuillez lire les commentaires dans le code et voir la sortie console du code ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
