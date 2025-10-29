---
title: Travailler avec les formats d affichage des données du champ de données dans le tableau croisé dynamique avec Golang via C++
linktitle: Travailler avec les formats d affichage des données du DataField dans un tableau croisé dynamique
type: docs
weight: 140
url: /fr/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Apprenez comment travailler avec les formats d affichage des données du DataField dans un tableau croisé dynamique à l aide de Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge tous les formats d'affichage des données de DataField.

{{% /alert %}}

## **Option de format d'affichage "Classement du plus petit au plus grand" et "Classement du plus grand au plus petit"**

Aspose.Cells offre la possibilité de définir l'option de format d'affichage pour les champs de pivot. Pour cela, l'API fournit la propriété [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/). Pour classer du plus grand au plus petit, vous pouvez définir la propriété [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) à [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). L'extrait de code suivant démontre comment définir ces options de format d'affichage.

Les fichiers source et de sortie de l'échantillon peuvent être téléchargés d'ici pour tester le code d'échantillon:

[Fichier Excel source](101089332.xlsx)

[Fichier Excel de sortie](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
