---
title: Filtrer le type de données lors du chargement du classeur à partir du fichier de modèle
type: docs
weight: 400
url: /fr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez spécifier quel type de données doit être chargé lors de la construction du classeur à partir du fichier de modèle. Le filtrage des données chargées peut améliorer les performances à des fins spéciales, notamment lors de l'utilisation des [API LightCells](/cells/fr/net/using-lightcells-api/). Veuillez utiliser la propriété [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) à cette fin.

{{% /alert %}}

Le code d'exemple suivant charge uniquement des objets de forme lors du chargement du classeur à partir du [fichier de modèle](5115552.xlsx) que vous pouvez télécharger à partir du lien donné. La capture d'écran suivante montre le contenu du [fichier de modèle](5115552.xlsx) et explique également que les données en couleur rouge et arrière-plan jaune ne seront pas chargées car la propriété [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) a été définie sur [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La capture d'écran suivante montre le [PDF de sortie](5115555.pdf) que vous pouvez télécharger à partir du lien donné. Ici, vous pouvez voir que les données en couleur rouge et arrière-plan jaune ne sont pas présentes mais que toutes les formes sont là.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
