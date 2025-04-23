---
title: Regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique
type: docs
weight: 80
url: /fr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: Comment grouper les champs de pivot dans le tableau croisé dynamique avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, bibliothèque Excel Node.js, Comment grouper les champs de pivot dans le tableau croisé dynamique en utilisant la bibliothèque Aspose.Cells for Node.js via C++ Excel.
---

## **Scénarios d'utilisation possibles**

Microsoft Excel permet de grouper les champs de pivot du tableau croisé dynamique. Lorsqu’il y a une grande quantité de données liées à un champ de pivot, il est souvent utile de les regrouper en sections. Aspose.Cells for Node.js via C++ offre également cette fonctionnalité via la méthode [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **Comment regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716818.xlsx) et effectue un groupement sur le premier champ de tableau croisé dynamique en utilisant la méthode [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). Ensuite, il actualise et calcule les données du tableau croisé dynamique et enregistre le classeur sous le nom de [fichier Excel de sortie](64716817.xlsx). La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le premier champ de tableau croisé dynamique est maintenant regroupé par mois et par trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
