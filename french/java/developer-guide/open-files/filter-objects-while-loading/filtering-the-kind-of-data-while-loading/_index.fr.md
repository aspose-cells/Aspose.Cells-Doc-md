---
title: Filtrer le type de données lors du chargement du classeur à partir du fichier de modèle
type: docs
weight: 680
url: /fr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

Parfois, vous souhaitez spécifier quel type de données doit être chargé lors de la construction du classeur à partir d'un fichier modèle. Filtrer les données chargées peut améliorer les performances pour votre utilisation spéciale, surtout lors de l'utilisation des [API LightCells](/cells/fr/java/using-lightcells-api/). Veuillez utiliser la propriété [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) à cette fin.

{{% /alert %}} 
## **Filtrer le type de données lors du chargement du classeur à partir d'un fichier modèle**
Le code d'exemple suivant charge uniquement des objets de forme lors du chargement du classeur à partir du [fichier modèle](5472556.xlsx) que vous pouvez télécharger depuis le lien donné.

La capture d'écran suivante montre le contenu du [fichier modèle](5472556.xlsx) et explique également que les données en couleur rouge et arrière-plan jaune ne seront pas chargées car la propriété [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) a été définie sur [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La capture d'écran suivante montre le [PDF de sortie](5472554.pdf) que vous pouvez télécharger depuis le lien donné. Ici, vous pouvez voir que les données en couleur rouge et arrière-plan jaune ne sont pas présentes, mais toutes les formes y sont.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
