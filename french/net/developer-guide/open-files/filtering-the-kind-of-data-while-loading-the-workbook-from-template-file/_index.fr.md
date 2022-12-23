---
title: Filtrage du type de données lors du chargement du classeur à partir du fichier de modèle
type: docs
weight: 400
url: /fr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez spécifier le type de données à charger lors de la création du classeur à partir du fichier de modèle. Le filtrage des données chargées peut améliorer les performances pour votre objectif spécifique, en particulier lors de l'utilisation[API LightCells](/cells/fr/net/using-lightcells-api/) . Veuillez utiliser le[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) propriété à cet effet.

{{% /alert %}}

L'exemple de code suivant charge uniquement les objets de forme lors du chargement du classeur à partir du[fichier modèle](5115552.xlsx) que vous pouvez télécharger à partir du lien indiqué. La capture d'écran suivante montre le[fichier modèle](5115552.xlsx)contenu et explique également que les données en couleur rouge et fond jaune ne seront pas chargées car[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)la propriété a été définie sur[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![tâche : image_autre_texte](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La capture d'écran suivante montre le[sortie PDF](5115555.pdf) que vous pouvez télécharger à partir du lien indiqué. Ici vous pouvez voir, les données en couleur rouge et fond jaune ne sont pas présentes mais toutes les formes sont là.

![tâche : image_autre_texte](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
