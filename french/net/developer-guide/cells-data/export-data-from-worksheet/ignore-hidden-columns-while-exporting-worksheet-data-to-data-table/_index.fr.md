---
title: Ignorer les colonnes masquées lors de l exportation des données de la feuille de calcul vers le tableau de données
type: docs
weight: 330
url: /fr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/
description: Apprenez comment ignorer les colonnes masquées lors de l exportation des données de la feuille de calcul vers le tableau de données via l API Aspose.Cells for .NET.
keywords: Exporter les données des colonnes visibles vers DataTable, exporter les données des colonnes non masquées vers DataTable, exporter les données des colonnes vers DataTable et exclure les colonnes masquées, ignorer les colonnes masquées lors de l exportation des données de la feuille de calcul vers le tableau de données
---

{{% alert color="primary" %}}

Parfois, vous souhaitez ignorer les colonnes masquées lors de l'exportation des données de la feuille de calcul vers un tableau de données. Vous pouvez le faire avec Aspose.Cells en définissant la valeur de [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns) sur **true**. Par défaut, sa valeur est **false**, vous devez donc la définir sur **true** pour ignorer les colonnes masquées.

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la propriété [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns) pour ignorer les colonnes masquées lors de l'exportation de l'ensemble des données de la feuille de calcul vers le tableau de données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-IgnoreHiddenColumnsDataTable-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
