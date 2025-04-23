---
title: Modèle objet Aspose.Cells
type: docs
weight: 20
url: /fr/net/aspose-cells-object-model/
---

{{% alert color="primary" %}} 

Le modèle objet Aspose.Cells fournit des informations sur les relations structurelles entre les objets de la bibliothèque de classes Aspose.Cells. 

{{% /alert %}} 

La structure de niveau supérieur du modèle objet Aspose.Cells est présentée ci-dessous de manière hiérarchique.

|**Structure de niveau supérieur du modèle objet Aspose.Cells**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
Comme vous pouvez le voir sur la figure ci-dessus, la racine du modèle objet est l'objet Workbook. Une brève description de quelques-uns des objets est fournie ci-dessous à des fins d'introduction.
## **WorksheetCollection/Worksheet**
L'objet Workbook contient la WorksheetCollection, qui représente la collection de tous les objets Worksheet dans une feuille de calcul comme indiqué ci-dessous :

|**Feuilles de calcul et objets Feuille de calcul**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|
## **Cells/Cell**
Chaque objet Feuille de calcul contient un objet Cellules qui représente la collection de tous les objets Cellule dans une feuille de calcul comme indiqué ci-dessous:

|**Cellules et objets Cellule**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
Vous pouvez utiliser l'objet Cellule pour obtenir et définir la valeur, le style, la formule et d'autres propriétés d'une seule cellule.
## **ChartCollection/Chart**
L'objet Diagrammes représente une collection de tous les objets Diagramme dans une Feuille de calcul. Chaque objet Diagramme est composé de plusieurs autres objets qui travaillent ensemble pour créer et gérer des diagrammes. La structure du diagramme dans Aspose.Cells est montrée dans le diagramme ci-dessous:

|**Modèle d'objet du Diagramme**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|
## **CommentCollection/Comment**
Chaque objet Feuille de calcul contient également un objet Commentaires qui représente la collection de tous les objets Commentaire dans une feuille de calcul comme indiqué ci-dessous:

|**Commentaires et objets Commentaire**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Un objet Commentaire est utilisé pour ajouter un commentaire à n'importe quelle cellule spécifiée dans la feuille de calcul.
## **HorizontalPageBreakCollection/HorizontalPageBreak**
Chaque objet Feuille de calcul contient une CollectionSautsDePageHorizontaux qui représente une collection de tous les objets SautDePageHorizontal dans une feuille de calcul comme indiqué ci-dessous:

|**SautsDePageHorizontaux et objets SautDePageHorizontal**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
Un objet SautDePageHorizontal est utilisé pour créer un saut de page horizontal dans la feuille de calcul.
## **HyperlinkCollection/Hyperlink**
Un objet Feuille de calcul contient également une CollectionHyperlien qui représente une collection de tous les objets Hyperlien dans la feuille de calcul comme indiqué ci-dessous:

|**Hyperliens et objets Hyperlien**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Un objet Hyperlien représente un lien hypertexte dans la feuille de calcul. Les développeurs peuvent définir l'adresse du lien hypertexte et d'autres propriétés associées à l'aide de l'objet Hyperlien.
## **PictureCollection/Picture**
Chaque objet Feuille de calcul contient un objet CollectionImage qui représente une collection de tous les objets Image dans une feuille de calcul comme indiqué ci-dessous:

|**Images et objets Image**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Un objet Image représente une image dans la feuille de calcul. En utilisant l'objet Image, les développeurs peuvent non seulement ajouter des images dans leurs feuilles de calcul, mais aussi positionner ces images à n'importe quel endroit. Il est également possible de définir des bordures ou d'autres propriétés des images.

## **VerticalPageBreakCollection/VerticalPageBreak**
Chaque objet Feuille de calcul contient un objet VerticalPageBreakCollection qui représente une collection de tous les objets VerticalPageBreak dans une feuille de calcul comme montré ci-dessous:

|**Sauts de page verticaux & objets Saut de page vertical**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
Un objet VerticalPageBreak est utilisé pour créer un saut de page vertical dans la feuille de calcul.


## **PivotTableCollection/PivotTable**
Chaque objet Worksheet contient un objet PivotTableCollection qui représente une collection de tous les objets PivotTable dans une feuille de calcul comme indiqué ci-dessous:

|**PivotTables et objets PivotTable**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_10.png)|
Un objet PivotTable représente un tableau croisé dynamique dans la feuille de calcul. Les développeurs peuvent définir le style du tableau croisé dynamique et d'autres propriétés connexes à l'aide de l'objet PivotTable.

## **TimelineCollection/Timeline**
Chaque objet Worksheet contient un objet TimelineCollection qui représente une collection de tous les objets Timeline dans une feuille de calcul comme indiqué ci-dessous:

|**Chronologies et objets Timeline**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_11.png)|
Un objet Timeline représente une chronologie dans la feuille de calcul. Les développeurs peuvent définir le style de la chronologie et d'autres propriétés connexes à l'aide de l'objet Timeline.

## **SlicerCollection/Slicer**
Chaque objet FeuilleDeCalcul contient un objet CollectionSliceur qui représente une collection de tous les objets Sliceur dans une feuille de calcul comme indiqué ci-dessous :

|**Tranches et objets Sliceur**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_12.png)|
Un objet Sliceur représente un sliceur dans la feuille de calcul. Les développeurs peuvent définir le style du sliceur et d'autres propriétés connexes à l'aide de l'objet Sliceur.

## **ListObjectCollection/ListObject**
Chaque objet FeuilleDeCalcul contient un objet CollectionObjetListe qui représente une collection de tous les objets ObjetListe dans une feuille de calcul comme indiqué ci-dessous :

|**Listes d'objets et objets ObjetListe**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_13.png)|
Un objet ObjetListe représente un tableau dans la feuille de calcul. Les développeurs peuvent définir le style du tableau et d'autres propriétés connexes à l'aide de l'objet ObjetListe.

## **ShapeCollection/Shape**
Chaque objet FeuilleDeCalcul contient un objet CollectionForme qui représente une collection de tous les objets Forme dans une feuille de calcul comme indiqué ci-dessous :

|**Formes et objets Forme**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_14.png)|
Un objet Forme représente une forme dans la feuille de calcul. Les développeurs peuvent définir le style de la forme et d'autres propriétés connexes à l'aide de l'objet Forme.

## **SparklineGroupCollection/SparklineGroup**
Chaque objet FeuilleDeCalcul contient un objet CollectionGroupeMinigraphiques qui représente une collection de tous les objets GroupeMinigraphique dans une feuille de calcul comme indiqué ci-dessous :

|**Groupes de minigraphiques et objets GroupeMinigraphique**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_15.png)|
Un objet GroupeMinigraphique représente un groupe de minigraphiques dans la feuille de calcul. Les développeurs peuvent définir le style du groupe de minigraphiques et d'autres propriétés connexes à l'aide de l'objet GroupeMinigraphique.
{{< app/cells/assistant language="csharp" >}}
