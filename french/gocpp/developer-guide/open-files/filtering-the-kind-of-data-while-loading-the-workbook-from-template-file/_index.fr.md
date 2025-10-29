---
title: Filtrer le type de données lors du chargement du classeur à partir d un fichier modèle avec Golang via C++
linktitle: Filtrage des données lors du chargement du classeur
type: docs
weight: 400
url: /fr/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Apprenez comment filtrer des types de données spécifiques lors du chargement d un classeur à partir d un fichier modèle en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Parfois, vous souhaitez spécifier quel type de données doit être chargé lors de la construction du classeur à partir du fichier modèle. Le filtrage des données chargées peut améliorer la performance pour votre usage particulier, surtout lors de l’utilisation des API [LightCells](/cells/fr/cpp/using-lightcells-api/). Veuillez utiliser la propriété [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) à cette fin.

{{% /alert %}}

Le code d'exemple suivant charge uniquement des objets de forme lors du chargement du classeur à partir du [fichier de modèle](5115552.xlsx) que vous pouvez télécharger à partir du lien donné. La capture d'écran suivante montre le contenu du [fichier de modèle](5115552.xlsx) et explique également que les données en couleur rouge et arrière-plan jaune ne seront pas chargées car la propriété [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) a été définie sur [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La capture d'écran suivante montre le [PDF de sortie](5115555.pdf) que vous pouvez télécharger à partir du lien donné. Ici, vous pouvez voir que les données en couleur rouge et arrière-plan jaune ne sont pas présentes mais que toutes les formes sont là.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
