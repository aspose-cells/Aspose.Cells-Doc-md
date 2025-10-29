---
title: Spécification du Format de Motif Personnalisé DBNum
linktitle: Spécification du Format de Motif Personnalisé DBNum
description: Aspose.Cells est une bibliothèque pour Node.js via C++ qui supporte le formatage des dates et des nombres en utilisant des motifs de formatage personnalisés. Cet article montre comment spécifier le motif de format personnalisé dbnum pour un meilleur contrôle de l affichage des nombres.
keywords: Aspose.Cells, Node.js via C++, feuille de calcul électronique, motif de format personnalisé, formatage, dbnum , contrôle de l affichage
type: docs
weight: 110
url: /fr/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for Node.js via C++ supporte le motif de format personnalisé *DBNum*. Par exemple, si la valeur de votre cellule est 123 et que vous spécifiez son format personnalisé comme [DBNum2][$-804]General, elle sera affichée comme 壹佰贰拾叁. Vous pouvez spécifier votre format personnalisé pour la cellule en utilisant la méthode [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) et la méthode [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-).

## **Code d'exemple**

Le code d'exemple suivant illustre comment spécifier un motif personnalisé *DBNum*. Veuillez consulter son [PDF de sortie](43352081.pdf) pour plus d’aide.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyDBNumCustomPattern.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
