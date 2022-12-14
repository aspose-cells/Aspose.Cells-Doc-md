---
title: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul
type: docs
weight: 1060
url: /fr/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Scénarios d'utilisation possibles**
 Veuillez utiliser[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) propriété lors du filtrage des données du classeur. Mais si vous souhaitez filtrer les données de feuilles de calcul individuelles, vous devrez remplacer[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) méthode. Veuillez fournir la valeur appropriée à partir du[LoadDataFilterOptionsLoadDataFilterOptionsLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) énumération lors de la création ou de l'utilisation[ChargerFiltre](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 La[LoadDataFilterOptionsLoadDataFilterOptionsLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)énumération a les valeurs suivantes.

- [RIEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TOUT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_VIDE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMULE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [GRAPHIQUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORME](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [MISE EN FORME CONDITIONNELLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [LA VALIDATION DES DONNÉES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [PIVOT_TABLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TABLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLIENS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SHEET_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SHEET_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BOOK_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [RÉGLAGES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [STRUCTURE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [PROPRIÉTÉS DU DOCUMENT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filtrer les objets lors du chargement du classeur**
 L'exemple de code suivant montre comment filtrer les graphiques du classeur. S'il vous plaît, vérifiez le[exemple de fichier excel](5472489.xlsx) utilisé dans ce code et le[PDF de sortie](5472488.pdf)généré par celui-ci. Comme vous pouvez le voir dans le PDF de sortie, tous les graphiques ont été filtrés du classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filtrer les objets lors du chargement de la feuille de calcul**
 L'exemple de code suivant charge le[fichier excel source](5472492.xlsx) et filtre les données suivantes à partir de ses feuilles de calcul à l'aide d'un filtre personnalisé.

- Il filtre les graphiques de la feuille de calcul nommée NoCharts.
- Il filtre les formes de la feuille de calcul nommée NoShapes.
- Il filtre la mise en forme conditionnelle de la feuille de calcul nommée NoConditionalFormatting.

 Une fois, il charge le[fichier excel source](5472492.xlsx) avec un filtre personnalisé, il prend les images de toutes les feuilles de calcul une par une. Voici les images de sortie pour votre référence. Comme vous pouvez le voir, la première image n'a pas de graphiques, la deuxième image n'a pas de formes et la troisième image n'a pas de mise en forme conditionnelle.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
