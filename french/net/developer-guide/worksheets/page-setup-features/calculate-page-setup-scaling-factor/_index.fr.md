---
title: Calculer le facteur d'échelle de mise en page
type: docs
weight: 300
url: /fr/net/calculate-page-setup-scaling-factor/
description: Cet article fournit un exemple de code expliquant comment utiliser la bibliothèque C# API ou .NET pour calculer le facteur de mise à l'échelle de la mise en page à l'aide de l'option Ajuster à n page(s) de large sur m de hauteur de la feuille de calcul Excel par programmation.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

 Lorsque vous définissez la mise à l'échelle de la mise en page à l'aide de**Ajuster à n page(s) de large par m de haut** option, Microsoft Excel calcule le facteur de mise à l'échelle de la mise en page. Vous pouvez calculer la même chose en utilisant[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)propriété. Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, s'il renvoie 0,5, cela signifie que le facteur d'échelle est de 50 %.

{{% /alert %}}

 L'exemple de code suivant illustre comment calculer le facteur d'échelle de mise en page à l'aide de[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
