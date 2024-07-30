---
title: Calculer le facteur d échelle de la mise en page
type: docs
weight: 300
url: /fr/python-net/calculate-page-setup-scaling-factor/
description: Cet article fournit un code d exemple expliquant comment utiliser les APIs Aspose.Cells pour Python via .NET pour calculer le facteur d échelle de configuration de page en utilisant l option Ajuster à n page(s) de largeur sur m de hauteur de la feuille de calcul Excel de manière programmée.
keywords: Bibliothèque Python Excel, Ajuster à n pages de largeur sur m de hauteur Excel, calculer le facteur d échelle de configuration de page en Python.
---

{{% alert color="primary" %}}

Lorsque vous définissez l'échelle de la mise en page en utilisant l'option **Ajuster à n page(s) de largeur sur m page(s) de hauteur**, Microsoft Excel calcule le facteur d'échelle de la mise en page. Vous pouvez calculer la même chose en utilisant la propriété [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, si elle renvoie 0.5, cela signifie que le facteur d'échelle est de 50%.

{{% /alert %}}

Le code d'exemple suivant illustre comment calculer le facteur d'échelle de la mise en page en utilisant la propriété [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
