---
title: Regrouper les champs du tableau croisé dynamique dans le tableau croisé dynamique avec Golang via C++
linktitle: Regrouper les champs du tableau croisé dynamique dans le tableau croisé dynamique avec Golang via C++
description: Découvrez comment regrouper les champs de tableau croisé dynamique dans un tableau croisé dynamique à l’aide d’Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, tableau croisé dynamique, champ de tableau croisé dynamique, regrouper les champs de tableau croisé dynamique, GroupBy, PivotField, regroupement par date, Go
type: docs
weight: 80
url: /fr/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Microsoft Excel vous permet de regrouper les champs de tableau croisé dynamique **dans** le tableau croisé dynamique. Lorsqu’un grand nombre de données sont associées à un champ de tableau croisé dynamique, il est souvent utile de les regrouper par sections. Aspose.Cells fournit également cette fonctionnalité à l’aide de la méthode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/).

## **Regrouper les champs du tableau croisé dynamique dans le tableau croisé dynamique**
L’exemple de code suivant charge le [fichier Excel d’exemple](64716818.xlsx) et regroupe le premier champ de tableau croisé dynamique à l’aide de la méthode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/). Il actualise ensuite le tableau croisé dynamique, calcule ses données et enregistre le classeur sous le nom de [fichier Excel de sortie](64716817.xlsx). La capture d’écran montre l’effet de l’exemple de code sur le fichier Excel d’exemple. Comme vous pouvez le voir sur la capture d’écran, le premier champ de tableau croisé dynamique est désormais regroupé par mois et par trimestres.
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}