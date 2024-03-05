---
title: Aspose.Cells Modèle d'objet
type: docs
weight: 20
url: /fr/python-net/aspose-cells-object-model/
---
{{% alert color="primary" %}}

Le modèle d'objet Aspose.Cells fournit des informations sur les relations structurelles entre les objets de la bibliothèque de classes Aspose.Cells.

{{% /alert %}}

La structure de niveau supérieur du modèle d'objet Aspose.Cells est présentée ci-dessous de manière hiérarchique.

|**Structure de niveau supérieur du modèle d'objet Aspose.Cells**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_1.png)|
Comme vous pouvez le voir sur la figure ci-dessus, la racine du modèle d'objet est l'objet Workbook. Une brève description de quelques-uns des objets est fournie ci-dessous à des fins d'introduction.

## **WorksheetCollection/Worksheet**

L'objet Workbook contient WorksheetCollection, qui représente la collection de tous les objets Worksheet dans une feuille de calcul, comme indiqué ci-dessous :

|**Feuilles de calcul et objets de feuille de calcul**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_2.png)|

## **Cells/Cell**

Chaque objet Worksheet contient un objet Cells qui représente la collection de tous les objets Cell dans une feuille de calcul, comme illustré ci-dessous :

|**Cells & Cell objets**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_3.png)|
Vous pouvez utiliser l'objet Cell pour obtenir et définir la valeur, le style, la formule et d'autres propriétés d'une seule cellule.

## **Collection de graphiques/Graphique**

L'objet Charts représente une collection de tous les objets Chart d'une feuille de calcul. Chaque objet Chart est composé de plusieurs autres objets qui fonctionnent ensemble pour créer et gérer des graphiques. La structure du graphique dans Aspose.Cells est illustrée dans le diagramme ci-dessous :

|**Modèle d'objet du graphique**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_4.png)|

## **CommentCollection/Commentaire**

Chaque objet Worksheet contient également un objet Comments qui représente la collection de tous les objets Comment dans une feuille de calcul, comme illustré ci-dessous :

|**Commentaires et objets de commentaire**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_5.png)|
Un objet Comment est utilisé pour ajouter un commentaire à n'importe quelle cellule spécifiée dans la feuille de calcul.

## **HorizontalPageBreakCollection/HorizontalPageBreak**

Chaque objet Worksheet contient une HorizontalPageBreakCollection qui représente une collection de tous les objets HorizontalPageBreak dans une feuille de calcul, comme illustré ci-dessous :

|**Objets HPageBreaks et HPageBreak**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_6.png)|
Un objet HorizontalPageBreak est utilisé pour créer un saut de page horizontal dans la feuille de calcul.

## **Collection de liens hypertexte/lien hypertexte**

Un objet Worksheet contient également un HyperlinkCollection qui représente une collection de tous les objets Hyperlink dans la feuille de calcul, comme illustré ci-dessous :

|**Liens hypertexte et objets lien hypertexte**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_7.png)|
Un objet Hyperlink représente un lien hypertexte dans la feuille de calcul. Les développeurs peuvent définir l'adresse du lien hypertexte et d'autres propriétés associées à l'aide de l'objet Hyperlink.

## **Collection d'images/Image**

Chaque objet Worksheet contient un objet PictureCollection qui représente une collection de tous les objets Picture d'une feuille de calcul, comme illustré ci-dessous :

|**Images et objets d'image**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_8.png)|
Un objet Picture représente une image dans la feuille de calcul. À l'aide de l'objet Image, les développeurs peuvent non seulement ajouter des images dans leurs feuilles de calcul, mais également positionner ces images à n'importe quel endroit. Il est également possible de définir des bordures ou d'autres propriétés des images.

## **VerticalPageBreakCollection/VerticalPageBreak**

Chaque objet Worksheet contient un objet VerticalPageBreakCollection qui représente une collection de tous les objets VerticalPageBreak dans une feuille de calcul, comme illustré ci-dessous :

|**Objets VPageBreaks et VPageBreak**|
|:- |
|![tâche : image_autre_texte](aspose-cells-object-model_9.png)|
Un objet VerticalPageBreak est utilisé pour créer un saut de page vertical dans la feuille de calcul.
