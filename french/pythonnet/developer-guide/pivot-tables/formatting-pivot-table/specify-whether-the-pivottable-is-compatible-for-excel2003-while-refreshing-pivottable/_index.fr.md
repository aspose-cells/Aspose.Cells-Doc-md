---
title: Précisez si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique
type: docs
weight: 80
url: /fr/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Cet article montre comment spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, bibliothèque Python Excel, Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fournit la propriété [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique. Si vrai, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si **faux**, une chaîne n'aura pas les restrictions susmentionnées. La valeur par défaut est **vrai**.

{{% /alert %}}

## **Comment spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique**

Le code d'exemple suivant explique l'utilisation de la propriété [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/). La chaîne d'origine fait 383 caractères de long. Mais lorsque la propriété [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) est définie sur **vrai** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères de long. Cependant, lorsque la propriété [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) est définie sur **faux** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
