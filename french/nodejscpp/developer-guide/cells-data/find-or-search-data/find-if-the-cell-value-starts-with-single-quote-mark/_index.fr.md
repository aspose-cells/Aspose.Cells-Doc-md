---
title: Trouvez si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 270
url: /fr/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Apprenez comment vérifier si la valeur de la cellule commence par une apostrophe simple via l API Aspose.Cells for Node.js via C++.
keywords: Rechercher si la valeur de la cellule commence par une apostrophe simple Node.js via C++, Rechercher si la valeur de la cellule commence par une apostrophe simple Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells propose désormais la méthode [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) pour vérifier si la valeur de la cellule commence par une apostrophe simple. Avant cette propriété, il n'existait aucun moyen de faire la distinction entre des chaînes comme sample et 'sample', etc.

{{% /alert %}}

Le code d'exemple suivant explique que les chaînes comme sample et 'sample' ne peuvent pas être différenciées avec la méthode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Par conséquent, nous devons utiliser la méthode [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) pour les distinguer.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
