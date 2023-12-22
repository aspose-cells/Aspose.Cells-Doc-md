---
title: Affichage de la plage Cell comme étiquettes de données
description: Découvrez comment afficher une plage de cellules sous forme d'étiquettes de données dans des graphiques en utilisant Aspose.Cells for .NET. Notre guide vous montrera comment lier les étiquettes à votre source de données et les formater pour fournir des informations précises et significatives dans vos graphiques.
keywords: Aspose.Cells for .NET, charting, data labels, cell range, data source, formatting, accuracy, meaningful information.
type: docs
weight: 130
url: /fr/net/showing-cell-range-as-the-data-labels/
---
{{% alert color="primary" %}}

Dans Microsoft Excel 2013, vous pouvez afficher une plage de cellules pour les étiquettes de données. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}

##  **Case à cocher pour afficher la plage Cell en tant qu'étiquettes de données**

Pour afficher la plage de cellules sous forme d'étiquettes de données dans Excel Microsoft :

1. Sélectionnez les étiquettes de données de série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1. Sélectionnez *Formater les étiquettes de données**. Les options d'étiquette s'affichent.
1. Sélectionnez ou décochez l'option *L'étiquette contient - Valeur de Cells**.

 L'exemple de code ci-dessous accède aux étiquettes de données d'une série de graphiques et définit le[**DataLabels.ShowCellRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/showcellrange) propriété à**vrai** pour sélectionner le**L'étiquette contient - Valeur à partir de Cells** option.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-ShowCellRangeAsDataLabels-ShowCellRangeAsDataLabels.cs" >}}
