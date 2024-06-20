---
title: Calculer le facteur d échelle de la mise en page
type: docs
weight: 300
url: /fr/net/calculate-page-setup-scaling-factor/
description: Cet article fournit un code d exemple expliquant comment utiliser l API C# ou la bibliothèque .NET pour calculer le facteur d échelle de la mise en page en utilisant l option Ajuster à n page(s) de largeur sur m page(s) de hauteur de la feuille de calcul Excel de manière programmatique.
keywords: Ajuster à n page de largeur sur m de hauteur excel c#, calculer le facteur d échelle de la mise en page c#
---

{{% alert color="primary" %}}

Lorsque vous définissez l'échelle de la mise en page en utilisant l'option **Ajuster à n page(s) de largeur sur m page(s) de hauteur**, Microsoft Excel calcule le facteur d'échelle de la mise en page. Vous pouvez calculer la même chose en utilisant la propriété [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale). Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, si elle renvoie 0.5, cela signifie que le facteur d'échelle est de 50%.

{{% /alert %}}

Le code d'exemple suivant illustre comment calculer le facteur d'échelle de la mise en page en utilisant la propriété [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
