---
title: Filtrer le type de données lors du chargement du classeur à partir du fichier de modèle
type: docs
weight: 400
url: /fr/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez spécifier le type de données à charger lors de la création du classeur à partir du fichier modèle. Le filtrage des données chargées peut améliorer la performance pour votre objectif spécifique. Veuillez utiliser la propriété [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) à cette fin.

{{% /alert %}}

Le code d'exemple suivant charge uniquement des objets de forme lors du chargement du classeur à partir du [fichier de modèle](5115552.xlsx) que vous pouvez télécharger à partir du lien donné. La capture d'écran suivante montre le contenu du [fichier de modèle](5115552.xlsx) et explique également que les données en couleur rouge et arrière-plan jaune ne seront pas chargées car la propriété [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) a été définie sur [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La capture d'écran suivante montre le [PDF de sortie](5115555.pdf) que vous pouvez télécharger à partir du lien donné. Ici, vous pouvez voir que les données en couleur rouge et arrière-plan jaune ne sont pas présentes mais que toutes les formes sont là.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
