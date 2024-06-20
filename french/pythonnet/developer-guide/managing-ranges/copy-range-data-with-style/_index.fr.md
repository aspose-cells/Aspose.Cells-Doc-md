---
title: Copier les données de la plage avec style
type: docs
weight: 610
url: /fr/python-net/copy-range-data-with-style/
description: Cet article décrit comment Copier la plage de données avec le style avec la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Python Comment copier la plage de données avec le style, Python Comment copier la plage de données avec le style avec la bibliothèque python excel.
---

{{% alert color="primary" %}}

[Copier uniquement les données de plage](/cells/fr/python-net/copy-range-data-only/) a expliqué comment copier les données d'une plage de cellules vers une autre plage. Plus précisément, il a appliqué un nouvel ensemble de styles aux cellules copiées. Aspose.Cells pour Python via .NET peut également copier une plage avec mise en forme. Cet article explique comment.

{{% /alert %}}

Aspose.Cells pour Python via .NET fournit une série de classes et de méthodes pour travailler avec des plages, par exemple, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) et [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

Cet exemple :

1. Crée un classeur.
1. Remplit un certain nombre de cellules dans la première feuille de calcul avec des données.
1. Crée un [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Crée un objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) avec des attributs de mise en forme spécifiés.
1. Applique le style à la plage de données.
1. Crée un deuxième groupe de cellules.
1. Copie les données avec la mise en forme de la première plage vers la deuxième plage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
