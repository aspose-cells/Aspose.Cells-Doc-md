---
title: Spécification d avertissement de tri lors du tri des données
type: docs
weight: 140
url: /fr/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: Apprenez comment spécifier l avertissement de tri lors du tri des données en utilisant l API Aspose.Cells for Node.js via C++.
keywords: Ajouter un avertissement de tri lors du tri des données, définir un avertissement de tri lors du tri des données, sélectionner un avertissement de tri lors du tri des données.
---

## **Scénarios d'utilisation possibles**

Considérez ces données textuelles : {11, 111, 22}. Ces données sont triées parce qu'en termes de texte, 111 vient avant 22. Mais si vous souhaitez trier ces données en tant que nombres et non en tant que texte, elles deviendront {11, 22, 111} car numériquement 111 vient après 22. L'API Aspose.Cells for Node.js via C++ offre la propriété {0} pour gérer cette problématique. Veuillez définir cette propriété **true** et vos données textuelles seront triées comme des données numériques. La capture d'écran suivante montre l'avertissement de tri affiché par Microsoft Excel lorsque des données textuelles semblant être numériques sont triées.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Code d'exemple**

Le code d'exemple suivant illustre l'utilisation de la propriété [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-) comme expliqué précédemment. Veuillez consulter son [fichier Excel d'exemple](43352075.xlsx) et son [fichier Excel de sortie](43352076.xlsx) pour plus d'aide.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

