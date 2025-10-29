---
title: Spécifier si le Tableau Croisé Dynamique est compatible avec Excel 2003 lors de son actualisation avec Golang via C++
linktitle: Spécifier la compatibilité pour Excel2003 dans PivotTable
type: docs
weight: 80
url: /fr/go-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Apprenez comment spécifier la compatibilité d un PivotTable pour Excel2003 à l aide de Aspose.Cells for C++ lors du rafraîchissement du PivotTable.
---

{{% alert color="primary" %}}

Aspose.Cells offre la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel 2003 lors du rafraîchissement du tableau croisé dynamique. Si true, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si **false**, une chaîne n'aura pas la restriction mentionnée. La valeur par défaut est **true**.

{{% /alert %}}

## **Spécifiez si le PivotTable est compatible pour Excel2003 lors de l'actualisation du PivotTable**

Le code d'exemple suivant explique l'utilisation de la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/). La chaîne d'origine fait 383 caractères de long. Mais lorsque la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) est définie sur **vrai** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères de long. Cependant, lorsque la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) est définie sur **faux** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyWhetherThePivottableIsCompatibleForExcel2003WhileRefreshingPivottable.go" >}}
