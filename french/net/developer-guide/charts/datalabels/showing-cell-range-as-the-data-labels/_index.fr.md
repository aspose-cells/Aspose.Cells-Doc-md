---
title: Afficher la plage de cellules en tant qu étiquettes de données
description: Apprenez comment afficher une plage de cellules en tant qu étiquettes de données dans les graphiques en utilisant Aspose.Cells for .NET. Notre guide vous montrera comment lier les étiquettes à votre source de données et les formater pour fournir des informations précises et significatives dans vos graphiques.
keywords: Aspose.Cells for .NET, création de graphiques, étiquettes de données, plage de cellules, source de données, formatage, précision, informations significatives.
type: docs
weight: 130
url: /fr/net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

Dans Microsoft Excel 2013, vous pouvez afficher une plage de cellules pour les étiquettes de données. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}

## **Case à cocher pour afficher la plage de cellules en tant qu'étiquettes de données**

Pour afficher la plage de cellules en tant qu'étiquettes de données dans Microsoft Excel :

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1. Sélectionnez **Format des étiquettes de données**. Les options d'étiquetage sont affichées.
1. Sélectionnez ou désélectionnez l'option **L'étiquette contient - Valeur à partir des cellules**.

Le code d'exemple ci-dessous accède aux étiquettes de données d'une série de graphiques et définit la propriété [**DataLabels.ShowCellRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/showcellrange) à **true** pour sélectionner l'option **L'étiquette contient - Valeur à partir des cellules**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-ShowCellRangeAsDataLabels-ShowCellRangeAsDataLabels.cs" >}}
{{< app/cells/assistant language="csharp" >}}
