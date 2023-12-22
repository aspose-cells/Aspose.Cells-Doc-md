---
title: Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique
type: docs
weight: 80
url: /fr/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Cet article montre comment spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET fournit le[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) propriété que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique. Si vrai, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si *false**, une chaîne n'aura pas la restriction susmentionnée. La valeur par défaut est *true**.

{{% /alert %}}

##  **Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique**

 L'exemple de code suivant explique l'utilisation de[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) propriété. La chaîne d'origine comporte 383 caractères. Mais quand[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) la propriété est définie**vrai** et le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et elles comportent 255 caractères. Cependant, quand[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) la propriété est définie**FAUX**et le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
