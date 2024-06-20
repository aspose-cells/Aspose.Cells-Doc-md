---
title: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul
type: docs
weight: 1060
url: /fr/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Scénarios d'utilisation possibles**
Veuillez utiliser la propriété [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) pour filtrer les données du classeur. Mais si vous voulez filtrer les données des feuilles de calcul individuelles, alors vous devrez remplacer la méthode [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)) . Veuillez fournir la valeur appropriée de l'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) lors de la création ou de la manipulation de [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

L'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) comporte les valeurs suivantes.

- [AUCUN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TOUS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELLULE_VIDE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELLULE_TEXTE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELLULE_NUMÉRIQUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELLULE_ERREUR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELLULE_BOOLÉENNE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [VALEUR_CELLULE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMULE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [DONNÉES_CELLULE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [DIAGRAMME](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORME](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [ZONE_FUSIONNÉE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [MISE_EN_FORME_CONDITIONNELLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [VALIDATION_DES_DONNÉES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [TABLEAU_CROISÉ_DYNAMIQUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TABLEAU](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLIENS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [PARAMÈTRES_DE_FEUILLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [DONNÉES_FEUILLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [PARAMÈTRES_DU_LIVRE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [PARAMÈTRES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [STRUCTURE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [PROPRIÉTÉS_DU_DOCUMENT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [NOMS_DÉFINIS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Objets de filtre lors du chargement du classeur**
Le code d'exemple suivant illustre comment filtrer les graphiques du classeur. Veuillez vérifier le [fichier Excel d'exemple](5472489.xlsx) utilisé dans ce code et le [PDF de sortie](5472488.pdf) généré par celui-ci. Comme vous pouvez le voir dans le PDF de sortie, tous les graphiques ont été filtrés du classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Objets de filtre lors du chargement de la feuille de calcul**
Le code d'exemple suivant charge le [fichier Excel source](5472492.xlsx) et filtre les données suivantes de ses feuilles de calcul à l'aide d'un filtre personnalisé.

- Il filtre les graphiques de la feuille de calcul nommée NoCharts.
- Il filtre les formes de la feuille de calcul nommée NoShapes.
- Il filtre la mise en forme conditionnelle de la feuille de calcul nommée NoConditionalFormatting.

Une fois, le [fichier Excel source](5472492.xlsx) chargé avec un filtre personnalisé, il prend les images de toutes les feuilles de calcul une par une. Voici les images de sortie pour votre référence. Comme vous pouvez le voir, la première image n'a pas de graphiques, la deuxième image n'a pas de formes et la troisième image n'a pas de mise en forme conditionnelle.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
