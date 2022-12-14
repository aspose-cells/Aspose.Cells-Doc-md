---
title: Ignorer les colonnes masquées lors de l'exportation des données de la feuille de calcul vers la table de données
type: docs
weight: 330
url: /fr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez ignorer les colonnes masquées lors de l'exportation des données de la feuille de calcul vers une table de données. Vous pouvez y parvenir en utilisant Aspose.Cells en réglant le[**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns) à**vrai** . Par défaut, sa valeur est**faux** , vous devez donc le définir**vrai** pour ignorer les colonnes masquées.

{{% /alert %}}

 L'exemple de code suivant explique l'utilisation de[**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns)propriété en ignorant les colonnes masquées lors de l'exportation des données entières de la feuille de calcul vers la table de données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-IgnoreHiddenColumnsDataTable-1.cs" >}}
