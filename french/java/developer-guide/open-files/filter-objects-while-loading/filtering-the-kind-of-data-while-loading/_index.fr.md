---
title: Filtrage du type de données lors du chargement du classeur à partir du fichier de modèle
type: docs
weight: 680
url: /fr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 Parfois, vous souhaitez spécifier le type de données à charger lors de la création du classeur à partir d'un fichier de modèle. Le filtrage des données chargées peut améliorer les performances pour votre objectif spécifique, en particulier lors de l'utilisation[API LightCells](/cells/fr/java/using-lightcells-api/) . Veuillez utiliser le[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) propriété à cet effet.

{{% /alert %}} 
## **Filtrage du type de données lors du chargement du classeur à partir d'un fichier de modèle**
L'exemple de code suivant charge uniquement les objets de forme lors du chargement du classeur à partir du[fichier modèle](5472556.xlsx)que vous pouvez télécharger à partir du lien indiqué.

 La capture d'écran suivante montre le[fichier modèle](5472556.xlsx) contenu et explique également que les données en couleur rouge et fond jaune ne seront pas chargées car le[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)la propriété a été définie sur[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![tâche : image_autre_texte](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

 La capture d'écran suivante montre le[PDF de sortie](5472554.pdf) que vous pouvez télécharger à partir du lien indiqué. Ici vous pouvez voir, les données en couleur rouge et fond jaune ne sont pas présentes mais toutes les formes sont là.

![tâche : image_autre_texte](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
